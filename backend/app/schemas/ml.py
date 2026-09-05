"""Machine Learning inference contract schemas."""
from typing import Dict, Optional, Any
from pydantic import BaseModel, Field


class MLModelInput(BaseModel):
    """
    Standardized, clean input contract fed to any ML Model Service.
    Decoupled from internal database schemas.
    """
    case_id: str
    amount: float
    currency: str = "INR"
    payment_method: str = "card"
    failure_code: Optional[str] = None
    issuing_bank: Optional[str] = None
    attempt_count: int = 1
    
    # Customer history & behavior features
    customer_tenure_days: int = 30
    customer_ltv: float = 0.0
    customer_segment: str = "standard"
    total_lifetime_payments: int = 1
    successful_lifetime_payments: int = 0
    failed_lifetime_payments: int = 1
    days_since_last_success: Optional[int] = None
    is_first_ever_failure: int = 0
    
    # Timing & channel features
    time_since_failure_minutes: float = 0.0
    previous_interventions_count: int = 0
    hours_since_last_contact: Optional[float] = None
    device_type: str = "mobile_android"
    
    # Extensible raw metadata map for future model features
    additional_features: Optional[Dict[str, Any]] = None


class MLModelPrediction(BaseModel):
    """
    Standardized prediction output returned by any ML Model Service implementation.
    """
    model_name: str = "MockPropensityUplift"
    model_version: str = "1.0.0"
    
    # Natural recovery probability P(recovery | no intervention)
    natural_recovery_probability: float = Field(..., ge=0.0, le=1.0)
    
    # Probability of recovery given each intervention action P(recovery | action)
    action_outcomes: Dict[str, float] = Field(
        default_factory=dict,
        description="Predicted recovery probability for each candidate action"
    )
    
    # Uplift = action_outcomes[action] - natural_recovery_probability
    uplift: Dict[str, float] = Field(
        default_factory=dict,
        description="Incremental lift predicted for each candidate action"
    )
    
    # Model confidence score in [0, 1]
    confidence: float = Field(default=0.85, ge=0.0, le=1.0)
    
    # Diagnostics & feature importance if provided by model
    explanation_notes: Optional[str] = None
    feature_attributions: Optional[Dict[str, float]] = None
