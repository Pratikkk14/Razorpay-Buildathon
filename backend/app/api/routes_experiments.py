"""Experiments API routes."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.experiment import Experiment
from app.services.experiments.experiment_service import ExperimentService
from app.schemas.experiment import ExperimentCreate, ExperimentMetrics

router = APIRouter(prefix="/experiments", tags=["Experiments"])


@router.get("", response_model=List[dict])
def list_experiments(db: Session = Depends(get_db)):
    """Lists all active and completed A/B experiments."""
    exps = db.query(Experiment).all()
    if not exps:
        # Create default
        ExperimentService.get_or_create_default_experiment(db)
        exps = db.query(Experiment).all()

    return [
        {
            "id": e.id,
            "name": e.name,
            "description": e.description,
            "status": e.status,
            "traffic_split_ratio": e.traffic_split_ratio,
            "total_cases": e.total_cases,
            "control_cases": e.control_cases,
            "treatment_cases": e.treatment_cases
        }
        for e in exps
    ]


@router.get("/{experiment_id}/metrics", response_model=ExperimentMetrics)
def get_experiment_metrics(experiment_id: str, db: Session = Depends(get_db)):
    """Returns calculated statistical metrics for an experiment."""
    try:
        return ExperimentService.get_experiment_metrics(db, experiment_id)
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Experiment '{experiment_id}' not found.")
