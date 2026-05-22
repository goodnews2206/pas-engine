# PAS204 — Broker Conversation Intelligence Layer

## Purpose

PAS193–PAS203 give PAS the *evidence* layer — rehearsals,
strategies, packages, runtimes, inspections, behavioural
evaluations, the PAS201 digest, and a read-only Slack surface to
view it. PAS204 takes the next bounded step: it makes PAS respond
**like a useful operations staff member**, not a technical audit
tool.

A broker who types `/pas hot leads` or `did we miss anything
today?` should not get back closed-vocabulary tokens like
`behavioral_low_friction_observed`. They should get a plain
sentence a teammate would write.

PAS204 ships four pure-Python modules and a deterministic
30,000-evaluation simulation runner. Nothing in PAS204 takes any
autonomous action, switches a live strategy, calls Twilio,
mutates Supabase, or sends an outbound Slack message. It is a
**voice layer**, not a routing layer.

## Research basis

Brokers and agents consistently care about a small number of
operational concerns:

* **Lead response time** — minutes-to-first-contact, especially
  for portal leads (Zillow, realtor.com, Facebook).
* **Missed follow-up** — leads that came in but didn't get
  reached in the response window.
* **Stale lead recovery** — older threads that have gone quiet
  and need a soft nudge, not a hard sell.
* **Appointment booking** — showings booked, on the calendar.
* **Lead qualification** — does PAS actually capture intent /
  budget / timeline before handing off.
* **After-hours coverage** — does anyone answer at 2 AM, on
  weekends, on holidays.
* **CRM sync** — is the CRM seeing what PAS sees.
* **ISA performance comparison** — how PAS stacks up against a
  human ISA on the metrics the brokerage actually tracks.
* **Pipeline visibility** — which sources convert, which agents
  get the leads, which integrations are connected.
* **"What should I do next?"** — the operator's morning
  prioritisation question.
* **"Is it safe to trust?"** — the founder's risk question.

PAS204 builds a closed catalogue of 300+ realistic broker
phrasings of those concerns (including typos, shorthand,
unfinished context, casual phrasing, beginner phrasing, and
impatient-owner phrasing), classifies them deterministically,
and renders plain-English answers grounded — when available — in
the PAS201 evidence digest.

## What PAS204 proves

* **A deterministic broker-question catalogue exists.** 308
  realistic broker-style entries across 22 intents and 22
  categories, all closed-vocabulary, no PII, no real names.
* **A deterministic intent classifier handles messy input.**
  100% accuracy on the canonical text of every catalogue entry;
  typo-tolerant (single edit-distance for tokens ≥5 chars);
  closed-vocabulary fallback (`fallback_clarify`) for
  unclassifiable phrases. No LLM, no network, no fuzzy ML.
* **A broker-facing voice exists.** A closed token-to-human
  translation table covers every PAS200/PAS201 closed-vocab
  token an operator might see (safety markers, evidence
  strengths, behavioural flags, lineage states), plus a
  per-intent response builder that:
  - never invents lead names, counts, addresses, or phone
    numbers,
  - never asserts live activity,
  - never emits a forbidden live-routing token,
  - always includes at least one next-step suggestion,
  - falls back honestly to "I don't have that data plumbed in
    yet" rather than guessing.
* **A conversation surface ties them together.** `build_broker_response(text, *, evidence=None)`
  returns a closed envelope dict and optionally grounds the
  response in a PAS201 digest when supplied.
* **A 30,000-evaluation simulation runner scores the layer.**
  308 questions × 100 deterministic variants (case, punctuation,
  whitespace, typos, casual prefixes, leet substitutions,
  truncation) per question, scored on 8 quality booleans
  (understood_intent, human_tone, useful_answer, no_jargon,
  no_false_claim, no_live_action, suggests_next_step,
  handles_typo_or_fragment). A run passes when all 8 are True.
* **Zero jargon leaks and zero false-live claims.** Across all
  30,000 evaluations, the rendered response body contains no
  PAS internal closed-vocab token verbatim and no "we just
  routed" / "live deployment" / "now live" phrasing.
* **PAS191 / PAS192 / PAS203 carry-forward is intact.** PAS204
  ships parallel infrastructure in a NEW namespace (`broker_*`),
  does not modify PAS191's `INTENT_CODES` tuple (still exactly
  15 entries — both PAS191 and PAS192 carry-forward tests
  assert this strictly), does not touch
  `operator_intents.py` / `operator_responses.py` /
  `slack_command.py`, and does not collide with PAS203's
  `simulation_digest_intent` module.
* **No external service imports.** PAS204 production source
  imports nothing from `twilio`, `slack_sdk`, `openai`,
  `anthropic`, `dotenv`, `supabase`, the live state machine,
  the outbound notifications client, or PAS191's intent /
  response modules.
* **No forbidden status literals.** `APPROVED`, `APPLIED`,
  `AUTO_APPLIED`, `LIVE`, `DEPLOYED` never appear as string
  constants in any PAS204 production source file.
* **No live-mutation / outbound-messaging identifiers.**
  Fourteen identifier names (apply_recommendation /
  deploy_strategy / switch_strategy_live / auto_apply /
  auto_promote / force_promote / live_apply / auto_deploy /
  route_lead_live / route_call_live / send_real_sms /
  send_real_call / send_slack_message / post_to_slack) are
  all absent.

## What PAS204 does not prove

* **PAS204 does not take any autonomous action.** It returns
  strings; the dispatcher (PAS203 follow-up phase or later)
  decides whether to surface them.
* **PAS204 does not have operational data plumbed in.** Every
  data-dependent intent (leads_today, hot_leads, missed_leads,
  callbacks, appointments, response_speed, source quality,
  CRM sync, source handling) sets `no_data_available=True` in
  the response envelope and emits a body that is honest about
  not having the numbers. PAS204 deliberately ships the voice
  layer first; data plumbing is PAS205+.
* **PAS204 does not auto-improve the strategy.** It surfaces
  behavioural evaluation in plain English, but humans still
  decide whether to change strategy.
* **PAS204 does not modify PAS191 / PAS192 / PAS203 behaviour.**
  The existing fast-path keeps working unchanged.
* **PAS204 does not validate against live broker conversations.**
  Calibration of broker-voice tone against real broker reaction
  belongs to PAS205+.

## How broker-facing tone works

Every PAS204 response has the same shape:

1. **A plain-sentence answer body** that explains the broker's
   question in operations-staff language ("Hot leads are the
   ones engaging most — quick replies, repeat questions,
   time-window asks. I can't list specific names without more
   data plumbed in, but I'll never guess.")
2. **A bounded "no data" honesty layer** that names the
   limitation explicitly, with no fake counts or names.
3. **A safety reminder** that the underlying rehearsal evidence
   is SIMULATION_ONLY and `no_live_behavior_changed`.
4. **One or two next-step suggestions** drawn from a closed
   per-intent suggestion table: "Ask: 'any callbacks owed'…",
   "Ask: 'response speed'…". Brokers don't get stuck — there's
   always a next question to ask.
5. **For ambiguous fallback input only**, a single clarifying
   question.

The voice deliberately avoids:

* **Technical token leakage** — PAS200/PAS201 closed-vocab
  tokens are translated into plain sentences before they ever
  reach the broker.
* **Live-action claims** — no phrase like "we just routed",
  "now live", "live deployment", or any of the closed
  `FORBIDDEN_OUTPUT_TOKENS` list ever appears.
* **Inventing data** — no fake counts, no fake names, no fake
  percentages. If the data isn't there, the answer says so.
* **Long marketing prose** — answers are short, factual, and
  end on a useful next step.

## Claimable today (with PAS204 merged)

* PAS responds to broker-style questions in plain English from
  a closed-vocabulary 22-intent catalogue, with 100% canonical
  classification accuracy and >= 95% pass rate across 30,000
  deterministic typo/fragment/casual-phrasing variants.
* The voice layer is deterministic — same input always
  produces the same response. Zero LLM, zero network, zero
  randomness.
* The voice layer is bounded — no PII, no production
  brokerage IDs, no fake counts, no live-routing wording, no
  PAS internal jargon leakage.
* PAS191 / PAS192 / PAS203 intents continue to work unchanged.
* The 30,000-evaluation simulation runner produces a single
  bounded JSON report (`pas204_broker_conversation_simulation_<ts>.json`)
  under `reports/simulations/` for audit.
* When operational data is missing, the response says so
  explicitly rather than guessing.

## Still not claimable (PAS205+)

* PAS204 does not yet have operational data plumbed in (lead
  counts, callbacks owed, response speed metrics). The voice
  layer is correct; the data sources still need a bounded
  PAS205 read-only adapter.
* PAS204 does not validate broker-facing tone against real
  broker reactions. A calibration loop against real Slack
  workspace conversations is a future phase.
* PAS204 does not consume the PAS201 digest from disk inside
  the Slack dispatcher — that wiring is PAS203's job; PAS204
  exposes `build_broker_response(text, evidence=...)` for the
  dispatcher to plug in when it chooses.
* PAS204 does not auto-improve responses based on what brokers
  ignore. There is no learning loop, and that is deliberate.

## Future PAS205 path

PAS205 is the next bounded step: a **read-only operational data
adapter** that plumbs lead counts, callbacks owed, appointments
today, response speed, and source breakdowns into the same
voice layer this phase ships. Expected shape:

1. A bounded read-only adapter that returns *only* the numbers
   the voice layer needs, in a closed schema.
2. No new Supabase write paths, no new background jobs.
3. PAS204 voice unchanged — only the `evidence=` argument grows
   to include operational data alongside the PAS201 digest.
4. A PAS205 readiness gate asserting the adapter cannot
   mutate, cannot trigger calls, cannot bypass the
   no-real-PII rule.

PAS205 is **not** PAS204's responsibility. PAS204 ships the
deterministic voice layer; PAS205 ships the bounded data the
voice layer can ground its answers in.

## Safety constraints (inherited + extended)

PAS204 inherits the full PAS191 / PAS192 / PAS201 / PAS202 /
PAS203 safety doctrine:

* No real leads, no real phone calls, no Twilio live calls.
* No outbound Slack messages — PAS204 returns strings; the
  existing dispatcher decides what to do with them.
* No worker auto-start, no production brokerage mutation.
* No new SQL migration, no edits to
  `combined_supabase_migration.sql`.
* No secret-shaped tokens in source or in any rendered
  response.
* No PII in renderings — no free-form text fields, no real
  user ids, no email addresses, no phone numbers, no
  production brokerage UUIDs.
* No autonomous-apply / outbound-messaging identifiers in
  PAS204 production source — readiness gate enforces by AST
  scan.
* No forbidden status literals (`APPROVED`, `APPLIED`,
  `AUTO_APPLIED`, `LIVE`, `DEPLOYED`) in PAS204 production
  source — readiness gate enforces by AST string-constant
  scan.
* No live-routing assertions in any rendering — a defensive
  guard refuses any output that contains a forbidden token.
* Input data the voice layer doesn't have is treated as
  "missing" and honestly named, not invented.

## How to run

```
# Compile-check.
python -m compileall -q app scripts tests

# Unit + integration tests (PAS204 only).
python -m pytest tests/mvp/test_pas204_broker_conversation_intelligence.py -q

# Read-only readiness gate.
python scripts/pas204_broker_conversation_readiness_check.py --summary-only

# Full 30,000-evaluation simulation (writes one JSON report
# under reports/simulations/).
python scripts/pas204_run_broker_question_simulations.py --questions 308 --variants 100

# Faster smoke run.
python scripts/pas204_run_broker_question_simulations.py --questions 50 --variants 20 --summary-only
```

Simulation reports land under `reports/simulations/` with
filenames of shape
`pas204_broker_conversation_simulation_<utc-timestamp>.json`.

## Relationship to PAS191 / PAS192 / PAS203

PAS204 is purely additive over all three:

* **PAS191 / PAS192** — new namespace (`broker_*`), separate
  intent set, separate response builders. `INTENT_CODES`
  remains exactly 15. `operator_intents.py` /
  `operator_responses.py` are byte-for-byte unmodified.
* **PAS203** — PAS204 *consumes* the same PAS201 digest shape
  PAS203 surfaces. The dispatcher integration is the same
  pattern as PAS203's `try_route_simulation_digest`; PAS204
  exposes `build_broker_response(text, evidence=...)` for the
  dispatcher to call when the broker types something that is
  *not* one of PAS203's six digest phrases. Wiring is a future
  phase decision.
