"""Demo Guided Walkthrough API routes for Buildathon Judging."""
from typing import List, Dict, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.simulator.scenarios import DEMO_SCENARIOS, get_scenario_by_id
from app.services.simulator.simulator_service import SimulatorService

router = APIRouter(prefix="/demo", tags=["Demo"])
sim_service = SimulatorService()


@router.get("/scenarios")
def list_demo_scenarios():
    """Returns the 5 curated judge demo scenarios."""
    return [
        {
            "id": s.scenario_id,
            "title": s.title,
            "description": s.description,
            "customer_name": s.customer_name,
            "amount": s.amount,
            "natural_recovery_rate": s.natural_recovery_rate,
            "expected_decision": s.expected_decision,
            "expected_action": s.expected_action,
            "expected_rationale": s.expected_rationale
        }
        for s in DEMO_SCENARIOS
    ]


@router.post("/scenarios/{scenario_id}/execute")
def execute_demo_scenario(scenario_id: str, db: Session = Depends(get_db)):
    """Executes a specific demo scenario and returns the full decision & economic breakdown."""
    try:
        result = sim_service.load_demo_scenario(db, scenario_id)
        return result
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Demo scenario '{scenario_id}' not found.")


@router.post("/seed-all")
def seed_all_demo_scenarios(db: Session = Depends(get_db)):
    """Seeds all 5 demo scenarios into the database for immediate review."""
    results = []
    for s in DEMO_SCENARIOS:
        res = sim_service.load_demo_scenario(db, s.scenario_id)
        results.append(res)
    return {"message": "Successfully seeded all 5 demo scenarios.", "scenarios": results}
