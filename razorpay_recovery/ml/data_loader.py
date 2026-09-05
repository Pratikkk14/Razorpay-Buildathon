"""
data_loader.py

Loads the official episodes train/val/test parquet splits as-is.

IMPORTANT: per the project spec, these are treated as the OFFICIAL split.
We do not create a new random row-level split. We only verify the split's
integrity (no episode_id leakage across splits) and fail loudly if that
assumption is violated.
"""

from __future__ import annotations
from dataclasses import dataclass
import pandas as pd

from . import config


@dataclass
class SplitOverlapReport:
    train_val: int
    train_test: int
    val_test: int

    @property
    def is_clean(self) -> bool:
        return self.train_val == 0 and self.train_test == 0 and self.val_test == 0


def load_episode_splits(paths: dict | None = None) -> dict:
    """Load train/val/test parquet files. Returns dict of DataFrames."""
    paths = paths or config.DATA_PATHS
    frames = {}
    for split_name, path in paths.items():
        df = pd.read_parquet(path)
        frames[split_name] = df
    return frames


def verify_episode_overlap(frames: dict) -> SplitOverlapReport:
    """Verify episode_id does not leak across splits. Raises if it does."""
    train_ids = set(frames["train"]["episode_id"].unique())
    val_ids = set(frames["val"]["episode_id"].unique())
    test_ids = set(frames["test"]["episode_id"].unique())

    report = SplitOverlapReport(
        train_val=len(train_ids & val_ids),
        train_test=len(train_ids & test_ids),
        val_test=len(val_ids & test_ids),
    )
    return report


def basic_schema_check(frames: dict) -> None:
    """Ensure train/val/test have identical columns (spec section 10, item 8)."""
    cols = {name: list(df.columns) for name, df in frames.items()}
    reference = cols["train"]
    for name, c in cols.items():
        if c != reference:
            raise ValueError(
                f"Schema mismatch: split '{name}' columns differ from 'train'.\n"
                f"train: {reference}\n{name}: {c}"
            )


def load_and_verify(paths: dict | None = None) -> dict:
    """Convenience entrypoint used by the notebook: load + verify in one call."""
    frames = load_episode_splits(paths)
    basic_schema_check(frames)
    overlap = verify_episode_overlap(frames)
    if not overlap.is_clean:
        raise ValueError(
            f"Episode ID leakage detected across splits: {overlap}. "
            "Refusing to proceed -- this would invalidate evaluation."
        )
    return frames
