"""Append-only audit trail logging model."""
from sqlalchemy import Column, String, JSON, DateTime, Integer
from datetime import datetime
from app.core.database import Base
from app.models.base import UUIDMixin


class AuditEvent(Base, UUIDMixin):
    """
    Immutable audit event record for complete regulatory and debugging traceability.
    """
    __tablename__ = "audit_events"

    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    case_id = Column(String(36), index=True, nullable=True)
    payment_id = Column(String(100), index=True, nullable=True)
    event_type = Column(String(100), nullable=False, index=True)  # CASE_CREATED, CONTEXT_AGGREGATED, ML_PREDICTED, POLICY_EVALUATED, DECISION_GENERATED, ACTION_EXECUTED, OUTCOME_RECORDED
    
    actor = Column(String(100), default="SYSTEM", nullable=False)
    summary = Column(String(500), nullable=False)
    details = Column(JSON, nullable=True)
