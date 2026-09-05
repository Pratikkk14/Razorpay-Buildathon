"""Action execution schemas."""
from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, ConfigDict


class ActionExecutionRequest(BaseModel):
    case_id: str
    action_type: Optional[str] = None  # if None, executes case.recommended_action
    force: bool = False  # override for manual admin execution


class ActionExecutionResponse(BaseModel):
    id: str
    case_id: str
    action_type: str
    gateway: str
    gateway_reference_id: Optional[str] = None
    payment_link_url: Optional[str] = None
    status: str
    cost_incurred: float
    executed_at: datetime
    error_message: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
