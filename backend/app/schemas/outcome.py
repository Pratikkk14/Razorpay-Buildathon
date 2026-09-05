"""Outcome recording schemas."""
from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, ConfigDict


class OutcomeCreate(BaseModel):
    case_id: str
    is_recovered: bool
    recovered_amount: float
    attribution_type: str = "NATURAL"  # NATURAL, INTERVENTION_DIRECT, INTERVENTION_ASSISTED, UNRECOVERED
    recovery_payment_id: Optional[str] = None
    recovery_channel: Optional[str] = None
    outcome_metadata: Optional[Dict[str, Any]] = None


class OutcomeResponse(OutcomeCreate):
    id: str
    total_intervention_cost: float
    net_incremental_contribution: float
    recovered_at: Optional[datetime] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
