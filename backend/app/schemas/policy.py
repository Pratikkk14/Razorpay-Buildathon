"""Policy rules and safety evaluation schemas."""
from typing import Optional, Dict, Any, List
from pydantic import BaseModel


class PolicyRuleSchema(BaseModel):
    rule_key: str
    rule_name: str
    description: Optional[str] = None
    is_active: bool = True
    parameters: Optional[Dict[str, Any]] = None


class PolicyCheckResult(BaseModel):
    rule_key: str
    rule_name: str
    passed: bool
    action_targeted: Optional[str] = None
    veto_reason: Optional[str] = None
    details: Optional[Dict[str, Any]] = None


class PolicyEvaluationSummary(BaseModel):
    case_id: str
    overall_status: str  # APPROVED, VETOED, SUPPRESSED, ESCALATED
    allowed_actions: List[str]
    blocked_actions: Dict[str, str]  # action -> reason
    rule_results: List[PolicyCheckResult]
    veto_reason: Optional[str] = None
