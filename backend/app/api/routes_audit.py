"""Audit Log API routes."""
from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.core.database import get_db
from app.models.audit_event import AuditEvent

router = APIRouter(prefix="/audit", tags=["Audit"])


@router.get("/events")
def list_audit_events(
    case_id: Optional[str] = Query(None),
    event_type: Optional[str] = Query(None),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    """Queries immutable system audit trail logs."""
    query = db.query(AuditEvent)
    if case_id:
        query = query.filter(AuditEvent.case_id == case_id)
    if event_type:
        query = query.filter(AuditEvent.event_type == event_type)

    events = query.order_by(desc(AuditEvent.timestamp)).offset(offset).limit(limit).all()

    return [
        {
            "id": e.id,
            "timestamp": e.timestamp.isoformat() + "Z",
            "case_id": e.case_id,
            "payment_id": e.payment_id,
            "event_type": e.event_type,
            "actor": e.actor,
            "summary": e.summary,
            "details": e.details
        }
        for e in events
    ]
