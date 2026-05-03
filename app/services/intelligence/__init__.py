"""
Response Intelligence — deterministic V1 scoring, leakage detection,
recommendations, query helpers, and portal sanitiser.

PAS129/PAS130 backend foundation. No LLM calls, no provider calls.
Pure functions everywhere except queries.py (single read against pas_events).
"""

from app.services.intelligence.leakage import detect_leakage
from app.services.intelligence.recommendations import handoff_recommendation
from app.services.intelligence.sanitize import sanitize_event_for_portal
from app.services.intelligence.scoring import (
    SCORING_VERSION,
    callback_priority_score,
    readiness_score,
)

__all__ = [
    "SCORING_VERSION",
    "callback_priority_score",
    "detect_leakage",
    "handoff_recommendation",
    "readiness_score",
    "sanitize_event_for_portal",
]
