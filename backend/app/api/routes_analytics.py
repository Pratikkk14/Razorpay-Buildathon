"""Analytics and Dashboard KPI routes."""
from typing import Dict, Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.core.database import get_db
from app.models.case import Case
from app.models.action_execution import ActionExecutionRecord
from app.models.outcome import OutcomeRecord
from app.models.audit_event import AuditEvent
from app.schemas.analytics import (
    AnalyticsOverview,
    DashboardKPIs,
    ActionPerformance,
    LiftDistributionBucket
)

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/overview", response_model=AnalyticsOverview)
def get_analytics_overview(db: Session = Depends(get_db)):
    """Computes all aggregate executive KPIs, action performance breakdowns, and lift distributions."""
    cases = db.query(Case).all()
    executions = db.query(ActionExecutionRecord).all()
    outcomes = db.query(OutcomeRecord).all()
    recent_events = db.query(AuditEvent).order_by(desc(AuditEvent.timestamp)).limit(10).all()

    total_cases = len(cases)
    
    # Revenue at risk: sum of all failed payment amounts
    revenue_at_risk = sum(c.amount for c in cases)
    
    # Expected recoverable revenue = sum(amount * best_action_recovery_prob)
    expected_recoverable = sum(c.amount * (c.best_action_recovery_prob or 0.0) for c in cases)
    
    # Total incremental contribution = sum(expected_incremental_contribution for active/recommended/executed)
    total_contrib = sum(c.expected_incremental_contribution or 0.0 for c in cases if c.final_decision in ["ACT", "RECOVERED"])
    
    # Gross recovery
    recovered_cases = sum(1 for c in cases if c.status == "RECOVERED")
    gross_recovery_rate = (recovered_cases / total_cases * 100) if total_cases > 0 else 0.0
    
    # Lift
    valid_lifts = [c.incremental_lift for c in cases if c.incremental_lift is not None and c.final_decision == "ACT"]
    avg_lift = (sum(valid_lifts) / len(valid_lifts) * 100) if valid_lifts else 0.0
    
    # Costs
    total_cost = sum(ex.cost_incurred for ex in executions)
    
    # Active & Suppressed
    active_cases = sum(1 for c in cases if c.status in ["NEW", "ANALYZING", "WAITING", "ACTION_RECOMMENDED", "ACTION_EXECUTED"])
    suppressed_cases = sum(1 for c in cases if c.policy_status in ["VETOED", "SUPPRESSED"])

    kpis = DashboardKPIs(
        revenue_at_risk=round(revenue_at_risk, 2),
        expected_recoverable_revenue=round(expected_recoverable, 2),
        total_incremental_contribution=round(total_contrib, 2),
        gross_recovery_rate_pct=round(gross_recovery_rate, 2),
        average_incremental_lift_pct=round(avg_lift, 2),
        total_intervention_cost=round(total_cost, 2),
        active_recovery_cases=active_cases,
        cases_suppressed_by_safety=suppressed_cases,
        recovered_cases_count=recovered_cases,
        total_cases_analyzed=total_cases
    )

    # Action performance breakdown
    action_types = ["RETRY", "PAYMENT_LINK", "REMINDER", "ALTERNATE_METHOD", "HUMAN_ESCALATION"]
    actions_breakdown: List[ActionPerformance] = []
    
    for act in action_types:
        act_execs = [ex for ex in executions if ex.action_type == act]
        count = len(act_execs)
        act_costs = sum(ex.cost_incurred for ex in act_execs)
        act_cases = [c for c in cases if c.executed_action == act]
        rec_count = sum(1 for c in act_cases if c.status == "RECOVERED")
        succ_rate = (rec_count / len(act_cases) * 100) if act_cases else 0.0
        act_contrib = sum(c.expected_incremental_contribution or 0.0 for c in act_cases)

        actions_breakdown.append(
            ActionPerformance(
                action_type=act,
                count_executed=count,
                success_rate_pct=round(succ_rate, 2),
                total_cost=round(act_costs, 2),
                net_contribution=round(act_contrib, 2)
            )
        )

    # Lift distribution
    buckets = [
        {"label": "0 - 10%", "min": 0.0, "max": 0.10, "cases": []},
        {"label": "10 - 25%", "min": 0.10, "max": 0.25, "cases": []},
        {"label": "25 - 50%", "min": 0.25, "max": 0.50, "cases": []},
        {"label": "50%+", "min": 0.50, "max": 1.00, "cases": []}
    ]
    for c in cases:
        lift = c.incremental_lift or 0.0
        for b in buckets:
            if b["min"] <= lift < b["max"] or (b["label"] == "50%+" and lift >= 0.50):
                b["cases"].append(c)
                break

    lift_dist = [
        LiftDistributionBucket(
            bucket_label=b["label"],
            case_count=len(b["cases"]),
            avg_contribution=round(sum(c.expected_incremental_contribution or 0.0 for c in b["cases"]) / len(b["cases"]), 2) if b["cases"] else 0.0
        )
        for b in buckets
    ]

    recent_act = [
        {
            "id": e.id,
            "timestamp": e.timestamp.isoformat() + "Z",
            "event_type": e.event_type,
            "summary": e.summary,
            "actor": e.actor
        }
        for e in recent_events
    ]

    return AnalyticsOverview(
        kpis=kpis,
        actions_breakdown=actions_breakdown,
        lift_distribution=lift_dist,
        recent_activity=recent_act
    )
