"""In-memory Simulator Payment Gateway for zero-dependency local runs and demo testing."""
import uuid
from typing import Optional
from app.services.execution.gateway_interface import PaymentGatewayInterface, GatewayExecutionResult


class SimulatorGateway(PaymentGatewayInterface):
    """
    Pure in-memory sandbox gateway.
    Ensures safe zero-credential execution without network dependencies.
    """

    def trigger_retry(self, payment_id: str, amount: float, currency: str = "INR") -> GatewayExecutionResult:
        ref_id = f"sim_retry_{uuid.uuid4().hex[:8]}"
        return GatewayExecutionResult(
            success=True,
            gateway_name="SIMULATOR",
            action_type="RETRY",
            reference_id=ref_id,
            cost_incurred=0.50,
            response_payload={"simulated": True, "action": "RETRY", "reference_id": ref_id}
        )

    def create_payment_link(
        self,
        case_id: str,
        amount: float,
        customer_name: Optional[str] = None,
        customer_email: Optional[str] = None,
        customer_phone: Optional[str] = None,
        description: str = "Recovery Payment Link"
    ) -> GatewayExecutionResult:
        ref_id = f"sim_plink_{uuid.uuid4().hex[:8]}"
        url = f"https://simulator.recovery-engine.local/pay/{ref_id}"
        return GatewayExecutionResult(
            success=True,
            gateway_name="SIMULATOR",
            action_type="PAYMENT_LINK",
            reference_id=ref_id,
            payment_link_url=url,
            cost_incurred=2.00,
            response_payload={"simulated": True, "action": "PAYMENT_LINK", "payment_link_url": url}
        )

    def send_reminder(
        self,
        case_id: str,
        customer_phone: Optional[str] = None,
        customer_email: Optional[str] = None,
        amount: float = 0.0
    ) -> GatewayExecutionResult:
        ref_id = f"sim_rem_{uuid.uuid4().hex[:8]}"
        return GatewayExecutionResult(
            success=True,
            gateway_name="SIMULATOR",
            action_type="REMINDER",
            reference_id=ref_id,
            cost_incurred=0.75,
            response_payload={"simulated": True, "action": "REMINDER", "reference_id": ref_id}
        )

    def request_alternate_method(
        self,
        case_id: str,
        customer_phone: Optional[str] = None,
        customer_email: Optional[str] = None,
        amount: float = 0.0
    ) -> GatewayExecutionResult:
        ref_id = f"sim_alt_{uuid.uuid4().hex[:8]}"
        return GatewayExecutionResult(
            success=True,
            gateway_name="SIMULATOR",
            action_type="ALTERNATE_METHOD",
            reference_id=ref_id,
            cost_incurred=1.50,
            response_payload={"simulated": True, "action": "ALTERNATE_METHOD", "reference_id": ref_id}
        )

    def escalate_to_human(
        self,
        case_id: str,
        amount: float,
        reason: str
    ) -> GatewayExecutionResult:
        ref_id = f"sim_esc_{uuid.uuid4().hex[:8]}"
        return GatewayExecutionResult(
            success=True,
            gateway_name="SIMULATOR",
            action_type="HUMAN_ESCALATION",
            reference_id=ref_id,
            cost_incurred=150.00,
            response_payload={"simulated": True, "action": "HUMAN_ESCALATION", "reference_id": ref_id}
        )
