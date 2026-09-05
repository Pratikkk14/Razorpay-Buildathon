"""Domain randomization and synthetic event generation."""
import random
from typing import Dict, Any, List, Optional


FAILURE_TYPES = [
    ("GATEWAY_TIMEOUT", "technical", 0.70),
    ("BANK_DOWNTIME", "technical", 0.75),
    ("INSUFFICIENT_FUNDS", "funds", 0.15),
    ("CARD_DECLINED", "funds", 0.18),
    ("OTP_EXPIRED", "auth", 0.35),
    ("3DS_AUTH_FAILED", "auth", 0.32),
    ("INVALID_CARD", "technical", 0.05),
    ("USER_CANCELLED", "user_cancelled", 0.20),
]

PAYMENT_METHODS = ["upi", "card", "netbanking", "wallet"]
CUSTOMER_NAMES = [
    "Rajesh Kumar", "Sneha Rao", "Vikram Malhotra", "Ananya Deshmukh",
    "Arjun Singhania", "Pooja Hegde", "Siddharth Sen", "Deepika Iyer",
    "Manish Agarwal", "Kavita Reddy", "Harish Pillai", "Meera Joshi",
    "Acme Corp", "Zeta Technologies", "Nexus Logistics", "Apex Ventures"
]


def generate_synthetic_case(seed_id: int, random_state: Optional[random.Random] = None) -> Dict[str, Any]:
    """Generates a realistic synthetic failed payment case."""
    rng = random_state or random.Random(seed_id)
    
    fail_code, fail_cat, base_nat = rng.choice(FAILURE_TYPES)
    method = rng.choice(PAYMENT_METHODS)
    name = rng.choice(CUSTOMER_NAMES)
    
    # Amount distribution: mostly ₹500 to ₹10,000, with occasional high-value up to ₹85,000
    if rng.random() < 0.08:
        amount = round(rng.uniform(50000.0, 95000.0), 2)
        segment = "enterprise"
    elif rng.random() < 0.30:
        amount = round(rng.uniform(5000.0, 25000.0), 2)
        segment = "vip" if rng.random() < 0.5 else "standard"
    else:
        amount = round(rng.uniform(499.0, 4999.0), 2)
        segment = "standard"

    tenure_days = rng.randint(5, 730)
    attempts = 1 if rng.random() < 0.80 else rng.randint(2, 3)
    is_opted_out = 1 if rng.random() < 0.05 else 0
    is_disputed = 1 if rng.random() < 0.02 else 0
    hours_contact = rng.uniform(1.0, 72.0) if rng.random() < 0.25 else None

    return {
        "payment_id": f"pay_sim_{seed_id:06d}",
        "customer_id": f"cust_sim_{rng.randint(100, 999)}",
        "customer_name": name,
        "customer_email": f"{name.lower().replace(' ', '.')}@example.com",
        "customer_phone": f"+9198{rng.randint(10000000, 99999999)}",
        "amount": amount,
        "currency": "INR",
        "payment_method": method,
        "failure_code": fail_code,
        "failure_reason": f"Synthetic simulation failure: {fail_code}",
        "attempt_count": attempts,
        "context_features": {
            "customer_tenure_days": tenure_days,
            "customer_ltv": round(amount * rng.uniform(2.0, 8.0), 2),
            "customer_segment": segment,
            "total_lifetime_payments": rng.randint(1, 20),
            "successful_lifetime_payments": rng.randint(0, 19),
            "failed_lifetime_payments": attempts,
            "is_opted_out": is_opted_out,
            "is_disputed": is_disputed,
            "hours_since_last_contact": hours_contact,
        }
    }
