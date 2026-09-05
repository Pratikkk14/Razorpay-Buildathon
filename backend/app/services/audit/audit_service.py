"""Audit Service: Records immutable audit events."""
import logging
from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.audit_event import AuditEvent

logger = logging.getLogger(__name__)


class AuditService:
    """Manages append-only immutable audit logging."""

    @staticmethod
    def log_event(
        db: Session,
        event_type: str,
        summary: str,
        case_id: Optional[str] = None,
        payment_id: Optional[str] = None,
        actor: str = "SYSTEM",
        details: Optional[Dict[str, Any]] = None
    ) -> AuditEvent:
        """Appends a new audit log event."""
        event = AuditEvent(
            timestamp=datetime.utcnow(),
            case_id=case_id,
            payment_id=payment_id,
            event_type=event_type,
            actor=actor,
            summary=summary,
            details=details or {}
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        return event
