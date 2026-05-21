"""
PAS194 — Conversation strategy profiles.

A closed catalogue of five conversation strategies, each
expressing a different posture toward qualification, booking,
callback offers, and objection handling. Each strategy is a pure
modifier over the PAS193 default action plan; running scenarios
under different strategies is what makes PAS194 a comparison
layer rather than a single-strategy rehearsal.

Strict properties (enforced by tests and the readiness gate):

  * count(STRATEGIES) >= 5
  * every strategy carries STRATEGY_REQUIRED_KEYS
  * strategy_id values are unique and drawn from STRATEGY_IDS
  * plan_for(strategy_id, scenario) is deterministic
  * safety_violation_for(strategy_id, scenario_type) is
    deterministic and only returns values from
    KNOWN_SAFETY_VIOLATIONS
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple


STRATEGY_REQUIRED_KEYS: Tuple[str, ...] = (
    "strategy_id",
    "tone",
    "qualification_depth",
    "booking_pressure",
    "callback_preference",
    "objection_style",
    "safety_notes",
)


STRATEGY_IDS: Tuple[str, ...] = (
    "conservative",
    "balanced",
    "assertive",
    "callback_first",
    "booking_first",
)


KNOWN_SAFETY_VIOLATIONS: Tuple[str, ...] = (
    "agent_poaching",
    "language_misclaim",
    "qualification_pressure",
)


STRATEGIES: Tuple[Dict, ...] = (
    {
        "strategy_id":          "conservative",
        "tone":                 "deferential",
        "qualification_depth":  "deep",
        "booking_pressure":     "low",
        "callback_preference":  "prefer_callback",
        "objection_style":      "gentle",
        "safety_notes": (
            "Never injects an appointment offer on agent-conflict "
            "or language-unsupported scenarios. Always includes a "
            "qualify step. Replaces appointment offers with "
            "callback offers."
        ),
    },
    {
        "strategy_id":          "balanced",
        "tone":                 "neutral",
        "qualification_depth":  "standard",
        "booking_pressure":     "medium",
        "callback_preference":  "context_dependent",
        "objection_style":      "even",
        "safety_notes": (
            "Uses the PAS193 default action plan unchanged. Carries "
            "no per-scenario safety overrides."
        ),
    },
    {
        "strategy_id":          "assertive",
        "tone":                 "direct",
        "qualification_depth":  "shallow",
        "booking_pressure":     "high",
        "callback_preference":  "deprioritise_callback",
        "objection_style":      "firm",
        "safety_notes": (
            "Trades safety for booking pressure. Triggers "
            "agent_poaching on already_has_agent, "
            "language_misclaim on language_unsupported, and "
            "qualification_pressure on refuses_qualification. "
            "Comparison surfaces this trade-off."
        ),
    },
    {
        "strategy_id":          "callback_first",
        "tone":                 "supportive",
        "qualification_depth":  "standard",
        "booking_pressure":     "low",
        "callback_preference":  "always_offer_callback",
        "objection_style":      "even",
        "safety_notes": (
            "Always inserts a callback offer before closing, even "
            "when the default plan did not include one. Carries no "
            "safety overrides."
        ),
    },
    {
        "strategy_id":          "booking_first",
        "tone":                 "decisive",
        "qualification_depth":  "shallow",
        "booking_pressure":     "high",
        "callback_preference":  "fallback_only",
        "objection_style":      "firm",
        "safety_notes": (
            "Always inserts an appointment offer before closing, "
            "even when the scenario calls for restraint. Triggers "
            "agent_poaching on already_has_agent and "
            "language_misclaim on language_unsupported."
        ),
    },
)


STRATEGY_INDEX: Dict[str, Dict] = {s["strategy_id"]: s for s in STRATEGIES}


def strategy_count() -> int:
    return len(STRATEGIES)


def list_strategy_ids() -> List[str]:
    return [s["strategy_id"] for s in STRATEGIES]


# ──────────────────────────────────────────────────────────────────
# Plan modifiers
# ──────────────────────────────────────────────────────────────────

def _replace(plan: Tuple[str, ...], src: str, dst: str) -> List[str]:
    return [dst if a == src else a for a in plan]


def _ensure_before_close(plan: List[str], action: str) -> List[str]:
    if action in plan:
        return plan
    if "close" in plan:
        idx = plan.index("close")
        return plan[:idx] + [action] + plan[idx:]
    return plan + [action]


def _ensure_after_greet(plan: List[str], action: str) -> List[str]:
    if action in plan:
        return plan
    if plan and plan[0] == "greet":
        return [plan[0], action] + plan[1:]
    return [action] + plan


def plan_for(strategy_id: str, scenario: Dict, base_plan: Tuple[str, ...]) -> Tuple[str, ...]:
    """
    Return a strategy-modified action plan for the given scenario.

    `base_plan` is the PAS193 default plan for the scenario type.
    This function never mutates `base_plan` and always returns a
    new tuple.
    """
    if strategy_id == "balanced":
        return tuple(base_plan)

    if strategy_id == "conservative":
        out = _replace(base_plan, "offer_appointment", "offer_callback")
        out = _ensure_after_greet(out, "qualify")
        return tuple(out)

    if strategy_id == "assertive":
        out = _replace(base_plan, "offer_callback", "offer_appointment")
        return tuple(out)

    if strategy_id == "callback_first":
        out = _ensure_before_close(list(base_plan), "offer_callback")
        return tuple(out)

    if strategy_id == "booking_first":
        out = _ensure_before_close(list(base_plan), "offer_appointment")
        return tuple(out)

    return tuple(base_plan)


# ──────────────────────────────────────────────────────────────────
# Safety overrides
# ──────────────────────────────────────────────────────────────────
#
# Some (strategy, scenario_type) pairs are unsafe by construction.
# Assertive / booking_first strategies that push an appointment on
# a lead who already has an agent commit agent_poaching; pushing
# on a Spanish-only lead the engine cannot serve commits a
# language_misclaim; pressing for qualification on a lead who
# explicitly refused is qualification_pressure.
#
# Surfacing these via auto-fail is the point of the comparison
# layer: PAS194 must be able to show which strategies trade safety
# for raw conversion metrics.

_SAFETY_VIOLATIONS: Dict[Tuple[str, str], str] = {
    ("assertive",     "already_has_agent"):    "agent_poaching",
    ("booking_first", "already_has_agent"):    "agent_poaching",
    ("assertive",     "language_unsupported"): "language_misclaim",
    ("booking_first", "language_unsupported"): "language_misclaim",
    ("assertive",     "refuses_qualification"): "qualification_pressure",
}


def safety_violation_for(strategy_id: str, scenario_type: str) -> Optional[str]:
    return _SAFETY_VIOLATIONS.get((strategy_id, scenario_type))
