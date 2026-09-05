"""Economic Allocation Engine: Ranks candidate interventions by expected incremental contribution."""
import logging
from typing import List, Dict, Optional
from app.schemas.ml import MLModelPrediction
from app.schemas.economics import CostConfig, CandidateActionScore, EconomicOptimizationResult

logger = logging.getLogger(__name__)


class EconomicAllocationEngine:
    """
    Core business optimization engine.
    Calculates incremental lift, expected incremental revenue, friction/incentive/action costs,
    and ranks all actions by net incremental contribution.
    """

    def __init__(self, cost_config: Optional[CostConfig] = None):
        self.cost_config = cost_config or CostConfig()

    def evaluate_case(
        self,
        case_id: str,
        payment_amount: float,
        prediction: MLModelPrediction,
        policy_allowed_map: Optional[Dict[str, bool]] = None,
        policy_block_reasons: Optional[Dict[str, str]] = None,
    ) -> EconomicOptimizationResult:
        """
        Evaluates candidate interventions and determines the economically optimal action.
        """
        policy_allowed_map = policy_allowed_map or {}
        policy_block_reasons = policy_block_reasons or {}
        natural_p = prediction.natural_recovery_probability

        # Define mapping of action names
        action_map = {
            "RETRY": ("retry", self.cost_config.retry_action_cost, self.cost_config.retry_friction_cost),
            "PAYMENT_LINK": ("payment_link", self.cost_config.payment_link_cost, self.cost_config.payment_link_friction_cost),
            "REMINDER": ("reminder", self.cost_config.reminder_cost, self.cost_config.reminder_friction_cost),
            "ALTERNATE_METHOD": ("alternate_method", self.cost_config.alternate_method_cost, self.cost_config.alternate_method_friction_cost),
            "HUMAN_ESCALATION": ("human_escalation", self.cost_config.human_escalation_cost, self.cost_config.human_escalation_friction_cost),
            "NO_ACTION": ("no_action", self.cost_config.no_action_cost, self.cost_config.no_action_friction_cost),
        }

        candidate_scores: List[CandidateActionScore] = []

        for action_name, (ml_key, action_cost, friction_cost) in action_map.items():
            if action_name == "NO_ACTION":
                action_p = natural_p
                lift = 0.0
            else:
                action_p = prediction.action_outcomes.get(ml_key, natural_p)
                lift = round(action_p - natural_p, 4)

            expected_recovery_val = round(action_p * payment_amount, 2)
            expected_inc_rev = round(lift * payment_amount, 2)
            
            # Total cost deduction
            incentive_cost = 0.0
            total_cost = round(action_cost + incentive_cost + friction_cost, 2)
            
            # Net Incremental Contribution = Expected Incremental Revenue - Total Cost
            if action_name == "NO_ACTION":
                net_contribution = 0.0
            else:
                net_contribution = round(expected_inc_rev - total_cost, 2)

            is_allowed = policy_allowed_map.get(action_name, True)
            block_reason = policy_block_reasons.get(action_name) if not is_allowed else None

            candidate_scores.append(
                CandidateActionScore(
                    action_type=action_name,
                    natural_recovery_prob=natural_p,
                    action_recovery_prob=action_p,
                    incremental_lift=lift,
                    payment_amount=payment_amount,
                    expected_recovery_value=expected_recovery_val,
                    expected_incremental_revenue=expected_inc_rev,
                    action_cost=action_cost,
                    incentive_cost=incentive_cost,
                    friction_cost=friction_cost,
                    total_cost=total_cost,
                    expected_incremental_contribution=net_contribution,
                    policy_allowed=is_allowed,
                    policy_block_reason=block_reason,
                    rank=1,
                    is_selected=False
                )
            )

        # Sort all actions by net incremental contribution descending
        candidate_scores.sort(key=lambda x: x.expected_incremental_contribution, reverse=True)
        for i, score in enumerate(candidate_scores):
            score.rank = i + 1

        # Identify highest raw recovery action vs highest net contribution action
        highest_recovery_action = max(candidate_scores, key=lambda x: x.action_recovery_prob)
        highest_contrib_action = candidate_scores[0]

        # Select best VALID (policy allowed) action with positive contribution
        best_valid_action: Optional[CandidateActionScore] = None
        for score in candidate_scores:
            if score.policy_allowed and score.action_type != "NO_ACTION" and score.expected_incremental_contribution > 0:
                best_valid_action = score
                score.is_selected = True
                break

        # If no positive contribution action exists or all valid are <= 0, default to NO_ACTION
        if not best_valid_action:
            for score in candidate_scores:
                if score.action_type == "NO_ACTION":
                    best_valid_action = score
                    score.is_selected = True
                    break

        is_positive = best_valid_action.expected_incremental_contribution > 0 if best_valid_action else False

        return EconomicOptimizationResult(
            case_id=case_id,
            payment_amount=payment_amount,
            candidate_actions=candidate_scores,
            best_action=best_valid_action,
            highest_contribution_action=highest_contrib_action,
            highest_recovery_action=highest_recovery_action,
            is_positive_contribution=is_positive
        )
