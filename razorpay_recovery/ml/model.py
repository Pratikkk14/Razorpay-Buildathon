"""
model.py

The action-conditioned recovery model: P(resolved=1 | state, action).

One model, not one-per-action. `action` is fed in as a native categorical
feature -- see project spec section 6.
"""

from __future__ import annotations
from pathlib import Path
import pandas as pd
from catboost import CatBoostClassifier, Pool

from . import config
from . import features as feat


def build_pool(X: pd.DataFrame, y: pd.Series | None = None) -> Pool:
    cat_features = feat.get_categorical_feature_names()
    return Pool(data=X, label=y, cat_features=cat_features)


def train_model(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_val: pd.DataFrame,
    y_val: pd.Series,
    params: dict | None = None,
) -> CatBoostClassifier:
    params = dict(params or config.CATBOOST_PARAMS)
    model = CatBoostClassifier(**params)

    train_pool = build_pool(X_train, y_train)
    val_pool = build_pool(X_val, y_val)

    model.fit(train_pool, eval_set=val_pool, use_best_model=True)
    return model


def predict_proba(model: CatBoostClassifier, X: pd.DataFrame) -> pd.Series:
    pool = build_pool(X)
    proba = model.predict_proba(pool)[:, 1]
    return pd.Series(proba, index=X.index, name="recovery_probability")


def save_model(model: CatBoostClassifier, path: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    model.save_model(path)


def load_model(path: str) -> CatBoostClassifier:
    model = CatBoostClassifier()
    model.load_model(path)
    return model
