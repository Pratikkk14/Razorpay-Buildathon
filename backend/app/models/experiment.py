"""Experimentation and A/B testing models."""
from sqlalchemy import Column, String, Float, Integer, JSON, Boolean
from app.core.database import Base
from app.models.base import UUIDMixin, TimestampMixin


class Experiment(Base, UUIDMixin, TimestampMixin):
    """
    Tracks controlled experiments (e.g. Uplift Engine vs Fixed Retries vs No Action).
    """
    __tablename__ = "experiments"

    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    status = Column(String(50), default="ACTIVE", nullable=False)  # ACTIVE, PAUSED, COMPLETED
    traffic_split_ratio = Column(Float, default=0.5, nullable=False)  # 0.5 = 50% treatment, 50% control
    
    # Statistical counters & metrics
    total_cases = Column(Integer, default=0)
    control_cases = Column(Integer, default=0)
    treatment_cases = Column(Integer, default=0)
    
    control_recovered_amount = Column(Float, default=0.0)
    treatment_recovered_amount = Column(Float, default=0.0)
    
    control_cost = Column(Float, default=0.0)
    treatment_cost = Column(Float, default=0.0)
    
    config_json = Column(JSON, nullable=True)
