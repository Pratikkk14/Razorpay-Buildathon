"""Deterministic safety rules definitions."""
from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class PolicyCheckOutcome:
    passed: bool
    rule_key: str
    rule_name: str
    action_targeted: Optional[str] = None
    veto_reason: Optional[str] = None
    details: Optional[Dict[str, Any]] = None
