"""
PAS191 — Bounded Slack Natural-Language Operator Intents.

A deterministic, read-only string-matching layer that maps a small
set of natural-English operator phrases to a fixed, closed set of
intent codes. NO LLM. NO autonomous decisioning. NO eval/exec.
NO SQL construction from user input.

Doctrine:

  * Closed intent set. Every recognised phrase resolves to one of
    the 12 intent codes in INTENT_CODES. Anything else resolves to
    INTENT_UNKNOWN. There is no fallback to an LLM and no
    free-form execution path.

  * Pure-function matcher. match_intent() reads the raw operator
    text, lower-cases it, and walks an alias table. No I/O, no
    randomness, no global state mutation. Same input → same
    output forever.

  * Mutation commands are NOT mapped here. pause / resume / push /
    remove must continue to be handled by the existing
    exact-command branch in app/routes/slack_command.py. PAS191
    is read-only by construction — any caller that passes pause
    or resume to match_intent() will get INTENT_UNKNOWN.

  * Alias table is intentionally small and hand-curated. We do
    NOT regex-explode operator language; the surface is a fleet
    of about twelve human questions a brokerage manager actually
    asks. Adding a new intent is a deliberate code change with a
    closed payload allow-list.

  * No PII or secrets ever touch this module. Inputs are
    operator-typed Slack command text; outputs are a closed
    {intent, normalized_phrase} envelope. There is no carry-through
    of the raw operator text into logs.

References:

  * app/routes/slack_command.py — wires the deterministic mapper
    as a fast-path BEFORE the existing LLM intent parser. LLM
    only fires when match_intent() returns INTENT_UNKNOWN AND the
    text is not an exact mutation command.

  * app/services/slack/operator_responses.py — companion module
    that turns an intent code + DB result into a safe Slack
    message string. Never echoes PII.
"""

from __future__ import annotations

from typing import Dict, Tuple


# ──────────────────────────────────────────────────────────────────
# Closed intent set — 12 read-only intents.
# ──────────────────────────────────────────────────────────────────

INTENT_STATS           = "stats"
INTENT_CALLS_TODAY     = "calls_today"
INTENT_CALLS_WEEK      = "calls_week"
INTENT_RESPONSE_RATE   = "response_rate"
INTENT_BOOKINGS_TODAY  = "bookings_today"
INTENT_CALLBACKS_DUE   = "callbacks_due"
INTENT_QUEUE           = "queue"
INTENT_INCIDENTS       = "incidents"
INTENT_POLICY          = "policy"
INTENT_HEALTH          = "health"
INTENT_PAUSED_STATUS   = "paused_status"
INTENT_HELP            = "help"
INTENT_LEADS_TODAY     = "leads_today"
# PAS192 — operator experience layer
INTENT_TODAY_SUMMARY   = "today_summary"
INTENT_NEXT_ACTION     = "next_action"

INTENT_UNKNOWN         = "unknown"


INTENT_CODES: Tuple[str, ...] = (
    INTENT_STATS,
    INTENT_CALLS_TODAY,
    INTENT_CALLS_WEEK,
    INTENT_RESPONSE_RATE,
    INTENT_BOOKINGS_TODAY,
    INTENT_CALLBACKS_DUE,
    INTENT_QUEUE,
    INTENT_INCIDENTS,
    INTENT_POLICY,
    INTENT_HEALTH,
    INTENT_PAUSED_STATUS,
    INTENT_HELP,
    INTENT_LEADS_TODAY,
    INTENT_TODAY_SUMMARY,
    INTENT_NEXT_ACTION,
)


# ──────────────────────────────────────────────────────────────────
# Mutation commands — explicitly NOT handled here.
# ──────────────────────────────────────────────────────────────────
# These remain on the exact-command path in slack_command.py.
# match_intent() will refuse to bind them: it returns
# INTENT_UNKNOWN so the caller falls through to the existing
# exact-command branch. The list exists so the readiness check
# can assert that pause / resume / push / remove never appear as
# alias keys in ALIAS_TABLE.

MUTATION_COMMAND_TOKENS: Tuple[str, ...] = (
    "pause",
    "resume",
    "push",
    "remove",
)


# ──────────────────────────────────────────────────────────────────
# Alias table.
# ──────────────────────────────────────────────────────────────────
# Hand-curated, hand-audited. Keys are LOWER-CASED, stripped, and
# collapsed-whitespace. Values are intent codes from INTENT_CODES.
#
# Naming convention: phrase-level keys. We deliberately avoid
# regex / NLP / stemming. If an operator phrases a question in a
# way that isn't in this table they receive the help intent.

_ALIAS_TABLE: Dict[str, str] = {
    # ── stats (all-time) ──────────────────────────────────────
    "stats":                                   INTENT_STATS,
    "show stats":                              INTENT_STATS,
    "show me stats":                           INTENT_STATS,
    "all time stats":                          INTENT_STATS,
    "all-time stats":                          INTENT_STATS,
    "overall stats":                           INTENT_STATS,
    "how are we doing overall":                INTENT_STATS,
    "lifetime stats":                          INTENT_STATS,

    # ── today_summary (PAS192) ────────────────────────────────
    # Operational daily wrap. Combines today's leads + calls +
    # bookings + response rate + warnings into a single Slack
    # response. Read-only — same closed-formatter discipline as
    # every other PAS191 intent.
    "summary":                                 INTENT_TODAY_SUMMARY,
    "give me a summary":                       INTENT_TODAY_SUMMARY,
    "today":                                   INTENT_TODAY_SUMMARY,
    "today summary":                           INTENT_TODAY_SUMMARY,
    "todays summary":                          INTENT_TODAY_SUMMARY,
    "today's summary":                         INTENT_TODAY_SUMMARY,
    "daily summary":                           INTENT_TODAY_SUMMARY,
    "what happened today":                     INTENT_TODAY_SUMMARY,
    "show today":                              INTENT_TODAY_SUMMARY,
    "show me today":                           INTENT_TODAY_SUMMARY,
    "show today's summary":                    INTENT_TODAY_SUMMARY,
    "show todays summary":                     INTENT_TODAY_SUMMARY,
    "operator summary":                        INTENT_TODAY_SUMMARY,
    "ops summary":                             INTENT_TODAY_SUMMARY,
    "how are we doing today":                  INTENT_TODAY_SUMMARY,
    "how are we doing":                        INTENT_TODAY_SUMMARY,

    # ── next_action (PAS192) ──────────────────────────────────
    # Ranks up to three operational priorities. Read-only: PAS
    # never executes the suggested action, only describes it.
    "what should i do now":                    INTENT_NEXT_ACTION,
    "what should i do":                        INTENT_NEXT_ACTION,
    "what do i do now":                        INTENT_NEXT_ACTION,
    "next action":                             INTENT_NEXT_ACTION,
    "next actions":                            INTENT_NEXT_ACTION,
    "next steps":                              INTENT_NEXT_ACTION,
    "priorities":                              INTENT_NEXT_ACTION,
    "top priorities":                          INTENT_NEXT_ACTION,
    "what needs attention":                    INTENT_NEXT_ACTION,
    "what needs my attention":                 INTENT_NEXT_ACTION,
    "what should i focus on":                  INTENT_NEXT_ACTION,
    "what's important":                        INTENT_NEXT_ACTION,
    "whats important":                         INTENT_NEXT_ACTION,
    "show priorities":                         INTENT_NEXT_ACTION,
    "what's the priority":                     INTENT_NEXT_ACTION,
    "whats the priority":                      INTENT_NEXT_ACTION,
    "what is the priority":                    INTENT_NEXT_ACTION,

    # ── calls today ───────────────────────────────────────────
    "calls today":                             INTENT_CALLS_TODAY,
    "calls so far today":                      INTENT_CALLS_TODAY,
    "today's calls":                           INTENT_CALLS_TODAY,
    "todays calls":                            INTENT_CALLS_TODAY,
    "how many calls today":                    INTENT_CALLS_TODAY,
    "how many calls did we make today":        INTENT_CALLS_TODAY,
    "how many calls have we had today":        INTENT_CALLS_TODAY,
    "calls made today":                        INTENT_CALLS_TODAY,
    "what's our call volume today":            INTENT_CALLS_TODAY,
    "whats our call volume today":             INTENT_CALLS_TODAY,

    # ── calls this week ───────────────────────────────────────
    "calls this week":                         INTENT_CALLS_WEEK,
    "calls week":                              INTENT_CALLS_WEEK,
    "this week's calls":                       INTENT_CALLS_WEEK,
    "this weeks calls":                        INTENT_CALLS_WEEK,
    "how many calls this week":                INTENT_CALLS_WEEK,
    "weekly calls":                            INTENT_CALLS_WEEK,
    "calls in the last 7 days":                INTENT_CALLS_WEEK,
    "calls last 7 days":                       INTENT_CALLS_WEEK,

    # ── response rate ─────────────────────────────────────────
    "response rate":                           INTENT_RESPONSE_RATE,
    "what's our response rate":                INTENT_RESPONSE_RATE,
    "whats our response rate":                 INTENT_RESPONSE_RATE,
    "what is our response rate":               INTENT_RESPONSE_RATE,
    "show response rate":                      INTENT_RESPONSE_RATE,
    "answer rate":                             INTENT_RESPONSE_RATE,
    "pickup rate":                             INTENT_RESPONSE_RATE,
    "connection rate":                         INTENT_RESPONSE_RATE,

    # ── bookings today ────────────────────────────────────────
    "bookings today":                          INTENT_BOOKINGS_TODAY,
    "did we book any clients":                 INTENT_BOOKINGS_TODAY,
    "did we book any clients today":           INTENT_BOOKINGS_TODAY,
    "did we book any clients for showing":     INTENT_BOOKINGS_TODAY,
    "did we book anyone today":                INTENT_BOOKINGS_TODAY,
    "any bookings today":                      INTENT_BOOKINGS_TODAY,
    "showings booked today":                   INTENT_BOOKINGS_TODAY,
    "showings today":                          INTENT_BOOKINGS_TODAY,
    "how many bookings today":                 INTENT_BOOKINGS_TODAY,

    # ── callbacks due ─────────────────────────────────────────
    "callbacks":                               INTENT_CALLBACKS_DUE,
    "callbacks due":                           INTENT_CALLBACKS_DUE,
    "callbacks owed":                          INTENT_CALLBACKS_DUE,
    "what callbacks do we owe":                INTENT_CALLBACKS_DUE,
    "what callbacks are due":                  INTENT_CALLBACKS_DUE,
    "who do we owe callbacks":                 INTENT_CALLBACKS_DUE,
    "pending callbacks":                       INTENT_CALLBACKS_DUE,

    # ── queue ─────────────────────────────────────────────────
    "queue":                                   INTENT_QUEUE,
    "show queue":                              INTENT_QUEUE,
    "queue size":                              INTENT_QUEUE,
    "how many calls in queue":                 INTENT_QUEUE,
    "how many in queue":                       INTENT_QUEUE,
    "pending calls":                           INTENT_QUEUE,
    "how many pending calls":                  INTENT_QUEUE,
    "queue depth":                             INTENT_QUEUE,

    # ── incidents ─────────────────────────────────────────────
    "incidents":                               INTENT_INCIDENTS,
    "open incidents":                          INTENT_INCIDENTS,
    "any incidents":                           INTENT_INCIDENTS,
    "any open incidents":                      INTENT_INCIDENTS,
    "what incidents are open":                 INTENT_INCIDENTS,
    "show incidents":                          INTENT_INCIDENTS,
    "incident status":                         INTENT_INCIDENTS,

    # ── policy ────────────────────────────────────────────────
    "policy":                                  INTENT_POLICY,
    "policy report":                           INTENT_POLICY,
    "policy posture":                          INTENT_POLICY,
    "what's our policy posture":               INTENT_POLICY,
    "whats our policy posture":                INTENT_POLICY,
    "policy status":                           INTENT_POLICY,
    "operational posture":                     INTENT_POLICY,

    # ── health ────────────────────────────────────────────────
    "health":                                  INTENT_HEALTH,
    "system health":                           INTENT_HEALTH,
    "are we healthy":                          INTENT_HEALTH,
    "is pas healthy":                          INTENT_HEALTH,
    "is the system up":                        INTENT_HEALTH,
    "service health":                          INTENT_HEALTH,

    # ── paused status ─────────────────────────────────────────
    "are we paused":                           INTENT_PAUSED_STATUS,
    "is pas paused":                           INTENT_PAUSED_STATUS,
    "are we active":                           INTENT_PAUSED_STATUS,
    "are we calling":                          INTENT_PAUSED_STATUS,
    "are we live":                             INTENT_PAUSED_STATUS,
    "paused status":                           INTENT_PAUSED_STATUS,
    "calling status":                          INTENT_PAUSED_STATUS,
    "active status":                           INTENT_PAUSED_STATUS,

    # ── leads today ───────────────────────────────────────────
    "leads today":                             INTENT_LEADS_TODAY,
    "new leads today":                         INTENT_LEADS_TODAY,
    "todays leads":                            INTENT_LEADS_TODAY,
    "today's leads":                           INTENT_LEADS_TODAY,
    "how many leads today":                    INTENT_LEADS_TODAY,
    "how many leads did we get today":         INTENT_LEADS_TODAY,
    "how many new leads today":                INTENT_LEADS_TODAY,
    "how many new leads did we get today":     INTENT_LEADS_TODAY,
    "how many new leads came in today":        INTENT_LEADS_TODAY,
    "how many leads came in today":            INTENT_LEADS_TODAY,
    "did we get any leads today":              INTENT_LEADS_TODAY,
    "did we get any new leads today":          INTENT_LEADS_TODAY,
    "any leads today":                         INTENT_LEADS_TODAY,
    "any new leads today":                     INTENT_LEADS_TODAY,
    "leads in today":                          INTENT_LEADS_TODAY,
    "new leads":                               INTENT_LEADS_TODAY,
    "lead count today":                        INTENT_LEADS_TODAY,

    # ── help ──────────────────────────────────────────────────
    "help":                                    INTENT_HELP,
    "what can you do":                         INTENT_HELP,
    "what can i ask":                          INTENT_HELP,
    "what can i ask you":                      INTENT_HELP,
    "what can pas do":                         INTENT_HELP,
    "what commands":                           INTENT_HELP,
    "list commands":                           INTENT_HELP,
    "show commands":                           INTENT_HELP,
    "commands":                                INTENT_HELP,
    "examples":                                INTENT_HELP,
    "show examples":                           INTENT_HELP,
}


# ──────────────────────────────────────────────────────────────────
# Normalisation
# ──────────────────────────────────────────────────────────────────

def _normalize(text: str) -> str:
    """
    Lower-case, strip, collapse internal whitespace, drop a single
    leading question mark / period / exclamation and any trailing
    punctuation. Deterministic and bounded.
    """
    if not isinstance(text, str):
        return ""
    t = text.strip().lower()
    if not t:
        return ""
    # Collapse internal whitespace runs.
    t = " ".join(t.split())
    # Strip a single trailing punctuation character, repeated up to
    # 3 times. We do NOT do regex; this is a bounded loop.
    for _ in range(3):
        if t and t[-1] in "?.!,":
            t = t[:-1].rstrip()
        else:
            break
    return t


# ──────────────────────────────────────────────────────────────────
# Public surface
# ──────────────────────────────────────────────────────────────────

def match_intent(text: str) -> Dict[str, str]:
    """
    Map operator-typed Slack text to a closed intent code.

    Returns a closed envelope:

        {
          "intent":            <one of INTENT_CODES, or INTENT_UNKNOWN>,
          "normalized_phrase": <the normalised text used for the lookup>,
          "matched_alias":     <the alias key that matched, or "">,
        }

    NEVER returns the raw operator text. NEVER raises.
    """
    normalized = _normalize(text)
    if not normalized:
        return {
            "intent":            INTENT_UNKNOWN,
            "normalized_phrase": "",
            "matched_alias":     "",
        }
    # Refuse to bind mutation commands. The exact-command branch in
    # slack_command.py owns these.
    first_token = normalized.split(" ", 1)[0]
    if first_token in MUTATION_COMMAND_TOKENS:
        return {
            "intent":            INTENT_UNKNOWN,
            "normalized_phrase": normalized,
            "matched_alias":     "",
        }
    intent = _ALIAS_TABLE.get(normalized, INTENT_UNKNOWN)
    return {
        "intent":            intent,
        "normalized_phrase": normalized,
        "matched_alias":     normalized if intent != INTENT_UNKNOWN else "",
    }


def list_supported_intents() -> Tuple[str, ...]:
    """Return the closed tuple of supported intent codes."""
    return INTENT_CODES


def alias_count() -> int:
    """Return the number of alias keys (for readiness instrumentation)."""
    return len(_ALIAS_TABLE)
