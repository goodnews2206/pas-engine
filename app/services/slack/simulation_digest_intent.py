"""
PAS203 — Slack read-only evidence digest intent.

Self-contained operator intent that lets a brokerage operator
view the latest PAS201 simulation evidence digest summary from
inside Slack, without triggering any live behaviour and without
sending any outbound Slack message.

The module is strictly additive over PAS191/PAS192/PAS202:

  * It does NOT modify PAS191's INTENT_CODES tuple or
    _ALIAS_TABLE — PAS191 / PAS192 carry-forward tests assert
    INTENT_CODES has exactly 15 entries and would break if a
    16th intent were appended there.
  * It does NOT modify PAS191's format_help — the help-line
    additions live as a closed tuple here
    (SIMULATION_DIGEST_HELP_LINES) for the dispatcher (or any
    operator-facing surface) to concatenate.
  * It does NOT import slack_sdk, twilio, supabase, openai,
    anthropic, or dotenv. The module is pure Python plus
    standard library file I/O, and it consumes PAS202's
    `format_digest_for_slack` for the rendered output.
  * It does NOT execute a simulation, generate a digest, or
    write any artefact. The Slack path is exclusively a read of
    `reports/simulations/` plus a string format.
  * It does NOT post a Slack message. It returns a string the
    dispatcher may render however it wishes (the Slack
    integration in PAS191 already converts strings into Slack
    responses through the existing pipeline).

Public surface:

  * INTENT_SIMULATION_DIGEST                — intent code string
  * SIMULATION_DIGEST_ALIASES               — closed tuple of
                                              recognised operator
                                              phrases
  * SIMULATION_DIGEST_HELP_LINES            — closed tuple of
                                              help-line additions
  * MISSING_DIGEST_FALLBACK_MESSAGE         — bounded fallback
                                              text used when no
                                              digest is on disk
  * REPORTS_SUBDIR                          — relative path the
                                              loader walks
  * DIGEST_FILENAME_PREFIX                  — filename prefix the
                                              loader matches
  * match_simulation_digest_intent(text)    — pure phrase matcher
  * find_latest_digest_path(reports_dir)    — deterministic file
                                              selection by sorted
                                              filename
  * load_digest(path)                       — read + structural
                                              validation
  * format_simulation_digest_response(...)  — bounded Slack-safe
                                              response builder
                                              (delegates rendering
                                              to PAS202)
  * try_route_simulation_digest(text, dir)  — full path: match +
                                              load + format, or
                                              None if no match

Integration with the existing slack_command.py dispatcher is a
small, deliberate, additive edit documented in
`docs/pas203_slack_evidence_digest_command.md`. This module ships
the building blocks; wiring is a follow-up step that fits in
roughly two lines of dispatcher code.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# Defer import to keep this module loadable even if the
# evidence_digest_surface module is moved or renamed in a future
# phase; the dispatcher should still load this module cleanly.
from app.services.simulation.evidence_digest_surface import (
    EvidenceDigestSurfaceValidationError,
    format_digest_for_slack,
)


# ──────────────────────────────────────────────────────────────────
# Closed vocabularies
# ──────────────────────────────────────────────────────────────────

INTENT_SIMULATION_DIGEST: str = "simulation_digest"


# Hand-curated, hand-audited operator phrases. The dispatcher
# normalises operator text the same way PAS191 does (lower-case +
# strip + trailing punctuation strip) and looks the result up
# here. Adding a new phrase is a deliberate code change.
SIMULATION_DIGEST_ALIASES: Tuple[str, ...] = (
    # Spec-required phrases.
    "simulation digest",
    "evidence digest",
    "show simulation evidence",
    "what did the simulation prove",
    "rehearsal evidence",
    "strategy evidence",
    # Natural variants operators are likely to type.
    "show simulation digest",
    "show evidence digest",
    "show me the simulation digest",
    "show me the evidence digest",
    "show the digest",
    "simulation evidence",
    "simulation evidence summary",
    "evidence summary",
    "pas201 digest",
    "latest simulation digest",
    "latest evidence digest",
    "what did the simulation show",
    "what does the simulation prove",
    "what does the rehearsal show",
)


# Help-line additions for any operator-facing help renderer. We do
# NOT modify PAS191's format_help() — the dispatcher concatenates
# these lines after PAS191's help block at integration time.
SIMULATION_DIGEST_HELP_LINES: Tuple[str, ...] = (
    "• _simulation digest_ — show the latest PAS201 simulation evidence summary",
    "• _what did the simulation prove?_ — show the latest PAS201 simulation evidence summary",
)


# Bounded fallback message when no PAS201 digest is on disk. The
# wording carries no PII, no live-routing claim, and no free-form
# operator instruction beyond pointing at the PAS201 CLI.
MISSING_DIGEST_FALLBACK_MESSAGE: str = (
    "ℹ️ *No simulation evidence digest found yet.* "
    "Run the PAS201 digest generator first: "
    "`python scripts/pas201_build_simulation_evidence_digest.py "
    "--recommendation <path> --review <path> --package <path> "
    "--runtime <path> --inspection <path> --behavioral-evaluation <path>`."
)


# Where the loader looks for digests on disk. Resolved by callers
# relative to the repository root. Defined here as a constant so
# the readiness gate can assert the module does not write into
# any other directory.
REPORTS_SUBDIR: str = "reports/simulations"


# Filename prefix that identifies a PAS201 digest artefact. The
# loader refuses any other filename shape.
DIGEST_FILENAME_PREFIX: str = "pas201_simulation_evidence_digest_"
DIGEST_FILENAME_SUFFIX: str = ".json"


# Tokens this module refuses to emit at any layer — defensive
# parallel to PAS202's FORBIDDEN_OUTPUT_TOKENS, replicated here so
# the Slack response cannot accidentally claim live activity even
# if a future change accidentally bypasses PAS202.
FORBIDDEN_OUTPUT_TOKENS: Tuple[str, ...] = (
    "live_routing_active",
    "live_call_routed",
    "strategy_deployed_live",
    "real_lead_handled",
    "production_traffic_served",
)


# ──────────────────────────────────────────────────────────────────
# Normalisation (mirrors PAS191's logic without importing it)
# ──────────────────────────────────────────────────────────────────

def _normalize(text: str) -> str:
    if not isinstance(text, str):
        return ""
    t = text.strip().lower()
    if not t:
        return ""
    t = " ".join(t.split())
    for _ in range(3):
        if t and t[-1] in "?.!,":
            t = t[:-1].rstrip()
        else:
            break
    return t


_ALIAS_SET = frozenset(SIMULATION_DIGEST_ALIASES)


# ──────────────────────────────────────────────────────────────────
# Public surface
# ──────────────────────────────────────────────────────────────────

def match_simulation_digest_intent(text: str) -> bool:
    """
    Pure phrase matcher. Returns True iff the normalised operator
    text exactly matches a SIMULATION_DIGEST_ALIASES entry.
    Anything else (including the empty string) returns False.

    The matcher is closed-vocabulary and never falls through to an
    LLM or fuzzy match.
    """
    return _normalize(text) in _ALIAS_SET


# Pre-compiled filename regex for safe sorting. We accept only the
# strict pattern PAS201's CLI emits.
_DIGEST_FILENAME_RE: "re.Pattern[str]" = re.compile(
    r"^pas201_simulation_evidence_digest_"
    r"[0-9TZ]{8,32}_"               # timestamp segment
    r"pas201-dgst-[0-9a-f]{8,32}"   # digest_id
    r"\.json$"
)


def find_latest_digest_path(reports_dir: Path) -> Optional[Path]:
    """
    Deterministic newest-first selection of a PAS201 digest file
    under `reports_dir`. Selection key is the filename itself
    (PAS201 filenames embed a sortable UTC timestamp), so identical
    filesystem state yields identical selection across processes.

    Returns None if `reports_dir` is missing or contains no
    matching file. Never raises on filesystem absence.
    """
    p = Path(reports_dir)
    if not p.is_dir():
        return None
    candidates: List[Path] = []
    for entry in p.iterdir():
        if not entry.is_file():
            continue
        name = entry.name
        if not name.startswith(DIGEST_FILENAME_PREFIX):
            continue
        if not name.endswith(DIGEST_FILENAME_SUFFIX):
            continue
        if not _DIGEST_FILENAME_RE.match(name):
            continue
        candidates.append(entry)
    if not candidates:
        return None
    candidates.sort(key=lambda x: x.name, reverse=True)
    return candidates[0]


def load_digest(path: Path) -> Dict:
    """
    Read a PAS201 digest JSON from disk and validate its top-level
    contract: phase must be "PAS201", allowed_environment must be
    "SIMULATION_ONLY", live_behavior_changed must be False. Raises
    ValueError on any contract violation. Never raises FileNotFoundError
    or json.JSONDecodeError into the caller — re-raises both as
    ValueError so the Slack dispatcher has a single exception type
    to handle.
    """
    try:
        raw = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError as e:
        raise ValueError(f"digest file not found: {path}") from e
    except OSError as e:
        raise ValueError(f"cannot read digest file: {type(e).__name__}") from e
    try:
        digest = json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError("digest file is not valid JSON") from e
    if not isinstance(digest, dict):
        raise ValueError("digest must be a JSON object")
    if digest.get("phase") != "PAS201":
        raise ValueError(
            f"digest.phase must be 'PAS201'; got {digest.get('phase')!r}"
        )
    if digest.get("allowed_environment") != "SIMULATION_ONLY":
        raise ValueError(
            f"digest.allowed_environment must be 'SIMULATION_ONLY'; "
            f"got {digest.get('allowed_environment')!r}"
        )
    if digest.get("live_behavior_changed") is not False:
        raise ValueError("digest.live_behavior_changed must be False")
    return digest


def _enforce_no_forbidden_tokens(out: str) -> None:
    lower = out.lower()
    for tok in FORBIDDEN_OUTPUT_TOKENS:
        if tok in lower:
            raise ValueError(
                f"slack response would emit forbidden token {tok!r}"
            )


def format_simulation_digest_response(digest: Optional[Dict]) -> str:
    """
    Build the Slack-safe response string for the
    simulation_digest intent. If `digest` is None (no digest on
    disk), returns the bounded MISSING_DIGEST_FALLBACK_MESSAGE.
    Otherwise delegates rendering to PAS202's
    `format_digest_for_slack`, then defensively scans the output
    for any forbidden live-routing token.
    """
    if digest is None:
        out = MISSING_DIGEST_FALLBACK_MESSAGE
    else:
        try:
            out = format_digest_for_slack(digest)
        except EvidenceDigestSurfaceValidationError as e:
            raise ValueError(f"digest is not a valid PAS201 digest: {e}") from e
    _enforce_no_forbidden_tokens(out)
    return out


def try_route_simulation_digest(
    text: str,
    reports_dir: Path,
) -> Optional[str]:
    """
    Full Slack fast-path: match phrase, load latest digest, format
    response. Returns a Slack-ready response string if the phrase
    matched, or None if the phrase is not a simulation_digest
    alias — in which case the dispatcher should fall through to
    PAS191's match_intent() unchanged.

    This function never writes to disk, never calls any network
    service, and never imports slack_sdk. It is purely a read +
    format operation.
    """
    if not match_simulation_digest_intent(text):
        return None
    digest_path = find_latest_digest_path(reports_dir)
    if digest_path is None:
        return format_simulation_digest_response(None)
    try:
        digest = load_digest(digest_path)
    except ValueError:
        # Treat any contract violation on disk as "no usable
        # digest" — surface the same bounded fallback rather than
        # leaking the underlying exception text into Slack.
        return format_simulation_digest_response(None)
    return format_simulation_digest_response(digest)


def alias_count() -> int:
    """Number of recognised aliases (used by the readiness gate)."""
    return len(SIMULATION_DIGEST_ALIASES)


def list_aliases() -> Tuple[str, ...]:
    """Return the closed alias tuple."""
    return SIMULATION_DIGEST_ALIASES
