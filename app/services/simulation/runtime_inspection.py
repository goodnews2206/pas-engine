"""
PAS199 — Operational runtime inspection service.

Pure function. Consumes the four artefacts that comprise a single
PAS lineage —

    PAS195 recommendation
        -> PAS196 review
            -> PAS197 package
                -> PAS198 runtime

— validates the joins, reconstructs the lineage graph, summarises
the runtime / safety / capability / transcript surface, exposes
bounded read-only transcript-replay helpers, and (optionally)
diffs a second PAS198 runtime against the first.

The inspection is strictly read-only. It never executes anything,
never imports Twilio, Slack, Supabase, OpenAI, Anthropic, dotenv,
or the live state machine, never reads .env, never opens a
network connection, never mutates anything. The CLI is the only
writer; it writes exclusively under reports/simulations/.

Contract for a valid input set:

  * recommendation["recommendation_id"]      non-empty str
  * recommendation["status"]                 == "CANDIDATE"
  * recommendation["operator_required"]      is True
  * recommendation["recommended_strategy"]   non-empty str
  * review["review_id"]                      non-empty str
  * review["recommendation_id"]              == recommendation["recommendation_id"]
  * review["new_status"]                     == "APPROVED_FOR_MANUAL_TEST"
  * review["live_behavior_changed"]          is False
  * package["package_id"]                    non-empty str
  * package["recommendation_id"]             == recommendation["recommendation_id"]
  * package["review_id"]                     == review["review_id"]
  * package["strategy_id"]                   == recommendation["recommended_strategy"]
  * package["status"]                        == "READY_FOR_MANUAL_TEST"
  * package["allowed_environment"]           == "SIMULATION_ONLY"
  * package["live_behavior_changed"]         is False
  * runtime["runtime_id"]                    non-empty str
  * runtime["package_id"]                    == package["package_id"]
  * runtime["executed_strategy"]             == package["strategy_id"]
  * runtime["status"]                        == "EXECUTED"
  * runtime["allowed_environment"]           == "SIMULATION_ONLY"
  * runtime["live_behavior_changed"]         is False

Any contract violation raises RuntimeInspectionValidationError.

Output inspection artefact (closed schema):

  * inspection_id           — deterministic SHA-256-derived hash
  * phase                   — "PAS199"
  * generated_at            — caller-supplied ISO timestamp
  * allowed_environment     — fixed to "SIMULATION_ONLY"
  * live_behavior_changed   — fixed to False
  * lineage_summary
  * runtime_summary
  * safety_summary
  * capability_summary
  * transcript_summary
  * artifact_integrity
  * comparison              — null unless compare_runtime supplied
"""

from __future__ import annotations

import hashlib
from typing import Dict, List, Optional, Tuple


# ──────────────────────────────────────────────────────────────────
# Closed vocabularies
# ──────────────────────────────────────────────────────────────────

INSPECTION_ENVIRONMENT_SIMULATION_ONLY: str = "SIMULATION_ONLY"


REQUIRED_RECOMMENDATION_STATUS: str = "CANDIDATE"
REQUIRED_REVIEW_NEW_STATUS:     str = "APPROVED_FOR_MANUAL_TEST"
REQUIRED_PACKAGE_STATUS:        str = "READY_FOR_MANUAL_TEST"
REQUIRED_PACKAGE_ENVIRONMENT:   str = "SIMULATION_ONLY"
REQUIRED_RUNTIME_STATUS:        str = "EXECUTED"
REQUIRED_RUNTIME_ENVIRONMENT:   str = "SIMULATION_ONLY"


INSPECTION_REQUIRED_KEYS: Tuple[str, ...] = (
    "inspection_id",
    "phase",
    "generated_at",
    "allowed_environment",
    "live_behavior_changed",
    "lineage_summary",
    "runtime_summary",
    "safety_summary",
    "capability_summary",
    "transcript_summary",
    "artifact_integrity",
    "comparison",
)


LINEAGE_SUMMARY_KEYS: Tuple[str, ...] = (
    "recommendation_id",
    "review_id",
    "package_id",
    "runtime_id",
    "strategy_id",
    "lineage_intact",
    "lineage_chain",
)


RUNTIME_SUMMARY_KEYS: Tuple[str, ...] = (
    "executed_strategy",
    "execution_status",
    "scenarios_executed",
    "pass_rate",
    "average_score",
)


SAFETY_SUMMARY_KEYS: Tuple[str, ...] = (
    "outcome",
    "auto_fail_count",
    "auto_fail_reasons",
    "unsafe_output_count",
    "hallucinated_policy_count",
    "pii_leak_count",
)


CAPABILITY_SUMMARY_KEYS: Tuple[str, ...] = (
    "qualification_captured_rate",
    "objection_handled_rate",
    "callback_captured_rate",
    "booking_attempted_rate",
)


TRANSCRIPT_SUMMARY_KEYS: Tuple[str, ...] = (
    "scenario_count",
    "total_turns",
    "agent_turns",
    "lead_turns",
    "per_scenario",
    "replay_sample",
)


REPLAY_KEYS: Tuple[str, ...] = (
    "scenario_id",
    "sequence_ids",
    "actors",
    "capability_markers",
    "safety_markers",
)


ARTIFACT_INTEGRITY_KEYS: Tuple[str, ...] = (
    "recommendation_status_candidate",
    "recommendation_operator_required",
    "review_new_status_approved_for_manual_test",
    "review_live_behavior_changed_false",
    "package_status_ready_for_manual_test",
    "package_allowed_environment_simulation_only",
    "package_live_behavior_changed_false",
    "runtime_status_executed",
    "runtime_allowed_environment_simulation_only",
    "runtime_live_behavior_changed_false",
    "review_recommendation_id_matches_recommendation",
    "package_recommendation_id_matches_recommendation",
    "package_review_id_matches_review",
    "package_strategy_id_matches_recommendation",
    "runtime_package_id_matches_package",
    "runtime_executed_strategy_matches_package",
)


COMPARISON_KEYS: Tuple[str, ...] = (
    "compared_runtime_id",
    "pass_rate_delta",
    "average_score_delta",
    "capability_delta",
    "safety_delta",
    "transcript_size_delta",
    "flipped_scenarios",
)


# Closed actor vocabulary that replay helpers expect to find in
# PAS198 transcript turns.
ACTORS: Tuple[str, ...] = ("agent", "lead")


# Closed capability marker vocabulary mirrored from PAS198. Replay
# helpers refuse markers outside this set.
CAPABILITY_MARKERS: Tuple[str, ...] = (
    "qualification_captured",
    "appointment_attempted",
    "callback_captured",
    "objection_handled",
    "conversation_completed",
)


# Closed safety marker vocabulary mirrored from PAS198.
SAFETY_MARKERS: Tuple[str, ...] = (
    "unsafe_claim",
    "pii_leak",
    "hallucinated_policy",
    "agent_poaching",
    "qualification_pressure",
    "language_misclaim",
    "pii_pattern_in_utterance",
    "supported_false_no_safe_handoff",
    "empty_transcript",
)


# ──────────────────────────────────────────────────────────────────
# Validation
# ──────────────────────────────────────────────────────────────────

class RuntimeInspectionValidationError(ValueError):
    """Raised when the four-artefact set violates the PAS199 contract."""


def _require_keys(payload: Dict, keys: Tuple[str, ...], label: str) -> None:
    if not isinstance(payload, dict):
        raise RuntimeInspectionValidationError(
            f"{label} must be a dict"
        )
    for k in keys:
        if k not in payload:
            raise RuntimeInspectionValidationError(
                f"{label} missing required key {k!r}"
            )


def _require_non_empty_str(value, label: str) -> None:
    if not isinstance(value, str) or not value:
        raise RuntimeInspectionValidationError(
            f"{label} must be a non-empty string"
        )


def _validate_recommendation(recommendation: Dict) -> None:
    _require_keys(
        recommendation,
        ("recommendation_id", "status", "operator_required",
         "recommended_strategy"),
        label="recommendation",
    )
    _require_non_empty_str(
        recommendation["recommendation_id"], "recommendation.recommendation_id",
    )
    if recommendation["status"] != REQUIRED_RECOMMENDATION_STATUS:
        raise RuntimeInspectionValidationError(
            f"recommendation.status must be "
            f"{REQUIRED_RECOMMENDATION_STATUS!r}; "
            f"got {recommendation['status']!r}"
        )
    if recommendation["operator_required"] is not True:
        raise RuntimeInspectionValidationError(
            "recommendation.operator_required must be True"
        )
    _require_non_empty_str(
        recommendation["recommended_strategy"],
        "recommendation.recommended_strategy",
    )


def _validate_review(review: Dict, recommendation: Dict) -> None:
    _require_keys(
        review,
        ("review_id", "recommendation_id", "new_status",
         "live_behavior_changed"),
        label="review",
    )
    _require_non_empty_str(review["review_id"], "review.review_id")
    if review["new_status"] != REQUIRED_REVIEW_NEW_STATUS:
        raise RuntimeInspectionValidationError(
            f"review.new_status must be {REQUIRED_REVIEW_NEW_STATUS!r}; "
            f"got {review['new_status']!r}"
        )
    if review["live_behavior_changed"] is not False:
        raise RuntimeInspectionValidationError(
            "review.live_behavior_changed must be False"
        )
    if review["recommendation_id"] != recommendation["recommendation_id"]:
        raise RuntimeInspectionValidationError(
            f"review.recommendation_id "
            f"({review['recommendation_id']!r}) must match "
            f"recommendation.recommendation_id "
            f"({recommendation['recommendation_id']!r})"
        )


def _validate_package(package: Dict, recommendation: Dict, review: Dict) -> None:
    _require_keys(
        package,
        ("package_id", "recommendation_id", "review_id", "strategy_id",
         "status", "allowed_environment", "live_behavior_changed"),
        label="package",
    )
    _require_non_empty_str(package["package_id"], "package.package_id")
    if package["status"] != REQUIRED_PACKAGE_STATUS:
        raise RuntimeInspectionValidationError(
            f"package.status must be {REQUIRED_PACKAGE_STATUS!r}; "
            f"got {package['status']!r}"
        )
    if package["allowed_environment"] != REQUIRED_PACKAGE_ENVIRONMENT:
        raise RuntimeInspectionValidationError(
            f"package.allowed_environment must be "
            f"{REQUIRED_PACKAGE_ENVIRONMENT!r}; "
            f"got {package['allowed_environment']!r}"
        )
    if package["live_behavior_changed"] is not False:
        raise RuntimeInspectionValidationError(
            "package.live_behavior_changed must be False"
        )
    if package["recommendation_id"] != recommendation["recommendation_id"]:
        raise RuntimeInspectionValidationError(
            f"package.recommendation_id "
            f"({package['recommendation_id']!r}) must match "
            f"recommendation.recommendation_id "
            f"({recommendation['recommendation_id']!r})"
        )
    if package["review_id"] != review["review_id"]:
        raise RuntimeInspectionValidationError(
            f"package.review_id ({package['review_id']!r}) must "
            f"match review.review_id ({review['review_id']!r})"
        )
    if package["strategy_id"] != recommendation["recommended_strategy"]:
        raise RuntimeInspectionValidationError(
            f"package.strategy_id ({package['strategy_id']!r}) must "
            f"match recommendation.recommended_strategy "
            f"({recommendation['recommended_strategy']!r})"
        )


def _validate_runtime(runtime: Dict, package: Dict) -> None:
    _require_keys(
        runtime,
        ("runtime_id", "package_id", "executed_strategy", "status",
         "allowed_environment", "live_behavior_changed",
         "transcript_bundle", "runtime_score", "capability_summary",
         "safety_outcome", "execution_status", "executed_scenarios"),
        label="runtime",
    )
    _require_non_empty_str(runtime["runtime_id"], "runtime.runtime_id")
    if runtime["status"] != REQUIRED_RUNTIME_STATUS:
        raise RuntimeInspectionValidationError(
            f"runtime.status must be {REQUIRED_RUNTIME_STATUS!r}; "
            f"got {runtime['status']!r}"
        )
    if runtime["allowed_environment"] != REQUIRED_RUNTIME_ENVIRONMENT:
        raise RuntimeInspectionValidationError(
            f"runtime.allowed_environment must be "
            f"{REQUIRED_RUNTIME_ENVIRONMENT!r}; "
            f"got {runtime['allowed_environment']!r}"
        )
    if runtime["live_behavior_changed"] is not False:
        raise RuntimeInspectionValidationError(
            "runtime.live_behavior_changed must be False"
        )
    if runtime["package_id"] != package["package_id"]:
        raise RuntimeInspectionValidationError(
            f"runtime.package_id ({runtime['package_id']!r}) must "
            f"match package.package_id ({package['package_id']!r})"
        )
    if runtime["executed_strategy"] != package["strategy_id"]:
        raise RuntimeInspectionValidationError(
            f"runtime.executed_strategy "
            f"({runtime['executed_strategy']!r}) must match "
            f"package.strategy_id ({package['strategy_id']!r})"
        )


# ──────────────────────────────────────────────────────────────────
# Read-only transcript replay
# ──────────────────────────────────────────────────────────────────

def replay_transcript(runtime: Dict, scenario_id: str) -> Dict:
    """
    Deterministic read-only replay of one scenario's transcript
    from a PAS198 runtime artefact. Returns a bounded record with
    sequence_ids, actors, per-turn capability markers, and per-turn
    safety markers. Raises if the scenario_id is not present in the
    runtime's transcript bundle.

    Never executes anything. Never mutates the runtime.
    """
    _require_non_empty_str(scenario_id, "scenario_id")
    bundle = runtime.get("transcript_bundle") or []
    target: Optional[Dict] = None
    for entry in bundle:
        if entry.get("scenario_id") == scenario_id:
            target = entry
            break
    if target is None:
        raise RuntimeInspectionValidationError(
            f"scenario_id {scenario_id!r} not present in runtime "
            f"transcript bundle"
        )
    turns = target.get("turns") or []
    sequence_ids: List[int] = []
    actors:       List[str] = []
    caps:         List[List[str]] = []
    safes:        List[List[str]] = []
    for t in turns:
        sequence_ids.append(int(t["sequence_id"]))
        actors.append(str(t["actor"]))
        caps.append(list(t.get("capability_markers") or []))
        safes.append(list(t.get("safety_markers") or []))
    return {
        "scenario_id":        scenario_id,
        "sequence_ids":       sequence_ids,
        "actors":             actors,
        "capability_markers": caps,
        "safety_markers":     safes,
    }


def _transcript_summary(runtime: Dict) -> Dict:
    bundle = runtime.get("transcript_bundle") or []
    per_scenario: List[Dict] = []
    total_turns = 0
    agent_turns = 0
    lead_turns  = 0
    for entry in bundle:
        turns = entry.get("turns") or []
        a = sum(1 for t in turns if t.get("actor") == "agent")
        b = sum(1 for t in turns if t.get("actor") == "lead")
        total_turns += len(turns)
        agent_turns += a
        lead_turns  += b
        per_scenario.append({
            "scenario_id":        entry.get("scenario_id"),
            "scenario_type":      entry.get("scenario_type"),
            "supported":          bool(entry.get("supported", True)),
            "turn_count":         len(turns),
            "agent_turns":        a,
            "lead_turns":         b,
            "capability_markers": list(entry.get("capability_markers") or []),
            "safety_markers":     list(entry.get("safety_markers") or []),
        })
    replay_sample: Optional[Dict] = None
    if bundle:
        first_sid = bundle[0].get("scenario_id")
        if isinstance(first_sid, str) and first_sid:
            replay_sample = replay_transcript(runtime, first_sid)
    return {
        "scenario_count": len(bundle),
        "total_turns":    total_turns,
        "agent_turns":    agent_turns,
        "lead_turns":     lead_turns,
        "per_scenario":   per_scenario,
        "replay_sample":  replay_sample,
    }


# ──────────────────────────────────────────────────────────────────
# Summaries
# ──────────────────────────────────────────────────────────────────

def _lineage_summary(
    recommendation: Dict, review: Dict, package: Dict, runtime: Dict,
) -> Dict:
    return {
        "recommendation_id": str(recommendation["recommendation_id"]),
        "review_id":         str(review["review_id"]),
        "package_id":        str(package["package_id"]),
        "runtime_id":        str(runtime["runtime_id"]),
        "strategy_id":       str(package["strategy_id"]),
        "lineage_intact":    True,
        "lineage_chain": [
            "pas195->pas196",
            "pas196->pas197",
            "pas197->pas198",
        ],
    }


def _runtime_summary(runtime: Dict) -> Dict:
    score = runtime.get("runtime_score") or {}
    return {
        "executed_strategy":  str(runtime.get("executed_strategy") or ""),
        "execution_status":   str(runtime.get("execution_status") or ""),
        "scenarios_executed": len(runtime.get("executed_scenarios") or ()),
        "pass_rate":          float(score.get("pass_rate") or 0.0),
        "average_score":      float(score.get("average_score") or 0.0),
    }


def _safety_summary(runtime: Dict) -> Dict:
    safety = runtime.get("safety_outcome") or {}
    per = (runtime.get("runtime_score") or {}).get("per_scenario") or []
    unsafe = sum(1 for r in per if r.get("unsafe_output_detected"))
    halluc = sum(1 for r in per if r.get("hallucinated_policy_detected"))
    pii    = sum(1 for r in per if r.get("pii_leak_detected"))
    return {
        "outcome":                   str(safety.get("outcome") or ""),
        "auto_fail_count":           int(safety.get("auto_fail_count") or 0),
        "auto_fail_reasons":         list(safety.get("auto_fail_reasons") or []),
        "unsafe_output_count":       unsafe,
        "hallucinated_policy_count": halluc,
        "pii_leak_count":            pii,
    }


def _capability_summary(runtime: Dict) -> Dict:
    caps = runtime.get("capability_summary") or {}
    return {
        "qualification_captured_rate": float(caps.get("qualification_captured_rate") or 0.0),
        "objection_handled_rate":      float(caps.get("objection_handled_rate")      or 0.0),
        "callback_captured_rate":      float(caps.get("callback_captured_rate")      or 0.0),
        "booking_attempted_rate":      float(caps.get("booking_attempted_rate")      or 0.0),
    }


def _artifact_integrity(
    recommendation: Dict, review: Dict, package: Dict, runtime: Dict,
) -> Dict:
    return {
        "recommendation_status_candidate": (
            recommendation.get("status") == REQUIRED_RECOMMENDATION_STATUS
        ),
        "recommendation_operator_required": (
            recommendation.get("operator_required") is True
        ),
        "review_new_status_approved_for_manual_test": (
            review.get("new_status") == REQUIRED_REVIEW_NEW_STATUS
        ),
        "review_live_behavior_changed_false": (
            review.get("live_behavior_changed") is False
        ),
        "package_status_ready_for_manual_test": (
            package.get("status") == REQUIRED_PACKAGE_STATUS
        ),
        "package_allowed_environment_simulation_only": (
            package.get("allowed_environment") == REQUIRED_PACKAGE_ENVIRONMENT
        ),
        "package_live_behavior_changed_false": (
            package.get("live_behavior_changed") is False
        ),
        "runtime_status_executed": (
            runtime.get("status") == REQUIRED_RUNTIME_STATUS
        ),
        "runtime_allowed_environment_simulation_only": (
            runtime.get("allowed_environment") == REQUIRED_RUNTIME_ENVIRONMENT
        ),
        "runtime_live_behavior_changed_false": (
            runtime.get("live_behavior_changed") is False
        ),
        "review_recommendation_id_matches_recommendation": (
            review.get("recommendation_id")
            == recommendation.get("recommendation_id")
        ),
        "package_recommendation_id_matches_recommendation": (
            package.get("recommendation_id")
            == recommendation.get("recommendation_id")
        ),
        "package_review_id_matches_review": (
            package.get("review_id") == review.get("review_id")
        ),
        "package_strategy_id_matches_recommendation": (
            package.get("strategy_id")
            == recommendation.get("recommended_strategy")
        ),
        "runtime_package_id_matches_package": (
            runtime.get("package_id") == package.get("package_id")
        ),
        "runtime_executed_strategy_matches_package": (
            runtime.get("executed_strategy") == package.get("strategy_id")
        ),
    }


# ──────────────────────────────────────────────────────────────────
# Runtime comparison
# ──────────────────────────────────────────────────────────────────

def _validate_runtime_for_comparison(runtime: Dict, label: str) -> None:
    _require_keys(
        runtime,
        ("runtime_id", "status", "allowed_environment",
         "live_behavior_changed", "executed_scenarios",
         "transcript_bundle", "runtime_score", "capability_summary",
         "safety_outcome"),
        label=label,
    )
    if runtime["status"] != REQUIRED_RUNTIME_STATUS:
        raise RuntimeInspectionValidationError(
            f"{label}.status must be {REQUIRED_RUNTIME_STATUS!r}; "
            f"got {runtime['status']!r}"
        )
    if runtime["allowed_environment"] != REQUIRED_RUNTIME_ENVIRONMENT:
        raise RuntimeInspectionValidationError(
            f"{label}.allowed_environment must be "
            f"{REQUIRED_RUNTIME_ENVIRONMENT!r}; "
            f"got {runtime['allowed_environment']!r}"
        )
    if runtime["live_behavior_changed"] is not False:
        raise RuntimeInspectionValidationError(
            f"{label}.live_behavior_changed must be False"
        )


def _per_scenario_index(runtime: Dict) -> Dict[str, Dict]:
    rows = (runtime.get("runtime_score") or {}).get("per_scenario") or []
    return {str(r["scenario_id"]): r for r in rows}


def compare_runtimes(runtime_a: Dict, runtime_b: Dict) -> Dict:
    """
    Deterministic delta between two PAS198 runtimes. Both must be
    EXECUTED, SIMULATION_ONLY, and live_behavior_changed=False.
    The result is a bounded record of score/capability/safety/
    transcript-size deltas plus a sorted list of scenarios whose
    `passed` flag flipped between A and B.

    Pure function. Never mutates either runtime.
    """
    _validate_runtime_for_comparison(runtime_a, label="runtime_a")
    _validate_runtime_for_comparison(runtime_b, label="runtime_b")

    score_a = runtime_a.get("runtime_score") or {}
    score_b = runtime_b.get("runtime_score") or {}
    caps_a  = runtime_a.get("capability_summary") or {}
    caps_b  = runtime_b.get("capability_summary") or {}
    safe_a  = runtime_a.get("safety_outcome") or {}
    safe_b  = runtime_b.get("safety_outcome") or {}

    def _f(d: Dict, k: str) -> float:
        return float(d.get(k) or 0.0)

    def _diff(d_a: Dict, d_b: Dict, k: str) -> float:
        return round(_f(d_b, k) - _f(d_a, k), 4)

    capability_delta = {
        "qualification_captured_rate": _diff(caps_a, caps_b, "qualification_captured_rate"),
        "objection_handled_rate":      _diff(caps_a, caps_b, "objection_handled_rate"),
        "callback_captured_rate":      _diff(caps_a, caps_b, "callback_captured_rate"),
        "booking_attempted_rate":      _diff(caps_a, caps_b, "booking_attempted_rate"),
    }

    safety_delta = {
        "auto_fail_count_delta": (
            int(safe_b.get("auto_fail_count") or 0)
            - int(safe_a.get("auto_fail_count") or 0)
        ),
        "outcome_changed": (
            safe_a.get("outcome") != safe_b.get("outcome")
        ),
        "outcome_a": str(safe_a.get("outcome") or ""),
        "outcome_b": str(safe_b.get("outcome") or ""),
    }

    bundle_a = runtime_a.get("transcript_bundle") or []
    bundle_b = runtime_b.get("transcript_bundle") or []
    turns_a = sum(len(e.get("turns") or []) for e in bundle_a)
    turns_b = sum(len(e.get("turns") or []) for e in bundle_b)
    transcript_size_delta = {
        "total_turns_a": turns_a,
        "total_turns_b": turns_b,
        "total_turns_delta": turns_b - turns_a,
        "scenario_count_a": len(bundle_a),
        "scenario_count_b": len(bundle_b),
        "scenario_count_delta": len(bundle_b) - len(bundle_a),
    }

    idx_a = _per_scenario_index(runtime_a)
    idx_b = _per_scenario_index(runtime_b)
    shared = sorted(set(idx_a.keys()) & set(idx_b.keys()))
    flipped: List[Dict] = []
    for sid in shared:
        pa = bool(idx_a[sid].get("passed"))
        pb = bool(idx_b[sid].get("passed"))
        if pa != pb:
            flipped.append({
                "scenario_id": sid,
                "passed_a":    pa,
                "passed_b":    pb,
            })

    return {
        "compared_runtime_id":   str(runtime_b.get("runtime_id") or ""),
        "pass_rate_delta":       _diff(score_a, score_b, "pass_rate"),
        "average_score_delta":   _diff(score_a, score_b, "average_score"),
        "capability_delta":      capability_delta,
        "safety_delta":          safety_delta,
        "transcript_size_delta": transcript_size_delta,
        "flipped_scenarios":     flipped,
    }


# ──────────────────────────────────────────────────────────────────
# Inspection ID
# ──────────────────────────────────────────────────────────────────

def _inspection_id(
    recommendation_id: str,
    review_id: str,
    package_id: str,
    runtime_id: str,
    compared_runtime_id: Optional[str],
) -> str:
    h = hashlib.sha256()
    for piece in (
        recommendation_id,
        review_id,
        package_id,
        runtime_id,
        compared_runtime_id or "",
    ):
        h.update(str(piece).encode("utf-8"))
        h.update(b"||")
    return "pas199-insp-" + h.hexdigest()[:16]


# ──────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────

def build_inspection(
    recommendation: Dict,
    review: Dict,
    package: Dict,
    runtime: Dict,
    *,
    generated_at: str,
    compare_runtime: Optional[Dict] = None,
) -> Dict:
    """
    Validate the four-artefact lineage and build the inspection
    artefact. Pure function. Same inputs produce the same
    inspection, including the same inspection_id, every call.

    The inspection's `allowed_environment` is fixed at
    SIMULATION_ONLY and `live_behavior_changed` is fixed at False
    by construction — neither can be set by the caller.

    If `compare_runtime` is supplied, a deterministic delta against
    the primary runtime is attached as `comparison`.
    """
    _require_non_empty_str(generated_at, "generated_at")

    _validate_recommendation(recommendation)
    _validate_review(review, recommendation)
    _validate_package(package, recommendation, review)
    _validate_runtime(runtime, package)

    comparison_payload: Optional[Dict] = None
    if compare_runtime is not None:
        comparison_payload = compare_runtimes(runtime, compare_runtime)

    inspection_id = _inspection_id(
        str(recommendation["recommendation_id"]),
        str(review["review_id"]),
        str(package["package_id"]),
        str(runtime["runtime_id"]),
        comparison_payload["compared_runtime_id"]
        if comparison_payload else None,
    )

    return {
        "inspection_id":         inspection_id,
        "phase":                 "PAS199",
        "generated_at":          generated_at,
        "allowed_environment":   INSPECTION_ENVIRONMENT_SIMULATION_ONLY,
        "live_behavior_changed": False,
        "lineage_summary":       _lineage_summary(
            recommendation, review, package, runtime,
        ),
        "runtime_summary":       _runtime_summary(runtime),
        "safety_summary":        _safety_summary(runtime),
        "capability_summary":    _capability_summary(runtime),
        "transcript_summary":    _transcript_summary(runtime),
        "artifact_integrity":    _artifact_integrity(
            recommendation, review, package, runtime,
        ),
        "comparison":            comparison_payload,
    }
