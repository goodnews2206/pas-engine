"""
PAS197 — Manual-test package service.

Pure function. Takes a PAS195 recommendation and a PAS196 review
envelope and, if and only if the review approves the
recommendation for manual test, produces a structured manual-test
package for human inspection. The package is for SIMULATION_ONLY
consumption. It cannot route a live call. It cannot select a
runtime strategy. It carries no PII and no free-form text.

Contract for a valid input pair:

  * recommendation["status"]                  == "CANDIDATE"
  * recommendation["operator_required"]       is True
  * recommendation["recommended_strategy"]    is a non-empty str
  * review["new_status"]                      == "APPROVED_FOR_MANUAL_TEST"
  * review["live_behavior_changed"]           is False
  * review["recommendation_id"]               == recommendation["recommendation_id"]

Any contract violation raises ManualTestPackageValidationError.

Output package:

  * package_id (deterministic SHA-256-derived hash)
  * recommendation_id
  * review_id
  * strategy_id
  * status:              "READY_FOR_MANUAL_TEST"
  * live_behavior_changed: False
  * allowed_environment: "SIMULATION_ONLY"
  * test_plan        — closed-vocabulary step tokens
  * success_metrics  — closed-vocabulary metric tokens
  * rollback_notes   — closed-vocabulary rollback tokens
  * safety_notes     — closed-vocabulary safety tokens
  * created_at       — caller-supplied ISO timestamp
  * phase            — "PAS197"
"""

from __future__ import annotations

import hashlib
from typing import Dict, Tuple


# ──────────────────────────────────────────────────────────────────
# Closed vocabularies
# ──────────────────────────────────────────────────────────────────

STATUS_READY_FOR_MANUAL_TEST: str = "READY_FOR_MANUAL_TEST"
ALLOWED_ENVIRONMENT_SIMULATION_ONLY: str = "SIMULATION_ONLY"


REQUIRED_RECOMMENDATION_STATUS: str = "CANDIDATE"
REQUIRED_REVIEW_NEW_STATUS:     str = "APPROVED_FOR_MANUAL_TEST"


PACKAGE_REQUIRED_KEYS: Tuple[str, ...] = (
    "package_id",
    "phase",
    "recommendation_id",
    "review_id",
    "strategy_id",
    "status",
    "live_behavior_changed",
    "allowed_environment",
    "test_plan",
    "success_metrics",
    "rollback_notes",
    "safety_notes",
    "created_at",
)


PACKAGE_TEST_STEPS: Tuple[str, ...] = (
    "review_simulation_evidence",
    "review_strategy_safety_notes",
    "review_failure_modes",
    "rehearse_one_synthetic_lead",
    "verify_no_safety_auto_fail",
    "verify_capability_capture",
    "verify_score_threshold",
    "manual_signoff_required",
)


PACKAGE_SUCCESS_METRICS: Tuple[str, ...] = (
    "no_safety_auto_fail_in_manual_test",
    "qualification_captured_when_relevant",
    "no_pii_leak_in_manual_test",
    "no_unsafe_claim_in_manual_test",
    "strategy_action_plan_matches_recommendation",
    "deterministic_outcome_observed",
)


PACKAGE_ROLLBACK_NOTES: Tuple[str, ...] = (
    "no_runtime_change_to_rollback",
    "discard_package_if_manual_test_fails",
    "do_not_promote_to_runtime_routing",
)


PACKAGE_SAFETY_NOTES: Tuple[str, ...] = (
    "operator_must_review_before_any_future_runtime_use",
    "package_carries_no_runtime_behavior_change",
    "package_carries_no_pii",
    "package_consumes_only_simulation_evidence",
)


# ──────────────────────────────────────────────────────────────────
# Validation
# ──────────────────────────────────────────────────────────────────

class ManualTestPackageValidationError(ValueError):
    """Raised when a (recommendation, review) pair violates the contract."""


def _require_keys(payload: Dict, keys: Tuple[str, ...], label: str) -> None:
    for k in keys:
        if k not in payload:
            raise ManualTestPackageValidationError(
                f"{label} missing required key {k!r}"
            )


def _validate_inputs(recommendation: Dict, review: Dict) -> None:
    _require_keys(
        recommendation,
        ("recommendation_id", "status", "operator_required",
         "recommended_strategy"),
        label="recommendation",
    )
    _require_keys(
        review,
        ("review_id", "recommendation_id", "new_status",
         "live_behavior_changed"),
        label="review",
    )

    if recommendation["status"] != REQUIRED_RECOMMENDATION_STATUS:
        raise ManualTestPackageValidationError(
            f"recommendation.status must be "
            f"{REQUIRED_RECOMMENDATION_STATUS!r}; "
            f"got {recommendation['status']!r}"
        )

    if recommendation["operator_required"] is not True:
        raise ManualTestPackageValidationError(
            "recommendation.operator_required must be True"
        )

    strategy = recommendation.get("recommended_strategy")
    if not isinstance(strategy, str) or not strategy:
        raise ManualTestPackageValidationError(
            f"recommendation.recommended_strategy must be a non-empty "
            f"string; got {strategy!r}"
        )

    if review["new_status"] != REQUIRED_REVIEW_NEW_STATUS:
        raise ManualTestPackageValidationError(
            f"review.new_status must be "
            f"{REQUIRED_REVIEW_NEW_STATUS!r}; "
            f"got {review['new_status']!r}"
        )

    if review["live_behavior_changed"] is not False:
        raise ManualTestPackageValidationError(
            "review.live_behavior_changed must be False"
        )

    if review["recommendation_id"] != recommendation["recommendation_id"]:
        raise ManualTestPackageValidationError(
            f"review.recommendation_id ({review['recommendation_id']!r}) "
            f"must match recommendation.recommendation_id "
            f"({recommendation['recommendation_id']!r})"
        )


def _package_id(
    recommendation_id: str,
    review_id: str,
    strategy_id: str,
    status: str,
    allowed_environment: str,
) -> str:
    h = hashlib.sha256()
    for piece in (
        recommendation_id,
        review_id,
        strategy_id,
        status,
        allowed_environment,
    ):
        h.update(str(piece).encode("utf-8"))
        h.update(b"||")
    return "pas197-pkg-" + h.hexdigest()[:16]


# ──────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────

def build_manual_test_package(
    recommendation: Dict,
    review: Dict,
    *,
    created_at: str,
) -> Dict:
    """
    Validate a (recommendation, review) pair and build the manual-
    test package. Pure function. Same inputs produce the same
    package, including the same package_id, every call.

    The package's `allowed_environment` is fixed at
    SIMULATION_ONLY and `live_behavior_changed` is fixed at False
    by construction — neither can be set by the caller.
    """
    if not isinstance(created_at, str) or not created_at:
        raise ManualTestPackageValidationError(
            "created_at must be a non-empty ISO timestamp string"
        )

    _validate_inputs(recommendation, review)

    recommendation_id = str(recommendation["recommendation_id"])
    review_id         = str(review["review_id"])
    strategy_id       = str(recommendation["recommended_strategy"])

    return {
        "package_id": _package_id(
            recommendation_id,
            review_id,
            strategy_id,
            STATUS_READY_FOR_MANUAL_TEST,
            ALLOWED_ENVIRONMENT_SIMULATION_ONLY,
        ),
        "phase":                  "PAS197",
        "recommendation_id":      recommendation_id,
        "review_id":              review_id,
        "strategy_id":            strategy_id,
        "status":                 STATUS_READY_FOR_MANUAL_TEST,
        "live_behavior_changed":  False,
        "allowed_environment":    ALLOWED_ENVIRONMENT_SIMULATION_ONLY,
        "test_plan":              list(PACKAGE_TEST_STEPS),
        "success_metrics":        list(PACKAGE_SUCCESS_METRICS),
        "rollback_notes":         list(PACKAGE_ROLLBACK_NOTES),
        "safety_notes":           list(PACKAGE_SAFETY_NOTES),
        "created_at":             created_at,
    }
