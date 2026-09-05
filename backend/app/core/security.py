"""Security utilities: HMAC-SHA256 signature verification for Razorpay webhooks."""
import hmac
import hashlib
import logging
from typing import Union

logger = logging.getLogger(__name__)


def generate_razorpay_signature(payload: Union[bytes, str], secret: str) -> str:
    """
    Generate an HMAC-SHA256 signature for a payload using the secret.
    Always operates on raw bytes to ensure exact signature matching.
    """
    if isinstance(payload, str):
        payload_bytes = payload.encode("utf-8")
    else:
        payload_bytes = payload
    secret_bytes = secret.encode("utf-8")
    return hmac.new(secret_bytes, payload_bytes, hashlib.sha256).hexdigest()


def verify_razorpay_signature(payload_bytes: bytes, signature: str, secret: str) -> bool:
    """
    Verify Razorpay webhook signature in constant time using hmac.compare_digest
    to prevent timing attacks. Computes the HMAC over the raw request bytes.
    """
    if not signature or not secret:
        return False
    expected_signature = generate_razorpay_signature(payload_bytes, secret)
    return hmac.compare_digest(expected_signature, signature)
