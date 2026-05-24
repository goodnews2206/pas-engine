# PAS207 — Slack needs-attention digest

## What PAS207 proves

PAS207 surfaces the PAS205 read-only proactive observer through
Slack as a broker-friendly needs-attention digest. It proves that:

* The proactive observer can be reached by an operator through a
  natural-language Slack command, without any change to PAS191's
  alias table, PAS192's priorities surface, PAS203's simulation
  digest fast-path, or PAS204's broker conversation layer.
* The Slack surface adds zero outbound side effects: no Slack API
  write, no Twilio call, no SMS, no email, no DB mutation, no
  scheduler, no worker. The dispatcher returns a string.
* The observer's broker-voice rendering is acceptable as a Slack
  response without sanitisation. No PAS internals
  (`PAS205` / `PAS207` / `SIMULATION_ONLY` / `live_behavior_changed`
  / closed-vocab signal tokens) leak into operator-visible output.
* The proactive layer is reachable by operators even though no
  scheduler exists yet — proactivity here means "always ready to
  answer when asked", not "wakes up unprompted".

## What PAS207 does NOT prove

PAS207 is a pull/read surface only. It does **not** prove:

* PAS207 does not push or schedule notifications. Operators must
  ask. (That is PAS208's surface to design, behind explicit
  approval.)
* PAS207 does not propose any action or operator prompt. It only
  describes what needs attention.
* PAS207 does not execute any bounded action, even an
  operator-approved one. (PAS209.)
* PAS207 does not yet pull from live Supabase by default. It runs
  on a deterministic seeded snapshot. PAS206's adapter exists and
  can be wired behind an explicit operator acknowledgement, but
  that wiring is out of PAS207 scope.
* PAS207 does not modify the PAS engine, the live state machine,
  the call path, or the worker.
* PAS207 does not introduce a new external vendor.

## Why this is proactive visibility, not autonomous action

The proactive observer watches; it does not act. PAS207 makes the
"watching" addressable by operators through the same Slack surface
they already use for PAS191/PAS192/PAS203/PAS204 commands. Every
operator-visible interaction with PAS207 is initiated by a typed
phrase from the operator — there is no path by which PAS207 can
post to Slack on its own, send SMS, place a call, write to the
database, or schedule a future action.

That property is asserted three ways:

1. The readiness gate forbids `.insert(`, `.update(`, `.delete(`,
   `.upsert(`, `.rpc(` and any Twilio / Slack outbound / openai /
   anthropic / smtplib / apscheduler / celery / schedule import in
   the PAS207 intent source.
2. The PAS207 test suite asserts the renderer never emits closed
   vocab tokens (`callback_overdue`, `lead_unassigned`, ...) and
   never mentions PAS internals.
3. The PAS207 readiness gate asserts the alias tuple is exactly
   the eight phrases from the spec, that the tuple contains no
   PAS191 next-action phrase, and that the dispatcher fast-path
   sits before the PAS191 deterministic dispatch.

## Supported phrases

PAS207 owns a closed alias vocabulary. Anything else falls through
to PAS191 / PAS204 / LLM unchanged.

| Phrase                          |
|---------------------------------|
| what needs attention            |
| what should I look at           |
| anything slipping               |
| pipeline risks                  |
| show risks                      |
| what is at risk                 |
| what should I handle next       |
| what needs human review         |

The matcher normalises case, trailing punctuation, and internal
whitespace, but does no fuzzy / LLM matching. PAS191 phrases
("next action", "priorities", "next steps", "top priorities",
"what should I focus on", "what should I do now", ...) continue
to route to PAS191's `next_action` intent exactly as before.

## Dispatcher placement

`slack_command.py` order, post-PAS207:

1. PAS203 simulation evidence digest fast-path
2. PAS191 `match_intent()` lookup (computed but not yet acted on)
3. PAS204 broker conversation (only fires when PAS191 returns
   `INTENT_UNKNOWN`)
4. **PAS207 needs-attention digest fast-path (new)**
5. PAS191 deterministic dispatch (when PAS191 had a match)
6. LLM fallback

Placing PAS207 between PAS204 and PAS191 dispatch lets PAS207
own the phrase "what needs attention" (which PAS191 also has in
its alias table for `next_action`) while leaving every other
PAS191 phrase unaffected. The PAS207 fast-path returns immediately
on a match.

## Source-agnostic snapshot

The PAS207 intent service accepts a `snapshot_provider` callable
argument:

```python
try_route_needs_attention(text, snapshot_provider=my_provider)
```

By default it uses `build_demo_snapshot()` — a deterministic,
PII-free, bounded in-memory snapshot. A later wiring step can pass
PAS206's Supabase adapter behind an explicit operator
acknowledgement without touching this module.

## Future path: PAS208

PAS208 will turn the PAS207 digest's signals into bounded,
operator-approved recommendations. PAS207 names what is at risk.
PAS208 proposes what an operator could do about it. PAS209 then
gates bounded action execution behind operator approval. Each step
is additive and reversible.

## Safety doctrine

* **READ-ONLY.** Dispatcher returns a string; no Slack API write.
* **NO MUTATION.** No `insert / update / delete / upsert / rpc`.
* **NO TWILIO.** Calling logic is not imported.
* **NO SMS / EMAIL.** Outbound messaging tokens forbidden.
* **NO SCHEDULER, NO WORKER, NO CRON.**
* **NO MIGRATIONS.** No `combined_supabase_migration.sql`.
* **NO SECRETS.** Credentials never touched.
* **PARKED STASH UNTOUCHED.**
* **PAS191/PAS192/PAS203/PAS204 BEHAVIOR PRESERVED.**
