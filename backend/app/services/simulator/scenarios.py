"""Pre-seeded canonical failure scenarios and 5 buildathon demo scenarios."""
from typing import Dict, Any, List
from app.schemas.simulator import ScenarioDefinition


DEMO_SCENARIOS: List[ScenarioDefinition] = [
    ScenarioDefinition(
        scenario_id="scenario_1_high_natural",
        title="Scenario 1: High Natural Recovery (Suppression)",
        description="Customer experiencing a transient gateway glitch with 82% natural recovery probability. Intervention increases recovery to 87% (only 5% lift).",
        customer_name="TechCorp India Ltd",
        amount=3499.0,
        payment_method="upi",
        failure_code="GATEWAY_TIMEOUT",
        failure_reason="Transient gateway timeout during UPI intent callback",
        natural_recovery_rate=0.82,
        expected_decision="DONT_ACT",
        expected_action="NO_ACTION",
        expected_rationale="Intervention produces insufficient incremental value (5% lift). Avoiding unnecessary messaging cost and customer friction.",
        context_features={
            "customer_tenure_days": 240,
            "customer_ltv": 45000.0,
            "customer_segment": "vip",
            "total_lifetime_payments": 12,
            "successful_lifetime_payments": 12,
            "failed_lifetime_payments": 1,
            "is_first_ever_failure": 1,
            "mock_natural_recovery": 0.82,
            "mock_action_outcomes": {
                "retry": 0.84,
                "payment_link": 0.87,
                "reminder": 0.83,
                "alternate_method": 0.84,
                "human_escalation": 0.88
            },
            "mock_confidence": 0.94
        }
    ),
    ScenarioDefinition(
        scenario_id="scenario_2_high_uplift",
        title="Scenario 2: Low Natural Recovery + High Uplift",
        description="Customer with insufficient funds. Natural recovery is only 12%. Payment link with UPI/card alternative achieves 71% recovery (59% incremental lift).",
        customer_name="Aarav Sharma",
        amount=4999.0,
        payment_method="card",
        failure_code="INSUFFICIENT_FUNDS",
        failure_reason="Card transaction declined due to insufficient balance",
        natural_recovery_rate=0.12,
        expected_decision="ACT",
        expected_action="PAYMENT_LINK",
        expected_rationale="Low natural recovery (12%) and massive incremental lift (+59%) generates expected net contribution of ₹2,946.41 after all costs.",
        context_features={
            "customer_tenure_days": 90,
            "customer_ltv": 15000.0,
            "customer_segment": "standard",
            "total_lifetime_payments": 4,
            "successful_lifetime_payments": 3,
            "failed_lifetime_payments": 1,
            "is_first_ever_failure": 0,
            "mock_natural_recovery": 0.12,
            "mock_action_outcomes": {
                "retry": 0.16,
                "payment_link": 0.71,
                "reminder": 0.35,
                "alternate_method": 0.65,
                "human_escalation": 0.72
            },
            "mock_confidence": 0.91
        }
    ),
    ScenarioDefinition(
        scenario_id="scenario_3_multi_action_economics",
        title="Scenario 3: Multi-Action Economic Optimization",
        description="Comparing Retry vs Payment Link vs Reminder vs Alternate Method. Demonstrates that highest recovery % is not always highest net contribution.",
        customer_name="Priya Nair",
        amount=1999.0,
        payment_method="netbanking",
        failure_code="NETBANKING_AUTH_FAIL",
        failure_reason="Customer session timed out at bank authentication page",
        natural_recovery_rate=0.28,
        expected_decision="ACT",
        expected_action="PAYMENT_LINK",
        expected_rationale="Payment Link yields highest expected incremental contribution after subtracting channel delivery costs and customer friction.",
        context_features={
            "customer_tenure_days": 120,
            "customer_ltv": 12000.0,
            "customer_segment": "standard",
            "total_lifetime_payments": 6,
            "successful_lifetime_payments": 5,
            "failed_lifetime_payments": 1,
            "is_first_ever_failure": 0,
            "mock_natural_recovery": 0.28,
            "mock_action_outcomes": {
                "retry": 0.32,
                "payment_link": 0.76,
                "reminder": 0.52,
                "alternate_method": 0.68,
                "human_escalation": 0.78
            },
            "mock_confidence": 0.89
        }
    ),
    ScenarioDefinition(
        scenario_id="scenario_4_safety_veto",
        title="Scenario 4: Deterministic Policy Veto",
        description="ML recommends sending a payment link (+45% lift), but customer was already contacted 3 hours ago. Policy engine vetoes outreach to prevent customer spam.",
        customer_name="Rohan Verma",
        amount=2499.0,
        payment_method="card",
        failure_code="CARD_DECLINED",
        failure_reason="Card limit exceeded on previous attempt",
        natural_recovery_rate=0.20,
        expected_decision="DONT_ACT",
        expected_action="NO_ACTION",
        expected_rationale="AI recommendation rejected by deterministic policy: Contact cooldown active (contacted 3.0h ago, 24h required).",
        context_features={
            "customer_tenure_days": 60,
            "customer_ltv": 8000.0,
            "customer_segment": "standard",
            "hours_since_last_contact": 3.0,
            "previous_interventions_count": 1,
            "mock_natural_recovery": 0.20,
            "mock_action_outcomes": {
                "retry": 0.20,
                "payment_link": 0.65,
                "reminder": 0.40,
                "alternate_method": 0.55,
                "human_escalation": 0.20
            },
            "mock_confidence": 0.85
        }
    ),
    ScenarioDefinition(
        scenario_id="scenario_5_high_value_escalation",
        title="Scenario 5: High-Value Enterprise Escalation",
        description="Enterprise customer with ₹75,000 annual subscription payment failure. Policy mandates VIP white-glove human escalation rather than automated bots.",
        customer_name="Apex Global Enterprise Ltd",
        amount=75000.0,
        payment_method="card",
        failure_code="AUTHENTICATION_FAILED",
        failure_reason="Corporate card 3D Secure corporate approval pending",
        natural_recovery_rate=0.30,
        expected_decision="ESCALATE",
        expected_action="HUMAN_ESCALATION",
        expected_rationale="High-value payment of ₹75,000 exceeds ₹50,000 policy threshold. Escalated to VIP Support.",
        context_features={
            "customer_tenure_days": 720,
            "customer_ltv": 350000.0,
            "customer_segment": "enterprise",
            "total_lifetime_payments": 24,
            "successful_lifetime_payments": 24,
            "failed_lifetime_payments": 1,
            "is_first_ever_failure": 1,
            "mock_natural_recovery": 0.30,
            "mock_action_outcomes": {
                "retry": 0.35,
                "payment_link": 0.60,
                "reminder": 0.50,
                "alternate_method": 0.55,
                "human_escalation": 0.92
            },
            "mock_confidence": 0.95
        }
    )
]


def get_scenario_by_id(scenario_id: str) -> ScenarioDefinition:
    """Returns the scenario matching scenario_id."""
    for s in DEMO_SCENARIOS:
        if s.scenario_id == scenario_id:
            return s
    raise KeyError(f"Scenario '{scenario_id}' not found.")
