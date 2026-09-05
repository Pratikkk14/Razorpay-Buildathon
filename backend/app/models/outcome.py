"""Recovery outcome and attribution model."""
from sqlalchemy import Column, String, Float, Integer, ForeignKey, JSON, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base
from app.models.base import UUIDMixin, TimestampMixin


class OutcomeRecord(Base, UUIDMixin, TimestampMixin):
    """
    Final outcome of a recovery case.
    Captures financial realization, attribution (Natural vs Intervention), and net profit.
    """
    __tablename__ = "outcomes"

    case_id = Column(String(36), ForeignKey("cases.id", ondelete="CASCADE"), nullable=False, index=True)

    is_recovered = Column(Boolean, default=False, nullable=False)
    recovered_amount = Column(Float, default=0.0, nullable=False)
    
    # Attribution: NATURAL, INTERVENTION_DIRECT, INTERVENTION_ASSISTED, UNRECOVERED
    attribution_type = Column(String(50), default="UNRECOVERED", nullable=False)
    
    # Financial metrics
    total_intervention_cost = Column(Float, default=0.0)
    net_incremental_contribution = Column(Float, default=0.0)
    
    recovered_at = Column(DateTime, nullable=True)
    recovery_payment_id = Column(String(100), nullable=True)
    recovery_channel = Column(String(50), nullable=True)
    
    outcome_metadata = Column(JSON, nullable=True)

    # Relationship
    case = relationship("Case", back_populates="outcomes")
