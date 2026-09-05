"""Simulator API routes."""
from typing import List, Dict, Any
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.simulator import (
    SimulatorConfig,
    ScenarioDefinition,
    MultiPolicyBenchmarkResult
)
from app.services.simulator.scenarios import DEMO_SCENARIOS
from app.services.simulator.simulator_service import SimulatorService
from app.services.simulator.domain_randomization import generate_synthetic_case
from app.models.case import Case
from app.services.context.aggregator import ContextAggregator
from app.services.ml.registry import get_ml_service
from app.services.decision.decision_engine import DecisionEngine

router = APIRouter(prefix="/simulator", tags=["Simulator"])
sim_service = SimulatorService()


@router.get("/scenarios", response_model=List[ScenarioDefinition])
def list_scenarios():
    """Lists all pre-configured demo and test scenarios."""
    return DEMO_SCENARIOS


@router.post("/scenarios/{scenario_id}/load")
def load_scenario(scenario_id: str, db: Session = Depends(get_db)):
    """Loads and executes a specific seeded scenario."""
    try:
        result = sim_service.load_demo_scenario(db, scenario_id)
        return result
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Scenario '{scenario_id}' not found.")


@router.post("/benchmark", response_model=MultiPolicyBenchmarkResult)
def run_benchmark(config: SimulatorConfig):
    """
    Executes a Monte Carlo comparative simulation benchmarking the 5 canonical policies:
    A (No Action), B (Fixed Retry), C (Rule-Based), D (ML Propensity), E (Uplift + Economics).
    """
    return sim_service.run_multi_policy_benchmark(config)


@router.post("/generate-batch")
def generate_batch_cases(config: SimulatorConfig, db: Session = Depends(get_db)):
    """Generates a batch of synthetic payment cases and runs full decision pipeline on them."""
    cases_created = []
    dec_engine = DecisionEngine()
    ml_service = get_ml_service()

    for i in range(1, config.num_cases + 1):
        synth = generate_synthetic_case(seed_id=i + int(datetime.utcnow().timestamp()) % 10000)
        case = Case(
            payment_id=synth["payment_id"],
            customer_id=synth["customer_id"],
            customer_name=synth["customer_name"],
            customer_email=synth["customer_email"],
            customer_phone=synth["customer_phone"],
            amount=synth["amount"],
            currency=synth["currency"],
            payment_method=synth["payment_method"],
            failure_code=synth["failure_code"],
            failure_reason=synth["failure_reason"],
            attempt_count=synth["attempt_count"],
            metadata_json=synth["context_features"]
        )
        db.add(case)
        db.commit()
        db.refresh(case)

        # Context -> ML -> Decision
        context = ContextAggregator.aggregate_context(db, case)
        ml_input = ContextAggregator.to_ml_input(case, context)
        prediction = ml_service.predict(ml_input)
        dec_engine.evaluate_and_decide(db, case, context, prediction)
        
        cases_created.append(case.id)

    return {"message": f"Successfully created and evaluated {len(cases_created)} synthetic recovery cases.", "case_ids": cases_created}
