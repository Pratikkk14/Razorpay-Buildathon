"""Decisions API routes."""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.core.database import get_db
from app.models.case import Case
from app.services.context.aggregator import ContextAggregator
from app.services.ml.registry import get_ml_service
from app.services.decision.decision_engine import DecisionEngine
from app.schemas.decision import DecisionOutput, DecisionExplanation

router = APIRouter(prefix="/decisions", tags=["Decisions"])


@router.post("/evaluate/{case_id}", response_model=DecisionOutput)
def evaluate_case_decision(
    case_id: str,
    simulated_hour: Optional[int] = Query(None, description="Simulate specific hour (0-23) for quiet hours check"),
    db: Session = Depends(get_db)
):
    """
    Triggers on-demand evaluation of a recovery case through Context -> ML -> Economics -> Policy -> Decision.
    """
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail=f"Case '{case_id}' not found.")

    context = ContextAggregator.aggregate_context(db, case)
    ml_service = get_ml_service()
    ml_input = ContextAggregator.to_ml_input(case, context)
    prediction = ml_service.predict(ml_input)

    dec_engine = DecisionEngine()
    decision_out = dec_engine.evaluate_and_decide(
        db=db,
        case=case,
        context=context,
        prediction=prediction,
        simulated_hour=simulated_hour
    )

    return decision_out


@router.get("/explain/{case_id}", response_model=DecisionExplanation)
def explain_decision(case_id: str, db: Session = Depends(get_db)):
    """
    Provides an explainability breakdown of why a decision was reached for a case.
    """
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail=f"Case '{case_id}' not found.")

    decision_rec = case.decisions[-1] if case.decisions else None
    if not decision_rec:
        # Evaluate now if not yet evaluated
        context = ContextAggregator.aggregate_context(db, case)
        prediction = get_ml_service().predict(ContextAggregator.to_ml_input(case, context))
        DecisionEngine().evaluate_and_decide(db, case, context, prediction)
        db.refresh(case)
        decision_rec = case.decisions[-1]

    candidates = [
        {
            "action": ca.action_type,
            "natural_prob": ca.natural_recovery_prob,
            "action_prob": ca.action_recovery_prob,
            "lift": ca.incremental_lift,
            "expected_incremental_revenue": ca.expected_incremental_revenue,
            "total_cost": ca.total_cost,
            "net_contribution": ca.expected_incremental_contribution,
            "policy_allowed": bool(ca.policy_allowed),
            "policy_block_reason": ca.policy_block_reason
        }
        for ca in decision_rec.candidate_actions
    ]

    policies = [
        {
            "rule_name": p.rule_name,
            "passed": p.passed,
            "veto_reason": p.veto_reason
        }
        for p in case.policy_evaluations
    ]

    return DecisionExplanation(
        case_id=case.id,
        decision=decision_rec.decision,
        action=decision_rec.recommended_action,
        why_this_decision=decision_rec.decision_reason,
        natural_recovery_rationale=f"Estimated natural recovery probability is {decision_rec.natural_recovery_prob*100:.1f}%.",
        economic_breakdown={
            "expected_incremental_revenue": decision_rec.expected_incremental_revenue,
            "expected_action_cost": decision_rec.expected_action_cost,
            "expected_friction_cost": decision_rec.expected_friction_cost,
            "expected_incremental_contribution": decision_rec.expected_incremental_contribution,
        },
        safety_checks_applied=policies,
        alternative_actions_considered=candidates
    )
