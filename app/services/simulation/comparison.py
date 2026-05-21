"""
PAS194 — Strategy comparison engine.

Runs the PAS193 scenario catalogue under every strategy in
STRATEGIES and produces a structured comparison report.

Strict properties (enforced by tests and the readiness gate):

  * Pure function chain. Same (strategies, scenarios, seed)
    produces the same comparison report.
  * Never imports twilio, slack_sdk, openai, anthropic, dotenv,
    supabase, or app.engine.state_machine.
  * Re-uses the PAS193 adapter's transcript primitives via
    in-package access to its internal action vocabulary tables —
    no behavioural mutation of the PAS193 adapter.
  * Carries no PII or production brokerage IDs through to the
    report.
"""

from __future__ import annotations

import hashlib
from typing import Dict, List, Optional, Sequence, Tuple

from app.services.simulation.adapter import (
    AGENT_ACTIONS,
    _ACTION_CAPABILITIES,
    _ACTION_PLAN_BY_TYPE,
    _AGENT_LINES,
)
from app.services.simulation.scoring import score_conversation
from app.services.simulation.strategies import (
    STRATEGIES,
    STRATEGY_IDS,
    STRATEGY_INDEX,
    plan_for,
    safety_violation_for,
)


COMPARISON_REPORT_REQUIRED_KEYS: Tuple[str, ...] = (
    "phase",
    "report_id",
    "generated_at",
    "strategy_count",
    "scenario_count",
    "best_strategy",
    "worst_strategy",
    "per_strategy_metrics",
    "per_scenario_winners",
    "failure_modes_by_strategy",
    "recommendation",
    "safety_invariants",
)


SAFETY_INVARIANTS: Tuple[str, ...] = (
    "no_real_phone_calls",
    "no_twilio_imports",
    "no_slack_imports",
    "no_supabase_mutation",
    "no_real_brokerage_ids",
    "no_secrets_in_report",
    "deterministic_scoring",
    "deterministic_strategy_modifiers",
)


# ──────────────────────────────────────────────────────────────────
# Strategy-aware conversation runner
# ──────────────────────────────────────────────────────────────────

def _default_plan_for(scenario_type: str) -> Tuple[str, ...]:
    return _ACTION_PLAN_BY_TYPE.get(
        scenario_type,
        ("greet", "ask_intent", "qualify", "offer_callback", "close"),
    )


def _build_turns(scenario: Dict, plan: Tuple[str, ...]) -> Tuple[List[Dict], List[str], List[str]]:
    turns: List[Dict] = []
    actions: List[str] = []
    capabilities: List[str] = []
    lead_script = scenario.get("lead_script") or ()
    for idx, action in enumerate(plan):
        lead_text = lead_script[idx] if idx < len(lead_script) else ""
        agent_text = _AGENT_LINES[action]
        turns.append({
            "turn":         len(turns) + 1,
            "agent_action": action,
            "agent_text":   agent_text,
            "lead_text":    lead_text,
        })
        actions.append(action)
        for cap in _ACTION_CAPABILITIES.get(action, ()):
            if cap not in capabilities:
                capabilities.append(cap)
    return turns, actions, capabilities


def run_scenario_under_strategy(strategy_id: str, scenario: Dict) -> Dict:
    """
    Run a single (strategy, scenario) pair and return a
    conversation record compatible with score_conversation.
    """
    if strategy_id not in STRATEGY_INDEX:
        raise ValueError(f"unknown strategy_id: {strategy_id!r}")

    base = _default_plan_for(scenario["scenario_type"])
    plan = plan_for(strategy_id, scenario, base)
    turns, actions, capabilities = _build_turns(scenario, plan)

    safety = {
        "unsafe_claim":           False,
        "pii_leak":               False,
        "hallucinated_policy":    False,
        "agent_poaching":         False,
        "qualification_pressure": False,
        "language_misclaim":      False,
    }
    violation = safety_violation_for(strategy_id, scenario["scenario_type"])
    if violation in safety:
        safety[violation] = True

    return {
        "scenario_id":      scenario["scenario_id"],
        "scenario_type":    scenario["scenario_type"],
        "supported":        scenario["supported"],
        "strategy_id":      strategy_id,
        "expected_goal":    scenario["expected_goal"],
        "turns":             turns,
        "actions":           actions,
        "capabilities":      capabilities,
        "agent_utterances":  [t["agent_text"] for t in turns],
        "lead_utterances":   [t["lead_text"]  for t in turns],
        "safety":            safety,
    }


# ──────────────────────────────────────────────────────────────────
# Comparison
# ──────────────────────────────────────────────────────────────────

def _rate(numerator: int, denominator: int) -> float:
    if denominator <= 0:
        return 0.0
    return round(numerator / denominator, 4)


def _avg(values: Sequence[float]) -> float:
    if not values:
        return 0.0
    return round(sum(values) / len(values), 2)


def _strategy_metrics(scored_rows: Sequence[Dict]) -> Dict:
    total = len(scored_rows)
    passed = sum(1 for r in scored_rows if r["passed"])
    booking = sum(1 for r in scored_rows if "appointment_attempted" in (r.get("capabilities_observed") or ()))
    callback = sum(1 for r in scored_rows if "callback_captured"    in (r.get("capabilities_observed") or ()))
    objection = sum(1 for r in scored_rows if "objection_handled"   in (r.get("capabilities_observed") or ()))
    scores = [float(r["score"]) for r in scored_rows]
    return {
        "runs":                     total,
        "pass_rate":                _rate(passed, total),
        "average_score":            _avg(scores),
        "booking_attempt_rate":     _rate(booking,   total),
        "callback_capture_rate":    _rate(callback,  total),
        "objection_handling_rate":  _rate(objection, total),
    }


def _failure_modes(scored_rows: Sequence[Dict], limit: int = 5) -> List[Dict]:
    counts: Dict[str, int] = {}
    for r in scored_rows:
        for reason in r.get("failure_reasons") or ():
            counts[reason] = counts.get(reason, 0) + 1
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return [{"reason": r, "count": c} for r, c in ordered[:limit]]


def _composite_rank(metrics: Dict) -> Tuple[float, float]:
    """
    Composite ranking: pass_rate first, then average_score. Higher
    is better. Used for best/worst selection.
    """
    return (float(metrics["pass_rate"]), float(metrics["average_score"]))


def _select_best_worst(
    per_strategy: Dict[str, Dict],
) -> Tuple[str, str]:
    items = sorted(
        per_strategy.items(),
        key=lambda kv: (_composite_rank(kv[1]), kv[0]),
        reverse=True,
    )
    best = items[0][0]
    worst = items[-1][0]
    return best, worst


def _per_scenario_winners(
    rows_by_strategy: Dict[str, List[Dict]],
    scenarios: Sequence[Dict],
) -> List[Dict]:
    out: List[Dict] = []
    by_strategy_by_scenario: Dict[str, Dict[str, Dict]] = {}
    for strat_id, rows in rows_by_strategy.items():
        by_strategy_by_scenario[strat_id] = {r["scenario_id"]: r for r in rows}
    for scenario in scenarios:
        sid = scenario["scenario_id"]
        best_score = -1
        winners: List[str] = []
        for strat_id in sorted(rows_by_strategy.keys()):
            row = by_strategy_by_scenario[strat_id].get(sid)
            if not row:
                continue
            sc = int(row["score"])
            if sc > best_score:
                best_score = sc
                winners = [strat_id]
            elif sc == best_score:
                winners.append(strat_id)
        out.append({
            "scenario_id": sid,
            "winners":     winners,
            "top_score":   best_score if best_score >= 0 else 0,
        })
    return out


def _recommendation(best: str, worst: str, per_strategy: Dict[str, Dict]) -> str:
    best_pass = per_strategy[best]["pass_rate"]
    worst_pass = per_strategy[worst]["pass_rate"]
    if best_pass >= 0.95 and worst_pass < 0.7:
        return (
            f"promote '{best}' as the default strategy; "
            f"do not deploy '{worst}' without safety review"
        )
    if best_pass >= 0.95:
        return f"promote '{best}' as the default strategy"
    return f"all strategies require further rehearsal before pilot"


def _report_id(
    strategy_ids: Sequence[str],
    scenario_ids: Sequence[str],
    seed: int,
) -> str:
    h = hashlib.sha256()
    h.update(("|".join(sorted(strategy_ids))).encode("utf-8"))
    h.update(b"||")
    h.update(("|".join(scenario_ids)).encode("utf-8"))
    h.update(f"|seed={int(seed)}".encode("utf-8"))
    return "pas194-cmp-" + h.hexdigest()[:16]


def compare_strategies(
    strategies: Sequence[Dict],
    scenarios: Sequence[Dict],
) -> Dict[str, List[Dict]]:
    """
    Run every strategy against every scenario and return a dict of
    {strategy_id: [scored_row, ...]}. Pure function.
    """
    out: Dict[str, List[Dict]] = {}
    for strategy in strategies:
        sid = strategy["strategy_id"]
        rows: List[Dict] = []
        for scenario in scenarios:
            conv = run_scenario_under_strategy(sid, scenario)
            result = score_conversation(conv, scenario)
            rows.append({
                "scenario_id":           scenario["scenario_id"],
                "scenario_type":         scenario["scenario_type"],
                "supported":             scenario["supported"],
                "score":                 result["score"],
                "passed":                result["passed"],
                "failure_reasons":       result["failure_reasons"],
                "recommendation_label":  result["recommendation_label"],
                "capabilities_observed": result["capabilities_observed"],
                "missing_criteria":      result["missing_criteria"],
            })
        out[sid] = rows
    return out


def build_comparison_report(
    rows_by_strategy: Dict[str, List[Dict]],
    scenarios: Sequence[Dict],
    generated_at: str,
    seed: int = 0,
) -> Dict:
    strategy_ids = sorted(rows_by_strategy.keys())
    scenario_ids = [s["scenario_id"] for s in scenarios]

    per_strategy: Dict[str, Dict] = {}
    failure_modes: Dict[str, List[Dict]] = {}
    for sid in strategy_ids:
        rows = rows_by_strategy[sid]
        per_strategy[sid] = _strategy_metrics(rows)
        failure_modes[sid] = _failure_modes(rows)

    best, worst = _select_best_worst(per_strategy)

    return {
        "phase":                     "PAS194",
        "report_id":                 _report_id(strategy_ids, scenario_ids, seed),
        "generated_at":              generated_at,
        "strategy_count":            len(strategy_ids),
        "scenario_count":            len(scenarios),
        "best_strategy":             best,
        "worst_strategy":            worst,
        "per_strategy_metrics":      per_strategy,
        "per_scenario_winners":      _per_scenario_winners(rows_by_strategy, scenarios),
        "failure_modes_by_strategy": failure_modes,
        "recommendation":            _recommendation(best, worst, per_strategy),
        "safety_invariants":         list(SAFETY_INVARIANTS),
    }
