"""Tests for CatBoost ML Model Service integration with outputs/recovery_model.cbm."""
import pytest
from app.services.ml.catboost_service import CatBoostMLModelService
from app.services.ml.registry import get_ml_service, set_active_service, list_available_services
from app.schemas.ml import MLModelInput


def test_catboost_model_service_load():
    """Verify CatBoost model loads from outputs/recovery_model.cbm."""
    service = CatBoostMLModelService()
    assert service.is_loaded is True
    assert service.model_name == "CatBoostRecoveryPropensity"
    assert service.model_version == "1.2.0"


def test_catboost_inference_insufficient_funds():
    """Verify inference for insufficient funds produces plausible uplift."""
    service = CatBoostMLModelService()
    input_data = MLModelInput(
        case_id="case_test_catboost_1",
        amount=1500.0,
        currency="INR",
        payment_method="card",
        failure_code="INSUFFICIENT_FUNDS",
        attempt_count=1,
        customer_tenure_days=90,
        customer_ltv=12000.0,
        customer_segment="standard",
        total_lifetime_payments=4,
        successful_lifetime_payments=3,
        failed_lifetime_payments=1,
    )
    pred = service.predict(input_data)
    assert 0.0 <= pred.natural_recovery_probability <= 1.0
    assert "retry" in pred.action_outcomes
    assert "payment_link" in pred.action_outcomes
    assert "reminder" in pred.action_outcomes
    assert "alternate_method" in pred.action_outcomes
    assert "human_escalation" in pred.action_outcomes
    assert pred.confidence > 0.5
    # For insufficient funds, payment link should have positive recovery probability
    assert pred.action_outcomes["payment_link"] > 0.1


def test_catboost_inference_card_expired():
    """Verify inference for expired card favors alternate payment method."""
    service = CatBoostMLModelService()
    input_data = MLModelInput(
        case_id="case_test_catboost_2",
        amount=3000.0,
        currency="INR",
        payment_method="card",
        failure_code="CARD_EXPIRED",
        attempt_count=1,
        customer_tenure_days=180,
        customer_ltv=25000.0,
        customer_segment="vip",
    )
    pred = service.predict(input_data)
    # Natural recovery for expired card should be low
    assert pred.natural_recovery_probability < 0.20
    # Alternate method or payment link should provide substantial uplift
    assert pred.uplift["alternate_method"] > 0.20 or pred.uplift["payment_link"] > 0.20


def test_catboost_scenario_override_support():
    """Verify scenario override allows exact deterministic injection."""
    service = CatBoostMLModelService()
    input_data = MLModelInput(
        case_id="case_override",
        amount=1000.0,
        additional_features={
            "mock_natural_recovery": 0.85,
            "mock_action_outcomes": {
                "retry": 0.90,
                "payment_link": 0.92,
                "reminder": 0.88,
                "alternate_method": 0.86,
                "human_escalation": 0.95,
            },
            "mock_confidence": 0.99
        }
    )
    pred = service.predict(input_data)
    assert pred.natural_recovery_probability == 0.85
    assert pred.uplift["retry"] == 0.05
    assert pred.confidence == 0.99


def test_ml_registry_switching():
    """Verify registry supports dynamic service switching and listing."""
    services = list_available_services()
    assert "mock" in services
    assert "catboost" in services

    # Switch to mock
    assert set_active_service("mock") is True
    svc_mock = get_ml_service()
    assert svc_mock.model_name == "MockPropensityUpliftV1"

    # Switch back to catboost
    assert set_active_service("catboost") is True
    svc_catboost = get_ml_service()
    assert svc_catboost.model_name == "CatBoostRecoveryPropensity"
