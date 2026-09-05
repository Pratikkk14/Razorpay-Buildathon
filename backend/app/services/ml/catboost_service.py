"""CatBoost ML Model Service implementation for real-world recovery inference."""
import json
import logging
import os
from pathlib import Path
from typing import Dict, Any, Optional, List
import pandas as pd
import numpy as np

from app.services.ml.interface import MLModelService
from app.schemas.ml import MLModelInput, MLModelPrediction
from app.core.config import settings

logger = logging.getLogger(__name__)

# Map backend action names <-> model action names
ACTION_MAP_TO_MODEL = {
    "wait": "WAIT",
    "retry": "RETRY",
    "payment_link": "PAYMENT_LINK",
    "reminder": "SEND_REMINDER",
    "alternate_method": "REQUEST_ALTERNATE_METHOD",
    "human_escalation": "ESCALATE_TO_HUMAN",
    "stop": "STOP_RECOVERY",
}

ACTION_MAP_FROM_MODEL = {
    "WAIT": "wait",
    "RETRY": "retry",
    "PAYMENT_LINK": "payment_link",
    "SEND_REMINDER": "reminder",
    "REQUEST_ALTERNATE_METHOD": "alternate_method",
    "ESCALATE_TO_HUMAN": "human_escalation",
    "STOP_RECOVERY": "stop",
}

MODEL_ACTIONS = [
    "WAIT",
    "RETRY",
    "PAYMENT_LINK",
    "SEND_REMINDER",
    "REQUEST_ALTERNATE_METHOD",
    "ESCALATE_TO_HUMAN",
]


class CatBoostMLModelService(MLModelService):
    """
    Production ML Model Service powered by CatBoost trained model (.cbm).
    Calculates true counterfactual uplift vs. the WAIT baseline.
    """

    def __init__(
        self,
        model_path: Optional[str] = None,
        feature_config_path: Optional[str] = None,
        economic_config_path: Optional[str] = None,
    ):
        self._model_path = model_path or getattr(
            settings, "CATBOOST_MODEL_PATH", "razorpay_recovery/outputs/recovery_model.cbm"
        )
        self._feature_config_path = feature_config_path or getattr(
            settings, "CATBOOST_FEATURE_CONFIG_PATH", "razorpay_recovery/outputs/feature_config.json"
        )
        self._economic_config_path = economic_config_path or getattr(
            settings, "CATBOOST_ECONOMIC_CONFIG_PATH", "razorpay_recovery/outputs/economic_config.json"
        )
        
        self._model = None
        self._feature_config = {}
        self._economic_config = {}
        self._load_resources()

    def _load_resources(self):
        """Loads CatBoost model and configuration files."""
        # 1. Feature Config
        if os.path.exists(self._feature_config_path):
            try:
                with open(self._feature_config_path, "r", encoding="utf-8") as f:
                    self._feature_config = json.load(f)
                logger.info(f"Loaded feature config from {self._feature_config_path}")
            except Exception as e:
                logger.warning(f"Could not load feature config: {e}")

        # 2. Economic Config
        if os.path.exists(self._economic_config_path):
            try:
                with open(self._economic_config_path, "r", encoding="utf-8") as f:
                    self._economic_config = json.load(f)
                logger.info(f"Loaded economic config from {self._economic_config_path}")
            except Exception as e:
                logger.warning(f"Could not load economic config: {e}")

        # 3. CatBoost Model
        if os.path.exists(self._model_path):
            try:
                from catboost import CatBoostClassifier
                self._model = CatBoostClassifier()
                self._model.load_model(self._model_path)
                logger.info(f"Successfully loaded CatBoost model from {self._model_path}")
            except Exception as e:
                logger.error(f"Failed to load CatBoost model from {self._model_path}: {e}")
                self._model = None
        else:
            logger.warning(f"CatBoost model file not found at {self._model_path}")

    @property
    def is_loaded(self) -> bool:
        return self._model is not None

    @property
    def model_name(self) -> str:
        return "CatBoostRecoveryPropensity"

    @property
    def model_version(self) -> str:
        return "1.2.0"

    def _map_failure_reason(self, failure_code: Optional[str]) -> str:
        """Map raw failure code / string to the 6 canonical failure reasons expected by the model."""
        code = (failure_code or "").lower()
        if any(k in code for k in ["insufficient", "funds", "balance", "limit"]):
            return "insufficient_funds"
        if any(k in code for k in ["auth", "otp", "2fa", "3ds", "verification", "pin"]):
            return "authentication_failed"
        if any(k in code for k in ["expired", "validity"]):
            return "card_expired"
        if any(k in code for k in ["invalid", "declined", "honor", "lost", "stolen", "block"]):
            return "invalid_payment_method"
        if any(k in code for k in ["timeout", "network", "conn", "latency"]):
            return "network_error"
        if any(k in code for k in ["bank", "gateway", "down", "technical", "internal", "unavailable"]):
            return "temporary_bank_failure"
        return "temporary_bank_failure"

    def _map_customer_archetype(self, segment: Optional[str], tenure_days: int, failure_rate: float) -> str:
        """Map customer features to archetype."""
        seg = (segment or "").lower()
        if seg in ["vip", "enterprise", "prime"] or (tenure_days > 180 and failure_rate < 0.15):
            return "reliable"
        if seg in ["dormant", "at_risk"] or (tenure_days > 180 and failure_rate >= 0.15):
            return "reliable_dormant"
        if seg in ["high_risk", "new"] or failure_rate > 0.40:
            return "high_risk"
        return "occasional"

    def _build_feature_row(self, input_data: MLModelInput, action: str) -> Dict[str, Any]:
        """Constructs a single feature dictionary for the CatBoost model."""
        amount = float(input_data.amount)
        attempts = int(input_data.attempt_count)
        hours_since_first = float(input_data.time_since_failure_minutes / 60.0)
        interventions = int(input_data.previous_interventions_count)
        
        # Customer history stats
        total_payments = max(1, input_data.total_lifetime_payments)
        success_payments = max(0, input_data.successful_lifetime_payments)
        failed_payments = max(0, input_data.failed_lifetime_payments)
        
        failure_rate = float(failed_payments / total_payments) if total_payments > 0 else 0.1
        success_rate = float(success_payments / total_payments) if total_payments > 0 else 0.9
        
        tenure_days = int(input_data.customer_tenure_days)
        ltv = float(input_data.customer_ltv if input_data.customer_ltv > 0 else amount * 4)
        days_since_last_success = float(
            input_data.days_since_last_success if input_data.days_since_last_success is not None else min(tenure_days, 14)
        )
        
        consecutive_failures = max(1, attempts)
        timestep = max(0, attempts - 1)
        
        # Categoricals
        failure_reason = self._map_failure_reason(input_data.failure_code)
        customer_archetype = self._map_customer_archetype(input_data.customer_segment, tenure_days, failure_rate)
        
        # Derived features
        amount_to_ltv_ratio = float(amount / ltv) if ltv > 0 else 0.0
        
        if attempts <= 1:
            attempt_bucket = "first_attempt"
        elif attempts == 2:
            attempt_bucket = "second_attempt"
        else:
            attempt_bucket = "third_plus"
            
        if hours_since_first <= 0.0:
            failure_recency_bucket = "immediate"
        elif hours_since_first <= 24.0:
            failure_recency_bucket = "within_1_day"
        elif hours_since_first <= 72.0:
            failure_recency_bucket = "within_3_days"
        else:
            failure_recency_bucket = "over_3_days"
            
        intervention_pressure = float(interventions / consecutive_failures) if consecutive_failures > 0 else 0.0

        is_weekend = 0
        if input_data.additional_features and "is_weekend" in input_data.additional_features:
            is_weekend = int(input_data.additional_features["is_weekend"])

        return {
            "amount": amount,
            "attempt_count": attempts,
            "hours_since_first_failure": hours_since_first,
            "interventions_count": interventions,
            "consecutive_failures": consecutive_failures,
            "customer_ltv": ltv,
            "customer_failure_rate": failure_rate,
            "subscription_paid_count": success_payments,
            "account_tenure_days": tenure_days,
            "lifetime_success_rate": success_rate,
            "days_since_last_success": days_since_last_success,
            "historical_ltv": ltv,
            "timestep": timestep,
            "is_weekend": is_weekend,
            "is_first_ever_failure": int(input_data.is_first_ever_failure),
            "failure_reason": failure_reason,
            "customer_archetype": customer_archetype,
            "action": action,
            "amount_to_ltv_ratio": amount_to_ltv_ratio,
            "attempt_bucket": attempt_bucket,
            "failure_recency_bucket": failure_recency_bucket,
            "intervention_pressure": intervention_pressure,
        }

    def predict(self, input_data: MLModelInput) -> MLModelPrediction:
        """
        Runs inference across all candidate actions using CatBoost.
        Returns predicted natural recovery probability, action outcome probabilities, uplift, and confidence.
        """
        # 1. Support scenario overrides if explicitly provided (e.g. for deterministic mock benchmarks)
        if input_data.additional_features and "mock_natural_recovery" in input_data.additional_features:
            features = input_data.additional_features
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
                explanation_notes=f"CatBoost Service (Scenario Override: Natural {natural_p*100:.1f}%)"
            )

        # 2. Check if model is loaded
        if not self._model:
            logger.warning("CatBoost model is not loaded. Falling back to default predictions.")
            return MLModelPrediction(
                model_name=self.model_name,
                model_version=self.model_version,
                natural_recovery_probability=0.25,
                action_outcomes={
                    "retry": 0.35,
                    "payment_link": 0.65,
                    "reminder": 0.45,
                    "alternate_method": 0.55,
                    "human_escalation": 0.70,
                },
                uplift={
                    "retry": 0.10,
                    "payment_link": 0.40,
                    "reminder": 0.20,
                    "alternate_method": 0.30,
                    "human_escalation": 0.45,
                },
                confidence=0.70,
                explanation_notes="Fallback prediction (model not loaded)"
            )

        # 3. Build candidate feature matrix
        rows = [self._build_feature_row(input_data, action) for action in MODEL_ACTIONS]
        df = pd.DataFrame(rows)

        # 4. Predict probabilities with CatBoost
        try:
            probabilities = self._model.predict_proba(df)[:, 1]
        except Exception as e:
            logger.error(f"CatBoost predict_proba failed: {e}", exc_info=True)
            raise e

        # Extract baseline (WAIT) recovery probability
        wait_idx = MODEL_ACTIONS.index("WAIT")
        natural_p = float(probabilities[wait_idx])

        # Construct action_outcomes and uplift dictionaries
        action_outcomes = {}
        uplift = {}

        for act_model, prob in zip(MODEL_ACTIONS, probabilities):
            if act_model == "WAIT" or act_model == "STOP_RECOVERY":
                continue
            backend_action = ACTION_MAP_FROM_MODEL.get(act_model, act_model.lower())
            p_val = round(float(prob), 4)
            action_outcomes[backend_action] = p_val
            uplift[backend_action] = round(p_val - natural_p, 4)

        # Determine confidence score based on margin of uplift
        max_uplift = max(uplift.values()) if uplift else 0.0
        confidence = 0.92 if abs(max_uplift) >= 0.15 else (0.82 if abs(max_uplift) >= 0.05 else 0.70)

        failure_reason = rows[0]["failure_reason"]
        customer_archetype = rows[0]["customer_archetype"]

        return MLModelPrediction(
            model_name=self.model_name,
            model_version=self.model_version,
            natural_recovery_probability=round(natural_p, 4),
            action_outcomes=action_outcomes,
            uplift=uplift,
            confidence=confidence,
            explanation_notes=f"CatBoost v{self.model_version} inference: {failure_reason} for {customer_archetype} customer."
        )
