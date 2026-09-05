"""Mock ML Model Service implementation for realistic development & demo simulations."""
import logging
from typing import Dict, Any, Optional
from app.services.ml.interface import MLModelService
from app.schemas.ml import MLModelInput, MLModelPrediction

logger = logging.getLogger(__name__)


class MockMLModelService(MLModelService):
    """
    High-fidelity heuristic mock ML model service.
    Simulates propensity and uplift estimation across actions based on payment & customer features.
    Supports overrides for exact demo scenarios.
    """

    @property
    def model_name(self) -> str:
        return "MockPropensityUpliftV1"

    @property
    def model_version(self) -> str:
        return "1.0.0"

    def predict(self, input_data: MLModelInput) -> MLModelPrediction:
        """Generates realistic mock predictions for recovery actions."""
        # 1. Check for manual scenario override injection (used in seeded demos & tests)
        if input_data.additional_features:
            features = input_data.additional_features
            if "mock_natural_recovery" in features:
                natural_p = float(features["mock_natural_recovery"])
                actions = features.get("mock_action_outcomes", {
                    "retry": min(0.95, natural_p + 0.10),
                    "payment_link": min(0.95, natural_p + 0.35),
                    "reminder": min(0.95, natural_p + 0.20),
                    "alternate_method": min(0.95, natural_p + 0.25),
                    "human_escalation": min(0.98, natural_p + 0.40),
                })
                uplift = {act: round(p - natural_p, 4) for act, p in actions.items()}
                confidence = float(features.get("mock_confidence", 0.90))
                return MLModelPrediction(
                    model_name=self.model_name,
                    model_version=self.model_version,
                    natural_recovery_probability=round(natural_p, 4),
                    action_outcomes=actions,
                    uplift=uplift,
                    confidence=confidence,
                    explanation_notes=f"Seeded demo scenario override (Natural: {natural_p*100:.1f}%)"
                )

        # 2. Heuristic prediction based on failure type, customer history, amount & attempts
        failure_code = (input_data.failure_code or "").upper()
        amount = input_data.amount
        attempts = input_data.attempt_count
        tenure = input_data.customer_tenure_days
        ltv = input_data.customer_ltv
        segment = input_data.customer_segment

        # Base natural recovery by failure type
        if "TIMEOUT" in failure_code or "GATEWAY" in failure_code or "BANK_DOWNTIME" in failure_code:
            # High natural recovery as banks recover quickly
            base_natural = 0.70
            p_retry = 0.85
            p_link = 0.88
            p_reminder = 0.78
            p_alternate = 0.75
            p_escalate = 0.90
        elif "INSUFFICIENT" in failure_code or "FUNDS" in failure_code:
            # Low natural recovery; customer needs to add funds or try another instrument
            base_natural = 0.15
            p_retry = 0.20  # Retrying immediately rarely works for insufficient funds
            p_link = 0.68   # Link allows them to pay later or use another card/UPI
            p_reminder = 0.45
            p_alternate = 0.65
            p_escalate = 0.70
        elif "AUTH" in failure_code or "OTP" in failure_code or "2FA" in failure_code:
            base_natural = 0.35
            p_retry = 0.40
            p_link = 0.72   # Link lets them re-enter OTP at convenience
            p_reminder = 0.55
            p_alternate = 0.60
            p_escalate = 0.75
        elif "EXPIRED" in failure_code or "INVALID_CARD" in failure_code:
            base_natural = 0.05
            p_retry = 0.05  # Retry will definitely fail again
            p_link = 0.60
            p_reminder = 0.30
            p_alternate = 0.75  # Alternate payment method is ideal here!
            p_escalate = 0.80
        else:
            base_natural = 0.25
            p_retry = 0.38
            p_link = 0.65
            p_reminder = 0.48
            p_alternate = 0.55
            p_escalate = 0.70

        # Adjust for attempts (fatigue & burn-down)
        if attempts > 1:
            base_natural = max(0.05, base_natural - (attempts - 1) * 0.10)
            p_retry = max(0.05, p_retry - (attempts - 1) * 0.25)
            p_link = max(0.15, p_link - (attempts - 1) * 0.08)

        # Adjust for customer loyalty/history
        if tenure > 180 or ltv > 30000 or input_data.is_first_ever_failure == 1:
            base_natural = min(0.90, base_natural + 0.15)
            p_link = min(0.95, p_link + 0.10)
            p_reminder = min(0.90, p_reminder + 0.12)

        # Action outcomes dictionary
        actions = {
            "retry": round(min(0.99, max(0.01, p_retry)), 4),
            "payment_link": round(min(0.99, max(0.01, p_link)), 4),
            "reminder": round(min(0.99, max(0.01, p_reminder)), 4),
            "alternate_method": round(min(0.99, max(0.01, p_alternate)), 4),
            "human_escalation": round(min(0.99, max(0.01, p_escalate)), 4),
        }

        # Calculate incremental uplift for each action
        uplift = {
            action: round(actions[action] - base_natural, 4)
            for action in actions
        }

        # Model confidence score
        confidence = 0.88 if attempts == 1 else 0.75

        return MLModelPrediction(
            model_name=self.model_name,
            model_version=self.model_version,
            natural_recovery_probability=round(base_natural, 4),
            action_outcomes=actions,
            uplift=uplift,
            confidence=confidence,
            explanation_notes=f"Inference generated based on {failure_code} failure category and customer tenure {tenure} days."
        )
