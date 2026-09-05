"""Analytics and Dashboard KPI schemas."""
from typing import Dict, List, Any, Optional
from pydantic import BaseModel


class DashboardKPIs(BaseModel):
    revenue_at_risk: float
    expected_recoverable_revenue: float
    total_incremental_contribution: float
    gross_recovery_rate_pct: float
    average_incremental_lift_pct: float
    total_intervention_cost: float
    active_recovery_cases: int
    cases_suppressed_by_safety: int
    recovered_cases_count: int
    total_cases_analyzed: int


class ActionPerformance(BaseModel):
    action_type: str
    count_executed: int
    success_rate_pct: float
    total_cost: float
    net_contribution: float


class LiftDistributionBucket(BaseModel):
    bucket_label: str  # e.g., "0-10%", "10-25%", "25-50%", "50%+"
    case_count: int
    avg_contribution: float


class AnalyticsOverview(BaseModel):
    kpis: DashboardKPIs
    actions_breakdown: List[ActionPerformance]
    lift_distribution: List[LiftDistributionBucket]
    recent_activity: List[Dict[str, Any]]
