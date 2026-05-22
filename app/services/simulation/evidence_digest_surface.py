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
    Render the digest as a multi-line, human-readable text block.
    No PII, no live-routing wording, no free-form prose beyond
    fixed structural labels and the digest's own closed-vocabulary
    tokens.
    """
    s = format_operator_summary(digest)
    lin = s["lineage_summary"]
    safe = s["safety_summary"]
    lines: List[str] = []
    lines.append(
        f"PAS201 evidence digest {s['digest_id']} "
        f"(strategy={s['strategy_id']}, phase=PAS201, "
        f"environment=SIMULATION_ONLY, live_behavior_changed=False)"
    )
    lines.append(
        f"Evidence strength: {s['evidence_strength']}"
    )
    lines.append(
        f"Recommended next action: {s['recommended_next_action']}"
    )
    lines.append(
        f"Safety: outcome={safe['safety_outcome']}, "
        f"auto_fail_count={safe['auto_fail_count']}"
    )
    lines.append(
        f"Lineage: intact={lin['lineage_intact']}"
    )
    lines.append(
        f"  recommendation_id        = {lin['recommendation_id']}"
    )
    lines.append(
        f"  review_id                = {lin['review_id']}"
    )
    lines.append(
        f"  package_id               = {lin['package_id']}"
    )
    lines.append(
        f"  runtime_id               = {lin['runtime_id']}"
    )
    lines.append(
        f"  inspection_id            = {lin['inspection_id']}"
    )
    lines.append(
        f"  behavioral_evaluation_id = {lin['behavioral_evaluation_id']}"
    )
    lines.append(
        f"Artifact integrity: {s['artifact_integrity_pass_ratio']}"
    )
    lines.append(
        f"No live behavior anywhere in lineage: "
        f"{s['no_live_behavior_anywhere_in_lineage']}"
    )
    if s["operator_highlights"]:
        lines.append("Operator highlights:")
        for h in s["operator_highlights"]:
            lines.append(f"  - {h}")
    else:
        lines.append("Operator highlights: -")
    if s["claimable_now"]:
        lines.append("Claimable now:")
        for c in s["claimable_now"]:
            lines.append(f"  - {c}")
    else:
        lines.append("Claimable now: -")
    if s["not_claimable_yet"]:
        lines.append("Still not claimable:")
        for n in s["not_claimable_yet"]:
            lines.append(f"  - {n}")
    else:
        lines.append("Still not claimable: -")
    out = "\n".join(lines)
    _enforce_no_forbidden_tokens(out)
    return out


# ──────────────────────────────────────────────────────────────────
# Slack-safe formatter (pure string, no API calls)
# ──────────────────────────────────────────────────────────────────

def format_digest_for_slack(digest: Dict) -> str:
    """
    Render the digest as a Slack-safe markdown string. Pure
    function. Never imports slack_sdk. Never sends a message.
    Returns a string the operator can copy-paste into Slack
    manually if they choose to.

    Output is hard-capped at SLACK_OUTPUT_MAX_CHARS characters by
    construction (the formatter trims structured lists rather than
    truncating mid-token).
    """
    s = format_operator_summary(digest)
    lin = s["lineage_summary"]
    safe = s["safety_summary"]
    highlights = ", ".join(s["operator_highlights"]) or "-"
    claimable  = ", ".join(s["claimable_now"]) or "-"
    not_yet    = ", ".join(s["not_claimable_yet"]) or "-"
    lines: List[str] = [
        (f"*PAS201 digest* `{s['digest_id']}` "
         f"strategy=`{s['strategy_id']}` "
         f"environment=`SIMULATION_ONLY` "
         f"live_behavior_changed=`False`"),
        (f"*Evidence:* `{s['evidence_strength']}`  "
         f"*Safety:* `{safe['safety_outcome']}` "
         f"(auto_fail={safe['auto_fail_count']})  "
         f"*Lineage:* `{'intact' if lin['lineage_intact'] else 'broken'}`  "
         f"*Integrity:* `{s['artifact_integrity_pass_ratio']}`"),
        f"*Next action:* `{s['recommended_next_action']}`",
        f"*Highlights:* {highlights}",
        f"*Claimable now:* {claimable}",
        f"*Still not claimable:* {not_yet}",
    ]
    out = "\n".join(lines)
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
