"""Action execution record model."""
from sqlalchemy import Column, String, Float, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base
from app.models.base import UUIDMixin, TimestampMixin


class ActionExecutionRecord(Base, UUIDMixin, TimestampMixin):
    """
    Records an executed recovery action (e.g. payment link sent, retry dispatched).
    """
    __tablename__ = "action_executions"

    case_id = Column(String(36), ForeignKey("cases.id", ondelete="CASCADE"), nullable=False, index=True)
    decision_id = Column(String(36), nullable=True)

    action_type = Column(String(50), nullable=False)  # RETRY, PAYMENT_LINK, REMINDER, ALTERNATE_METHOD, HUMAN_ESCALATION
    gateway = Column(String(50), default="SIMULATOR")  # RAZORPAY_TEST, SIMULATOR
    
    # Gateway specific reference (e.g., plink_Hdf7283ns)
    gateway_reference_id = Column(String(100), nullable=True)
    payment_link_url = Column(String(500), nullable=True)

    status = Column(String(50), default="INITIATED")  # INITIATED, SUCCESS, FAILED, TIMEOUT
    cost_incurred = Column(Float, default=0.0)
    
    # Response from gateway/channel
    execution_payload = Column(JSON, nullable=True)
    error_message = Column(String(500), nullable=True)
    executed_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationship
    case = relationship("Case", back_populates="action_executions")
