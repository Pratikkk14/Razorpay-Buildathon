"""Policy rules configuration and policy evaluation models."""
from sqlalchemy import Column, String, Float, Integer, ForeignKey, JSON, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import UUIDMixin, TimestampMixin


class PolicyRuleConfig(Base, UUIDMixin, TimestampMixin):
    """
    Configurable deterministic policy rules.
    """
    __tablename__ = "policy_rule_configs"

    rule_key = Column(String(100), unique=True, nullable=False, index=True)
    rule_name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    parameters = Column(JSON, nullable=True)


class PolicyEvaluationRecord(Base, UUIDMixin, TimestampMixin):
    """
    Audit record for every deterministic policy check evaluated for a case.
    """
    __tablename__ = "policy_evaluations"

    case_id = Column(String(36), ForeignKey("cases.id", ondelete="CASCADE"), nullable=False, index=True)
    rule_key = Column(String(100), nullable=False)
    rule_name = Column(String(255), nullable=False)
    passed = Column(Boolean, nullable=False)
    action_targeted = Column(String(50), nullable=True)
    veto_reason = Column(String(500), nullable=True)
    evaluation_details = Column(JSON, nullable=True)

    # Relationship
    case = relationship("Case", back_populates="policy_evaluations")
