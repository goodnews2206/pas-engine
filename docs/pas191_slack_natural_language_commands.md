# PAS191 — Bounded Slack Natural-Language Operator Commands

## Purpose

PAS191 adds a small, deterministic, **read-only** natural-language
layer on top of the existing PAS Slack slash-command surface so a
brokerage operator can ask the twelve most common operational
questions in plain English and receive a Slack-safe answer in
under a second — without any large-language-model interpretation,
without any autonomous action, and without any leak of personally
identifiable information.

It is the smallest possible step toward "the brokerage talks to
their AI staff" while keeping every PAS160-PAS190 safety doctrine
in place.

## Relationship to PAS190

PAS190 closed the final operational wire-through gates for the
pilot cutover rehearsal. PAS191 stands on top of that work:

* The dispatcher reads from the same PAS189 / PAS190 closed
  surfaces (`circuit_breaker_policy`, fleet status, tenant
  incidents) — it never writes.
* The PAS190 fail-open + no-autonomous-remediation discipline
  carries forward verbatim.
* The PAS190 doctrine that "no surface in the operator path may
  echo PII, secrets, or webhook URLs" is enforced again at the
  formatter layer by a defence-in-depth forbidden-token scrub.

PAS191 introduces no schema changes, no new background jobs, and
no new external-system dependencies.

## Deterministic mapping doctrine

The natural-language layer is a **closed alias table**, not a
classifier. A pure-function matcher (`match_intent()` in
`app/services/slack/operator_intents.py`) lower-cases the
operator's text, collapses whitespace, strips trailing
punctuation, and looks the phrase up in a hand-curated
dictionary. Same input always produces the same output. No
randomness, no probability, no implicit state.

If the phrase is not in the table, the matcher returns the
`unknown` intent and the existing slash-command path takes over.
There is no "best guess" branch.

## Closed intent set doctrine

There are exactly twelve recognised intent codes:

| Intent code        | Meaning                                              |
|--------------------|------------------------------------------------------|
| `stats`            | All-time conversion summary                          |
| `calls_today`      | Today's call volume + booked count                   |
| `calls_week`       | This week's call volume + booked count               |
| `response_rate`    | Pickup / answer rate                                 |
| `bookings_today`   | Showings booked today                                |
| `callbacks_due`    | Pending and overdue callback counts                  |
| `queue`            | Pending-call queue depth + worker state              |
| `incidents`        | Open operational incidents with severity breakdown   |
| `policy`           | Circuit-breaker + cutover + security posture summary |
| `health`           | Database + worker + telephony readiness              |
| `paused_status`    | Whether PAS is actively dialling for this brokerage  |
| `help`             | Static list of supported questions                   |

Plus one sentinel:

| Intent code        | Meaning                                              |
|--------------------|------------------------------------------------------|
| `unknown`          | Fall through to the existing exact-command branch    |

The list is closed. Adding a new intent is a deliberate code
change with a new alias-table entry, a new formatter, and a new
dispatcher branch — guarded by the readiness check.

## No LLM doctrine

The PAS191 fast-path never imports, calls, or instantiates a
large-language-model provider. The readiness gate enforces this
by scanning `app/services/slack/operator_intents.py` and
`app/services/slack/operator_responses.py` for forbidden imports
and asserting that the deterministic call to `match_intent(text)`
appears **before** the existing `_parse_intent(text)` call in
`app/routes/slack_command.py`.

The pre-existing LLM-based intent parser remains in the file as
the fallback path. It only fires when `match_intent()` returns
`unknown` (i.e., the phrase is not in the closed alias table).
For the twelve recognised intents, no LLM call is ever made.

## No mutation via natural language

The matcher refuses to bind any phrase whose first token is
`pause`, `resume`, `push`, or `remove`. Even if an operator types
`"please pause everything for a moment"`, the matcher returns
`unknown` and the request flows to the existing exact-command
path, which requires the literal command. Mutation commands must
remain unambiguous, deliberate, and exact.

This is enforced both by the `MUTATION_COMMAND_TOKENS` guard in
the matcher and by a unit test in
`tests/mvp/test_pas191_slack_natural_language_commands.py`.

## PII redaction doctrine

The response formatter operates on already-redacted, count-only
inputs. Every formatter:

* Accepts a small dict of integers, booleans, and short label
  strings — never a row from the database.
* Builds the response string from a fixed template — no
  string-format from raw operator text.
* Runs a defence-in-depth scan (`_safe()`) for the forbidden
  token list (`phone`, `email`, `lead_name`, `transcript`,
  `raw_payload`, `secret`, `signature`, `api_key`,
  `webhook_url`, `stack_trace`, etc.). If any of these tokens
  appear in the formatted string the entire message collapses
  to a generic "response redacted — contact operator" line.

The dispatcher (`_pas191_dispatch` in `slack_command.py`)
never reads phone numbers, names, transcripts, or raw payloads
into the response path. It runs aggregate queries (counts,
booleans, status enums) only.

## Fail-closed on unknown intent

`match_intent()` returning `unknown` does **not** trigger an
auto-action. Instead the request continues to the existing
exact-command branch, which itself returns a static help string
if it cannot identify the command. Operators are never silently
ignored, and the system never invents a command on their behalf.

## Operator help doctrine

The `help` intent returns a static, code-controlled message that
lists every supported question and reminds the operator that
mutation commands use the exact-command path. The help text
never references roadmap items, hypothetical features, or
external integrations.

## Alias table curation doctrine

The alias table is hand-curated. Adding a new alias is a one-line
code change, reviewable in diff. The matcher never auto-learns
from operator behaviour, never persists operator phrases, and
never adapts the table at runtime. This is the same governance
posture as PAS179: no learning autopilot, no adaptive-memory
auto-write.

## Intentionally does not build

PAS191 deliberately does **not** introduce:

* An AI chat assistant or conversational agent of any kind.
* Auto-rephrasing or follow-up clarification questions.
* Any mutation surface reachable via natural language.
* Any cross-brokerage aggregation (each Slack workspace sees
  only its own brokerage's metrics).
* Any new external-service dependency: no gmail, no
  composio, no trust claw, no embedding pipeline, no vector
  database, no imap mailbox poller, no pop3 mailbox poller.
* Any background worker, scheduler, or cron job.
* Any change to the Memory Review surface.
* Any dashboard redesign.

## No autonomous remediation

PAS191 never trips the circuit breaker, resolves an incident,
pauses a brokerage, or clears a queue on its own. The
`policy`, `incidents`, and `health` intents are pure
read-outs. Mutation remains the sole responsibility of the
exact-command path, two-person cutover discipline (PAS187),
and operator-driven runners (PAS188-PAS190).

## Remaining limitations

* The alias table covers the twelve operator questions ORVN has
  heard from real-estate brokerages so far. Phrases outside the
  table return `unknown`; future PAS phases may expand the
  table as more brokerages onboard.
* `_pas191_health` derives Twilio readiness from the presence
  of `TWILIO_AUTH_TOKEN` only — it does not perform a live
  Twilio health probe. A future phase may add a cached probe.
* `_pas191_policy` shows the most recent cutover row's status;
  it does not summarise the full two-person approval chain.
* The matcher does not support multilingual phrasing.
