"""
PAS193 — Simulation report builder.

Pure function. Takes a list of scored rehearsals plus a stable
seed (for the deterministic report_id) and returns a structured
report dict carrying the metrics PAS193 promises:

    total_simulations, pass_rate, average_score,
    booking_attempt_rate, callback_capture_rate,
    objection_handling_rate, top_failure_modes,
    best_performing_scenario_types,
    worst_performing_scenario_types,
    generated_at, report_id

`generated_at` is taken from the caller (so the rest of the report
is fully deterministic given the same inputs and timestamp). The
`report_id` is a stable hash of (scenario_ids tuple, seed) so two
runs over the same inputs produce the same id.
"""

from __future__ import annotations

import hashlib
from typing import Dict, List, Sequence, Tuple


REPORT_REQUIRED_KEYS: Tuple[str, ...] = (
    "phase",
    "report_id",
    "generated_at",
    "total_simulations",
    "pass_rate",
    "average_score",
    "booking_attempt_rate",
    "callback_capture_rate",
    "objection_handling_rate",
    "top_failure_modes",
    "best_performing_scenario_types",
    "worst_performing_scenario_types",
    "results",
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
)


def _rate(numerator: int, denominator: int) -> float:
    if denominator <= 0:
        return 0.0
    return round(numerator / denominator, 4)


def _avg(values: List[float]) -> float:
    if not values:
        return 0.0
    return round(sum(values) / len(values), 2)


def _top_failure_modes(results: Sequence[Dict], limit: int = 5) -> List[Dict]:
    counts: Dict[str, int] = {}
    for r in results:
        for reason in r.get("failure_reasons") or ():
            counts[reason] = counts.get(reason, 0) + 1
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return [{"reason": r, "count": c} for r, c in ordered[:limit]]


def _scenario_type_performance(results: Sequence[Dict]) -> List[Dict]:
    buckets: Dict[str, List[float]] = {}
    for r in results:
        buckets.setdefault(r["scenario_type"], []).append(float(r.get("score") or 0))
    out: List[Dict] = []
    for stype, scores in buckets.items():
        out.append({
            "scenario_type": stype,
            "average_score": _avg(scores),
            "runs":          len(scores),
        })
    return out


def _best_and_worst(
    perf: List[Dict],
    limit: int = 3,
) -> Tuple[List[Dict], List[Dict]]:
    best = sorted(
        perf,
        key=lambda d: (-d["average_score"], d["scenario_type"]),
    )[:limit]
    worst = sorted(
        perf,
        key=lambda d: (d["average_score"], d["scenario_type"]),
    )[:limit]
    return best, worst


def _report_id(scenario_ids: Sequence[str], seed: int) -> str:
    h = hashlib.sha256()
    h.update(("|".join(scenario_ids)).encode("utf-8"))
    h.update(f"|seed={int(seed)}".encode("utf-8"))
    return "pas193-rep-" + h.hexdigest()[:16]


def build_report(
    scored: Sequence[Dict],
    generated_at: str,
    seed: int = 0,
) -> Dict:
    total = len(scored)
    passed = sum(1 for r in scored if r.get("passed"))
    scores = [float(r.get("score") or 0) for r in scored]

    booking = sum(1 for r in scored if "appointment_attempted" in (r.get("capabilities_observed") or ()))
    callback = sum(1 for r in scored if "callback_captured"    in (r.get("capabilities_observed") or ()))
    objection = sum(1 for r in scored if "objection_handled"   in (r.get("capabilities_observed") or ()))

    perf = _scenario_type_performance(scored)
    best, worst = _best_and_worst(perf)

    scenario_ids = [r["scenario_id"] for r in scored]
    return {
        "phase":                            "PAS193",
        "report_id":                        _report_id(scenario_ids, seed),
        "generated_at":                     generated_at,
        "total_simulations":                total,
        "pass_rate":                        _rate(passed, total),
        "average_score":                    _avg(scores),
        "booking_attempt_rate":             _rate(booking,   total),
        "callback_capture_rate":            _rate(callback,  total),
        "objection_handling_rate":          _rate(objection, total),
        "top_failure_modes":                _top_failure_modes(scored),
        "best_performing_scenario_types":   best,
        "worst_performing_scenario_types":  worst,
        "results":                          list(scored),
        "safety_invariants":                list(SAFETY_INVARIANTS),
    }
