"""Case Pydantic schemas."""
from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, ConfigDict


class CaseBase(BaseModel):
    payment_id: str
    order_id: Optional[str] = None
    customer_id: str
    customer_email: Optional[str] = None
    customer_phone: Optional[str] = None
    customer_name: Optional[str] = None
    amount: float
    currency: str = "INR"
    payment_method: Optional[str] = "card"
    failure_code: Optional[str] = None
    failure_reason: Optional[str] = None
    issuing_bank: Optional[str] = None
    attempt_count: int = 1


class CaseCreate(CaseBase):
    raw_payload: Optional[Dict[str, Any]] = None
    metadata_json: Optional[Dict[str, Any]] = None
    experiment_id: Optional[str] = None
    experiment_group: Optional[str] = None


class CaseUpdate(BaseModel):
    status: Optional[str] = None
    final_decision: Optional[str] = None
    recommended_action: Optional[str] = None
    executed_action: Optional[str] = None
    policy_status: Optional[str] = None


class CaseResponse(CaseBase):
    id: str
    status: str
    final_decision: Optional[str] = None
    recommended_action: Optional[str] = None
    executed_action: Optional[str] = None
    policy_status: Optional[str] = None
    natural_recovery_prob: Optional[float] = None
    best_action_recovery_prob: Optional[float] = None
    incremental_lift: Optional[float] = None
    expected_incremental_contribution: Optional[float] = None
    decision_confidence: Optional[float] = None
    decision_reason: Optional[str] = None
    experiment_id: Optional[str] = None
    experiment_group: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CaseDetailResponse(CaseResponse):
    contexts: Optional[List[Dict[str, Any]]] = None
    decisions: Optional[List[Dict[str, Any]]] = None
    action_executions: Optional[List[Dict[str, Any]]] = None
    outcomes: Optional[List[Dict[str, Any]]] = None
    policy_evaluations: Optional[List[Dict[str, Any]]] = None
