"""Outcome attribution and financial settlement tracker."""
import logging
from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from datetime import datetime

from app.models.case import Case
from app.models.outcome import OutcomeRecord
from app.models.action_execution import ActionExecutionRecord
from app.services.audit.audit_service import AuditService

logger = logging.getLogger(__name__)


class OutcomeTracker:
    """
    Tracks and attributes recovery outcomes.
    Distinguishes natural recoveries from intervention-driven recoveries.
    """

    @staticmethod
    def record_outcome(
        db: Session,
        case: Case,
        is_recovered: bool,
        recovered_amount: Optional[float] = None,
        recovery_payment_id: Optional[str] = None,
        recovery_channel: Optional[str] = None,
        attribution_override: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> OutcomeRecord:
        """Records the outcome of a recovery case and attributes causality."""
        amount_rec = recovered_amount if (is_recovered and recovered_amount is not None) else (case.amount if is_recovered else 0.0)

        # Sum total intervention costs incurred for this case
        executions = db.query(ActionExecutionRecord).filter(ActionExecutionRecord.case_id == case.id).all()
        total_costs = sum(ex.cost_incurred for ex in executions)

        # Determine attribution type
        if not is_recovered:
            attribution = "UNRECOVERED"
        elif attribution_override:
            attribution = attribution_override
        elif not executions or case.executed_action in [None, "NO_ACTION"]:
            attribution = "NATURAL"
        elif case.executed_action in ["PAYMENT_LINK", "RETRY"]:
            attribution = "INTERVENTION_DIRECT"
        else:
            attribution = "INTERVENTION_ASSISTED"

        # Realized net contribution:
        # If intervention direct -> amount_rec - total_costs
        # If natural -> amount_rec (no costs needed)
        net_contrib = round(amount_rec - total_costs, 2)

        outcome = OutcomeRecord(
            case_id=case.id,
            is_recovered=is_recovered,
            recovered_amount=amount_rec,
            attribution_type=attribution,
            total_intervention_cost=total_costs,
            net_incremental_contribution=net_contrib,
            recovered_at=datetime.utcnow() if is_recovered else None,
            recovery_payment_id=recovery_payment_id,
            recovery_channel=recovery_channel,
            outcome_metadata=metadata or {}
        )
        db.add(outcome)

        # Update case entity status
        case.status = "RECOVERED" if is_recovered else "FAILED"
        db.commit()
        db.refresh(outcome)

        # Audit
        AuditService.log_event(
            db=db,
            case_id=case.id,
            payment_id=case.payment_id,
            event_type="OUTCOME_RECORDED",
            summary=f"Outcome: {'RECOVERED' if is_recovered else 'FAILED'} (Attribution: {attribution}) -> Net Contribution: ₹{net_contrib:,.2f}",
            details={
                "is_recovered": is_recovered,
                "recovered_amount": amount_rec,
                "attribution": attribution,
                "total_costs": total_costs,
                "net_contribution": net_contrib
            }
        )

        return outcome
