"""End-to-end payment failure lifecycle test."""
import json
from app.core.security import generate_razorpay_signature
from app.core.config import settings


def test_full_lifecycle_webhook_to_execution_and_recovery(client):
    secret = settings.RAZORPAY_WEBHOOK_SECRET

    # Step 1: Payment Fails -> Webhook delivered
    failed_event = {
        "event": "payment.failed",
        "payload": {
            "payment": {
                "entity": {
                    "id": "pay_e2e_lifecycle_123",
                    "amount": 499900,  # ₹4,999.00
                    "currency": "INR",
                    "method": "card",
                    "error_code": "INSUFFICIENT_FUNDS",
                    "error_description": "Card balance insufficient",
                    "contact": "+919876543210",
                    "email": "e2e_user@example.com"
                }
            }
        }
    }
    raw_failed = json.dumps(failed_event).encode("utf-8")
    sig = generate_razorpay_signature(raw_failed, secret)

    resp_fail = client.post(
        "/api/webhooks/razorpay",
        content=raw_failed,
        headers={"Content-Type": "application/json", "X-Razorpay-Signature": sig}
    )
    assert resp_fail.status_code == 200
    case_id = resp_fail.json()["case_id"]
    assert case_id is not None

    # Step 2: Query case details & verify decision
    case_resp = client.get(f"/api/cases/{case_id}")
    assert case_resp.status_code == 200
    case_data = case_resp.json()
    assert case_data["amount"] == 4999.0
    assert case_data["final_decision"] in ["ACT", "WAIT"]
    assert case_data["recommended_action"] is not None

    # Step 3: Execute Action
    exec_resp = client.post(
        "/api/actions/execute",
        json={"case_id": case_id, "action_type": case_data["recommended_action"]}
    )
    assert exec_resp.status_code == 200
    assert exec_resp.json()["status"] == "SUCCESS"

    # Step 4: Customer Pays via Generated Link -> payment.captured webhook delivered
    captured_event = {
        "event": "payment.captured",
        "payload": {
            "payment": {
                "entity": {
                    "id": "pay_e2e_lifecycle_123",
                    "amount": 499900,
                    "currency": "INR",
                    "method": "card",
                    "status": "captured"
                }
            }
        }
    }
    raw_captured = json.dumps(captured_event).encode("utf-8")
    sig_cap = generate_razorpay_signature(raw_captured, secret)

    resp_cap = client.post(
        "/api/webhooks/razorpay",
        content=raw_captured,
        headers={"Content-Type": "application/json", "X-Razorpay-Signature": sig_cap}
    )
    assert resp_cap.status_code == 200
    assert resp_cap.json()["status"] == "RECORDED_RECOVERY"

    # Step 5: Check Case status is now RECOVERED
    final_case_resp = client.get(f"/api/cases/{case_id}")
    assert final_case_resp.json()["status"] == "RECOVERED"
