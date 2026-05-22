"""
PAS202 — Operator-facing simulation evidence digest surface.

Pure formatting layer on top of PAS201. Consumes a PAS201
evidence digest and produces three bounded read-only renderings:

    format_operator_summary(digest)  -> dict   (structured)
    format_digest_as_text(digest)    -> str    (multi-line text)
    format_digest_for_slack(digest)  -> str    (Slack-safe markdown)

The surface is strictly read-only and SIMULATION_ONLY. It never
imports Twilio, Slack, Supabase, OpenAI, Anthropic, dotenv, or
the live state machine. It never opens a network connection,
never reads .env, never mutates anything, never sends a message.
The Slack formatter returns a *string*; it does not call any
Slack API.

Validation:

  * digest must be a dict
  * digest["phase"]                 == "PAS201"
  * digest["allowed_environment"]   == "SIMULATION_ONLY"
  * digest["live_behavior_changed"] is False
  * required keys present per OPERATOR_SUMMARY_REQUIRED_KEYS

Any contract violation raises EvidenceDigestSurfaceValidationError.
"""

from __future__ import annotations

from typing import Dict, List, Tuple


# ──────────────────────────────────────────────────────────────────
# Closed vocabularies
# ──────────────────────────────────────────────────────────────────

SURFACE_ENVIRONMENT_SIMULATION_ONLY: str = "SIMULATION_ONLY"

REQUIRED_DIGEST_PHASE:       str = "PAS201"
REQUIRED_DIGEST_ENVIRONMENT: str = "SIMULATION_ONLY"


OPERATOR_SUMMARY_REQUIRED_KEYS: Tuple[str, ...] = (
    "digest_id",
    "strategy_id",
    "evidence_strength",
    "recommended_next_action",
    "safety_summary",
    "lineage_summary",
    "operator_highlights",
    "claimable_now",
    "not_claimable_yet",
    "artifact_integrity_pass_ratio",
    "no_live_behavior_anywhere_in_lineage",
)


LINEAGE_SUMMARY_KEYS: Tuple[str, ...] = (
    "recommendation_id",
    "review_id",
    "package_id",
    "runtime_id",
    "inspection_id",
    "behavioral_evaluation_id",
    "lineage_intact",
)


SAFETY_SUMMARY_KEYS: Tuple[str, ...] = (
    "safety_outcome",
    "auto_fail_count",
)


# Tokens this surface refuses to emit at all — they would amount
# to live-routing claims even in a presentation layer.
FORBIDDEN_OUTPUT_TOKENS: Tuple[str, ...] = (
    "live_routing_active",
    "live_call_routed",
    "strategy_deployed_live",
    "real_lead_handled",
    "production_traffic_served",
)


# Hard cap on Slack-formatted output so the formatter cannot
# accidentally exceed a Slack message size. Slack's per-message
# limit is much larger; this is a defensive bound that keeps the
# formatter "concise" by construction.
SLACK_OUTPUT_MAX_CHARS: int = 4000


# ──────────────────────────────────────────────────────────────────
# Broker-voice token translations (PAS204-B polish)
# ──────────────────────────────────────────────────────────────────
#
# Owner-facing renderings (text + Slack) translate the PAS201
# closed-vocab tokens into plain English. The structured
# operator_summary dict still carries the raw tokens so
# machine-readable consumers (audit, pipelines) keep working
# unchanged.

_TOKEN_TRANSLATIONS: Dict[str, str] = {
    # Highlights
    "runtime_pass_rate_100_percent":
        "PAS completed the rehearsal successfully across the test set.",
    "runtime_pass_rate_at_or_above_95_percent":
        "PAS passed almost every rehearsal scenario.",
    "runtime_pass_rate_at_or_above_75_percent":
        "PAS passed most rehearsal scenarios.",
    "runtime_pass_rate_below_75_percent":
        "PAS missed the pass-rate bar — more rehearsal is needed.",
    "safety_outcome_clean":
        "No safety issues were triggered.",
    "safety_outcome_auto_fail":
        "At least one rehearsal scenario triggered a safety auto-fail.",
    "lineage_intact":
        "The evidence trail is complete and traceable.",
    "lineage_broken":
        "The evidence trail has a gap — something is missing in the chain.",
    "artifact_integrity_complete":
        "All evidence checks passed.",
    "artifact_integrity_incomplete":
        "One or more evidence checks failed.",
    "behavioral_low_friction_observed":
        "The conversations stayed smooth and avoided unnecessary pressure.",
    "behavioral_high_friction_observed":
        "Some rehearsals got bumpy — leads pushed back more than expected.",
    "behavioral_good_pacing_observed":
        "PAS paced the conversation well.",
    "behavioral_high_pressure_observed":
        "The strategy leans pushy — too many appointment asks too early.",
    "behavioral_low_trust_observed":
        "Some replies still feel too transactional and need a warmer tone.",
    "behavioral_trust_preservation_observed":
        "PAS acknowledged the lead before any qualification ask.",
    "behavioral_callback_continuity_observed":
        "PAS preserved the lead by moving to callback instead of forcing a booking.",
    "behavioral_early_escalation_observed":
        "PAS jumped to booking too early in some scenarios.",
    "no_live_behavior_change_anywhere_in_lineage":
        "No real lead or live call behavior was changed.",
    # claimable_now
    "no_live_behavior_changed":
        "No live customer behavior was changed.",
    "no_pii_in_simulation_artifacts":
        "No private lead data appears in the simulation artifacts.",
    "safety_auto_fails_remain_absolute":
        "Safety failures are never silently ignored — they always stop the rehearsal.",
    "operator_approved_strategy_for_manual_test":
        "The tested strategy required operator approval before manual testing.",
    "manual_test_executed_in_simulation_only":
        "PAS completed a simulation-only rehearsal.",
    "lineage_inspectable_end_to_end":
        "The evidence trail is inspectable end-to-end.",
    "behavioral_evaluation_emitted_deterministically":
        "Behavioural scoring is repeatable — same rehearsal, same scores.",
    "synthetic_rehearsal_passed_for_strategy":
        "The full rehearsal passed for this strategy.",
    # not_claimable_yet
    "live_call_routing_remains_out_of_scope":
        "This has not been proven on live calls yet.",
    "calibration_against_live_call_outcomes_pending":
        "Live-call outcome calibration is still pending.",
    "automated_promotion_to_runtime_strategy_pending":
        "PAS is not automatically changing real-call strategy.",
    "real_lead_exposure_remains_out_of_scope":
        "Real lead exposure is still out of scope for this evidence.",
    "slack_operator_surface_for_runtime_runs_pending":
        "Triggering rehearsal runs from Slack isn't built yet.",
    # Evidence strength labels (kept short for the header line)
    "strong":   "Strong — every safety check passed and the rehearsal cleared the pass-rate bar.",
    "moderate": "Moderate — rehearsal mostly passed; a few scenarios could use attention.",
    "weak":     "Weak — pass rate is below the bar; another rehearsal is recommended.",
    "blocked":  "Blocked — a safety issue surfaced; the evidence is not safe to claim yet.",
    # Recommended next actions
    "review_digest_then_decide_pilot_step":
        "Review the rehearsal evidence and decide whether to take it to a pilot.",
    "expand_synthetic_catalogue_before_pilot":
        "Expand the synthetic catalogue before taking this to a pilot.",
    "rerun_manual_test_with_alternative_strategy":
        "Re-run the manual test with an alternative strategy.",
    "block_until_safety_issue_resolved":
        "Block until the safety issue is resolved.",
}


def _humanize(token: str) -> str:
    """Translate one PAS internal token into plain English. Returns
    the original token if no translation is registered (defensive —
    a missing translation should NOT silently drop content)."""
    if not isinstance(token, str) or not token:
        return ""
    return _TOKEN_TRANSLATIONS.get(token, token)


# ──────────────────────────────────────────────────────────────────
# Validation
# ──────────────────────────────────────────────────────────────────

class EvidenceDigestSurfaceValidationError(ValueError):
    """Raised when the input digest violates the PAS202 surface contract."""


def _require_keys(payload: Dict, keys: Tuple[str, ...], label: str) -> None:
    if not isinstance(payload, dict):
        raise EvidenceDigestSurfaceValidationError(
            f"{label} must be a dict"
        )
    for k in keys:
        if k not in payload:
            raise EvidenceDigestSurfaceValidationError(
                f"{label} missing required key {k!r}"
            )


def _validate_digest(digest: Dict) -> None:
    _require_keys(
        digest,
        ("digest_id", "phase", "allowed_environment",
         "live_behavior_changed", "strategy_id",
         "evidence_strength", "operator_summary",
         "claimable_now", "not_claimable_yet",
         "recommendation_summary", "review_summary",
         "package_summary", "runtime_summary",
         "inspection_summary", "behavioral_summary",
         "artifact_integrity"),
        label="digest",
    )
    if digest["phase"] != REQUIRED_DIGEST_PHASE:
        raise EvidenceDigestSurfaceValidationError(
            f"digest.phase must be {REQUIRED_DIGEST_PHASE!r}; "
            f"got {digest['phase']!r}"
        )
    if digest["allowed_environment"] != REQUIRED_DIGEST_ENVIRONMENT:
        raise EvidenceDigestSurfaceValidationError(
            f"digest.allowed_environment must be "
            f"{REQUIRED_DIGEST_ENVIRONMENT!r}; "
            f"got {digest['allowed_environment']!r}"
        )
    if digest["live_behavior_changed"] is not False:
        raise EvidenceDigestSurfaceValidationError(
            "digest.live_behavior_changed must be False"
        )


# ──────────────────────────────────────────────────────────────────
# Operator summary
# ──────────────────────────────────────────────────────────────────

def _lineage_summary(digest: Dict) -> Dict:
    rec  = digest.get("recommendation_summary") or {}
    rev  = digest.get("review_summary")         or {}
    pkg  = digest.get("package_summary")        or {}
    rt   = digest.get("runtime_summary")        or {}
    insp = digest.get("inspection_summary")     or {}
    beh  = digest.get("behavioral_summary")     or {}
    return {
        "recommendation_id":        str(rec.get("recommendation_id") or ""),
        "review_id":                str(rev.get("review_id") or ""),
        "package_id":               str(pkg.get("package_id") or ""),
        "runtime_id":               str(rt.get("runtime_id") or ""),
        "inspection_id":            str(insp.get("inspection_id") or ""),
        "behavioral_evaluation_id": str(beh.get("behavioral_evaluation_id") or ""),
        "lineage_intact":           bool(insp.get("lineage_intact")),
    }


def _safety_summary(digest: Dict) -> Dict:
    rt = digest.get("runtime_summary") or {}
    return {
        "safety_outcome":  str(rt.get("safety_outcome") or ""),
        "auto_fail_count": int(rt.get("auto_fail_count") or 0),
    }


def _no_live_behavior_anywhere(digest: Dict) -> bool:
    integ = digest.get("artifact_integrity") or {}
    return bool(integ.get("no_live_behavior_change_anywhere_in_lineage"))


def _artifact_integrity_pass_ratio(digest: Dict) -> str:
    integ = digest.get("artifact_integrity") or {}
    n     = len(integ)
    n_ok  = sum(1 for v in integ.values() if v is True)
    return f"{n_ok}/{n}"


def format_operator_summary(digest: Dict) -> Dict:
    """
    Build the structured operator summary from a PAS201 digest.
    Pure function. Same input -> same output.
    """
    _validate_digest(digest)
    op = digest.get("operator_summary") or {}
    return {
        "digest_id":                            str(digest["digest_id"]),
        "strategy_id":                          str(digest["strategy_id"]),
        "evidence_strength":                    str(digest["evidence_strength"]),
        "recommended_next_action":              str(op.get("recommended_next_action") or ""),
        "safety_summary":                       _safety_summary(digest),
        "lineage_summary":                      _lineage_summary(digest),
        "operator_highlights":                  list(op.get("highlights") or []),
        "claimable_now":                        list(digest.get("claimable_now") or []),
        "not_claimable_yet":                    list(digest.get("not_claimable_yet") or []),
        "artifact_integrity_pass_ratio":        _artifact_integrity_pass_ratio(digest),
        "no_live_behavior_anywhere_in_lineage": _no_live_behavior_anywhere(digest),
    }


# ──────────────────────────────────────────────────────────────────
# Plain-text formatter
# ──────────────────────────────────────────────────────────────────

def format_digest_as_text(digest: Dict) -> str:
    """
    Render the digest as a multi-line, plain-English text block
    suitable for an operator or executive. Internal PAS tokens
    are translated via `_TOKEN_TRANSLATIONS`. The structured
    operator_summary dict still carries the raw tokens for
    machine-readable consumers.

    No PII, no live-routing wording, no internal-jargon leakage.
    The fixed labels "PAS201", "SIMULATION_ONLY", and the
    individual artifact IDs remain present so audit consumers
    can still grep them.
    """
    s = format_operator_summary(digest)
    lin = s["lineage_summary"]
    safe = s["safety_summary"]
    strength = s["evidence_strength"]
    next_action = s["recommended_next_action"]

    lines: List[str] = []
    lines.append(
        f"PAS201 evidence digest {s['digest_id']} (SIMULATION_ONLY)"
    )
    lines.append(
        "This was tested safely in rehearsal — no live behavior was changed."
    )
    lines.append(
        f"Strategy: {s['strategy_id']}  ·  Evidence: {strength}  ·  "
        f"Safety: {safe['safety_outcome']}  ·  Integrity: "
        f"{s['artifact_integrity_pass_ratio']}"
    )
    lines.append(f"Recommended next: {_humanize(next_action)}")
    lines.append("")
    lines.append("Summary:")
    lines.append(f"- {_humanize(strength)}")
    for h in s["operator_highlights"]:
        translated = _humanize(h)
        if translated and translated != h:
            lines.append(f"- {translated}")
    lines.append("")
    if s["claimable_now"]:
        lines.append("What this proves today:")
        for c in s["claimable_now"]:
            lines.append(f"- {_humanize(c)}")
        lines.append("")
    if s["not_claimable_yet"]:
        lines.append("What this does not yet prove:")
        for n in s["not_claimable_yet"]:
            lines.append(f"- {_humanize(n)}")
        lines.append("")
    lines.append("Lineage (for audit):")
    lines.append(f"  recommendation_id        = {lin['recommendation_id']}")
    lines.append(f"  review_id                = {lin['review_id']}")
    lines.append(f"  package_id               = {lin['package_id']}")
    lines.append(f"  runtime_id               = {lin['runtime_id']}")
    lines.append(f"  inspection_id            = {lin['inspection_id']}")
    lines.append(f"  behavioral_evaluation_id = {lin['behavioral_evaluation_id']}")
    out = "\n".join(lines).rstrip()
    _enforce_no_forbidden_tokens(out)
    return out


# ──────────────────────────────────────────────────────────────────
# Slack-safe formatter (pure string, no API calls)
# ──────────────────────────────────────────────────────────────────

def format_digest_for_slack(digest: Dict) -> str:
    """
    Render the digest as a Slack-safe markdown string in plain
    English. Pure function. Never imports slack_sdk, never sends
    a message. Returns a string the operator can copy-paste into
    Slack manually if they choose to.

    Internal PAS tokens (lineage_intact, behavioral_*,
    runtime_pass_rate_*, etc.) are translated via
    `_TOKEN_TRANSLATIONS` so no underscore-snake-case jargon
    appears in the rendered output. The structured
    operator_summary dict still carries the raw tokens for
    machine-readable consumers.

    Output is hard-capped at SLACK_OUTPUT_MAX_CHARS characters
    by construction.
    """
    s = format_operator_summary(digest)
    safe = s["safety_summary"]
    strength = s["evidence_strength"]
    next_action = s["recommended_next_action"]

    lines: List[str] = [
        (
            f"*PAS rehearsal evidence* `{s['digest_id']}` (SIMULATION_ONLY)\n"
            f"This was tested safely in rehearsal — "
            f"no live behavior was changed.\n"
            f"Strategy: `{s['strategy_id']}` · "
            f"Evidence: `{strength}` · "
            f"Safety: `{safe['safety_outcome']}` · "
            f"Integrity: `{s['artifact_integrity_pass_ratio']}`"
        ),
        f"*Recommended next:* {_humanize(next_action)}",
    ]

    # Summary: strength + highlights, all humanized.
    summary_bullets: List[str] = []
    summary_bullets.append(f"• {_humanize(strength)}")
    for h in s["operator_highlights"]:
        translated = _humanize(h)
        if translated and translated != h:
            summary_bullets.append(f"• {translated}")
    if summary_bullets:
        lines.append("*Summary:*\n" + "\n".join(summary_bullets))

    if s["claimable_now"]:
        bullets = [f"• {_humanize(c)}" for c in s["claimable_now"]]
        lines.append("*What this proves today:*\n" + "\n".join(bullets))

    if s["not_claimable_yet"]:
        bullets = [f"• {_humanize(n)}" for n in s["not_claimable_yet"]]
        lines.append(
            "*What this does not yet prove:*\n" + "\n".join(bullets)
        )

    out = "\n\n".join(lines)
    if len(out) > SLACK_OUTPUT_MAX_CHARS:
        out = out[:SLACK_OUTPUT_MAX_CHARS]
    _enforce_no_forbidden_tokens(out)
    return out


# ──────────────────────────────────────────────────────────────────
# Defensive: never emit forbidden live-routing wording
# ──────────────────────────────────────────────────────────────────

def _enforce_no_forbidden_tokens(out: str) -> None:
    lower = out.lower()
    for tok in FORBIDDEN_OUTPUT_TOKENS:
        if tok in lower:
            raise EvidenceDigestSurfaceValidationError(
                f"formatter would emit forbidden token {tok!r}"
            )
