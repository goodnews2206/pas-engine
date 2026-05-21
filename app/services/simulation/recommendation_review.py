"""
PAS196 — Simulation recommendation review service.

Pure function. Takes a PAS195 CANDIDATE recommendation and an
operator review action, validates the transition against a closed
status machine, and returns a deterministic review envelope.

The service never:

  * mutates production state,
  * applies the recommendation,
  * switches live behaviour,
  * carries raw operator notes or free-form strings.

It only records bounded review metadata: a closed-set reason
token, a shape-validated actor id token, the previous and new
statuses, and a deterministic review_id. Every envelope is
stamped with `operator_required: True` and
`live_behavior_changed: False`.

Allowed transitions:

    CANDIDATE                  -> APPROVED_FOR_MANUAL_TEST
    CANDIDATE                  -> REJECTED
    CANDIDATE                  -> EXPIRED
    APPROVED_FOR_MANUAL_TEST   -> EXPIRED

Forbidden status values (intentionally absent from this module):

    APPROVED, APPLIED, AUTO_APPLIED, LIVE, DEPLOYED
"""

from __future__ import annotations

import hashlib
import re
from typing import Dict, Optional, Tuple


# ──────────────────────────────────────────────────────────────────
# Closed vocabularies
# ──────────────────────────────────────────────────────────────────

STATUS_CANDIDATE                = "CANDIDATE"
STATUS_APPROVED_FOR_MANUAL_TEST = "APPROVED_FOR_MANUAL_TEST"
STATUS_REJECTED                 = "REJECTED"
STATUS_EXPIRED                  = "EXPIRED"


ALLOWED_STATUSES: Tuple[str, ...] = (
    STATUS_CANDIDATE,
    STATUS_APPROVED_FOR_MANUAL_TEST,
    STATUS_REJECTED,
    STATUS_EXPIRED,
)


ALLOWED_TRANSITIONS: Tuple[Tuple[str, str], ...] = (
    (STATUS_CANDIDATE,                STATUS_APPROVED_FOR_MANUAL_TEST),
    (STATUS_CANDIDATE,                STATUS_REJECTED),
    (STATUS_CANDIDATE,                STATUS_EXPIRED),
    (STATUS_APPROVED_FOR_MANUAL_TEST, STATUS_EXPIRED),
)


# CLI / API action vocabulary -> target status.
REVIEW_ACTIONS: Dict[str, str] = {
    "approve-manual-test": STATUS_APPROVED_FOR_MANUAL_TEST,
    "reject":              STATUS_REJECTED,
    "expire":              STATUS_EXPIRED,
}


ACTOR_TYPES: Tuple[str, ...] = (
    "operator",
    "automated_expiry",
)


# Closed reason vocabulary. The CLI and tests refuse any value
# outside this tuple. Reasons are deliberately bounded so the
# review log carries no raw operator notes and no PII.
REASON_TOKENS: Tuple[str, ...] = (
    "operator_approved_for_manual_test",
    "operator_rejected_unsafe",
    "operator_rejected_low_confidence",
    "operator_rejected_metric_threshold",
    "operator_rejected_pending_more_data",
    "candidate_expired_age",
    "candidate_expired_superseded",
    "manual_test_complete_expiring",
)


REVIEW_ENVELOPE_REQUIRED_KEYS: Tuple[str, ...] = (
    "review_id",
    "phase",
    "recommendation_id",
    "previous_status",
    "new_status",
    "actor_type",
    "actor_id_token",
    "reason_token",
    "reviewed_at",
    "operator_required",
    "live_behavior_changed",
)


# Shape regexes for the bounded actor id token. The token must
# carry no PII — no Slack user ids, no email addresses, no real
# names. Operators get an opaque op_ token; automated expiry uses
# the literal auto_expiry token.
_ACTOR_ID_TOKEN_PATTERNS: Dict[str, re.Pattern] = {
    "operator":         re.compile(r"^op_[a-z0-9]{4,32}$"),
    "automated_expiry": re.compile(r"^auto_expiry$"),
}


# ──────────────────────────────────────────────────────────────────
# Validation
# ──────────────────────────────────────────────────────────────────

class ReviewValidationError(ValueError):
    """Raised when a review submission violates the closed contract."""


def is_allowed_transition(previous_status: str, new_status: str) -> bool:
    return (previous_status, new_status) in ALLOWED_TRANSITIONS


def _validate_actor(actor_type: str, actor_id_token: str) -> None:
    if actor_type not in ACTOR_TYPES:
        raise ReviewValidationError(
            f"actor_type must be one of {ACTOR_TYPES}, got {actor_type!r}"
        )
    pat = _ACTOR_ID_TOKEN_PATTERNS[actor_type]
    if not isinstance(actor_id_token, str) or not pat.match(actor_id_token):
        raise ReviewValidationError(
            f"actor_id_token for {actor_type!r} must match {pat.pattern!r}, "
            f"got {actor_id_token!r}"
        )


def _validate_reason(reason_token: str) -> None:
    if reason_token not in REASON_TOKENS:
        raise ReviewValidationError(
            f"reason_token must be one of REASON_TOKENS, got {reason_token!r}"
        )


def _validate_action(action: str) -> str:
    if action not in REVIEW_ACTIONS:
        raise ReviewValidationError(
            f"action must be one of {tuple(REVIEW_ACTIONS.keys())}, "
            f"got {action!r}"
        )
    return REVIEW_ACTIONS[action]


def _validate_reviewed_at(reviewed_at: str) -> None:
    if not isinstance(reviewed_at, str) or not reviewed_at:
        raise ReviewValidationError(
            "reviewed_at must be a non-empty ISO timestamp string"
        )


def _validate_recommendation_shape(recommendation: Dict) -> None:
    for key in ("recommendation_id", "status"):
        if key not in recommendation:
            raise ReviewValidationError(
                f"recommendation missing required key {key!r}"
            )
    if recommendation["status"] not in ALLOWED_STATUSES:
        raise ReviewValidationError(
            f"recommendation has off-catalogue status "
            f"{recommendation['status']!r}; "
            f"only {ALLOWED_STATUSES} are accepted"
        )


def _review_id(
    recommendation_id: str,
    previous_status: str,
    new_status: str,
    actor_type: str,
    actor_id_token: str,
    reason_token: str,
    reviewed_at: str,
) -> str:
    h = hashlib.sha256()
    for piece in (
        recommendation_id,
        previous_status,
        new_status,
        actor_type,
        actor_id_token,
        reason_token,
        reviewed_at,
    ):
        h.update(str(piece).encode("utf-8"))
        h.update(b"||")
    return "pas196-rev-" + h.hexdigest()[:16]


# ──────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────

def submit_review(
    recommendation: Dict,
    action: str,
    *,
    actor_id_token: str,
    reason_token: str,
    reviewed_at: str,
    actor_type: str = "operator",
) -> Dict:
    """
    Validate and record an operator review action against a
    CANDIDATE (or APPROVED_FOR_MANUAL_TEST) recommendation.

    Returns a review envelope dict. The function is pure: same
    inputs produce the same envelope and the same review_id every
    call. It never mutates the input recommendation.

    Raises ReviewValidationError on any contract violation.
    """
    _validate_recommendation_shape(recommendation)
    _validate_actor(actor_type, actor_id_token)
    _validate_reason(reason_token)
    _validate_reviewed_at(reviewed_at)
    target_status = _validate_action(action)

    previous_status = recommendation["status"]
    if not is_allowed_transition(previous_status, target_status):
        raise ReviewValidationError(
            f"transition not allowed: "
            f"{previous_status!r} -> {target_status!r}"
        )

    recommendation_id = str(recommendation["recommendation_id"])
    return {
        "review_id": _review_id(
            recommendation_id,
            previous_status,
            target_status,
            actor_type,
            actor_id_token,
            reason_token,
            reviewed_at,
        ),
        "phase":                 "PAS196",
        "recommendation_id":     recommendation_id,
        "previous_status":       previous_status,
        "new_status":            target_status,
        "actor_type":            actor_type,
        "actor_id_token":        actor_id_token,
        "reason_token":          reason_token,
        "reviewed_at":           reviewed_at,
        "operator_required":     True,
        "live_behavior_changed": False,
    }
