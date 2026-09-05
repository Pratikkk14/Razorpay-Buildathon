"""
evaluation.py

Model-quality metrics (ROC-AUC, PR-AUC, etc.) AND policy/economic
evaluation that compares our incremental-lift policy against simple
baselines. Accuracy is intentionally NOT the headline metric -- see
spec section 12/28.
"""

from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.metrics import (
    roc_auc_score,
    average_precision_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    brier_score_loss,
)

from . import config


def model_metrics(y_true: pd.Series, y_proba: pd.Series, threshold: float = 0.5) -> dict:
    y_pred = (y_proba >= threshold).astype(int)
    return {
        "roc_auc": roc_auc_score(y_true, y_proba),
        "pr_auc": average_precision_score(y_true, y_proba),
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
        "brier_score": brier_score_loss(y_true, y_proba),
    }


def calibration_table(y_true: pd.Series, y_proba: pd.Series, n_bins: int = 10) -> pd.DataFrame:
    df = pd.DataFrame({"y": y_true.values, "p": y_proba.values})
    df["bin"] = pd.qcut(df["p"], q=n_bins, duplicates="drop")
    table = df.groupby("bin", observed=True).agg(
        mean_predicted=("p", "mean"), mean_observed=("y", "mean"), n=("y", "size")
    )
    return table.reset_index()


# ---------------------------------------------------------------------------
# Policy baselines (spec section 16)
# ---------------------------------------------------------------------------
#
# All baselines are evaluated the same way: for each held-out episode's
# FIRST decision point (timestep 0, the actual failed-payment moment),
# pick an action according to the baseline's rule, then look up what
# *actually happened in the logged data* for that (episode, action) if it
# matches the logged action, otherwise fall back to the model's own
# recovery-probability estimate for that (state, action) pair since the
# logged data only observed ONE action per state. This is made explicit in
# the notebook -- baselines here compare using the trained model's
# probability estimates for consistency (we cannot observe true
# counterfactual outcomes for actions that were not logged).


def apply_baseline_policy(scored_economics: pd.DataFrame, policy: str) -> pd.DataFrame:
    """
    scored_economics: long dataframe, one row per (state, candidate action),
        with recovery_probability, incremental_lift, net_incremental_contribution.

    policy: one of "no_action", "blind_retry", "rule_based",
            "propensity", "economic", "incremental" (our policy).

    Returns one row per state (_state_row_id) with the chosen action.
    """
    groups = scored_economics.groupby("_state_row_id")
    rows = []

    for state_id, g in groups:
        wait_row = g[g["action"] == config.BASELINE_ACTION]
        wait_prob = wait_row["recovery_probability"].iloc[0] if not wait_row.empty else np.nan

        if policy == "no_action":
            chosen = wait_row.iloc[0] if not wait_row.empty else g.iloc[0]
        elif policy == "blind_retry":
            retry_row = g[g["action"] == "RETRY"]
            chosen = retry_row.iloc[0] if not retry_row.empty else g.iloc[0]
        elif policy == "rule_based":
            # simple rule: if consecutive_failures >= 3 escalate, elif
            # amount is small just retry, else send a payment link.
            cf = g["consecutive_failures"].iloc[0]
            amt = g["amount"].iloc[0]
            if cf >= 3 and (g["action"] == "ESCALATE_TO_HUMAN").any():
                chosen = g[g["action"] == "ESCALATE_TO_HUMAN"].iloc[0]
            elif amt <= 2499 and (g["action"] == "RETRY").any():
                chosen = g[g["action"] == "RETRY"].iloc[0]
            elif (g["action"] == "PAYMENT_LINK").any():
                chosen = g[g["action"] == "PAYMENT_LINK"].iloc[0]
            else:
                chosen = g.iloc[0]
        elif policy == "propensity":
            chosen = g.loc[g["recovery_probability"].idxmax()]
        elif policy == "economic":
            # highest gross value after cost, ignoring the WAIT baseline
            gross_value = g["recovery_probability"] * g["amount"] - g["action_cost"]
            chosen = g.loc[gross_value.idxmax()]
        elif policy == "incremental":
            non_wait = g[g["action"] != config.BASELINE_ACTION]
            eligible = non_wait[
                (non_wait["net_incremental_contribution"] >= config.MIN_NET_CONTRIBUTION_TO_ACT)
                & (non_wait["incremental_lift"] >= config.MIN_INCREMENTAL_LIFT_TO_ACT)
            ]
            if eligible.empty:
                chosen = wait_row.iloc[0] if not wait_row.empty else g.iloc[0]
            else:
                chosen = eligible.loc[eligible["net_incremental_contribution"].idxmax()]
        else:
            raise ValueError(f"Unknown policy: {policy}")

        rows.append(
            {
                "_state_row_id": state_id,
                "policy": policy,
                "chosen_action": chosen["action"],
                "recovery_probability": chosen["recovery_probability"],
                "wait_probability": wait_prob,
                "amount": chosen["amount"],
                "action_cost": chosen.get("action_cost", config.ACTION_COSTS.get(chosen["action"], 0.0)),
                "incremental_lift": chosen["recovery_probability"] - wait_prob
                if pd.notna(wait_prob)
                else np.nan,
            }
        )

    return pd.DataFrame(rows)


def summarize_policy(policy_df: pd.DataFrame) -> dict:
    """Aggregate economic summary for one policy's chosen actions."""
    intervened = policy_df["chosen_action"] != config.BASELINE_ACTION
    expected_recovered_amount = (policy_df["recovery_probability"] * policy_df["amount"]).sum()
    expected_natural_recovery = (policy_df["wait_probability"] * policy_df["amount"]).sum()
    expected_incremental_recovery = expected_recovered_amount - expected_natural_recovery
    total_action_cost = policy_df.loc[intervened, "action_cost"].sum()
    net_contribution = expected_incremental_recovery - total_action_cost

    return {
        "policy": policy_df["policy"].iloc[0] if len(policy_df) else None,
        "n_states": len(policy_df),
        "intervention_count": int(intervened.sum()),
        "intervention_rate": float(intervened.mean()) if len(policy_df) else 0.0,
        "expected_recovery_rate": float(policy_df["recovery_probability"].mean()),
        "expected_recovered_amount": float(expected_recovered_amount),
        "expected_natural_recovery_amount": float(expected_natural_recovery),
        "expected_incremental_recovery_amount": float(expected_incremental_recovery),
        "total_action_cost": float(total_action_cost),
        "net_incremental_contribution": float(net_contribution),
    }


def compare_policies(scored_economics: pd.DataFrame, policies: list[str]) -> pd.DataFrame:
    summaries = []
    for p in policies:
        pdf = apply_baseline_policy(scored_economics, p)
        summaries.append(summarize_policy(pdf))
    return pd.DataFrame(summaries)
