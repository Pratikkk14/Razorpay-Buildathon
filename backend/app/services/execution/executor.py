"""Action Executor service: Coordinates safe execution across gateway adapters."""
import logging
from typing import Optional
from sqlalchemy.orm import Session
from datetime import datetime

from app.models.case import Case
from app.models.action_execution import ActionExecutionRecord
from app.services.execution.gateway_interface import PaymentGatewayInterface
from app.services.execution.razorpay_gateway import RazorpayTestGateway
from app.services.execution.simulator_gateway import SimulatorGateway
from app.services.audit.audit_service import AuditService
from app.core.config import settings

logger = logging.getLogger(__name__)


class ActionExecutor:
    """
    Executes policy-approved recovery actions through the appropriate gateway.
    Ensures safe simulated or test-mode execution.
    """

    def __init__(self, gateway: Optional[PaymentGatewayInterface] = None):
        if gateway:
            self.gateway = gateway
        elif settings.SIMULATION_MODE:
            self.gateway = SimulatorGateway()
        else:
            self.gateway = RazorpayTestGateway()

    def execute_action(
        self,
        db: Session,
        case: Case,
        action_type: Optional[str] = None,
        force: bool = False
    ) -> ActionExecutionRecord:
        """Executes a recommended action on a case."""
        target_action = action_type or case.recommended_action or "NO_ACTION"
        
        if target_action == "NO_ACTION":
            raise ValueError(f"Cannot execute NO_ACTION on case {case.id}")

        logger.info(f"Executing action {target_action} for case {case.id} amount ₹{case.amount}")

        # Dispatch via gateway
        if target_action == "RETRY":
            result = self.gateway.trigger_retry(payment_id=case.payment_id, amount=case.amount, currency=case.currency)
        elif target_action == "PAYMENT_LINK":
            result = self.gateway.create_payment_link(
                case_id=case.id,
                amount=case.amount,
                customer_name=case.customer_name,
                customer_email=case.customer_email,
                customer_phone=case.customer_phone
            )
        elif target_action == "REMINDER":
            result = self.gateway.send_reminder(
                case_id=case.id,
                customer_phone=case.customer_phone,
                customer_email=case.customer_email,
                amount=case.amount
            )
        elif target_action == "ALTERNATE_METHOD":
            result = self.gateway.request_alternate_method(
                case_id=case.id,
                customer_phone=case.customer_phone,
                customer_email=case.customer_email,
                amount=case.amount
            )
        elif target_action == "HUMAN_ESCALATION":
            result = self.gateway.escalate_to_human(
                case_id=case.id,
                amount=case.amount,
                reason=case.decision_reason or "Escalation requested"
            )
        else:
            raise ValueError(f"Unknown action type: {target_action}")

        # Record ActionExecutionRecord in database
        exec_record = ActionExecutionRecord(
            case_id=case.id,
            action_type=target_action,
            gateway=result.gateway_name,
            gateway_reference_id=result.reference_id,
            payment_link_url=result.payment_link_url,
            status="SUCCESS" if result.success else "FAILED",
            cost_incurred=result.cost_incurred,
            execution_payload=result.response_payload,
            error_message=result.error_message,
            executed_at=datetime.utcnow()
        )
        db.add(exec_record)

        # Update Case status
        case.executed_action = target_action
        case.status = "ACTION_EXECUTED"
        db.commit()
        db.refresh(exec_record)

        # Audit event
        AuditService.log_event(
            db=db,
            case_id=case.id,
            payment_id=case.payment_id,
            event_type="ACTION_EXECUTED",
            summary=f"Executed {target_action} via {result.gateway_name} (Cost: ₹{result.cost_incurred:.2f})",
            details={
                "action_type": target_action,
                "gateway": result.gateway_name,
                "reference_id": result.reference_id,
                "link_url": result.payment_link_url,
                "cost": result.cost_incurred
            }
        )

        return exec_record
