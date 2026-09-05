"""Deterministic Policy & Safety Engine: Absolute authority enforcing guardrails and safety vetoes."""
import logging
from datetime import datetime
from typing import List, Dict, Tuple, Optional
from sqlalchemy.orm import Session
from app.models.case import Case
from app.models.context import PaymentContext
from app.models.policy import PolicyEvaluationRecord
from app.services.policy.rules import PolicyCheckOutcome
from app.core.config import settings

logger = logging.getLogger(__name__)


class DeterministicSafetyEngine:
    """
    Deterministic safety and policy engine.
    Ensures that ML predictions and proposals NEVER bypass hard business constraints.
    Can veto candidate actions or mandate escalation.
    """

    def evaluate_policies(
        self,
        db: Session,
        case: Case,
        context: PaymentContext,
        simulated_hour: Optional[int] = None
    ) -> Tuple[Dict[str, bool], Dict[str, str], List[PolicyCheckOutcome]]:
        """
        Runs all deterministic policy rules for a case.
        Returns:
            - allowed_actions: Map of action_name -> bool
            - block_reasons: Map of action_name -> explanation reason
            - outcomes: List of PolicyCheckOutcome records for audit logging
        """
        all_actions = ["RETRY", "PAYMENT_LINK", "REMINDER", "ALTERNATE_METHOD", "HUMAN_ESCALATION", "NO_ACTION"]
        allowed_actions = {act: True for act in all_actions}
        block_reasons = {}
        outcomes: List[PolicyCheckOutcome] = []

        # Rule 1: Bounded Retry Limit Gate
        if case.attempt_count >= settings.DEFAULT_MAX_RETRIES:
            allowed_actions["RETRY"] = False
            reason = f"Max retry limit exceeded (attempts: {case.attempt_count} >= {settings.DEFAULT_MAX_RETRIES})"
            block_reasons["RETRY"] = reason
            outcomes.append(
                PolicyCheckOutcome(
                    passed=False,
                    rule_key="MAX_RETRY_LIMIT",
                    rule_name="Bounded Retry Limit",
                    action_targeted="RETRY",
                    veto_reason=reason,
                    details={"attempts": case.attempt_count, "limit": settings.DEFAULT_MAX_RETRIES}
                )
            )
        else:
            outcomes.append(
                PolicyCheckOutcome(
                    passed=True,
                    rule_key="MAX_RETRY_LIMIT",
                    rule_name="Bounded Retry Limit",
                    action_targeted="RETRY",
                    details={"attempts": case.attempt_count, "limit": settings.DEFAULT_MAX_RETRIES}
                )
            )

        # Rule 2: Customer Opt-Out / DND Gate
        if context.is_opted_out == 1:
            contact_actions = ["PAYMENT_LINK", "REMINDER", "ALTERNATE_METHOD"]
            for act in contact_actions:
                allowed_actions[act] = False
                block_reasons[act] = "Customer has opted out of automated recovery communications (DND)."
            outcomes.append(
                PolicyCheckOutcome(
                    passed=False,
                    rule_key="CUSTOMER_OPT_OUT",
                    rule_name="DND / Opt-Out Enforcement",
                    veto_reason="Customer is on DND list",
                    details={"is_opted_out": 1}
                )
            )
        else:
            outcomes.append(
                PolicyCheckOutcome(
                    passed=True,
                    rule_key="CUSTOMER_OPT_OUT",
                    rule_name="DND / Opt-Out Enforcement",
                    details={"is_opted_out": 0}
                )
            )

        # Rule 3: Contact Frequency Cooldown Gate (Max 1 contact per 24 hours)
        if context.hours_since_last_contact is not None and context.hours_since_last_contact < settings.DEFAULT_COOLDOWN_HOURS:
            contact_actions = ["PAYMENT_LINK", "REMINDER", "ALTERNATE_METHOD"]
            for act in contact_actions:
                allowed_actions[act] = False
                block_reasons[act] = f"Contact cooldown active. Contacted {context.hours_since_last_contact:.1f}h ago (minimum {settings.DEFAULT_COOLDOWN_HOURS}h required)."
            outcomes.append(
                PolicyCheckOutcome(
                    passed=False,
                    rule_key="CONTACT_FREQUENCY_COOLDOWN",
                    rule_name="Contact Frequency & Cooldown Gate",
                    veto_reason=f"Customer contacted too recently ({context.hours_since_last_contact:.1f}h ago)",
                    details={"hours_since_last_contact": context.hours_since_last_contact, "cooldown_hours": settings.DEFAULT_COOLDOWN_HOURS}
                )
            )
        else:
            outcomes.append(
                PolicyCheckOutcome(
                    passed=True,
                    rule_key="CONTACT_FREQUENCY_COOLDOWN",
                    rule_name="Contact Frequency & Cooldown Gate",
                    details={"hours_since_last_contact": context.hours_since_last_contact}
                )
            )

        # Rule 4: Quiet Hours Gate (No customer outreach 21:00 - 09:00)
        current_hour = simulated_hour if simulated_hour is not None else datetime.now().hour
        is_quiet_hours = (current_hour >= settings.DEFAULT_QUIET_HOURS_START or current_hour < settings.DEFAULT_QUIET_HOURS_END)
        if is_quiet_hours:
            # We don't permanently ban the action, but flag for delay/timing adjustment
            outcomes.append(
                PolicyCheckOutcome(
                    passed=False,
                    rule_key="QUIET_HOURS",
                    rule_name="Quiet Hours Compliance",
                    veto_reason=f"Current hour ({current_hour}:00) is within quiet hours ({settings.DEFAULT_QUIET_HOURS_START}:00 - {settings.DEFAULT_QUIET_HOURS_END}:00). Outbound contact must be scheduled for next business window.",
                    details={"current_hour": current_hour, "quiet_start": settings.DEFAULT_QUIET_HOURS_START, "quiet_end": settings.DEFAULT_QUIET_HOURS_END}
                )
            )
        else:
            outcomes.append(
                PolicyCheckOutcome(
                    passed=True,
                    rule_key="QUIET_HOURS",
                    rule_name="Quiet Hours Compliance",
                    details={"current_hour": current_hour}
                )
            )

        # Rule 5: High-Value Transaction Escalation Gate (> ₹50,000)
        if case.amount >= settings.DEFAULT_HIGH_VALUE_THRESHOLD:
            # Automated bulk retries or links are disallowed; human escalation is mandated
            allowed_actions["RETRY"] = False
            block_reasons["RETRY"] = f"High-value transaction (₹{case.amount:,.2f} >= ₹{settings.DEFAULT_HIGH_VALUE_THRESHOLD:,.2f}) requires human review."
            allowed_actions["PAYMENT_LINK"] = False
            block_reasons["PAYMENT_LINK"] = f"High-value transaction (₹{case.amount:,.2f}) requires white-glove human touch."
            allowed_actions["REMINDER"] = False
            block_reasons["REMINDER"] = "Automated reminder suppressed for high-value transaction."
            outcomes.append(
                PolicyCheckOutcome(
                    passed=False,
                    rule_key="HIGH_VALUE_TRANSACTION_ESCALATION",
                    rule_name="High-Value Transaction White-Glove Gate",
                    action_targeted="HUMAN_ESCALATION",
                    veto_reason=f"High-value payment of ₹{case.amount:,.2f} escalates to human review",
                    details={"amount": case.amount, "threshold": settings.DEFAULT_HIGH_VALUE_THRESHOLD}
                )
            )
        else:
            outcomes.append(
                PolicyCheckOutcome(
                    passed=True,
                    rule_key="HIGH_VALUE_TRANSACTION_ESCALATION",
                    rule_name="High-Value Transaction White-Glove Gate",
                    details={"amount": case.amount, "threshold": settings.DEFAULT_HIGH_VALUE_THRESHOLD}
                )
            )

        # Rule 6: Fraud / Dispute Suppression Gate
        if context.is_disputed == 1:
            for act in ["RETRY", "PAYMENT_LINK", "REMINDER", "ALTERNATE_METHOD"]:
                allowed_actions[act] = False
                block_reasons[act] = "Transaction is flagged for dispute/fraud investigation."
            outcomes.append(
                PolicyCheckOutcome(
                    passed=False,
                    rule_key="FRAUD_DISPUTE_SUPPRESSION",
                    rule_name="Fraud and Dispute Suppression Gate",
                    veto_reason="Dispute or fraud flag active",
                    details={"is_disputed": 1}
                )
            )
        else:
            outcomes.append(
                PolicyCheckOutcome(
                    passed=True,
                    rule_key="FRAUD_DISPUTE_SUPPRESSION",
                    rule_name="Fraud and Dispute Suppression Gate",
                    details={"is_disputed": 0}
                )
            )

        # Save policy evaluation records to database for case audit
        for outcome in outcomes:
            eval_record = PolicyEvaluationRecord(
                case_id=case.id,
                rule_key=outcome.rule_key,
                rule_name=outcome.rule_name,
                passed=outcome.passed,
                action_targeted=outcome.action_targeted,
                veto_reason=outcome.veto_reason,
                evaluation_details=outcome.details
            )
            db.add(eval_record)
        db.commit()

        return allowed_actions, block_reasons, outcomes
