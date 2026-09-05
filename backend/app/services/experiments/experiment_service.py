"""Experimentation Engine: Manages A/B experiment groups and causal lift metrics."""
import logging
import random
from typing import Optional, Dict, Any, List
from sqlalchemy.orm import Session

from app.models.case import Case
from app.models.experiment import Experiment
from app.models.outcome import OutcomeRecord
from app.schemas.experiment import ExperimentCreate, ExperimentMetrics

logger = logging.getLogger(__name__)


class ExperimentService:
    """Manages randomized A/B experiments for recovery interventions."""

    @staticmethod
    def get_or_create_default_experiment(db: Session) -> Experiment:
        """Retrieves or creates the primary Recovery Optimization A/B Experiment."""
        exp = db.query(Experiment).filter(Experiment.name == "Production_Uplift_Vs_Control").first()
        if not exp:
            exp = Experiment(
                name="Production_Uplift_Vs_Control",
                description="A/B Experiment evaluating Uplift & Economic Allocation Engine (Treatment) vs Natural Holdout (Control).",
                status="ACTIVE",
                traffic_split_ratio=0.80,  # 80% treatment, 20% holdout control
                config_json={"treatment_policy": "Uplift_Allocation", "control_policy": "Holdout_No_Action"}
            )
            db.add(exp)
            db.commit()
            db.refresh(exp)
        return exp

    @staticmethod
    def assign_case(db: Session, case: Case, experiment: Optional[Experiment] = None) -> str:
        """Assigns a case to CONTROL or TREATMENT."""
        exp = experiment or ExperimentService.get_or_create_default_experiment(db)
        
        # Consistent assignment based on payment ID hash
        hash_val = sum(ord(c) for c in case.payment_id) % 100
        split_threshold = int(exp.traffic_split_ratio * 100)
        
        group = "TREATMENT" if hash_val < split_threshold else "CONTROL"
        case.experiment_id = exp.id
        case.experiment_group = group
        
        exp.total_cases += 1
        if group == "TREATMENT":
            exp.treatment_cases += 1
        else:
            exp.control_cases += 1
            
        db.commit()
        return group

    @staticmethod
    def get_experiment_metrics(db: Session, experiment_id: str) -> ExperimentMetrics:
        """Calculates statistical performance metrics for an experiment."""
        exp = db.query(Experiment).filter(Experiment.id == experiment_id).first()
        if not exp:
            raise KeyError(f"Experiment '{experiment_id}' not found.")

        # Aggregate cases in control vs treatment
        control_cases = db.query(Case).filter(Case.experiment_id == exp.id, Case.experiment_group == "CONTROL").all()
        treatment_cases = db.query(Case).filter(Case.experiment_id == exp.id, Case.experiment_group == "TREATMENT").all()

        n_ctrl = len(control_cases)
        n_treat = len(treatment_cases)

        rec_ctrl = sum(1 for c in control_cases if c.status == "RECOVERED")
        rec_treat = sum(1 for c in treatment_cases if c.status == "RECOVERED")

        p_ctrl = (rec_ctrl / n_ctrl) if n_ctrl > 0 else 0.0
        p_treat = (rec_treat / n_treat) if n_treat > 0 else 0.0
        observed_lift = round(max(0.0, p_treat - p_ctrl) * 100, 2)

        rev_treat = sum(c.amount for c in treatment_cases if c.status == "RECOVERED")
        inc_rev_treat = round(rev_treat * (observed_lift / 100) if p_treat > 0 else 0.0, 2)
        cost_treat = round(sum(c.expected_incremental_contribution or 0.0 for c in treatment_cases if c.executed_action not in [None, "NO_ACTION"]), 2)
        net_contrib = round(inc_rev_treat - (exp.treatment_cost or 0.0), 2)
        contrib_per_case = round(net_contrib / n_treat, 2) if n_treat > 0 else 0.0

        return ExperimentMetrics(
            experiment_id=exp.id,
            name=exp.name,
            status=exp.status,
            total_cases=exp.total_cases,
            control_cases=n_ctrl,
            treatment_cases=n_treat,
            control_recovery_rate=round(p_ctrl * 100, 2),
            treatment_recovery_rate=round(p_treat * 100, 2),
            observed_lift_pct=observed_lift,
            treatment_incremental_revenue=inc_rev_treat,
            treatment_cost=exp.treatment_cost,
            treatment_net_contribution=net_contrib,
            contribution_per_case_inr=contrib_per_case
        )
