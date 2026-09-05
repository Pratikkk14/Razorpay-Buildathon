"""Decision Engine: Synthesizes ML inference, Economic Allocation, and Policy Safety into actionable decisions."""
import logging
from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from datetime import datetime

from app.models.case import Case
from app.models.context import PaymentContext
from app.models.decision import DecisionRecord, CandidateActionEvaluation
from app.schemas.ml import MLModelPrediction
from app.schemas.decision import DecisionOutput, DecisionExplanation
from app.services.economics.allocation_engine import EconomicAllocationEngine
from app.services.policy.safety_engine import DeterministicSafetyEngine
from app.services.audit.audit_service import AuditService
from app.core.config import settings

logger = logging.getLogger(__name__)


class DecisionEngine:
    """
    Decides what should happen for a recovery case (ACT, WAIT, DONT_ACT, ESCALATE).
    Enforces that ML only recommends, while deterministic economics and policies decide.
    """

    def __init__(
        self,
        economics_engine: Optional[EconomicAllocationEngine] = None,
        safety_engine: Optional[DeterministicSafetyEngine] = None
    ):
        self.economics_engine = economics_engine or EconomicAllocationEngine()
        self.safety_engine = safety_engine or DeterministicSafetyEngine()

    def evaluate_and_decide(
        self,
        db: Session,
        case: Case,
        context: PaymentContext,
        prediction: MLModelPrediction,
        simulated_hour: Optional[int] = None
    ) -> DecisionOutput:
        """
        Executes end-to-end evaluation:
        1. Run Deterministic Safety Checks
        2. Run Economic Allocation Engine with Policy Constraints
        3. Determine Final Action, Timing, and Structured Decision
        4. Persist Decision Record and Audit Trail
        """
        # 1. Deterministic Safety Checks
        allowed_actions, block_reasons, policy_outcomes = self.safety_engine.evaluate_policies(
            db=db,
            case=case,
            context=context,
            simulated_hour=simulated_hour
        )

        # 2. Economic Optimization under Policy Guardrails
        economic_result = self.economics_engine.evaluate_case(
            case_id=case.id,
            payment_amount=case.amount,
            prediction=prediction,
            policy_allowed_map=allowed_actions,
            policy_block_reasons=block_reasons
        )

        # Check quiet hours constraint (default to 14:00 business hours if unspecified)
        current_hour = simulated_hour if simulated_hour is not None else 14
        is_quiet_hours = (current_hour >= settings.DEFAULT_QUIET_HOURS_START or current_hour < settings.DEFAULT_QUIET_HOURS_END)

        # 3. Determine Final Decision & Timing
        decision_type = "DONT_ACT"
        recommended_action = "NO_ACTION"
        recommended_timing = "IMMEDIATE"
        policy_status = "APPROVED"
        policy_reason = None
        reason = ""

        # Case A: High-Value Escalation
        if case.amount >= settings.DEFAULT_HIGH_VALUE_THRESHOLD:
            decision_type = "ESCALATE"
            recommended_action = "HUMAN_ESCALATION"
            policy_status = "ESCALATED"
            policy_reason = f"High-value payment (₹{case.amount:,.2f}) mandates human review."
            reason = f"Escalating to VIP Operations. High-value payment of ₹{case.amount:,.2f} justifies white-glove manual assistance."

        # Case B: High Natural Recovery / Insufficient Incremental Lift
        elif prediction.natural_recovery_probability >= 0.75 and (
            not economic_result.best_action or economic_result.best_action.incremental_lift < 0.08
        ):
            decision_type = "DONT_ACT"
            recommended_action = "NO_ACTION"
            policy_status = "APPROVED"
            lift_pct = (economic_result.best_action.incremental_lift * 100) if economic_result.best_action else 0.0
            reason = (
                f"Natural recovery is high ({prediction.natural_recovery_probability*100:.1f}%). "
                f"Intervention produces insufficient incremental lift ({lift_pct:.1f}%), "
                f"making intervention economically wasteful."
            )

        # Case C: Safety Policy Veto on best ML action
        elif economic_result.highest_contribution_action and not economic_result.highest_contribution_action.policy_allowed:
            blocked_act = economic_result.highest_contribution_action.action_type
            block_msg = block_reasons.get(blocked_act, "Blocked by safety guardrail")
            
            # Check if there is an alternative valid action with positive contribution
            valid_action = economic_result.best_action
            if valid_action and valid_action.action_type != "NO_ACTION" and valid_action.expected_incremental_contribution > 0:
                decision_type = "ACT"
                recommended_action = valid_action.action_type
                policy_status = "APPROVED"
                reason = (
                    f"AI recommended {blocked_act}, but policy blocked it ({block_msg}). "
                    f"Safely fell back to valid action: {recommended_action} with positive contribution ₹{valid_action.expected_incremental_contribution:.2f}."
                )
            else:
                decision_type = "DONT_ACT"
                recommended_action = "NO_ACTION"
                policy_status = "VETOED"
                policy_reason = block_msg
                reason = f"AI recommendation ({blocked_act}) rejected by deterministic policy: {block_msg}. Case suppressed."

        # Case D: Viable Intervention with Positive Incremental Contribution
        elif economic_result.best_action and economic_result.best_action.action_type != "NO_ACTION" and economic_result.best_action.expected_incremental_contribution > 0:
            recommended_action = economic_result.best_action.action_type
            inc_contrib = economic_result.best_action.expected_incremental_contribution
            lift_pct = economic_result.best_action.incremental_lift * 100

            if is_quiet_hours and recommended_action in ["PAYMENT_LINK", "REMINDER", "ALTERNATE_METHOD"]:
                decision_type = "WAIT"
                recommended_timing = "NEXT_QUIET_HOURS_END"
                policy_status = "APPROVED"
                reason = (
                    f"Recommend {recommended_action} with expected net contribution ₹{inc_contrib:.2f} (lift +{lift_pct:.1f}%). "
                    f"Holding until quiet hours end (09:00 AM) before sending."
                )
            else:
                decision_type = "ACT"
                recommended_timing = "IMMEDIATE"
                policy_status = "APPROVED"
                reason = (
                    f"Act with {recommended_action}. Low natural recovery ({prediction.natural_recovery_probability*100:.1f}%) "
                    f"and high intervention lift (+{lift_pct:.1f}%) yields expected net contribution of ₹{inc_contrib:.2f}."
                )

        # Case E: Negative or Zero Incremental ROI
        else:
            decision_type = "DONT_ACT"
            recommended_action = "NO_ACTION"
            policy_status = "APPROVED"
            reason = "No candidate intervention generates positive incremental contribution after accounting for costs and customer friction."

        # 4. Extract metrics for saving
        best_score = economic_result.best_action
        inc_lift = best_score.incremental_lift if best_score else 0.0
        inc_rev = best_score.expected_incremental_revenue if best_score else 0.0
        action_cost = best_score.action_cost if best_score else 0.0
        incentive_cost = best_score.incentive_cost if best_score else 0.0
        friction_cost = best_score.friction_cost if best_score else 0.0
        inc_contrib = best_score.expected_incremental_contribution if best_score else 0.0

        # 5. Persist Decision Record
        decision_rec = DecisionRecord(
            case_id=case.id,
            decision=decision_type,
            recommended_action=recommended_action,
            recommended_timing=recommended_timing,
            ml_model_name=prediction.model_name,
            ml_model_version=prediction.model_version,
            ml_confidence=prediction.confidence,
            natural_recovery_prob=prediction.natural_recovery_probability,
            incremental_lift=inc_lift,
            expected_incremental_revenue=inc_rev,
            expected_action_cost=action_cost,
            expected_incentive_cost=incentive_cost,
            expected_friction_cost=friction_cost,
            expected_incremental_contribution=inc_contrib,
            policy_status=policy_status,
            policy_reason=policy_reason,
            decision_reason=reason,
            explanation_breakdown={
                "natural_recovery_probability": prediction.natural_recovery_probability,
                "best_action": recommended_action,
                "net_contribution": inc_contrib,
                "quiet_hours_active": is_quiet_hours,
                "policy_status": policy_status
            }
        )
        db.add(decision_rec)
        db.commit()
        db.refresh(decision_rec)

        # 6. Persist Candidate Action Evaluations
        for cand in economic_result.candidate_actions:
            eval_row = CandidateActionEvaluation(
                decision_id=decision_rec.id,
                case_id=case.id,
                action_type=cand.action_type,
                natural_recovery_prob=cand.natural_recovery_prob,
                action_recovery_prob=cand.action_recovery_prob,
                incremental_lift=cand.incremental_lift,
                payment_amount=cand.payment_amount,
                expected_recovery_value=cand.expected_recovery_value,
                expected_incremental_revenue=cand.expected_incremental_revenue,
                action_cost=cand.action_cost,
                incentive_cost=cand.incentive_cost,
                friction_cost=cand.friction_cost,
                total_cost=cand.total_cost,
                expected_incremental_contribution=cand.expected_incremental_contribution,
                policy_allowed=1 if cand.policy_allowed else 0,
                policy_block_reason=cand.policy_block_reason,
                rank=cand.rank,
                is_selected=1 if cand.is_selected else 0
            )
            db.add(eval_row)

        # Update Case Entity
        case.final_decision = decision_type
        case.recommended_action = recommended_action
        case.policy_status = policy_status
        case.natural_recovery_prob = prediction.natural_recovery_probability
        case.best_action_recovery_prob = best_score.action_recovery_prob if best_score else prediction.natural_recovery_probability
        case.incremental_lift = inc_lift
        case.expected_incremental_contribution = inc_contrib
        case.decision_confidence = prediction.confidence
        case.decision_reason = reason
        case.status = "ACTION_RECOMMENDED" if decision_type == "ACT" else ("WAITING" if decision_type == "WAIT" else "SUPPRESSED")
        
        db.commit()

        # 7. Audit Log
        AuditService.log_event(
            db=db,
            case_id=case.id,
            payment_id=case.payment_id,
            event_type="DECISION_GENERATED",
            summary=f"Decision: {decision_type} ({recommended_action}) -> Net Contribution: ₹{inc_contrib:,.2f}",
            details={
                "decision": decision_type,
                "recommended_action": recommended_action,
                "timing": recommended_timing,
                "policy_status": policy_status,
                "net_contribution": inc_contrib,
                "incremental_lift": inc_lift,
                "reason": reason
            }
        )

        return DecisionOutput(
            case_id=case.id,
            decision=decision_type,
            recommended_action=recommended_action,
            recommended_timing=recommended_timing,
            incremental_lift=inc_lift,
            expected_incremental_revenue=inc_rev,
            expected_incremental_contribution=inc_contrib,
            confidence=prediction.confidence,
            policy_status=policy_status,
            policy_reason=policy_reason,
            reason=reason,
            candidate_actions=economic_result.candidate_actions,
            ml_model_name=prediction.model_name,
            ml_model_version=prediction.model_version,
            natural_recovery_prob=prediction.natural_recovery_probability
        )
