"""
decision_engine.py

Deterministic decision layer. The ML model NEVER directly executes an
action -- this module takes scored+economic candidate rows and applies
transparent, reproducible rules to pick a final decision.

Pipeline (spec section 15):
    model predictions -> incremental lift -> economic value
    -> policy checks -> final decision
"""

from __future__ import annotations
import pandas as pd

from . import config


def apply_policy_filters(candidates: pd.DataFrame) -> pd.DataFrame:
    """
    Deterministic safety/policy filters. The current dataset does not carry
    real-world policy fields (opted_out is a constant placeholder, no DND /
    quiet-hours / fraud flags exist), so no rows are actually dropped here
    today. The hook is intentionally kept so future fields
    (opted_out, DND, quiet_hours, fraud_flag, human_escalation_cap, etc.)
    can be wired in without touching the model or economics layers.
    """
    out = candidates.copy()
    out["_policy_pass"] = True

    if "opted_out" in out.columns:
        out.loc[out["opted_out"] == 1, "_policy_pass"] = False

    return out[out["_policy_pass"]].drop(columns=["_policy_pass"])


def decide(
    scored_economics: pd.DataFrame,
    min_net_contribution: float = config.MIN_NET_CONTRIBUTION_TO_ACT,
    min_incremental_lift: float = config.MIN_INCREMENTAL_LIFT_TO_ACT,
) -> pd.DataFrame:
    """
    scored_economics: long dataframe, one row per (state, candidate action),
        already containing recovery_probability, wait_probability,
        incremental_lift, net_incremental_contribution, and `_state_row_id`.

    Returns: one row PER STATE (`_state_row_id`) with the final decision.
    """
    valid = apply_policy_filters(scored_economics)

    # Never recommend WAIT itself as "the intervention" -- WAIT is the baseline.
    non_wait = valid[valid["action"] != config.BASELINE_ACTION].copy()

    results = []
    for state_id, group in non_wait.groupby("_state_row_id"):
        wait_prob = group["wait_probability"].iloc[0]

        eligible = group[
            (group["net_incremental_contribution"] >= min_net_contribution)
            & (group["incremental_lift"] >= min_incremental_lift)
        ]

        if eligible.empty:
            best = group.loc[group["net_incremental_contribution"].idxmax()]
            results.append(
                {
                    "_state_row_id": state_id,
                    "baseline_action": config.BASELINE_ACTION,
                    "baseline_recovery_probability": wait_prob,
                    "recommended_action": config.BASELINE_ACTION,
                    "action_recovery_probability": wait_prob,
                    "estimated_incremental_lift": 0.0,
                    "estimated_incremental_value": 0.0,
                    "action_cost": 0.0,
                    "estimated_net_contribution": 0.0,
                    "decision": "WAIT" if wait_prob >= 0.5 else "DONT_ACT",
                    "reason": (
                        f"No candidate action clears the minimum economic threshold "
                        f"(net contribution >= {min_net_contribution}, lift >= "
                        f"{min_incremental_lift}). Best alternative "
                        f"({best['action']}) only offered "
                        f"{best['net_incremental_contribution']:.1f} net contribution."
                    ),
                }
            )
        else:
            best = eligible.loc[eligible["net_incremental_contribution"].idxmax()]
            results.append(
                {
                    "_state_row_id": state_id,
                    "baseline_action": config.BASELINE_ACTION,
                    "baseline_recovery_probability": wait_prob,
                    "recommended_action": best["action"],
                    "action_recovery_probability": best["recovery_probability"],
                    "estimated_incremental_lift": best["incremental_lift"],
                    "estimated_incremental_value": best["incremental_value"],
                    "action_cost": best["action_cost"],
                    "estimated_net_contribution": best["net_incremental_contribution"],
                    "decision": "ACT",
                    "reason": (
                        f"{best['action']} has {best['incremental_lift']*100:.1f}pp "
                        f"estimated incremental recovery over WAIT "
                        f"({wait_prob:.2f} -> {best['recovery_probability']:.2f}), "
                        f"worth an estimated net contribution of "
                        f"{best['net_incremental_contribution']:.1f} after action "
                        f"cost ({best['action_cost']:.0f}) and friction "
                        f"({best['friction_cost']:.1f})."
                    ),
                }
            )

    return pd.DataFrame(results)
