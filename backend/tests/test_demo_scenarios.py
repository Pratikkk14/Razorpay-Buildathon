"""Tests to verify that the 5 Buildathon Demo Scenarios produce the exact expected outputs."""
from app.services.simulator.simulator_service import SimulatorService


def test_scenario_1_high_natural_suppression(db_session):
    sim = SimulatorService()
    res = sim.load_demo_scenario(db_session, "scenario_1_high_natural")
    assert res["decision"]["decision"] == "DONT_ACT"
    assert res["decision"]["recommended_action"] == "NO_ACTION"
    assert "insufficient incremental" in res["decision"]["reason"].lower()


def test_scenario_2_low_natural_high_uplift(db_session):
    sim = SimulatorService()
    res = sim.load_demo_scenario(db_session, "scenario_2_high_uplift")
    assert res["decision"]["decision"] == "ACT"
    assert res["decision"]["recommended_action"] == "PAYMENT_LINK"
    assert res["decision"]["expected_incremental_contribution"] > 1000.0


def test_scenario_3_multi_action_economics(db_session):
    sim = SimulatorService()
    res = sim.load_demo_scenario(db_session, "scenario_3_multi_action_economics")
    assert res["decision"]["decision"] == "ACT"
    assert res["decision"]["recommended_action"] == "PAYMENT_LINK"


def test_scenario_4_safety_veto(db_session):
    sim = SimulatorService()
    res = sim.load_demo_scenario(db_session, "scenario_4_safety_veto")
    assert res["decision"]["decision"] == "DONT_ACT"
    assert res["decision"]["policy_status"] == "VETOED"
    assert "cooldown" in res["decision"]["reason"].lower() or "rejected by deterministic policy" in res["decision"]["reason"].lower()


def test_scenario_5_high_value_escalation(db_session):
    sim = SimulatorService()
    res = sim.load_demo_scenario(db_session, "scenario_5_high_value_escalation")
    assert res["decision"]["decision"] == "ESCALATE"
    assert res["decision"]["recommended_action"] == "HUMAN_ESCALATION"
    assert "high-value" in res["decision"]["reason"].lower()
