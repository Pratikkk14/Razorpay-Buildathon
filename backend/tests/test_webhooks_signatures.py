"""Tests for Razorpay Webhook signature verification."""
import json
from app.core.security import generate_razorpay_signature, verify_razorpay_signature
from app.core.config import settings


def test_signature_generation_and_verification():
    secret = "my_super_secret_webhook_key"
    payload = b'{"event":"payment.failed","payload":{"payment":{"entity":{"id":"pay_123"}}}}'
    
    sig = generate_razorpay_signature(payload, secret)
    assert len(sig) == 64
    assert verify_razorpay_signature(payload, sig, secret) is True
    
    # Tampered payload fails
    tampered_payload = b'{"event":"payment.failed","payload":{"payment":{"entity":{"id":"pay_999"}}}}'
    assert verify_razorpay_signature(tampered_payload, sig, secret) is False
    
    # Bad signature fails
    assert verify_razorpay_signature(payload, "0" * 64, secret) is False


def test_webhook_endpoint_rejects_invalid_signature(client):
    secret = settings.RAZORPAY_WEBHOOK_SECRET
    payload = json.dumps({
        "event": "payment.failed",
        "payload": {"payment": {"entity": {"id": "pay_test_invalid_sig", "amount": 250000}}}
    }).encode("utf-8")
    
    bad_sig = "a" * 64
    response = client.post(
        "/api/webhooks/razorpay",
        content=payload,
        headers={"Content-Type": "application/json", "X-Razorpay-Signature": bad_sig}
    )
    assert response.status_code == 400
    assert "Invalid Razorpay webhook signature" in response.json()["detail"]


def test_webhook_endpoint_accepts_valid_signature(client):
    secret = settings.RAZORPAY_WEBHOOK_SECRET
    payload = json.dumps({
        "event": "payment.failed",
        "payload": {
            "payment": {
                "entity": {
                    "id": "pay_test_valid_sig_101",
                    "amount": 150000,
                    "currency": "INR",
                    "method": "upi",
                    "error_code": "GATEWAY_TIMEOUT"
                }
            }
        }
    }).encode("utf-8")
    
    valid_sig = generate_razorpay_signature(payload, secret)
    response = client.post(
        "/api/webhooks/razorpay",
        content=payload,
        headers={"Content-Type": "application/json", "X-Razorpay-Signature": valid_sig}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "PROCESSED_FAILED_PAYMENT"
    assert data["case_id"] is not None
