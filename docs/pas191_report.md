# PAS191 — Bounded Slack Natural-Language Operator Commands — Build Report

**Status:** READY (review-gated; no commit, no push, no deploy)
**Date:** 2026-05-17
**Scope:** Additive deterministic Slack natural-language read-only layer

---

## Summary

PAS191 adds a closed, deterministic, read-only natural-language
layer to the existing PAS Slack slash-command surface. A
brokerage operator can now type one of twelve common operational
questions in plain English (e.g. `/pas what's our response rate?`,
`/pas did we book any clients for showing?`) and receive a
Slack-safe, PII-free answer in under a second — without invoking
the LLM, without any autonomous behaviour, and without exposing
the brokerage to free-form execution.

The deterministic mapper fires **before** the existing LLM intent
parser. Mutation commands (`pause`, `resume`, `push`, `remove`)
are explicitly refused by the fuzzy matcher and continue to flow
through the exact-command path. The Memory Review surface, the
worker enable-flag, and every PAS160-PAS190 invariant are
unchanged.

---

## Artefacts created

| Path | Purpose |
|------|---------|
| `app/services/slack/operator_intents.py` | Pure-function deterministic intent mapper + closed alias table + mutation-refusal guard |
| `app/services/slack/operator_responses.py` | Safe per-intent response formatters + PII forbidden-token defence |
| `docs/pas191_slack_natural_language_commands.md` | Doctrine doc (purpose, relationship to PAS190, deterministic mapping, closed intent set, no-LLM, no-mutation-via-NL, PII redaction, fail-closed, help, alias curation, intentionally-does-not-build, no-autonomous-remediation, remaining limitations) |
| `scripts/pas191_slack_nl_command_readiness_check.py` | Read-only structural readiness gate (119 checks) |
| `tests/mvp/test_pas191_slack_natural_language_commands.py` | 30 tests covering mapper, formatter, route wire-through, doctrine, event contract, gate, and PAS186-PAS190 carry-forward |

## Artefacts modified

| Path | Change |
|------|--------|
| `app/routes/slack_command.py` | Added deterministic fast-path (`_pas191_dispatch` + 8 read-only DB helpers) that fires before the existing LLM intent parser; existing signature verification, rate-limit guard, and LLM fallback path preserved verbatim |
| `app/services/events/contract.py` | Added `slack.intent.matched` + `slack.intent.unknown` to `KNOWN_EVENT_TYPES` with closed payload allow-list comment |

No other files touched. No schema changes. No migrations. No new
dependencies. No deletion of any prior-phase artefact.

---

## Doctrine summary

* **Deterministic mapping** — pure function, lower-case + trim
  + collapse-whitespace + strip trailing punctuation +
  dictionary lookup. Same input → same output forever.
* **Closed intent set** — twelve codes (`stats`,
  `calls_today`, `calls_week`, `response_rate`,
  `bookings_today`, `callbacks_due`, `queue`, `incidents`,
  `policy`, `health`, `paused_status`, `help`) plus one
  `unknown` sentinel. No free-form execution.
* **No LLM for the twelve intents** — the existing
  `_parse_intent` LLM call is preserved as the fallback for
  phrases the deterministic mapper does not recognise (so the
  long-standing pause / resume / push / remove paths still
  work), but it is **never** invoked for the twelve recognised
  intents.
* **No mutation via natural language** — `match_intent()`
  hard-refuses any phrase whose first token is `pause`,
  `resume`, `push`, or `remove`.
* **PII redaction** — formatters operate on count-only,
  pre-redacted inputs; defence-in-depth `_safe()` scrub
  collapses the response if a poisoned input slips through.
* **Fail-closed on unknown** — unknown phrases fall through
  to the existing exact-command path; the system never invents
  a command.
* **No autonomous remediation** — `policy` / `incidents` /
  `health` intents are pure read-outs.
* **No new external dependency** — no gmail, no composio,
  no trust claw, no embedding pipeline, no vector database, no
  imap mailbox poller, no pop3 mailbox poller.

---

## Twelve supported intents

| Intent code | Example phrases | Backing surface |
|---|---|---|
| `stats` | `stats`, `summary`, `how are we doing` | `calls` table (count-only aggregate) |
| `calls_today` | `calls today`, `how many calls today` | `calls` table (count + booked) |
| `calls_week` | `calls this week`, `weekly calls` | `calls` table (count + booked) |
| `response_rate` | `response rate`, `pickup rate`, `connection rate` | `calls` table (completed/total) |
| `bookings_today` | `bookings today`, `did we book any clients for showing` | `calls` table (booked outcome filter) |
| `callbacks_due` | `callbacks`, `what callbacks do we owe` | `callbacks` table (pending + overdue counts) |
| `queue` | `queue`, `how many pending calls` | `pending_calls` table + worker env flag |
| `incidents` | `incidents`, `any open incidents` | `pas_incidents` table (open + severity counts) |
| `policy` | `policy`, `what's our policy posture` | PAS189 circuit-breaker policy + `pas_cutover_approvals` + env gate |
| `health` | `health`, `is the system up` | Supabase liveness + worker env + Twilio env |
| `paused_status` | `are we paused`, `are we live` | `brokerages.is_active` already loaded |
| `help` | `help`, `what can you do` | Static template |

Alias table currently has 79 entries (curated, not regex-generated).

---

## Validation matrix

| Step | Result |
|---|---|
| `python -m compileall -q app scripts tests` | clean (no syntax errors) |
| `python -m pytest tests/mvp/ -q` | **2062 passed, 4 skipped** (0 failed) |
| `python scripts/pas186_final_cutover_readiness_check.py --summary-only` | READY (240/240 checks) |
| `python scripts/pas187_fleet_cutover_readiness_check.py --summary-only` | READY (105/105 checks) |
| `python scripts/pas188_operational_scaling_readiness_check.py --summary-only` | READY (132/132 checks) |
| `python scripts/pas189_operational_wirethrough_readiness_check.py --summary-only` | READY (134/134 checks) |
| `python scripts/pas190_final_wirethrough_readiness_check.py --summary-only` | READY (140/140 checks) |
| `python scripts/pas191_slack_nl_command_readiness_check.py --summary-only` | **READY (119/119 checks)** |

Total: **870 structural readiness checks PASS** across PAS186-PAS191
+ **2062 unit tests PASS**.

---

## What PAS191 deliberately does NOT do

* Does **not** introduce an AI chat assistant or conversational
  agent.
* Does **not** allow natural-language pause / resume / push /
  remove.
* Does **not** auto-rephrase or ask the operator clarifying
  questions.
* Does **not** persist operator phrases or learn from operator
  behaviour.
* Does **not** add a background worker, scheduler, or cron job.
* Does **not** change the Memory Review surface.
* Does **not** redesign the dashboard.
* Does **not** introduce gmail, composio, trust claw,
  embeddings, a vector database, an imap mailbox poller, or a
  pop3 mailbox poller.
* Does **not** auto-trip the circuit breaker or auto-resolve
  incidents.
* Does **not** call the LLM for any of the twelve recognised
  read-only intents.

---

## Remaining limitations (for transparency)

* The alias table covers the twelve question patterns ORVN
  has heard from real-estate brokerages so far. Phrases
  outside the table return `unknown` and fall through to
  the existing exact-command path.
* `_pas191_health` derives Twilio readiness from the presence
  of `TWILIO_AUTH_TOKEN` only; it does not perform a live
  Twilio health probe.
* `_pas191_policy` shows the most recent cutover row's status,
  not the full two-person approval chain.
* The matcher does not support multilingual phrasing.

---

## Operator-review boundary

Per project memory and engine-change discipline:

* **No commit, no push, no deploy in this phase.**
* PAS191 is staged on disk only; review the diff, then run
  `git status` / `git diff` and decide whether to ratify.
* If ratified, the additive surfaces (5 new files + 2 modified
  files) can be committed in a single PAS191 commit; the
  PAS191 readiness gate should remain green after the commit.
* The existing Twilio trial gate, the PAS-SECURITY-04
  deferred-reveal flow, and the off-limits
  `scripts/combined_supabase_migration.sql` are all preserved.

End of PAS191 build report.
