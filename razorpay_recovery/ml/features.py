"""
features.py

Builds ONLY decision-time-safe features. Every derived feature here is
computed from columns already present in config.NUMERICAL_FEATURES /
BOOLEAN_FEATURES / CATEGORICAL_FEATURES -- i.e. information available
before the action is taken. Nothing here touches reward, recovered_amount,
resolved, done, episode_return, or episode_length.
"""

from __future__ import annotations
import numpy as np
import pandas as pd

from . import config


def add_derived_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add safe, decision-time-only engineered features. Returns a copy."""
    out = df.copy()

    # amount relative to customer's historical LTV -- both known pre-action
    out["amount_to_ltv_ratio"] = out["amount"] / out["historical_ltv"].replace(0, np.nan)
    out["amount_to_ltv_ratio"] = out["amount_to_ltv_ratio"].fillna(0.0)

    # coarse bucket of how many payment attempts have already been made
    out["attempt_bucket"] = pd.cut(
        out["attempt_count"], bins=[0, 1, 2, np.inf], labels=["first_attempt", "second_attempt", "third_plus"]
    ).astype(str)

    # how long ago (in hours) the first failure happened, bucketed
    out["failure_recency_bucket"] = pd.cut(
        out["hours_since_first_failure"],
        bins=[-0.01, 0, 24, 72, np.inf],
        labels=["immediate", "within_1_day", "within_3_days", "over_3_days"],
    ).astype(str)

    # how much intervention pressure has already been applied to this customer
    # in this episode (prior interventions relative to consecutive failures)
    denom = out["consecutive_failures"].replace(0, np.nan)
    out["intervention_pressure"] = (out["interventions_count"] / denom).fillna(0.0)

    return out


def prepare_features(df: pd.DataFrame, fit_categories: bool = False) -> pd.DataFrame:
    """Prepare the full model-ready feature frame (features only, no target)."""
    df = add_derived_features(df)

    feature_cols = config.ALL_MODEL_FEATURES
    X = df[feature_cols].copy()

    # Categorical: cast to string, fill missing explicitly (spec section 10)
    for col in config.CATEGORICAL_FEATURES:
        X[col] = X[col].astype(str)
        X[col] = X[col].where(X[col].notna(), config.MISSING_CATEGORY_TOKEN)
        X[col] = X[col].replace({"nan": config.MISSING_CATEGORY_TOKEN, "None": config.MISSING_CATEGORY_TOKEN})

    # attempt_bucket / failure_recency_bucket are engineered categoricals (strings) too
    for col in ["attempt_bucket", "failure_recency_bucket"]:
        X[col] = X[col].astype(str)

    # Boolean -> int for CatBoost consistency
    for col in config.BOOLEAN_FEATURES:
        X[col] = X[col].astype(int)

    return X


def get_categorical_feature_names() -> list[str]:
    """All string/categorical columns CatBoost should treat natively as categorical."""
    return config.CATEGORICAL_FEATURES + ["attempt_bucket", "failure_recency_bucket"]


def extract_target(df: pd.DataFrame) -> pd.Series:
    return df[config.TARGET_COLUMN].astype(int)
