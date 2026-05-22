"""
PAS201 — Simulation evidence digest.

Pure function. Joins six bounded simulation artefacts —

    PAS195 recommendation
    PAS196 review
    PAS197 manual-test package
    PAS198 runtime
    PAS199 inspection
    PAS200 behavioural evaluation

— into a single operator-readable digest with deterministic
evidence-strength scoring. The digest is strictly read-only and
SIMULATION_ONLY. It never imports Twilio, Slack, Supabase, OpenAI,
Anthropic, dotenv, or the live state machine. It never opens a
network connection, never reads .env, never mutates anything. The
CLI is the only writer; it writes exclusively under
reports/simulations/.

Contract (validated at construction time):

  recommendation:
    * recommendation_id        non-empty str
    * status                   == "CANDIDATE"
    * operator_required        is True
    * recommended_strategy     non-empty str

  review:
    * review_id                non-empty str
    * recommendation_id        == recommendation.recommendation_id
    * new_status               == "APPROVED_FOR_MANUAL_TEST"
    * live_behavior_changed    is False

  package:
    * package_id               non-empty str
    * recommendation_id        == recommendation.recommendation_id
    * review_id                == review.review_id
    * strategy_id              == recommendation.recommended_strategy
    * status                   == "READY_FOR_MANUAL_TEST"
    * allowed_environment      == "SIMULATION_ONLY"
    * live_behavior_changed    is False

  runtime:
    * runtime_id               non-empty str
    * package_id               == package.package_id
    * executed_strategy        == package.strategy_id
    * status                   == "EXECUTED"
    * allowed_environment      == "SIMULATION_ONLY"
    * live_behavior_changed    is False

  inspection:
    * inspection_id            non-empty str
    * phase                    == "PAS199"
    * allowed_environment      == "SIMULATION_ONLY"
    * live_behavior_changed    is False
    * lineage_summary.{recommendation_id, review_id, package_id,
                       runtime_id, strategy_id} match the upstream
                       artefacts respectively

  behavioral_evaluation:
    * behavioral_evaluation_id non-empty str
    * phase                    == "PAS200"
    * allowed_environment      == "SIMULATION_ONLY"
    * live_behavior_changed    is False
    * runtime_id               == runtime.runtime_id
    * inspection_id            is None or == inspection.inspection_id

Any contract violation raises EvidenceDigestValidationError.

Output digest (closed schema):

  * digest_id                 — deterministic SHA-256 hash
  * phase                     — "PAS201"
  * generated_at              — caller-supplied ISO timestamp
  * allowed_environment       — fixed to "SIMULATION_ONLY"
  * live_behavior_changed     — fixed to False
  * strategy_id               — copied from package
  * recommendation_summary    — bounded subset of recommendation
  * review_summary            — bounded subset of review
  * package_summary           — bounded subset of package
  * runtime_summary           — bounded subset of runtime
  * inspection_summary        — bounded subset of inspection
  * behavioral_summary        — bounded subset of behavioural eval
  * evidence_strength         — "strong" | "moderate" | "weak" |
                                 "blocked"
  * operator_summary          — closed-vocab highlights +
                                 recommended_next_action
  * claimable_now             — closed-vocab tokens
  * not_claimable_yet         — closed-vocab tokens
  * artifact_integrity        — boolean integrity checks
"""

from __future__ import annotations

import hashlib
from typing import Dict, List, Optional, Tuple


# ──────────────────────────────────────────────────────────────────
# Closed vocabularies
# ──────────────────────────────────────────────────────────────────

DIGEST_ENVIRONMENT_SIMULATION_ONLY: str = "SIMULATION_ONLY"


REQUIRED_RECOMMENDATION_STATUS:      str = "CANDIDATE"
REQUIRED_REVIEW_NEW_STATUS:          str = "APPROVED_FOR_MANUAL_TEST"
REQUIRED_PACKAGE_STATUS:             str = "READY_FOR_MANUAL_TEST"
REQUIRED_PACKAGE_ENVIRONMENT:        str = "SIMULATION_ONLY"
REQUIRED_RUNTIME_STATUS:             str = "EXECUTED"
REQUIRED_RUNTIME_ENVIRONMENT:        str = "SIMULATION_ONLY"
REQUIRED_INSPECTION_PHASE:           str = "PAS199"
REQUIRED_INSPECTION_ENVIRONMENT:     str = "SIMULATION_ONLY"
REQUIRED_BEHAVIORAL_PHASE:           str = "PAS200"
REQUIRED_BEHAVIORAL_ENVIRONMENT:     str = "SIMULATION_ONLY"


EVIDENCE_STRENGTH_VALUES: Tuple[str, ...] = (
    "strong",
    "moderate",
    "weak",
    "blocked",
)


OPERATOR_HIGHLIGHTS: Tuple[str, ...] = (
    "runtime_pass_rate_100_percent",
    "runtime_pass_rate_at_or_above_95_percent",
    "runtime_pass_rate_at_or_above_75_percent",
    "runtime_pass_rate_below_75_percent",
    "safety_outcome_clean",
    "safety_outcome_auto_fail",
    "lineage_intact",
    "lineage_broken",
    "artifact_integrity_complete",
    "artifact_integrity_incomplete",
    "behavioral_low_friction_observed",
    "behavioral_high_friction_observed",
    "behavioral_good_pacing_observed",
    "behavioral_high_pressure_observed",
    "behavioral_low_trust_observed",
    "behavioral_trust_preservation_observed",
    "behavioral_callback_continuity_observed",
    "behavioral_early_escalation_observed",
    "no_live_behavior_change_anywhere_in_lineage",
)


OPERATOR_NEXT_ACTIONS: Tuple[str, ...] = (
    "review_digest_then_decide_pilot_step",
    "expand_synthetic_catalogue_before_pilot",
    "rerun_manual_test_with_alternative_strategy",
    "block_until_safety_issue_resolved",
)


_STRENGTH_TO_NEXT_ACTION: Dict[str, str] = {
    "strong":   "review_digest_then_decide_pilot_step",
    "moderate": "expand_synthetic_catalogue_before_pilot",
    "weak":     "rerun_manual_test_with_alternative_strategy",
    "blocked":  "block_until_safety_issue_resolved",
}


CLAIMABLE_NOW_VOCAB: Tuple[str, ...] = (
    "no_live_behavior_changed",
    "no_pii_in_simulation_artifacts",
    "safety_auto_fails_remain_absolute",
    "operator_approved_strategy_for_manual_test",
    "manual_test_executed_in_simulation_only",
    "lineage_inspectable_end_to_end",
    "behavioral_evaluation_emitted_deterministically",
    "synthetic_rehearsal_passed_for_strategy",
)


NOT_CLAIMABLE_YET_VOCAB: Tuple[str, ...] = (
    "live_call_routing_remains_out_of_scope",
    "calibration_against_live_call_outcomes_pending",
    "automated_promotion_to_runtime_strategy_pending",
    "real_lead_exposure_remains_out_of_scope",
    "slack_operator_surface_for_runtime_runs_pending",
)


DIGEST_REQUIRED_KEYS: Tuple[str, ...] = (
    "digest_id",
    "phase",
    "generated_at",
    "allowed_environment",
    "live_behavior_changed",
    "strategy_id",
    "recommendation_summary",
    "review_summary",
    "package_summary",
    "runtime_summary",
    "inspection_summary",
    "behavioral_summary",
    "evidence_strength",
    "operator_summary",
    "claimable_now",
    "not_claimable_yet",
    "artifact_integrity",
)


RECOMMENDATION_SUMMARY_KEYS: Tuple[str, ...] = (
    "recommendation_id",
    "recommendation_type",
    "recommended_strategy",
    "rejected_strategy",
    "confidence_level",
    "operator_required",
    "pass_rate_threshold",
)


REVIEW_SUMMARY_KEYS: Tuple[str, ...] = (
    "review_id",
    "previous_status",
    "new_status",
    "reason_token",
    "actor_type",
    "live_behavior_changed",
)


PACKAGE_SUMMARY_KEYS: Tuple[str, ...] = (
    "package_id",
    "status",
    "allowed_environment",
    "live_behavior_changed",
    "strategy_id",
)


RUNTIME_SUMMARY_KEYS: Tuple[str, ...] = (
    "runtime_id",
    "executed_strategy",
    "execution_status",
    "scenarios_executed",
    "pass_rate",
    "average_score",
    "safety_outcome",
    "auto_fail_count",
    "live_behavior_changed",
)


INSPECTION_SUMMARY_KEYS: Tuple[str, ...] = (
    "inspection_id",
    "lineage_intact",
    "artifact_integrity_ok",
    "artifact_integrity_pass_ratio",
)


BEHAVIORAL_SUMMARY_KEYS: Tuple[str, ...] = (
    "behavioral_evaluation_id",
    "aggregate_scores",
    "behavioral_flags",
    "annotation_count",
    "artifact_integrity_ok",
)


OPERATOR_SUMMARY_KEYS: Tuple[str, ...] = (
    "evidence_strength",
    "highlights",
    "recommended_next_action",
)


ARTIFACT_INTEGRITY_KEYS: Tuple[str, ...] = (
    "recommendation_status_candidate",
    "review_new_status_approved_for_manual_test",
    "review_live_behavior_changed_false",
    "package_status_ready_for_manual_test",
    "package_allowed_environment_simulation_only",
    "package_live_behavior_changed_false",
    "runtime_status_executed",
    "runtime_allowed_environment_simulation_only",
    "runtime_live_behavior_changed_false",
    "inspection_phase_pas199",
    "inspection_allowed_environment_simulation_only",
    "inspection_live_behavior_changed_false",
    "inspection_lineage_intact",
    "inspection_artifact_integrity_all_true",
    "behavioral_phase_pas200",
    "behavioral_allowed_environment_simulation_only",
    "behavioral_live_behavior_changed_false",
    "behavioral_artifact_integrity_all_true",
    "behavioral_runtime_id_matches_runtime",
    "behavioral_inspection_id_consistent_with_inspection",
    "package_strategy_id_matches_recommendation",
    "runtime_executed_strategy_matches_package",
    "inspection_lineage_summary_matches_upstream",
    "no_live_behavior_change_anywhere_in_lineage",
)


# ──────────────────────────────────────────────────────────────────
# Validation
# ──────────────────────────────────────────────────────────────────

class EvidenceDigestValidationError(ValueError):
    """Raised when the six-artefact set violates the PAS201 contract."""


def _require_keys(payload: Dict, keys: Tuple[str, ...], label: str) -> None:
    if not isinstance(payload, dict):
        raise EvidenceDigestValidationError(
            f"{label} must be a dict"
        )
    for k in keys:
        if k not in payload:
            raise EvidenceDigestValidationError(
                f"{label} missing required key {k!r}"
            )


def _require_non_empty_str(value, label: str) -> None:
    if not isinstance(value, str) or not value:
        raise EvidenceDigestValidationError(
            f"{label} must be a non-empty string"
        )


def _validate_recommendation(rec: Dict) -> None:
    _require_keys(
        rec,
        ("recommendation_id", "status", "operator_required",
         "recommended_strategy"),
        label="recommendation",
    )
    _require_non_empty_str(
        rec["recommendation_id"], "recommendation.recommendation_id",
    )
    if rec["status"] != REQUIRED_RECOMMENDATION_STATUS:
        raise EvidenceDigestValidationError(
            f"recommendation.status must be "
            f"{REQUIRED_RECOMMENDATION_STATUS!r}; "
            f"got {rec['status']!r}"
        )
    if rec["operator_required"] is not True:
        raise EvidenceDigestValidationError(
            "recommendation.operator_required must be True"
        )
    _require_non_empty_str(
        rec["recommended_strategy"], "recommendation.recommended_strategy",
    )


def _validate_review(rev: Dict, rec: Dict) -> None:
    _require_keys(
        rev,
        ("review_id", "recommendation_id", "new_status",
         "live_behavior_changed"),
        label="review",
    )
    _require_non_empty_str(rev["review_id"], "review.review_id")
    if rev["new_status"] != REQUIRED_REVIEW_NEW_STATUS:
        raise EvidenceDigestValidationError(
            f"review.new_status must be {REQUIRED_REVIEW_NEW_STATUS!r}; "
            f"got {rev['new_status']!r}"
        )
    if rev["live_behavior_changed"] is not False:
        raise EvidenceDigestValidationError(
            "review.live_behavior_changed must be False"
        )
    if rev["recommendation_id"] != rec["recommendation_id"]:
        raise EvidenceDigestValidationError(
            f"review.recommendation_id "
            f"({rev['recommendation_id']!r}) must match "
            f"recommendation.recommendation_id "
            f"({rec['recommendation_id']!r})"
        )


def _validate_package(pkg: Dict, rec: Dict, rev: Dict) -> None:
    _require_keys(
        pkg,
        ("package_id", "recommendation_id", "review_id", "strategy_id",
         "status", "allowed_environment", "live_behavior_changed"),
        label="package",
    )
    _require_non_empty_str(pkg["package_id"], "package.package_id")
    if pkg["status"] != REQUIRED_PACKAGE_STATUS:
        raise EvidenceDigestValidationError(
            f"package.status must be {REQUIRED_PACKAGE_STATUS!r}; "
            f"got {pkg['status']!r}"
        )
    if pkg["allowed_environment"] != REQUIRED_PACKAGE_ENVIRONMENT:
        raise EvidenceDigestValidationError(
            f"package.allowed_environment must be "
            f"{REQUIRED_PACKAGE_ENVIRONMENT!r}; "
            f"got {pkg['allowed_environment']!r}"
        )
    if pkg["live_behavior_changed"] is not False:
        raise EvidenceDigestValidationError(
            "package.live_behavior_changed must be False"
        )
    if pkg["recommendation_id"] != rec["recommendation_id"]:
        raise EvidenceDigestValidationError(
            f"package.recommendation_id "
            f"({pkg['recommendation_id']!r}) must match "
            f"recommendation.recommendation_id "
            f"({rec['recommendation_id']!r})"
        )
    if pkg["review_id"] != rev["review_id"]:
        raise EvidenceDigestValidationError(
            f"package.review_id ({pkg['review_id']!r}) must match "
            f"review.review_id ({rev['review_id']!r})"
        )
    if pkg["strategy_id"] != rec["recommended_strategy"]:
        raise EvidenceDigestValidationError(
            f"package.strategy_id ({pkg['strategy_id']!r}) must match "
            f"recommendation.recommended_strategy "
            f"({rec['recommended_strategy']!r})"
        )


def _validate_runtime(rt: Dict, pkg: Dict) -> None:
    _require_keys(
        rt,
        ("runtime_id", "package_id", "executed_strategy", "status",
         "allowed_environment", "live_behavior_changed",
         "executed_scenarios", "runtime_score", "safety_outcome",
         "capability_summary"),
        label="runtime",
    )
    _require_non_empty_str(rt["runtime_id"], "runtime.runtime_id")
    if rt["status"] != REQUIRED_RUNTIME_STATUS:
        raise EvidenceDigestValidationError(
            f"runtime.status must be {REQUIRED_RUNTIME_STATUS!r}; "
            f"got {rt['status']!r}"
        )
    if rt["allowed_environment"] != REQUIRED_RUNTIME_ENVIRONMENT:
        raise EvidenceDigestValidationError(
            f"runtime.allowed_environment must be "
            f"{REQUIRED_RUNTIME_ENVIRONMENT!r}; "
            f"got {rt['allowed_environment']!r}"
        )
    if rt["live_behavior_changed"] is not False:
        raise EvidenceDigestValidationError(
            "runtime.live_behavior_changed must be False"
        )
    if rt["package_id"] != pkg["package_id"]:
        raise EvidenceDigestValidationError(
            f"runtime.package_id ({rt['package_id']!r}) must match "
            f"package.package_id ({pkg['package_id']!r})"
        )
    if rt["executed_strategy"] != pkg["strategy_id"]:
        raise EvidenceDigestValidationError(
            f"runtime.executed_strategy "
            f"({rt['executed_strategy']!r}) must match "
            f"package.strategy_id ({pkg['strategy_id']!r})"
        )


def _validate_inspection(
    insp: Dict, rec: Dict, rev: Dict, pkg: Dict, rt: Dict,
) -> None:
    _require_keys(
        insp,
        ("inspection_id", "phase", "allowed_environment",
         "live_behavior_changed", "lineage_summary",
         "artifact_integrity"),
        label="inspection",
    )
    _require_non_empty_str(insp["inspection_id"], "inspection.inspection_id")
    if insp["phase"] != REQUIRED_INSPECTION_PHASE:
        raise EvidenceDigestValidationError(
            f"inspection.phase must be {REQUIRED_INSPECTION_PHASE!r}; "
            f"got {insp['phase']!r}"
        )
    if insp["allowed_environment"] != REQUIRED_INSPECTION_ENVIRONMENT:
        raise EvidenceDigestValidationError(
            f"inspection.allowed_environment must be "
            f"{REQUIRED_INSPECTION_ENVIRONMENT!r}; "
            f"got {insp['allowed_environment']!r}"
        )
    if insp["live_behavior_changed"] is not False:
        raise EvidenceDigestValidationError(
            "inspection.live_behavior_changed must be False"
        )
    lin = insp["lineage_summary"] or {}
    if lin.get("recommendation_id") != rec["recommendation_id"]:
        raise EvidenceDigestValidationError(
            "inspection.lineage_summary.recommendation_id must "
            "match recommendation.recommendation_id"
        )
    if lin.get("review_id") != rev["review_id"]:
        raise EvidenceDigestValidationError(
            "inspection.lineage_summary.review_id must match "
            "review.review_id"
        )
    if lin.get("package_id") != pkg["package_id"]:
        raise EvidenceDigestValidationError(
            "inspection.lineage_summary.package_id must match "
            "package.package_id"
        )
    if lin.get("runtime_id") != rt["runtime_id"]:
        raise EvidenceDigestValidationError(
            "inspection.lineage_summary.runtime_id must match "
            "runtime.runtime_id"
        )
    if lin.get("strategy_id") != pkg["strategy_id"]:
        raise EvidenceDigestValidationError(
            "inspection.lineage_summary.strategy_id must match "
            "package.strategy_id"
        )


def _validate_behavioral(
    beval: Dict, rt: Dict, insp: Dict,
) -> None:
    _require_keys(
        beval,
        ("behavioral_evaluation_id", "phase", "allowed_environment",
         "live_behavior_changed", "runtime_id", "inspection_id",
         "aggregate_scores", "behavioral_flags", "turn_annotations",
         "artifact_integrity"),
        label="behavioral_evaluation",
    )
    _require_non_empty_str(
        beval["behavioral_evaluation_id"],
        "behavioral_evaluation.behavioral_evaluation_id",
    )
    if beval["phase"] != REQUIRED_BEHAVIORAL_PHASE:
        raise EvidenceDigestValidationError(
            f"behavioral_evaluation.phase must be "
            f"{REQUIRED_BEHAVIORAL_PHASE!r}; "
            f"got {beval['phase']!r}"
        )
    if beval["allowed_environment"] != REQUIRED_BEHAVIORAL_ENVIRONMENT:
        raise EvidenceDigestValidationError(
            f"behavioral_evaluation.allowed_environment must be "
            f"{REQUIRED_BEHAVIORAL_ENVIRONMENT!r}; "
            f"got {beval['allowed_environment']!r}"
        )
    if beval["live_behavior_changed"] is not False:
        raise EvidenceDigestValidationError(
            "behavioral_evaluation.live_behavior_changed must be False"
        )
    if beval["runtime_id"] != rt["runtime_id"]:
        raise EvidenceDigestValidationError(
            f"behavioral_evaluation.runtime_id "
            f"({beval['runtime_id']!r}) must match "
            f"runtime.runtime_id ({rt['runtime_id']!r})"
        )
    b_insp_id = beval.get("inspection_id")
    if b_insp_id is not None and b_insp_id != insp["inspection_id"]:
        raise EvidenceDigestValidationError(
            f"behavioral_evaluation.inspection_id "
            f"({b_insp_id!r}) must be None or match "
            f"inspection.inspection_id ({insp['inspection_id']!r})"
        )


# ──────────────────────────────────────────────────────────────────
# Hash
# ──────────────────────────────────────────────────────────────────

def _digest_id(
    recommendation_id: str,
    review_id: str,
    package_id: str,
    runtime_id: str,
    inspection_id: str,
    behavioral_evaluation_id: str,
) -> str:
    h = hashlib.sha256()
    for piece in (
        recommendation_id,
        review_id,
        package_id,
        runtime_id,
        inspection_id,
        behavioral_evaluation_id,
    ):
        h.update(str(piece).encode("utf-8"))
        h.update(b"||")
    return "pas201-dgst-" + h.hexdigest()[:16]


# ──────────────────────────────────────────────────────────────────
# Summaries
# ──────────────────────────────────────────────────────────────────

def _recommendation_summary(rec: Dict) -> Dict:
    return {
        "recommendation_id":    str(rec["recommendation_id"]),
        "recommendation_type":  str(rec.get("recommendation_type") or ""),
        "recommended_strategy": str(rec["recommended_strategy"]),
        "rejected_strategy":    str(rec.get("rejected_strategy") or "")
                                or None,
        "confidence_level":     str(rec.get("confidence_level") or ""),
        "operator_required":    bool(rec["operator_required"]),
        "pass_rate_threshold":  float(rec.get("pass_rate_threshold") or 0.0),
    }


def _review_summary(rev: Dict) -> Dict:
    return {
        "review_id":             str(rev["review_id"]),
        "previous_status":       str(rev.get("previous_status") or ""),
        "new_status":            str(rev["new_status"]),
        "reason_token":          str(rev.get("reason_token") or ""),
        "actor_type":            str(rev.get("actor_type") or ""),
        "live_behavior_changed": bool(rev["live_behavior_changed"]),
    }


def _package_summary(pkg: Dict) -> Dict:
    return {
        "package_id":            str(pkg["package_id"]),
        "status":                str(pkg["status"]),
        "allowed_environment":   str(pkg["allowed_environment"]),
        "live_behavior_changed": bool(pkg["live_behavior_changed"]),
        "strategy_id":           str(pkg["strategy_id"]),
    }


def _runtime_summary(rt: Dict) -> Dict:
    score  = rt.get("runtime_score")    or {}
    safety = rt.get("safety_outcome")   or {}
    return {
        "runtime_id":            str(rt["runtime_id"]),
        "executed_strategy":     str(rt["executed_strategy"]),
        "execution_status":      str(rt.get("execution_status") or ""),
        "scenarios_executed":    int(len(rt.get("executed_scenarios") or ())),
        "pass_rate":             float(score.get("pass_rate")     or 0.0),
        "average_score":         float(score.get("average_score") or 0.0),
        "safety_outcome":        str(safety.get("outcome") or ""),
        "auto_fail_count":       int(safety.get("auto_fail_count") or 0),
        "live_behavior_changed": bool(rt["live_behavior_changed"]),
    }


def _inspection_summary(insp: Dict) -> Dict:
    lin   = insp.get("lineage_summary")    or {}
    integ = insp.get("artifact_integrity") or {}
    n_ok  = sum(1 for v in integ.values() if v is True)
    n     = len(integ)
    return {
        "inspection_id":                 str(insp["inspection_id"]),
        "lineage_intact":                bool(lin.get("lineage_intact")),
        "artifact_integrity_ok":         (n_ok == n and n > 0),
        "artifact_integrity_pass_ratio": f"{n_ok}/{n}",
    }


def _behavioral_summary(beval: Dict) -> Dict:
    integ = beval.get("artifact_integrity") or {}
    n_ok  = sum(1 for v in integ.values() if v is True)
    n     = len(integ)
    return {
        "behavioral_evaluation_id": str(beval["behavioral_evaluation_id"]),
        "aggregate_scores":         dict(beval.get("aggregate_scores") or {}),
        "behavioral_flags":         list(beval.get("behavioral_flags") or []),
        "annotation_count":         int(len(beval.get("turn_annotations") or ())),
        "artifact_integrity_ok":    (n_ok == n and n > 0),
    }


# ──────────────────────────────────────────────────────────────────
# Evidence strength + operator summary
# ──────────────────────────────────────────────────────────────────

def _all_inspection_integrity_true(insp: Dict) -> bool:
    integ = insp.get("artifact_integrity") or {}
    return bool(integ) and all(v is True for v in integ.values())


def _all_behavioral_integrity_true(beval: Dict) -> bool:
    integ = beval.get("artifact_integrity") or {}
    return bool(integ) and all(v is True for v in integ.values())


def _evidence_strength(
    rt: Dict, insp: Dict, beval: Dict,
    artifact_integrity: Dict[str, bool],
) -> str:
    safety = (rt.get("safety_outcome") or {}).get("outcome") or ""
    safety_clean = (safety == "clean")
    pass_rate = float((rt.get("runtime_score") or {}).get("pass_rate") or 0.0)
    live_changed = bool(rt.get("live_behavior_changed"))
    lin_intact = bool((insp.get("lineage_summary") or {}).get("lineage_intact"))
    insp_integ = _all_inspection_integrity_true(insp)
    beval_integ = _all_behavioral_integrity_true(beval)
    overall_integ_ok = all(artifact_integrity.values())

    if (
        not safety_clean
        or not lin_intact
        or not insp_integ
        or not beval_integ
        or not overall_integ_ok
        or live_changed
    ):
        return "blocked"
    if pass_rate >= 0.95:
        return "strong"
    if pass_rate >= 0.75:
        return "moderate"
    return "weak"


def _operator_highlights(
    rt: Dict, insp: Dict, beval: Dict,
) -> List[str]:
    out: List[str] = []
    pass_rate = float((rt.get("runtime_score") or {}).get("pass_rate") or 0.0)
    safety = (rt.get("safety_outcome") or {}).get("outcome") or ""
    lin_intact = bool((insp.get("lineage_summary") or {}).get("lineage_intact"))
    integ_ok = _all_inspection_integrity_true(insp) and _all_behavioral_integrity_true(beval)

    if pass_rate >= 1.0:
        out.append("runtime_pass_rate_100_percent")
    elif pass_rate >= 0.95:
        out.append("runtime_pass_rate_at_or_above_95_percent")
    elif pass_rate >= 0.75:
        out.append("runtime_pass_rate_at_or_above_75_percent")
    else:
        out.append("runtime_pass_rate_below_75_percent")

    if safety == "clean":
        out.append("safety_outcome_clean")
    else:
        out.append("safety_outcome_auto_fail")

    out.append("lineage_intact" if lin_intact else "lineage_broken")

    out.append(
        "artifact_integrity_complete"
        if integ_ok
        else "artifact_integrity_incomplete"
    )

    flags = set(beval.get("behavioral_flags") or [])
    if "low_friction_observed"     in flags: out.append("behavioral_low_friction_observed")
    if "high_friction_observed"    in flags: out.append("behavioral_high_friction_observed")
    if "good_pacing_observed"      in flags: out.append("behavioral_good_pacing_observed")
    if "high_pressure_strategy"    in flags: out.append("behavioral_high_pressure_observed")
    if "low_trust_strategy"        in flags: out.append("behavioral_low_trust_observed")
    if "trust_preservation_observed" in flags:
        out.append("behavioral_trust_preservation_observed")
    if "callback_continuity_observed" in flags:
        out.append("behavioral_callback_continuity_observed")
    if "early_escalation_observed" in flags:
        out.append("behavioral_early_escalation_observed")

    if (
        not bool(rt.get("live_behavior_changed"))
        and not bool(insp.get("live_behavior_changed"))
        and not bool(beval.get("live_behavior_changed"))
    ):
        out.append("no_live_behavior_change_anywhere_in_lineage")

    return out


def _operator_summary(
    strength: str, highlights: List[str],
) -> Dict:
    return {
        "evidence_strength":       strength,
        "highlights":              highlights,
        "recommended_next_action": _STRENGTH_TO_NEXT_ACTION[strength],
    }


# ──────────────────────────────────────────────────────────────────
# Claimable / not-yet-claimable
# ──────────────────────────────────────────────────────────────────

def _claimable_now(strength: str) -> List[str]:
    base = [
        "no_live_behavior_changed",
        "no_pii_in_simulation_artifacts",
    ]
    if strength != "blocked":
        base.extend([
            "safety_auto_fails_remain_absolute",
            "operator_approved_strategy_for_manual_test",
            "manual_test_executed_in_simulation_only",
            "lineage_inspectable_end_to_end",
            "behavioral_evaluation_emitted_deterministically",
        ])
    if strength == "strong":
        base.append("synthetic_rehearsal_passed_for_strategy")
    return sorted(set(base))


def _not_claimable_yet() -> List[str]:
    # Always the same — these gaps are structural, not condition-
    # dependent. Operators reading the digest must always see them.
    return list(NOT_CLAIMABLE_YET_VOCAB)


# ──────────────────────────────────────────────────────────────────
# Artifact integrity
# ──────────────────────────────────────────────────────────────────

def _artifact_integrity(
    rec: Dict, rev: Dict, pkg: Dict, rt: Dict,
    insp: Dict, beval: Dict,
) -> Dict[str, bool]:
    lin = insp.get("lineage_summary") or {}
    b_insp_id = beval.get("inspection_id")
    return {
        "recommendation_status_candidate": (
            rec.get("status") == REQUIRED_RECOMMENDATION_STATUS
        ),
        "review_new_status_approved_for_manual_test": (
            rev.get("new_status") == REQUIRED_REVIEW_NEW_STATUS
        ),
        "review_live_behavior_changed_false": (
            rev.get("live_behavior_changed") is False
        ),
        "package_status_ready_for_manual_test": (
            pkg.get("status") == REQUIRED_PACKAGE_STATUS
        ),
        "package_allowed_environment_simulation_only": (
            pkg.get("allowed_environment") == REQUIRED_PACKAGE_ENVIRONMENT
        ),
        "package_live_behavior_changed_false": (
            pkg.get("live_behavior_changed") is False
        ),
        "runtime_status_executed": (
            rt.get("status") == REQUIRED_RUNTIME_STATUS
        ),
        "runtime_allowed_environment_simulation_only": (
            rt.get("allowed_environment") == REQUIRED_RUNTIME_ENVIRONMENT
        ),
        "runtime_live_behavior_changed_false": (
            rt.get("live_behavior_changed") is False
        ),
        "inspection_phase_pas199": (
            insp.get("phase") == REQUIRED_INSPECTION_PHASE
        ),
        "inspection_allowed_environment_simulation_only": (
            insp.get("allowed_environment") == REQUIRED_INSPECTION_ENVIRONMENT
        ),
        "inspection_live_behavior_changed_false": (
            insp.get("live_behavior_changed") is False
        ),
        "inspection_lineage_intact": (
            bool(lin.get("lineage_intact"))
        ),
        "inspection_artifact_integrity_all_true": (
            _all_inspection_integrity_true(insp)
        ),
        "behavioral_phase_pas200": (
            beval.get("phase") == REQUIRED_BEHAVIORAL_PHASE
        ),
        "behavioral_allowed_environment_simulation_only": (
            beval.get("allowed_environment") == REQUIRED_BEHAVIORAL_ENVIRONMENT
        ),
        "behavioral_live_behavior_changed_false": (
            beval.get("live_behavior_changed") is False
        ),
        "behavioral_artifact_integrity_all_true": (
            _all_behavioral_integrity_true(beval)
        ),
        "behavioral_runtime_id_matches_runtime": (
            beval.get("runtime_id") == rt.get("runtime_id")
        ),
        "behavioral_inspection_id_consistent_with_inspection": (
            b_insp_id is None or b_insp_id == insp.get("inspection_id")
        ),
        "package_strategy_id_matches_recommendation": (
            pkg.get("strategy_id") == rec.get("recommended_strategy")
        ),
        "runtime_executed_strategy_matches_package": (
            rt.get("executed_strategy") == pkg.get("strategy_id")
        ),
        "inspection_lineage_summary_matches_upstream": (
            lin.get("recommendation_id") == rec.get("recommendation_id")
            and lin.get("review_id")     == rev.get("review_id")
            and lin.get("package_id")    == pkg.get("package_id")
            and lin.get("runtime_id")    == rt.get("runtime_id")
            and lin.get("strategy_id")   == pkg.get("strategy_id")
        ),
        "no_live_behavior_change_anywhere_in_lineage": (
            rev.get("live_behavior_changed") is False
            and pkg.get("live_behavior_changed") is False
            and rt.get("live_behavior_changed") is False
            and insp.get("live_behavior_changed") is False
            and beval.get("live_behavior_changed") is False
        ),
    }


# ──────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────

def build_evidence_digest(
    recommendation: Dict,
    review: Dict,
    package: Dict,
    runtime: Dict,
    inspection: Dict,
    behavioral_evaluation: Dict,
    *,
    generated_at: str,
) -> Dict:
    """
    Validate the six-artefact lineage and build the PAS201
    evidence digest. Pure function. Same inputs produce the same
    digest, including the same digest_id, every call.

    The digest's `allowed_environment` is fixed at SIMULATION_ONLY
    and `live_behavior_changed` is fixed at False by construction —
    neither can be set by the caller.
    """
    _require_non_empty_str(generated_at, "generated_at")

    _validate_recommendation(recommendation)
    _validate_review(review, recommendation)
    _validate_package(package, recommendation, review)
    _validate_runtime(runtime, package)
    _validate_inspection(
        inspection, recommendation, review, package, runtime,
    )
    _validate_behavioral(behavioral_evaluation, runtime, inspection)

    rec_summary    = _recommendation_summary(recommendation)
    rev_summary    = _review_summary(review)
    pkg_summary    = _package_summary(package)
    rt_summary     = _runtime_summary(runtime)
    insp_summary   = _inspection_summary(inspection)
    beval_summary  = _behavioral_summary(behavioral_evaluation)
    integrity      = _artifact_integrity(
        recommendation, review, package, runtime,
        inspection, behavioral_evaluation,
    )
    strength       = _evidence_strength(
        runtime, inspection, behavioral_evaluation, integrity,
    )
    highlights     = _operator_highlights(
        runtime, inspection, behavioral_evaluation,
    )
    op_summary     = _operator_summary(strength, highlights)
    claimable      = _claimable_now(strength)
    not_claimable  = _not_claimable_yet()

    return {
        "digest_id": _digest_id(
            str(recommendation["recommendation_id"]),
            str(review["review_id"]),
            str(package["package_id"]),
            str(runtime["runtime_id"]),
            str(inspection["inspection_id"]),
            str(behavioral_evaluation["behavioral_evaluation_id"]),
        ),
        "phase":                  "PAS201",
        "generated_at":           generated_at,
        "allowed_environment":    DIGEST_ENVIRONMENT_SIMULATION_ONLY,
        "live_behavior_changed":  False,
        "strategy_id":            str(package["strategy_id"]),
        "recommendation_summary": rec_summary,
        "review_summary":         rev_summary,
        "package_summary":        pkg_summary,
        "runtime_summary":        rt_summary,
        "inspection_summary":     insp_summary,
        "behavioral_summary":     beval_summary,
        "evidence_strength":      strength,
        "operator_summary":       op_summary,
        "claimable_now":          claimable,
        "not_claimable_yet":      not_claimable,
        "artifact_integrity":     integrity,
    }
