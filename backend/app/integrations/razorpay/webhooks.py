"""Razorpay webhook processor and event handler."""
import logging
from typing import Dict, Any, Tuple
from sqlalchemy.orm import Session

from app.models.case import Case
from app.services.context.aggregator import ContextAggregator
from app.services.ml.registry import get_ml_service
from app.services.decision.decision_engine import DecisionEngine
from app.services.execution.executor import ActionExecutor
from app.services.attribution.outcome_tracker import OutcomeTracker
from app.services.audit.audit_service import AuditService

logger = logging.getLogger(__name__)


class RazorpayWebhookProcessor:
    """Processes incoming Razorpay webhook events and triggers recovery pipelines."""

    @staticmethod
    def process_event(db: Session, event_data: Dict[str, Any], auto_execute: bool = False) -> Tuple[str, Dict[str, Any]]:
        """Processes a single webhook event payload."""
        event_name = event_data.get("event", "")
        payload = event_data.get("payload", {})
        logger.info(f"Processing Razorpay webhook event: {event_name}")

        # 1. Event: payment.failed -> Ingest failure and trigger recovery intelligence
        if event_name == "payment.failed":
            payment_entity = payload.get("payment", {}).get("entity", {})
            payment_id = payment_entity.get("id", f"pay_unknown_{event_data.get('created_at', 0)}")
            
            # Check for existing duplicate case (Idempotency)
            existing_case = db.query(Case).filter(Case.payment_id == payment_id).first()
            if existing_case:
                logger.info(f"Duplicate payment.failed event for {payment_id}. Idempotency hit.")
                return "DUPLICATE", {"case_id": existing_case.id, "status": existing_case.status}

            amount = float(payment_entity.get("amount", 0)) / 100.0  # paise to INR
            if amount <= 0:
                amount = 1000.0  # fallback

            # Create recovery case
            case = Case(
                payment_id=payment_id,
                order_id=payment_entity.get("order_id"),
                customer_id=payment_entity.get("customer_id") or payment_entity.get("contact") or f"cust_{payment_id[:8]}",
                customer_email=payment_entity.get("email"),
                customer_phone=payment_entity.get("contact"),
                amount=amount,
                currency=payment_entity.get("currency", "INR"),
                payment_method=payment_entity.get("method", "card"),
                failure_code=payment_entity.get("error_code") or "PAYMENT_FAILED",
                failure_reason=payment_entity.get("error_description") or "Payment authorization failed",
                issuing_bank=payment_entity.get("bank"),
                status="NEW",
                raw_payload=event_data
            )
            db.add(case)
            db.commit()
            db.refresh(case)

            AuditService.log_event(
                db=db,
                case_id=case.id,
                payment_id=case.payment_id,
                event_type="CASE_CREATED",
                summary=f"Recovery case created for failed payment ₹{amount:,.2f}",
                details={"event": event_name, "failure_code": case.failure_code}
            )

            # Aggregate context
            context = ContextAggregator.aggregate_context(db, case)

            # ML Inference
            ml_service = get_ml_service()
            ml_input = ContextAggregator.to_ml_input(case, context)
            prediction = ml_service.predict(ml_input)

            # Decision Engine
            dec_engine = DecisionEngine()
            decision_out = dec_engine.evaluate_and_decide(db, case, context, prediction)

            # Auto-execution if requested and decision is ACT
            if auto_execute and decision_out.decision == "ACT" and decision_out.recommended_action:
                executor = ActionExecutor()
                executor.execute_action(db, case)

            return "PROCESSED_FAILED_PAYMENT", {
                "case_id": case.id,
                "decision": decision_out.decision,
                "recommended_action": decision_out.recommended_action,
                "net_contribution": decision_out.expected_incremental_contribution
            }

        # 2. Event: payment.captured or payment_link.paid -> Record recovery outcome
        elif event_name in ["payment.captured", "payment_link.paid", "order.paid"]:
            payment_entity = payload.get("payment", {}).get("entity", {})
            payment_id = payment_entity.get("id")
            order_id = payment_entity.get("order_id")

            # Match to case by payment_id or order_id
            case = None
            if payment_id:
                case = db.query(Case).filter(Case.payment_id == payment_id).first()
            if not case and order_id:
                case = db.query(Case).filter(Case.order_id == order_id).first()

            if case:
                amount_rec = float(payment_entity.get("amount", 0)) / 100.0 if payment_entity.get("amount") else case.amount
                OutcomeTracker.record_outcome(
                    db=db,
                    case=case,
                    is_recovered=True,
                    recovered_amount=amount_rec,
                    recovery_payment_id=payment_id,
                    recovery_channel=payment_entity.get("method"),
                    metadata=event_data
                )
                return "RECORDED_RECOVERY", {"case_id": case.id, "recovered": True}
            else:
                return "IGNORED_UNMATCHED", {"message": "Captured event did not match an active recovery case"}

        return "UNHANDLED_EVENT", {"event": event_name}
