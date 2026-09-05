"""Payment context schemas."""
from typing import Optional, Dict, Any
from pydantic import BaseModel, ConfigDict


class PaymentContextInput(BaseModel):
    case_id: str
    customer_id: str
    amount: float
    currency: str = "INR"
    payment_method: Optional[str] = "card"
    failure_code: Optional[str] = None
    failure_reason: Optional[str] = None
    issuing_bank: Optional[str] = None
    attempt_count: int = 1
    customer_tenure_days: int = 30
    customer_ltv: float = 0.0
    customer_segment: str = "standard"
    total_lifetime_payments: int = 1
    successful_lifetime_payments: int = 0
    failed_lifetime_payments: int = 1
    days_since_last_success: Optional[int] = None
    is_first_ever_failure: int = 0
    time_since_failure_minutes: float = 0.0
    previous_interventions_count: int = 0
    hours_since_last_contact: Optional[float] = None
    is_opted_out: int = 0
    is_disputed: int = 0
    device_type: str = "mobile_android"
    raw_payload: Optional[Dict[str, Any]] = None


class PaymentContextOutput(PaymentContextInput):
    id: str

    model_config = ConfigDict(from_attributes=True)
