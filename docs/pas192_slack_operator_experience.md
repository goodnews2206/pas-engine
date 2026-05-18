# PAS192 — Slack Operator Experience + Action Layer

## Purpose

PAS192 turns the PAS Slack surface from a command-response bot into
a useful operator interface for a brokerage owner. It adds two
read-only natural-language intents on top of PAS191:

* `today_summary` — the daily wrap (`/pas summary`, `/pas today`,
  `/pas what happened today`, `/pas daily summary`). Rolls up
  today's leads, calls, bookings, response rate, pending-queue
  depth, and a short list of operator-visible warnings.
* `next_action` — the top three operational priorities
  (`/pas what should I do now`, `/pas next action`,
  `/pas priorities`, `/pas what needs attention`). Ranked from
  existing data — assign agents, review overdue callbacks, follow
  up call-eligible leads, resolve open incidents, etc.

It also reword the `help` and `unknown` fallbacks so a brokerage
owner sees natural-language examples instead of command jargon.

## Relationship to PAS191

PAS191 introduced the deterministic alias-table mapper and the
closed read-only formatter surface. PAS192 stands directly on top
of that work and **does not** change the doctrine:

* The natural-language layer is still a closed alias table. No
  LLM. No regex. No best-guess classifier.
* The `today_summary` and `next_action` formatters live alongside
  the PAS191 formatters in `operator_responses.py` and follow the
  same PII-redaction guard.
* The dispatcher in `app/routes/slack_command.py` adds two new
  branches under the same `_pas191_dispatch` umbrella; the
  fast-path-before-LLM ordering invariant is preserved.

PAS192 introduces no schema changes, no new background jobs, and
no new external-system dependencies.

## Deterministic mapping doctrine

PAS192 adds entries to the PAS191 closed alias table. Each new
phrase is hand-curated. The matcher is still pure-function — no
regex, no NLP, no probability. Same input → same output forever.

If an operator phrase is not in the table, the matcher returns
`unknown` and the route falls through to the existing exact-command
branch (mutations) or the friendly fallback message.

## Closed intent set doctrine

The intent set grew from 13 to 15. The full closed list:

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
| `help`             | Natural-language examples + the closed intent list   |
| `leads_today`      | Today's new-lead intake (new / call-eligible / queued) |
| `today_summary`    | Operator daily wrap with warnings                    |
| `next_action`      | Top three operational priorities                     |

Plus the `unknown` sentinel.

The list is closed. Adding a 16th intent is a deliberate code
change with a new alias-table entry, a new formatter, and a new
dispatcher branch — guarded by the PAS192 readiness check.

## No LLM doctrine

The PAS191 + PAS192 fast-path never imports, calls, or
instantiates a large-language-model provider. The readiness gate
enforces this by scanning the pure service modules
(`operator_intents.py`, `operator_responses.py`) for any LLM
import. The LLM fallback path in `slack_command.py` only fires
when the deterministic matcher returns `unknown` AND the text
is not an exact mutation command.

## No mutation via natural language

PAS192 does **not** add mutation execution. `next_action` may
suggest "Assign agents" or "Resume PAS", but PAS never executes
the suggested action — it only describes the next step the
operator should take. Mutation commands (`pause`, `resume`,
`push`, `remove`) still go through the existing exact-command
branch. The `MUTATION_COMMAND_TOKENS` guard in
`operator_intents.match_intent()` continues to refuse to fuzzy-bind
any phrase that starts with one of those tokens.

## PII redaction doctrine

Both new formatters accept already-aggregated counts — they never
receive raw row data. The defence-in-depth forbidden-token scrub
in `operator_responses._safe()` still wraps every output. The
`next_action` formatter additionally restricts the optional
detail field to a short count phrase (digits + simple words +
`.,/()-`) so a future caller cannot accidentally smuggle PII
through the detail slot.

The PAS192 readiness gate asserts that the today_summary and
next_action formatters do not introduce new forbidden tokens
(phone, email, lead_name, transcript, etc.) and that the dispatch
helpers in `slack_command.py` never select PII columns
(phone_number / name / email / transcript) for the new intents.

## Fail-closed on unknown intent

The friendly fallback message replaces the previous robotic
"didn't recognise that command" line, but the routing behaviour
is unchanged: unknown phrases never reach a write path, never
echo back the operator's raw text, and never invoke an LLM in the
PAS191 fast-path. The exact-command branch is the only path that
can mutate state.

## Operator help doctrine

The help message now leads with natural-language examples
("how many leads did we get today?", "what should I do now?")
followed by a one-line list of quick references. Mutation
commands are still surfaced explicitly as a separate paragraph
so an operator knows how to pause / resume PAS.

## Alias table curation doctrine

PAS192 adds about 30 new phrase keys across the two new intents
and the help intent. We deliberately avoid regex / stemming /
NLP. The keys are hand-audited; the readiness gate's alias-count
check ensures the table grows monotonically.

## What PAS192 intentionally does not build

* No actual mutation execution. `next_action` describes what to
  do; it never executes it. No "retry booking", "assign agent",
  "pause", "resume" autonomous paths.
* No new memory writes. PAS192 never calls the memory store and
  is excluded from the auto-memory write path.
* No event_logger schema changes. PAS192 reuses the existing
  `slack.intent.matched` / `slack.intent.unknown` event types.
* No new background workers, cron jobs, or autonomous calling.
* No Twilio live-call paths. No real lead data reads.
* No migrations. No `combined_supabase_migration.sql` edits.
* No Gmail. No Composio. No vector-store / embedding / openai
  imports. No external chat integration. The readiness gate
  enforces this with a forbidden-import scan.

## No autonomous remediation

`next_action` ranks priorities from existing data. It does not
trip the circuit breaker, restart the worker, mutate the brokerage
`is_active` flag, send outreach, or write to any table. Every
priority code maps to a static label in
`_NEXT_ACTION_LABELS`; the dispatcher cannot emit free-form text.

## Remaining limitations

* `today_summary` is only as good as the data backing it — if
  Supabase is unavailable, every count falls back to zero and
  the operator sees an "no calls / no leads / no bookings"
  picture rather than an error.
* `next_action` priorities are deterministic and intentionally
  unsophisticated; they exist to direct operator attention, not
  to replace operator judgement.
* The help message is static. There is no per-brokerage tailoring
  — that is intentional, to keep the surface bounded and PII-safe.
* No Gmail. No Composio.
