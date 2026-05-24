"""
PAS207 — Slack read-only proactive needs-attention digest intent.

Surfaces the PAS205 read-only proactive observer through Slack as
a broker-friendly digest. The module is strictly additive over
PAS191/PAS192/PAS193/PAS203/PAS204/PAS205/PAS206 and carries the
same hard safety doctrine as PAS205/PAS206:

  * READ-ONLY. The Slack dispatcher returns a string. There is no
    Slack API write, no Twilio call, no SMS, no email, no DB
    mutation, no scheduler, no worker, no autonomous action.
  * Closed alias vocabulary. The matcher accepts only the bounded
    set of phrases in PROACTIVE_DIGEST_ALIASES. Anything else
    returns None and the dispatcher falls through to PAS191 / LLM.
  * PAS191 carry-forward safety. The PAS207 alias table
    deliberately EXCLUDES PAS191/PAS192 `next action` /
    `priorities` / `next steps` phrases — those continue to route
    to PAS191's INTENT_NEXT_ACTION exactly as today. PAS207 owns
    only the eight phrases listed by the spec.
  * Source-agnostic. The module accepts a callable
    `snapshot_provider` so the dispatcher can wire it to a
    deterministic stub today and to PAS206's Supabase adapter
    later without changing this module.

Public surface:

  * INTENT_NEEDS_ATTENTION              — intent code string
  * PROACTIVE_DIGEST_ALIASES            — closed tuple of phrases
  * match_needs_attention_intent(text)  — pure phrase matcher
  * build_demo_snapshot()               — deterministic, PII-free
                                          seeded snapshot
  * format_needs_attention_response(snapshot)
                                        — render observer digest
                                          into a Slack-safe
                                          broker-friendly string
  * try_route_needs_attention(text, snapshot_provider=None)
                                        — full path: match + run
                                          observer + format, or
                                          None on non-match
"""

from __future__ import annotations

import re
from typing import Callable, Optional, Tuple

from app.services.proactive.observer import observe
from app.services.proactive.observer_digest import to_broker_report
from app.services.proactive.observer_models import (
    ObservedAgent,
    ObservedBooking,
    ObservedCall,
    ObservedCallback,
    ObservedLead,
    ObservedSnapshot,
)


INTENT_NEEDS_ATTENTION = "needs_attention"


# ──────────────────────────────────────────────────────────────────
# Closed alias vocabulary.
#
# These are the eight phrases the PAS207 spec assigns to PAS207. The
# tuple is deliberately frozen here, not parameterised by config or
# locale, to keep the carry-forward surface predictable for the
# readiness gate and the dispatcher tests.
#
# IMPORTANT — PAS191 carry-forward safety:
#
#   PAS191's _ALIAS_TABLE maps several superficially similar phrases
#   ("next action", "priorities", "next steps", "what should i do
#   now", "what should i focus on", "top priorities", ...) to
#   INTENT_NEXT_ACTION. PAS207 must NEVER absorb those. The PAS191
#   carry-forward test (test_pas207_does_not_steal_pas191_next_action)
#   asserts none of those phrases appear in this tuple.
# ──────────────────────────────────────────────────────────────────

PROACTIVE_DIGEST_ALIASES: Tuple[str, ...] = (
    "what needs attention",
    "what should i look at",
    "anything slipping",
    "pipeline risks",
    "show risks",
    "what is at risk",
    "what should i handle next",
    "what needs human review",
)


_ALIAS_SET = frozenset(PROACTIVE_DIGEST_ALIASES)


_PUNCT_RE = re.compile(r"[!?.,;:]+$")
_WHITESPACE_RE = re.compile(r"\s+")


def _normalize(text: str) -> str:
    """Lowercase + collapse whitespace + strip trailing punctuation."""
    if not isinstance(text, str):
        return ""
    t = text.strip().lower()
    t = _PUNCT_RE.sub("", t)
    t = _WHITESPACE_RE.sub(" ", t)
    return t.strip()


def match_needs_attention_intent(text: str) -> bool:
    """Pure phrase matcher. Returns True iff the normalised operator
    text exactly matches a PROACTIVE_DIGEST_ALIASES entry. Closed
    vocabulary — no fuzzy match, no LLM fallback.
    """
    return _normalize(text) in _ALIAS_SET


# ──────────────────────────────────────────────────────────────────
# Deterministic in-memory demo snapshot.
#
# PAS207 returns a digest from a seeded snapshot today. PAS206's
# Supabase adapter exists but is not auto-wired into PAS207 — the
# Slack surface must remain reproducible on a laptop without any
# live database access. A later wiring step (out of PAS207 scope)
# can swap this for the live adapter behind an explicit operator
# acknowledgement.
# ──────────────────────────────────────────────────────────────────

_DEMO_OBSERVED_AT = "2026-05-24T05:00:00Z"


def build_demo_snapshot() -> ObservedSnapshot:
    """Return a bounded, PII-free seeded snapshot covering several
    of the PAS205 signal rules. Deterministic — identical across
    runs.
    """
    return ObservedSnapshot(
        observed_at = _DEMO_OBSERVED_AT,
        leads = (
            ObservedLead(
                lead_ref           = "L-901",
                created_at         = "2026-05-24T00:30:00Z",
                first_response_at  = None,
                last_activity_at   = "2026-05-24T00:30:00Z",
                assigned_agent_ref = None,
                source             = "web",
                value_tier         = "high",
                after_hours        = False,
                needs_human_review = False,
            ),
            ObservedLead(
                lead_ref           = "L-902",
                created_at         = "2026-05-21T09:00:00Z",
                first_response_at  = "2026-05-21T09:10:00Z",
                last_activity_at   = "2026-05-22T09:00:00Z",
                assigned_agent_ref = "A-1",
                source             = "referral",
                value_tier         = "standard",
                after_hours        = False,
                needs_human_review = True,
            ),
        ),
        calls = (
            ObservedCall(
                call_ref      = "C-701",
                lead_ref      = "L-901",
                started_at    = "2026-05-24T01:00:00Z",
                outcome       = "failed",
                attempt_index = 1,
            ),
            ObservedCall(
                call_ref      = "C-702",
                lead_ref      = "L-901",
                started_at    = "2026-05-24T01:10:00Z",
                outcome       = "failed",
                attempt_index = 2,
            ),
            ObservedCall(
                call_ref      = "C-703",
                lead_ref      = "L-901",
                started_at    = "2026-05-24T01:20:00Z",
                outcome       = "failed",
                attempt_index = 3,
            ),
        ),
        bookings = (
            ObservedBooking(
                booking_ref        = "B-501",
                lead_ref           = "L-902",
                proposed_at        = "2026-05-25T15:00:00Z",
                confirmation_state = "failed",
                last_attempt_at    = "2026-05-24T02:00:00Z",
            ),
        ),
        callbacks = (
            ObservedCallback(
                callback_ref = "K-301",
                lead_ref     = "L-901",
                requested_at = "2026-05-24T00:00:00Z",
                scheduled_at = "2026-05-24T00:30:00Z",
                state        = "pending",
            ),
        ),
        agents = (
            ObservedAgent(
                agent_ref    = "A-1",
                available    = False,
                last_seen_at = "2026-05-24T01:00:00Z",
            ),
        ),
    )


# ──────────────────────────────────────────────────────────────────
# Renderer.
# ──────────────────────────────────────────────────────────────────

EMPTY_DIGEST_MESSAGE = (
    "Nothing is currently flagged for attention. The pipeline is "
    "running cleanly right now. I have not taken any action — I "
    "only watch."
)


def format_needs_attention_response(snapshot: ObservedSnapshot) -> str:
    """Run the PAS205 observer over `snapshot` and render a
    broker-friendly Slack response. Pure function — no I/O, no
    Slack API call, no DB read, no mutation.
    """
    digest = observe(snapshot)
    if not digest.signals:
        return EMPTY_DIGEST_MESSAGE
    return to_broker_report(digest)


# ──────────────────────────────────────────────────────────────────
# Dispatcher entry point.
# ──────────────────────────────────────────────────────────────────

SnapshotProvider = Callable[[], ObservedSnapshot]


def try_route_needs_attention(
    text:              str,
    snapshot_provider: Optional[SnapshotProvider] = None,
) -> Optional[str]:
    """Full PAS207 path. Returns a broker-friendly string if `text`
    matches a PAS207 alias, otherwise None — the dispatcher falls
    through to PAS191 / LLM in that case.

    `snapshot_provider` defaults to the deterministic demo snapshot.
    A later phase can inject a Supabase-backed provider without
    changing the matcher or the renderer.
    """
    if not match_needs_attention_intent(text):
        return None

    provider: SnapshotProvider = snapshot_provider or build_demo_snapshot
    snapshot = provider()
    return format_needs_attention_response(snapshot)


__all__ = (
    "INTENT_NEEDS_ATTENTION",
    "PROACTIVE_DIGEST_ALIASES",
    "EMPTY_DIGEST_MESSAGE",
    "match_needs_attention_intent",
    "build_demo_snapshot",
    "format_needs_attention_response",
    "try_route_needs_attention",
)
