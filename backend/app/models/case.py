"""Recovery case database model."""
from sqlalchemy import Column, String, Float, Integer, JSON, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import UUIDMixin, TimestampMixin


class Case(Base, UUIDMixin, TimestampMixin):
    """
    Core Recovery Case entity.
    Represents a payment failure undergoing recovery intelligence evaluation.
    """
    __tablename__ = "cases"

    # Razorpay or simulated payment references
    payment_id = Column(String(100), index=True, nullable=False)
    order_id = Column(String(100), index=True, nullable=True)
    customer_id = Column(String(100), index=True, nullable=False)
    customer_email = Column(String(255), nullable=True)
    customer_phone = Column(String(50), nullable=True)
    customer_name = Column(String(255), nullable=True)

    # Payment details
    amount = Column(Float, nullable=False)
    currency = Column(String(10), default="INR", nullable=False)
    payment_method = Column(String(50), nullable=True)  # card, upi, netbanking, wallet
    failure_code = Column(String(100), nullable=True)
    failure_reason = Column(String(500), nullable=True)
    issuing_bank = Column(String(100), nullable=True)
    attempt_count = Column(Integer, default=1, nullable=False)

    # Lifecycle Status:
    # NEW -> ANALYZING -> WAITING -> ACTION_RECOMMENDED -> ACTION_EXECUTED -> RECOVERED / FAILED / ESCALATED / SUPPRESSED / CLOSED
    status = Column(String(50), default="NEW", index=True, nullable=False)
    
    # Execution & Decision summary
    final_decision = Column(String(50), nullable=True)  # ACT, WAIT, DONT_ACT, ESCALATE
    recommended_action = Column(String(50), nullable=True)  # RETRY, PAYMENT_LINK, REMINDER, ALTERNATE_METHOD, HUMAN_ESCALATION
    executed_action = Column(String(50), nullable=True)
    policy_status = Column(String(50), nullable=True)  # APPROVED, VETOED, ESCALATED, SUPPRESSED
    
    # Economic metrics summary
    natural_recovery_prob = Column(Float, nullable=True)
    best_action_recovery_prob = Column(Float, nullable=True)
    incremental_lift = Column(Float, nullable=True)
    expected_incremental_contribution = Column(Float, nullable=True)
    decision_confidence = Column(Float, nullable=True)
    decision_reason = Column(String(1000), nullable=True)

    # Experiment Assignment
    experiment_id = Column(String(100), index=True, nullable=True)
    experiment_group = Column(String(50), nullable=True)  # CONTROL, TREATMENT

    # Metadata & raw webhook payload
    raw_payload = Column(JSON, nullable=True)
    metadata_json = Column(JSON, nullable=True)

    # Relationships
    contexts = relationship("PaymentContext", back_populates="case", cascade="all, delete-orphan")
    decisions = relationship("DecisionRecord", back_populates="case", cascade="all, delete-orphan")
    action_executions = relationship("ActionExecutionRecord", back_populates="case", cascade="all, delete-orphan")
    outcomes = relationship("OutcomeRecord", back_populates="case", cascade="all, delete-orphan")
    policy_evaluations = relationship("PolicyEvaluationRecord", back_populates="case", cascade="all, delete-orphan")
