"""Governance and Safety API routes."""
from typing import List, Dict, Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.core.database import get_db
from app.models.policy import PolicyEvaluationRecord
from app.models.case import Case
from app.core.config import settings

router = APIRouter(prefix="/governance", tags=["Governance"])


@router.get("/rules")
def list_governance_rules():
    """Lists all active deterministic policy rules and their current operational thresholds."""
    return [
        {
            "rule_key": "MAX_RETRY_LIMIT",
            "rule_name": "Bounded Retry Limit",
            "description": "Caps automated recurring retries to avoid unnecessary payment gateway charges and bank penalty flags.",
            "is_active": True,
            "threshold": f"Max {settings.DEFAULT_MAX_RETRIES} attempts"
        },
        {
            "rule_key": "CUSTOMER_OPT_OUT",
            "rule_name": "DND & Customer Opt-Out",
            "description": "Strictly suppresses outbound SMS/WhatsApp/email recovery messages for users on the DND registry.",
            "is_active": True,
            "threshold": "100% suppression on opt-out flag"
        },
        {
            "rule_key": "CONTACT_FREQUENCY_COOLDOWN",
            "rule_name": "Contact Cooldown Window",
            "description": "Mandates a minimum cooldown window between recovery communications to prevent customer fatigue.",
            "is_active": True,
            "threshold": f"{settings.DEFAULT_COOLDOWN_HOURS} hours minimum cooldown"
        },
        {
            "rule_key": "QUIET_HOURS",
            "rule_name": "Quiet Hours Compliance",
            "description": "Holds outbound customer outreach between 9:00 PM and 9:00 AM local time, scheduling delivery for the morning window.",
            "is_active": True,
            "threshold": f"{settings.DEFAULT_QUIET_HOURS_START}:00 - {settings.DEFAULT_QUIET_HOURS_END}:00 local"
        },
        {
            "rule_key": "HIGH_VALUE_TRANSACTION_ESCALATION",
            "rule_name": "High-Value Transaction White-Glove Gate",
            "description": "Vetoes generic automated bots for high-ticket transactions, immediately routing cases to VIP support agents.",
            "is_active": True,
            "threshold": f"> ₹{settings.DEFAULT_HIGH_VALUE_THRESHOLD:,.2f}"
        },
        {
            "rule_key": "FRAUD_DISPUTE_SUPPRESSION",
            "rule_name": "Dispute & Fraud Investigation Gate",
            "description": "Freezes all collection actions on payments currently subject to chargebacks or fraud alerts.",
            "is_active": True,
            "threshold": "Dispute/Fraud active flag"
        },
        {
            "rule_key": "MIN_CONTRIBUTION_FLOOR",
            "rule_name": "Positive Incremental ROI Constraint",
            "description": "Vetoes any action whose expected incremental revenue fails to cover channel delivery and customer friction costs.",
            "is_active": True,
            "threshold": f"> ₹{settings.DEFAULT_MIN_CONTRIBUTION_FLOOR:.2f} net contribution"
        }
    ]


@router.get("/veto-logs")
def list_safety_veto_logs(limit: int = 50, db: Session = Depends(get_db)):
    """Lists all cases where AI recommendations were vetoed or modified by deterministic safety guardrails."""
    vetoed_evals = db.query(PolicyEvaluationRecord).filter(
        PolicyEvaluationRecord.passed == False
    ).order_by(desc(PolicyEvaluationRecord.created_at)).limit(limit).all()

    return [
        {
            "id": v.id,
            "case_id": v.case_id,
            "rule_key": v.rule_key,
            "rule_name": v.rule_name,
            "action_targeted": v.action_targeted,
            "veto_reason": v.veto_reason,
            "details": v.evaluation_details,
            "timestamp": v.created_at.isoformat() + "Z"
        }
        for v in vetoed_evals
    ]
