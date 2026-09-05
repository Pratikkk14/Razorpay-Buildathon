"""Tests for Deterministic Policy & Safety Guardrails."""
from app.models.case import Case
from app.models.context import PaymentContext
from app.services.policy.safety_engine import DeterministicSafetyEngine
from app.core.config import settings


def test_retry_limit_veto(db_session):
    safety = DeterministicSafetyEngine()
    case = Case(payment_id="pay_pol_1", customer_id="c1", amount=1500.0, attempt_count=2)
    db_session.add(case)
    db_session.commit()
    context = PaymentContext(case_id=case.id, is_opted_out=0)

    allowed, reasons, outcomes = safety.evaluate_policies(db_session, case, context)
    assert allowed["RETRY"] is False
    assert "Max retry limit exceeded" in reasons["RETRY"]


def test_customer_dnd_opt_out(db_session):
    safety = DeterministicSafetyEngine()
    case = Case(payment_id="pay_pol_2", customer_id="c2", amount=1500.0, attempt_count=1)
    db_session.add(case)
    db_session.commit()
    context = PaymentContext(case_id=case.id, is_opted_out=1)

    allowed, reasons, outcomes = safety.evaluate_policies(db_session, case, context)
    assert allowed["PAYMENT_LINK"] is False
    assert allowed["REMINDER"] is False
    assert allowed["ALTERNATE_METHOD"] is False


def test_contact_cooldown_veto(db_session):
    safety = DeterministicSafetyEngine()
    case = Case(payment_id="pay_pol_3", customer_id="c3", amount=1500.0, attempt_count=1)
    db_session.add(case)
    db_session.commit()
    context = PaymentContext(case_id=case.id, hours_since_last_contact=4.5)  # < 24h

    allowed, reasons, outcomes = safety.evaluate_policies(db_session, case, context)
    assert allowed["PAYMENT_LINK"] is False
    assert "Contact cooldown active" in reasons["PAYMENT_LINK"]


def test_high_value_transaction_escalation(db_session):
    safety = DeterministicSafetyEngine()
    case = Case(payment_id="pay_pol_4", customer_id="c4", amount=75000.0, attempt_count=1)
    db_session.add(case)
    db_session.commit()
    context = PaymentContext(case_id=case.id)

    allowed, reasons, outcomes = safety.evaluate_policies(db_session, case, context)
    assert allowed["PAYMENT_LINK"] is False
    assert allowed["RETRY"] is False
    assert allowed["HUMAN_ESCALATION"] is True


def test_quiet_hours_compliance(db_session):
    safety = DeterministicSafetyEngine()
    case = Case(payment_id="pay_pol_5", customer_id="c5", amount=1500.0, attempt_count=1)
    db_session.add(case)
    db_session.commit()
    context = PaymentContext(case_id=case.id)

    # 11:00 PM (23:00) -> In quiet hours
    _, _, outcomes = safety.evaluate_policies(db_session, case, context, simulated_hour=23)
    quiet_check = next(o for o in outcomes if o.rule_key == "QUIET_HOURS")
    assert quiet_check.passed is False

    # 2:00 PM (14:00) -> Outside quiet hours
    _, _, outcomes2 = safety.evaluate_policies(db_session, case, context, simulated_hour=14)
    quiet_check2 = next(o for o in outcomes2 if o.rule_key == "QUIET_HOURS")
    assert quiet_check2.passed is True
