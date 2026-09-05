"""Economic allocation and financial optimization schemas."""
from typing import List, Optional
from pydantic import BaseModel, Field


class CostConfig(BaseModel):
    """Configuration for action costs, incentive costs, and friction costs."""
    retry_action_cost: float = 0.50             # ₹0.50 per payment retry attempt
    payment_link_cost: float = 2.00             # ₹2.00 per SMS/WhatsApp link dispatch
    reminder_cost: float = 0.75                 # ₹0.75 per reminder notification
    alternate_method_cost: float = 1.50         # ₹1.50 per alternate method prompt
    human_escalation_cost: float = 150.00       # ₹150.00 support agent labor cost
    no_action_cost: float = 0.00

    # Friction / customer fatigue costs
    retry_friction_cost: float = 0.10
    payment_link_friction_cost: float = 1.00
    reminder_friction_cost: float = 0.50
    alternate_method_friction_cost: float = 0.80
    human_escalation_friction_cost: float = 0.00
    no_action_friction_cost: float = 0.00


class CandidateActionScore(BaseModel):
    """Full economic score for a single candidate action."""
    action_type: str  # RETRY, PAYMENT_LINK, REMINDER, ALTERNATE_METHOD, HUMAN_ESCALATION, NO_ACTION
    
    natural_recovery_prob: float
    action_recovery_prob: float
    incremental_lift: float
    
    payment_amount: float
    expected_recovery_value: float          # action_recovery_prob * payment_amount
    expected_incremental_revenue: float     # incremental_lift * payment_amount
    
    action_cost: float
    incentive_cost: float = 0.0
    friction_cost: float = 0.0
    total_cost: float
    
    expected_incremental_contribution: float  # expected_incremental_revenue - total_cost
    
    policy_allowed: bool = True
    policy_block_reason: Optional[str] = None
    
    rank: int = 1
    is_selected: bool = False


class EconomicOptimizationResult(BaseModel):
    """Overall economic evaluation output."""
    case_id: str
    payment_amount: float
    candidate_actions: List[CandidateActionScore]
    best_action: Optional[CandidateActionScore] = None
    highest_contribution_action: Optional[CandidateActionScore] = None
    highest_recovery_action: Optional[CandidateActionScore] = None
    is_positive_contribution: bool = False
