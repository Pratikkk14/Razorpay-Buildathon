"""Tests for Economic Allocation Engine."""
from app.services.economics.allocation_engine import EconomicAllocationEngine
from app.schemas.ml import MLModelPrediction


def test_incremental_contribution_math():
    econ = EconomicAllocationEngine()
    prediction = MLModelPrediction(
        model_name="TestModel",
        model_version="1.0.0",
        natural_recovery_probability=0.20,
        action_outcomes={
            "retry": 0.30,          # Lift = 0.10
            "payment_link": 0.70,   # Lift = 0.50
            "reminder": 0.40,       # Lift = 0.20
            "alternate_method": 0.60,
            "human_escalation": 0.60
        },
        uplift={
            "retry": 0.10,
            "payment_link": 0.50,
            "reminder": 0.20
        },
        confidence=0.90
    )

    amount = 5000.0
    result = econ.evaluate_case(case_id="c_test", payment_amount=amount, prediction=prediction)

    # Check Payment Link math:
    # Expected Incremental Revenue = 0.50 * 5000 = ₹2500.00
    # Cost = 2.00 (action) + 1.00 (friction) = ₹3.00
    # Expected Net Contribution = 2500 - 3 = ₹2497.00
    plink = next(a for a in result.candidate_actions if a.action_type == "PAYMENT_LINK")
    assert plink.incremental_lift == 0.50
    assert plink.expected_incremental_revenue == 2500.00
    assert plink.total_cost == 3.00
    assert plink.expected_incremental_contribution == 2497.00

    # Best action is Payment Link
    assert result.best_action.action_type == "PAYMENT_LINK"
    assert result.is_positive_contribution is True
