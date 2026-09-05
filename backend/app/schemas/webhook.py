"""Razorpay Webhook schemas."""
from typing import Optional, Dict, Any
from pydantic import BaseModel


class RazorpayWebhookPayload(BaseModel):
    event: str
    account_id: Optional[str] = None
    created_at: Optional[int] = None
    contains: Optional[list] = None
    payload: Dict[str, Any]


class WebhookIngestResult(BaseModel):
    status: str
    event: str
    case_id: Optional[str] = None
    action_taken: Optional[str] = None
    message: str
