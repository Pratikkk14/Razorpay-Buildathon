"""Decision schemas and explainability contracts."""
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from app.schemas.economics import CandidateActionScore


class DecisionOutput(BaseModel):
    case_id: str
    decision: str                           # ACT, WAIT, DONT_ACT, ESCALATE
    recommended_action: Optional[str] = None # RETRY, PAYMENT_LINK, REMINDER, ALTERNATE_METHOD, HUMAN_ESCALATION, NO_ACTION
    recommended_timing: str = "IMMEDIATE"   # IMMEDIATE, DELAY_1H, DELAY_4H, DELAY_24H, NEXT_QUIET_HOURS_END
    
    # Financial & uplift attributes
    incremental_lift: Optional[float] = None
    expected_incremental_revenue: Optional[float] = None
    expected_incremental_contribution: Optional[float] = None
    confidence: float
    
    # Governance & Policy status
    policy_status: str                      # APPROVED, VETOED, SUPPRESSED, ESCALATED
    policy_reason: Optional[str] = None
    
    # Reasoning
    reason: str
    candidate_actions: List[CandidateActionScore] = []
    
    # ML details
    ml_model_name: str
    ml_model_version: str
    natural_recovery_prob: float


class DecisionExplanation(BaseModel):
    case_id: str
    decision: str
    action: Optional[str]
    why_this_decision: str
    natural_recovery_rationale: str
    economic_breakdown: Dict[str, Any]
    safety_checks_applied: List[Dict[str, Any]]
    alternative_actions_considered: List[Dict[str, Any]]
