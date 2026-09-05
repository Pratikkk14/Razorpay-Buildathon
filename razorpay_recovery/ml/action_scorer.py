"""
action_scorer.py

For each failed-payment STATE, generate one candidate row per allowed
action and score P(recovery | state, action) with the single trained
action-conditioned model.
"""

from __future__ import annotations
import pandas as pd
from catboost import CatBoostClassifier

from . import config
from . import features as feat
from . import model as model_mod


def _allowed_actions_for_row(row: pd.Series) -> list[str]:
    """Respect the dataset's own policy mask when present, else all actions."""
    if "allowed_actions" in row.index and pd.notna(row["allowed_actions"]):
        return str(row["allowed_actions"]).split(",")
    return list(config.ALL_ACTIONS)


def expand_candidate_actions(states: pd.DataFrame) -> pd.DataFrame:
    """
    states: one row per failed-payment decision point (must NOT include
            an 'action' column value we intend to keep -- it will be
            overwritten per candidate).
    Returns: one row per (state, candidate action), with a `_state_row_id`
             column linking rows back to the original state.
    """
    states = states.reset_index(drop=True).copy()
    states["_state_row_id"] = states.index

    expanded_rows = []
    for _, row in states.iterrows():
        candidates = _allowed_actions_for_row(row)
        for a in candidates:
            new_row = row.copy()
            new_row["action"] = a
            expanded_rows.append(new_row)

    expanded = pd.DataFrame(expanded_rows).reset_index(drop=True)
    return expanded


def score_candidate_actions(
    model: CatBoostClassifier, states: pd.DataFrame
) -> pd.DataFrame:
    """
    Returns a long dataframe: one row per (state, candidate action) with
    a `recovery_probability` column, plus `_state_row_id` to group back.
    """
    expanded = expand_candidate_actions(states)
    X = feat.prepare_features(expanded)
    X.index = expanded.index
    proba = model_mod.predict_proba(model, X)
    expanded["recovery_probability"] = proba.values
    return expanded


def attach_wait_baseline(scored: pd.DataFrame) -> pd.DataFrame:
    """
    Adds `wait_probability` (the WAIT-action prediction for the same state)
    to every row, so incremental lift can be computed vs. that baseline.
    If WAIT was not an allowed/candidate action for a state, wait_probability
    is NaN for that state's rows (the decision engine must handle this).
    """
    wait_rows = scored[scored["action"] == config.BASELINE_ACTION][
        ["_state_row_id", "recovery_probability"]
    ].rename(columns={"recovery_probability": "wait_probability"})

    return scored.merge(wait_rows, on="_state_row_id", how="left")
