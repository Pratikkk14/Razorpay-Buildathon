"""Payment Gateway abstraction interface."""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class GatewayExecutionResult:
    success: bool
    gateway_name: str
    action_type: str
    reference_id: Optional[str] = None
    payment_link_url: Optional[str] = None
    response_payload: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None
    cost_incurred: float = 0.0


class PaymentGatewayInterface(ABC):
    """Abstract interface for executing recovery interventions through gateways."""

    @abstractmethod
    def trigger_retry(self, payment_id: str, amount: float, currency: str = "INR") -> GatewayExecutionResult:
        """Dispatches an automated payment retry attempt."""
        pass

    @abstractmethod
    def create_payment_link(
        self,
        case_id: str,
        amount: float,
        customer_name: Optional[str] = None,
        customer_email: Optional[str] = None,
        customer_phone: Optional[str] = None,
        description: str = "Recovery Payment Link"
    ) -> GatewayExecutionResult:
        """Generates a dynamic payment link."""
        pass

    @abstractmethod
    def send_reminder(
        self,
        case_id: str,
        customer_phone: Optional[str] = None,
        customer_email: Optional[str] = None,
        amount: float = 0.0
    ) -> GatewayExecutionResult:
        """Sends an omnichannel payment reminder (SMS/WhatsApp)."""
        pass

    @abstractmethod
    def request_alternate_method(
        self,
        case_id: str,
        customer_phone: Optional[str] = None,
        customer_email: Optional[str] = None,
        amount: float = 0.0
    ) -> GatewayExecutionResult:
        """Sends an alternate payment method request (e.g. UPI fallback)."""
        pass

    @abstractmethod
    def escalate_to_human(
        self,
        case_id: str,
        amount: float,
        reason: str
    ) -> GatewayExecutionResult:
        """Creates a ticket for white-glove manual human recovery."""
        pass
