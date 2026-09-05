"""Simulator and Scenario schemas."""
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field


class SimulatorConfig(BaseModel):
    """Configurable environment parameters for recovery simulation."""
    num_cases: int = Field(default=100, ge=1, le=10000)
    natural_recovery_multiplier: float = Field(default=1.0, ge=0.1, le=3.0)
    payment_link_effectiveness: float = Field(default=1.0, ge=0.1, le=3.0)
    retry_effectiveness: float = Field(default=1.0, ge=0.1, le=3.0)
    reminder_effectiveness: float = Field(default=1.0, ge=0.1, le=3.0)
    customer_fatigue_penalty: float = Field(default=0.15, ge=0.0, le=0.9)
    avg_payment_amount: float = Field(default=3500.0, ge=100.0, le=500000.0)
    seed: Optional[int] = 42


class ScenarioDefinition(BaseModel):
    """Canonical test or demo scenario."""
    scenario_id: str
    title: str
    description: str
    customer_name: str
    amount: float
    payment_method: str
    failure_code: str
    failure_reason: str
    natural_recovery_rate: float
    expected_decision: str
    expected_action: Optional[str]
    expected_rationale: str
    context_features: Dict[str, Any]


class PolicyBenchmarkMetrics(BaseModel):
    """Aggregate metrics calculated for a simulated policy."""
    policy_name: str
    policy_description: str
    total_cases: int
    interventions_triggered: int
    interventions_suppressed_by_safety: int
    gross_recovered_cases: int
    gross_recovery_rate_pct: float
    gross_recovered_revenue: float
    natural_recovered_revenue: float
    true_incremental_revenue: float
    true_incremental_lift_pct: float
    total_intervention_cost: float
    net_incremental_contribution: float
    contribution_per_contacted_inr: float
    unnecessary_interventions_count: int  # Contacted someone who would have recovered naturally anyway


class MultiPolicyBenchmarkResult(BaseModel):
    """Side-by-side comparison of the 5 canonical policies."""
    simulation_id: str
    total_cases_simulated: int
    timestamp: str
    policies: Dict[str, PolicyBenchmarkMetrics]
    winner_policy: str
    incremental_value_generated_over_propensity: float
    unnecessary_contacts_avoided_count: int
