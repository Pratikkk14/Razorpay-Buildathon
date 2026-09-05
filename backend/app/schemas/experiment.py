"""Experiment schemas."""
from typing import Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel


class ExperimentCreate(BaseModel):
    name: str
    description: Optional[str] = None
    traffic_split_ratio: float = 0.5
    config_json: Optional[Dict[str, Any]] = None


class ExperimentMetrics(BaseModel):
    experiment_id: str
    name: str
    status: str
    total_cases: int
    control_cases: int
    treatment_cases: int
    control_recovery_rate: float
    treatment_recovery_rate: float
    observed_lift_pct: float
    treatment_incremental_revenue: float
    treatment_cost: float
    treatment_net_contribution: float
    contribution_per_case_inr: float
