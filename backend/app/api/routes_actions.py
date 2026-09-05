"""Actions execution API routes."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.case import Case
from app.services.execution.executor import ActionExecutor
from app.schemas.action import ActionExecutionRequest, ActionExecutionResponse

router = APIRouter(prefix="/actions", tags=["Actions"])


@router.post("/execute", response_model=ActionExecutionResponse)
def execute_action(req: ActionExecutionRequest, db: Session = Depends(get_db)):
    """Executes a recommended or overridden recovery action on a case."""
    case = db.query(Case).filter(Case.id == req.case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail=f"Case '{req.case_id}' not found.")

    target_action = req.action_type or case.recommended_action
    if not target_action or target_action == "NO_ACTION":
        raise HTTPException(status_code=400, detail="Cannot execute NO_ACTION or undefined action.")

    executor = ActionExecutor()
    try:
        exec_record = executor.execute_action(
            db=db,
            case=case,
            action_type=target_action,
            force=req.force
        )
        return exec_record
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Execution error: {str(e)}")
