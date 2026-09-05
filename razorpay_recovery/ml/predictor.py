"""
predictor.py

End-to-end entrypoint: failed-payment state(s) in -> structured decision(s)
out, matching the output schema from spec section 24.

This ties together action_scorer -> economics -> decision_engine into one
call, and formats the result as the structured dict the execution
agent / LLM explanation layer would consume.
"""

from __future__ import annotations
import pandas as pd
from catboost import CatBoostClassifier

from . import action_scorer, economics, decision_engine, config


def predict_decisions(model: CatBoostClassifier, states: pd.DataFrame) -> pd.DataFrame:
    """
    states: one row per failed-payment decision point. Any 'payment_id'-like
        identifier column present is carried through untouched.

    Returns: one row per state with the full structured decision.
    """
    scored = action_scorer.score_candidate_actions(model, states)
    scored = action_scorer.attach_wait_baseline(scored)
    scored = economics.score_economics(scored)
    decisions = decision_engine.decide(scored)

    # carry through any identifier columns from the original states
    states_indexed = states.reset_index(drop=True).copy()
    states_indexed["_state_row_id"] = states_indexed.index
    id_cols = [c for c in states_indexed.columns if c.lower() in ("payment_id", "episode_id")]
    merged = decisions.merge(
        states_indexed[["_state_row_id", "amount"] + id_cols], on="_state_row_id", how="left"
    )

    def confidence_label(row) -> str:
        gap = abs(row["estimated_incremental_lift"])
        if gap >= 0.15:
            return "high"
        if gap >= 0.05:
            return "medium"
        return "low"

    merged["confidence"] = merged.apply(confidence_label, axis=1)
    merged = merged.drop(columns=["_state_row_id"])
    return merged


def to_output_schema(decisions_df: pd.DataFrame) -> list[dict]:
    """Convert the decisions dataframe to the JSON-friendly schema of spec section 24."""
    records = []
    for _, row in decisions_df.iterrows():
        records.append(
            {
                "payment_id": row.get("payment_id", row.get("episode_id")),
                "amount": row["amount"],
                "baseline_action": row["baseline_action"],
                "baseline_recovery_probability": round(float(row["baseline_recovery_probability"]), 4),
                "recommended_action": row["recommended_action"],
                "action_recovery_probability": round(float(row["action_recovery_probability"]), 4),
                "estimated_incremental_lift": round(float(row["estimated_incremental_lift"]), 4),
                "estimated_incremental_value": round(float(row["estimated_incremental_value"]), 2),
                "action_cost": float(row["action_cost"]),
                "estimated_net_contribution": round(float(row["estimated_net_contribution"]), 2),
                "decision": row["decision"],
                "confidence": row["confidence"],
                "reason": row["reason"],
            }
        )
    return records
