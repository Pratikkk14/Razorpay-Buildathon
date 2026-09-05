"""Tests for Webhook and Case Idempotency."""
import json
from app.core.security import generate_razorpay_signature
from app.core.config import settings


def test_duplicate_webhook_event_idempotency(client):
    secret = settings.RAZORPAY_WEBHOOK_SECRET
    payload_dict = {
        "event": "payment.failed",
        "payload": {
            "payment": {
                "entity": {
                    "id": "pay_idempotency_test_999",
                    "amount": 299900,
                    "currency": "INR",
                    "method": "card",
                    "error_code": "INSUFFICIENT_FUNDS"
                }
            }
        }
    }
    payload_bytes = json.dumps(payload_dict).encode("utf-8")
    sig = generate_razorpay_signature(payload_bytes, secret)

    # First delivery
    resp1 = client.post(
        "/api/webhooks/razorpay",
        content=payload_bytes,
        headers={"Content-Type": "application/json", "X-Razorpay-Signature": sig}
    )
    assert resp1.status_code == 200
    assert resp1.json()["status"] == "PROCESSED_FAILED_PAYMENT"
    case_id = resp1.json()["case_id"]

    # Duplicate delivery with exact same payment ID
    resp2 = client.post(
        "/api/webhooks/razorpay",
        content=payload_bytes,
        headers={"Content-Type": "application/json", "X-Razorpay-Signature": sig}
    )
    assert resp2.status_code == 200
    assert resp2.json()["status"] == "DUPLICATE"
    assert resp2.json()["case_id"] == case_id
