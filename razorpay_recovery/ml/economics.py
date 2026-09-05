"""
economics.py

Converts recovery probabilities into incremental economic value.
Pure functions of (probabilities, amount, action costs) -- no ML here.

    incremental_lift(action)      = P(recovery|action) - P(recovery|WAIT)
    incremental_value(action)     = incremental_lift(action) * amount
    net_incremental_contribution  = incremental_value - action_cost - friction_cost

NOTE: "incremental" is always relative to the WAIT (no-intervention)
baseline -- never call the gross predicted recovered amount "incremental
revenue" (see spec section 14).

CAUSAL CAVEAT: incremental_lift as computed here is a MODEL-ESTIMATED
difference from an observational, logged-policy dataset (behavior_prob is
constant in this data and carries no usable propensity information). It is
NOT a randomized-controlled-trial causal effect. Treat it as "estimated
incremental recovery opportunity", not proven causal uplift.
"""

from __future__ import annotations
import pandas as pd

from . import config


def add_incremental_lift(scored: pd.DataFrame) -> pd.DataFrame:
    out = scored.copy()
    out["incremental_lift"] = out["recovery_probability"] - out["wait_probability"]
    return out


def add_economic_value(scored: pd.DataFrame) -> pd.DataFrame:
    out = scored.copy()
    out["action_cost"] = out["action"].map(config.ACTION_COSTS).fillna(0.0)
    out["friction_cost"] = out["interventions_count"].apply(config.friction_cost)

    out["incremental_value"] = out["incremental_lift"] * out["amount"]
    out["net_incremental_contribution"] = (
        out["incremental_value"] - out["action_cost"] - out["friction_cost"]
    )
    return out


def score_economics(scored_with_wait: pd.DataFrame) -> pd.DataFrame:
    """Full pipeline: lift -> economic value, given scored candidates + wait baseline."""
    out = add_incremental_lift(scored_with_wait)
    out = add_economic_value(out)
    return out
