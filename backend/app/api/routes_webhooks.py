"""Razorpay Webhook receiver API routes with HMAC-SHA256 signature verification."""
import logging
import json
from fastapi import APIRouter, Depends, Header, Request, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional

from app.core.database import get_db
from app.core.config import settings
from app.core.security import verify_razorpay_signature
from app.integrations.razorpay.webhooks import RazorpayWebhookProcessor
from app.schemas.webhook import WebhookIngestResult

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/webhooks", tags=["Webhooks"])


@router.post("/razorpay", response_model=WebhookIngestResult)
async def ingest_razorpay_webhook(
    request: Request,
    x_razorpay_signature: Optional[str] = Header(None, alias="X-Razorpay-Signature"),
    db: Session = Depends(get_db)
):
    """
    Ingests live or simulated Razorpay webhooks.
    Validates HMAC-SHA256 signature over raw request bytes before writing to database.
    """
    raw_body = await request.body()
    
    # 1. Signature Verification Check
    # If a signature is provided, verify it strictly against the webhook secret
    if x_razorpay_signature is not None:
        is_valid = verify_razorpay_signature(
            payload_bytes=raw_body,
            signature=x_razorpay_signature,
            secret=settings.RAZORPAY_WEBHOOK_SECRET
        )
        if not is_valid:
            logger.warning("Rejected webhook due to invalid HMAC-SHA256 signature.")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid Razorpay webhook signature"
            )
    elif not settings.SIMULATION_MODE and not settings.DEBUG:
        # In strict non-debug production mode, missing signature is an error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing X-Razorpay-Signature header"
        )

    # 2. Parse payload
    try:
        payload_data = json.loads(raw_body.decode("utf-8"))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Malformed JSON payload: {str(e)}"
        )

    # 3. Process event
    status_code, result = RazorpayWebhookProcessor.process_event(db, payload_data, auto_execute=False)

    return WebhookIngestResult(
        status=status_code,
        event=payload_data.get("event", "unknown"),
        case_id=result.get("case_id"),
        action_taken=result.get("recommended_action") or result.get("decision"),
        message=f"Event {payload_data.get('event')} processed successfully ({status_code})"
    )
