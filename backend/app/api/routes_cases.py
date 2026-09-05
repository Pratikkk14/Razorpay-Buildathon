"""Cases API routes."""
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.core.database import get_db
from app.models.case import Case
from app.models.context import PaymentContext
from app.models.decision import DecisionRecord, CandidateActionEvaluation
from app.models.action_execution import ActionExecutionRecord
from app.models.outcome import OutcomeRecord
from app.models.policy import PolicyEvaluationRecord
from app.models.audit_event import AuditEvent
from app.schemas.case import CaseResponse, CaseDetailResponse, CaseCreate

router = APIRouter(prefix="/cases", tags=["Cases"])


@router.get("", response_model=List[CaseResponse])
def list_cases(
    status: Optional[str] = Query(None, description="Filter by case status"),
    decision: Optional[str] = Query(None, description="Filter by decision (ACT, WAIT, DONT_ACT, ESCALATE)"),
    search: Optional[str] = Query(None, description="Search by customer name, payment ID or ID"),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    """Lists recovery cases with filtering and pagination."""
    query = db.query(Case)
    if status:
        query = query.filter(Case.status == status.upper())
    if decision:
        query = query.filter(Case.final_decision == decision.upper())
    if search:
        search_pattern = f"%{search}%"
        query = query.filter(
            (Case.customer_name.ilike(search_pattern)) |
            (Case.payment_id.ilike(search_pattern)) |
            (Case.customer_id.ilike(search_pattern)) |
            (Case.failure_code.ilike(search_pattern))
        )
    return query.order_by(desc(Case.created_at)).offset(offset).limit(limit).all()


@router.get("/{case_id}", response_model=CaseDetailResponse)
def get_case_detail(case_id: str, db: Session = Depends(get_db)):
    """Retrieves full case details with related contexts, decisions, policy checks, executions, and outcomes."""
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail=f"Case '{case_id}' not found.")
    
    contexts = [
        {
            "id": c.id,
            "tenure_days": c.customer_tenure_days,
            "ltv": c.customer_ltv,
            "segment": c.customer_segment,
            "is_first_failure": c.is_first_ever_failure,
            "is_opted_out": c.is_opted_out,
            "hours_since_last_contact": c.hours_since_last_contact,
            "failure_category": c.failure_category
        }
        for c in case.contexts
    ]

    decisions = [
        {
            "id": d.id,
            "decision": d.decision,
            "recommended_action": d.recommended_action,
            "recommended_timing": d.recommended_timing,
            "incremental_lift": d.incremental_lift,
            "expected_incremental_contribution": d.expected_incremental_contribution,
            "natural_recovery_prob": d.natural_recovery_prob,
            "confidence": d.ml_confidence,
            "policy_status": d.policy_status,
            "policy_reason": d.policy_reason,
            "reason": d.decision_reason,
            "candidate_actions": [
                {
                    "action_type": ca.action_type,
                    "natural_recovery_prob": ca.natural_recovery_prob,
                    "action_recovery_prob": ca.action_recovery_prob,
                    "incremental_lift": ca.incremental_lift,
                    "action_cost": ca.action_cost,
                    "friction_cost": ca.friction_cost,
                    "total_cost": ca.total_cost,
                    "expected_incremental_contribution": ca.expected_incremental_contribution,
                    "policy_allowed": bool(ca.policy_allowed),
                    "policy_block_reason": ca.policy_block_reason,
                    "rank": ca.rank,
                    "is_selected": bool(ca.is_selected)
                }
                for ca in d.candidate_actions
            ]
        }
        for d in case.decisions
    ]

    executions = [
        {
            "id": ex.id,
            "action_type": ex.action_type,
            "gateway": ex.gateway,
            "gateway_reference_id": ex.gateway_reference_id,
            "payment_link_url": ex.payment_link_url,
            "status": ex.status,
            "cost_incurred": ex.cost_incurred,
            "executed_at": ex.executed_at.isoformat() if ex.executed_at else None
        }
        for ex in case.action_executions
    ]

    outcomes = [
        {
            "id": out.id,
            "is_recovered": out.is_recovered,
            "recovered_amount": out.recovered_amount,
            "attribution_type": out.attribution_type,
            "total_intervention_cost": out.total_intervention_cost,
            "net_incremental_contribution": out.net_incremental_contribution,
            "recovered_at": out.recovered_at.isoformat() if out.recovered_at else None
        }
        for out in case.outcomes
    ]

    policies = [
        {
            "id": p.id,
            "rule_key": p.rule_key,
            "rule_name": p.rule_name,
            "passed": p.passed,
            "action_targeted": p.action_targeted,
            "veto_reason": p.veto_reason
        }
        for p in case.policy_evaluations
    ]

    return CaseDetailResponse(
        id=case.id,
        payment_id=case.payment_id,
        order_id=case.order_id,
        customer_id=case.customer_id,
        customer_email=case.customer_email,
        customer_phone=case.customer_phone,
        customer_name=case.customer_name,
        amount=case.amount,
        currency=case.currency,
        payment_method=case.payment_method,
        failure_code=case.failure_code,
        failure_reason=case.failure_reason,
        issuing_bank=case.issuing_bank,
        attempt_count=case.attempt_count,
        status=case.status,
        final_decision=case.final_decision,
        recommended_action=case.recommended_action,
        executed_action=case.executed_action,
        policy_status=case.policy_status,
        natural_recovery_prob=case.natural_recovery_prob,
        best_action_recovery_prob=case.best_action_recovery_prob,
        incremental_lift=case.incremental_lift,
        expected_incremental_contribution=case.expected_incremental_contribution,
        decision_confidence=case.decision_confidence,
        decision_reason=case.decision_reason,
        experiment_id=case.experiment_id,
        experiment_group=case.experiment_group,
        created_at=case.created_at,
        updated_at=case.updated_at,
        contexts=contexts,
        decisions=decisions,
        action_executions=executions,
        outcomes=outcomes,
        policy_evaluations=policies
    )


@router.get("/{case_id}/timeline")
def get_case_timeline(case_id: str, db: Session = Depends(get_db)):
    """
    Returns the complete 8-step chronological audit timeline for a recovery case:
    1. Payment Failed
    2. Context Diagnosis
    3. ML Inference
    4. Candidate Actions Evaluated
    5. Economic Allocation Ranked
    6. Policy Guardrail Checks
    7. Decision Finalized
    8. Action Executed / Outcome Recorded
    """
    case = db.query(Case).filter(Case.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail=f"Case '{case_id}' not found.")

    audit_events = db.query(AuditEvent).filter(
        (AuditEvent.case_id == case_id) | (AuditEvent.payment_id == case.payment_id)
    ).order_by(AuditEvent.timestamp).all()

    events_data = [
        {
            "id": e.id,
            "timestamp": e.timestamp.isoformat() + "Z",
            "event_type": e.event_type,
            "actor": e.actor,
            "summary": e.summary,
            "details": e.details
        }
        for e in audit_events
    ]

    return {
        "case_id": case.id,
        "payment_id": case.payment_id,
        "amount": case.amount,
        "status": case.status,
        "final_decision": case.final_decision,
        "recommended_action": case.recommended_action,
        "executed_action": case.executed_action,
        "events": events_data
    }
