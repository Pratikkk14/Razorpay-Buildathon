"""Payment context and feature snapshot model."""
from sqlalchemy import Column, String, Float, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import UUIDMixin, TimestampMixin


class PaymentContext(Base, UUIDMixin, TimestampMixin):
    """
    Structured context gathered for a payment failure.
    Contains clean, unengineered business & customer features.
    """
    __tablename__ = "payment_contexts"

    case_id = Column(String(36), ForeignKey("cases.id", ondelete="CASCADE"), nullable=False, index=True)

    # Customer historical context
    customer_tenure_days = Column(Integer, default=30)
    customer_ltv = Column(Float, default=0.0)
    customer_segment = Column(String(50), default="standard")  # standard, enterprise, high_risk, dormant, vip
    total_lifetime_payments = Column(Integer, default=1)
    successful_lifetime_payments = Column(Integer, default=0)
    failed_lifetime_payments = Column(Integer, default=1)
    days_since_last_success = Column(Integer, nullable=True)
    is_first_ever_failure = Column(Integer, default=0)  # 1 if first failure ever

    # Failure details
    failure_code = Column(String(100), nullable=True)
    failure_category = Column(String(100), default="technical")  # technical, funds, auth, user_cancelled, network
    time_since_failure_minutes = Column(Float, default=0.0)
    previous_interventions_count = Column(Integer, default=0)
    hours_since_last_contact = Column(Float, nullable=True)

    # Customer behavioral / risk flags
    is_opted_out = Column(Integer, default=0)
    is_disputed = Column(Integer, default=0)
    device_type = Column(String(50), default="mobile_android")  # mobile_android, mobile_ios, desktop_web
    
    # Raw context dictionary
    context_data = Column(JSON, nullable=True)

    # Relationship
    case = relationship("Case", back_populates="contexts")
