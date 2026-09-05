"""Context aggregation engine: transforms raw application & payment data into clean ML inputs."""
import logging
from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from app.models.case import Case
from app.models.context import PaymentContext
from app.schemas.ml import MLModelInput

logger = logging.getLogger(__name__)


class ContextAggregator:
    """
    Collects and validates raw contextual attributes for a recovery case.
    Does NOT do ML feature engineering; prepares structured raw model input.
    """

    @staticmethod
    def aggregate_context(db: Session, case: Case) -> PaymentContext:
        """Fetch existing context or construct a default context snapshot from case data."""
        existing_context = db.query(PaymentContext).filter(PaymentContext.case_id == case.id).first()
        if existing_context:
            return existing_context

        # Derive initial baseline features from payload if available
        raw = case.raw_payload or {}
        payment_entity = raw.get("payload", {}).get("payment", {}).get("entity", {})
        
        # Determine failure category
        failure_code = case.failure_code or payment_entity.get("error_code") or "BAD_REQUEST_ERROR"
        failure_category = "technical"
        if "INSUFFICIENT" in failure_code.upper() or "FUNDS" in failure_code.upper():
            failure_category = "funds"
        elif "AUTH" in failure_code.upper() or "OTP" in failure_code.upper() or "2FA" in failure_code.upper():
            failure_category = "auth"
        elif "TIMEOUT" in failure_code.upper() or "GATEWAY" in failure_code.upper() or "DOWN" in failure_code.upper():
            failure_category = "technical"
        elif "CANCEL" in failure_code.upper() or "USER" in failure_code.upper():
            failure_category = "user_cancelled"

        # Check metadata or customer presets
        meta = case.metadata_json or {}
        tenure_days = meta.get("customer_tenure_days", 45)
        ltv = meta.get("customer_ltv", case.amount * 4)
        segment = meta.get("customer_segment", "standard")
        if case.amount >= 50000:
            segment = "enterprise"
        elif tenure_days > 365 and ltv > 50000:
            segment = "vip"

        context = PaymentContext(
            case_id=case.id,
            customer_tenure_days=tenure_days,
            customer_ltv=ltv,
            customer_segment=segment,
            total_lifetime_payments=meta.get("total_lifetime_payments", 5),
            successful_lifetime_payments=meta.get("successful_lifetime_payments", 4),
            failed_lifetime_payments=meta.get("failed_lifetime_payments", 1),
            days_since_last_success=meta.get("days_since_last_success", 14),
            is_first_ever_failure=1 if meta.get("successful_lifetime_payments", 4) > 0 and meta.get("failed_lifetime_payments", 1) == 1 else 0,
            failure_code=failure_code,
            failure_category=failure_category,
            time_since_failure_minutes=meta.get("time_since_failure_minutes", 0.0),
            previous_interventions_count=meta.get("previous_interventions_count", 0),
            hours_since_last_contact=meta.get("hours_since_last_contact", None),
            is_opted_out=meta.get("is_opted_out", 0),
            is_disputed=meta.get("is_disputed", 0),
            device_type=meta.get("device_type", "mobile_android"),
            context_data=meta
        )

        db.add(context)
        db.commit()
        db.refresh(context)
        return context

    @staticmethod
    def to_ml_input(case: Case, context: PaymentContext) -> MLModelInput:
        """Converts Case + PaymentContext into the standard MLModelInput contract."""
        return MLModelInput(
            case_id=case.id,
            amount=case.amount,
            currency=case.currency,
            payment_method=case.payment_method or "card",
            failure_code=case.failure_code or context.failure_code,
            issuing_bank=case.issuing_bank,
            attempt_count=case.attempt_count,
            customer_tenure_days=context.customer_tenure_days,
            customer_ltv=context.customer_ltv,
            customer_segment=context.customer_segment,
            total_lifetime_payments=context.total_lifetime_payments,
            successful_lifetime_payments=context.successful_lifetime_payments,
            failed_lifetime_payments=context.failed_lifetime_payments,
            days_since_last_success=context.days_since_last_success,
            is_first_ever_failure=context.is_first_ever_failure,
            time_since_failure_minutes=context.time_since_failure_minutes,
            previous_interventions_count=context.previous_interventions_count,
            hours_since_last_contact=context.hours_since_last_contact,
            device_type=context.device_type,
            additional_features=context.context_data
        )
