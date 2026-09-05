"""
config.py

Central, explicit configuration for the Recovery Intelligence system.

Design principle (see project spec section 13/26):
    Economic and policy constants live HERE, not inside the ML model.
    This lets us change economics/policy without retraining.

NOTHING in this file is fit from data by default. Where the data audit
(see AUDIT.md / notebook Section 4-5) suggested a value, that is noted
in a comment so a future calibration pass can find it easily.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List


# ---------------------------------------------------------------------------
# Data paths (override as needed)
# ---------------------------------------------------------------------------

DATA_PATHS = {
    "train": "data/episodes_train.parquet",
    "val": "data/episodes_val.parquet",
    "test": "data/episodes_test.parquet",
}

# ---------------------------------------------------------------------------
# Target
# ---------------------------------------------------------------------------

TARGET_COLUMN = "resolved"

# ---------------------------------------------------------------------------
# Identifier / grouping columns (never used as model features)
# ---------------------------------------------------------------------------

ID_COLUMNS = ["episode_id"]

# ---------------------------------------------------------------------------
# Columns EXCLUDED from decision-time features.
#
# Verified against the actual parquet files (not assumed):
#   - resolved / reward / recovered_amount / done: outcome of the transition
#     at (episode_id, timestep) -- i.e. the RESULT of taking `action` at this
#     state. Available only after the action is taken. `resolved` is used as
#     the supervised TARGET, never as an input feature.
#   - episode_length / episode_return: aggregate over the WHOLE episode,
#     only knowable once the episode has terminated. Pure post-hoc leakage
#     if used as a feature.
#   - episode_id: identifier, no predictive content, would let a tree
#     memorize individual episodes.
#   - provenance: constant per file (SYNTHETIC_TRAINING_DATA / HELD_OUT_
#     OFFLINE_EVAL) -- a dataset-split marker, not a real-world feature.
#   - behavior_prob: constant (1.0) in every row of every split. It carries
#     no information and is NOT a usable propensity score for off-policy
#     correction -- do not treat lift estimates as causal (see NOTE below).
#   - allowed_actions: decision-time-available (it shrinks predictably with
#     attempt_count/timestep), but it is a *policy mask*, not a numeric/
#     categorical predictor of recovery. It is used by the action scorer to
#     restrict candidate actions, not fed to the classifier as a feature.
# ---------------------------------------------------------------------------

EXCLUDED_COLUMNS = [
    "episode_id",
    "reward",
    "recovered_amount",
    "episode_return",
    "episode_length",
    "done",
    "resolved",          # target, not a feature
    "provenance",
    "behavior_prob",
    "allowed_actions",   # used as a policy mask elsewhere, not a model feature
]

# ---------------------------------------------------------------------------
# Decision-time features actually used by the model
# ---------------------------------------------------------------------------

NUMERICAL_FEATURES: List[str] = [
    "amount",
    "attempt_count",
    "hours_since_first_failure",
    "interventions_count",
    "consecutive_failures",
    "customer_ltv",
    "customer_failure_rate",
    "subscription_paid_count",
    "account_tenure_days",
    "lifetime_success_rate",
    "days_since_last_success",
    "historical_ltv",
    "timestep",
]

BOOLEAN_FEATURES: List[str] = [
    "is_weekend",
    "is_first_ever_failure",
]

CATEGORICAL_FEATURES: List[str] = [
    "failure_reason",
    "customer_archetype",
    "action",
]

# Safe engineered features (computed only from decision-time columns above)
DERIVED_FEATURES: List[str] = [
    "amount_to_ltv_ratio",
    "attempt_bucket",
    "failure_recency_bucket",
    "intervention_pressure",
]

ALL_MODEL_FEATURES: List[str] = (
    NUMERICAL_FEATURES + BOOLEAN_FEATURES + CATEGORICAL_FEATURES + DERIVED_FEATURES
)

CATBOOST_CAT_FEATURES: List[str] = CATEGORICAL_FEATURES  # native categorical handling

MISSING_CATEGORY_TOKEN = "__MISSING__"

# ---------------------------------------------------------------------------
# Candidate actions
# ---------------------------------------------------------------------------

ALL_ACTIONS: List[str] = [
    "WAIT",
    "RETRY",
    "PAYMENT_LINK",
    "SEND_REMINDER",
    "REQUEST_ALTERNATE_METHOD",
    "ESCALATE_TO_HUMAN",
    "STOP_RECOVERY",
]

BASELINE_ACTION = "WAIT"

# ---------------------------------------------------------------------------
# Action costs
#
# NOTE (audit finding -- see notebook Section 5 / AUDIT.md):
# The raw `reward` column in the dataset does NOT decompose cleanly into
# `recovered_amount - fixed_action_cost`. Implied per-action costs from
# resolved rows vary widely and by state (e.g. ESCALATE_TO_HUMAN averages
# ~243 implied cost, not a fixed constant; WAIT is NOT free in the raw
# reward signal). We do not use the raw `reward`/`episode_return` columns
# at all (they are excluded as post-outcome leakage). The ACTION_COSTS
# below are therefore an explicit, human-specified economic ASSUMPTION for
# the decision layer -- exactly as instructed -- kept separate from the
# model so it can be recalibrated later against real operational cost data
# without retraining anything.
# ---------------------------------------------------------------------------

ACTION_COSTS: Dict[str, float] = {
    "WAIT": 0,
    "STOP_RECOVERY": 0,
    "RETRY": 5,
    "SEND_REMINDER": 10,
    "PAYMENT_LINK": 15,
    "REQUEST_ALTERNATE_METHOD": 20,
    "ESCALATE_TO_HUMAN": 150,
}

# ---------------------------------------------------------------------------
# Friction model (customer fatigue from repeated contact).
# Simple, transparent, and pre-action-known: scales with how many
# interventions have ALREADY happened (decision-time information).
# This is a placeholder economic assumption, not derived from the data,
# and is intentionally kept in config so it's easy to replace.
# ---------------------------------------------------------------------------

FRICTION_COST_PER_PRIOR_INTERVENTION: float = 2.0


def friction_cost(interventions_count: int) -> float:
    """Friction cost is a function of *pre-action* intervention history only."""
    return FRICTION_COST_PER_PRIOR_INTERVENTION * max(0, int(interventions_count))


# ---------------------------------------------------------------------------
# Decision engine thresholds
# ---------------------------------------------------------------------------

MIN_NET_CONTRIBUTION_TO_ACT: float = 25.0   # below this, prefer WAIT/DON'T ACT
MIN_INCREMENTAL_LIFT_TO_ACT: float = 0.01   # 1 percentage point floor

# ---------------------------------------------------------------------------
# CatBoost training configuration (per spec section 8)
# ---------------------------------------------------------------------------

CATBOOST_PARAMS: Dict = dict(
    loss_function="Logloss",
    eval_metric="AUC",
    iterations=500,
    depth=7,
    learning_rate=0.05,
    random_seed=42,
    verbose=100,
)

RANDOM_SEED = 42
