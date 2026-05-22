# PAS202 — Operator Evidence Digest Surface

## Purpose

PAS201 ships a single bounded JSON digest summarising the
PAS195 → PAS196 → PAS197 → PAS198 → PAS199 → PAS200 simulation
lineage. PAS202 takes the next bounded step: it makes that digest
**operator-readable** without changing anything else.

PAS202 is a **read-only presentation layer**. It consumes a PAS201
digest and produces three deterministic renderings — a structured
operator summary (dict), a multi-line plain-text block, and a
Slack-safe markdown string. Nothing in PAS202 sends a message,
executes a strategy, or touches production.

PAS202 is the smallest possible operator surface for the digest:

* A pure function (`format_operator_summary`) that validates the
  PAS201 digest contract and emits a bounded structured summary.
* A pure function (`format_digest_as_text`) that renders the
  digest as a human-readable text block.
* A pure function (`format_digest_for_slack`) that renders the
  digest as a Slack-safe markdown string. The Slack formatter
  **returns a string**; it does not call any Slack API.
* A CLI that wraps the three formatters and can optionally write
  the operator summary under `reports/simulations/`.
* A readiness gate that asserts the surface can never be anything
  other than `SIMULATION_ONLY`.

PAS202 does **not** send a Slack message. PAS202 does **not**
route a live call. PAS202 does **not** deploy anything. PAS202
does **not** generate evidence — it reads what PAS201 already
produced. Its only outputs are strings (printed to stdout) and an
optional read-only JSON summary file.

## What PAS202 proves

* **The PAS201 digest can be read deterministically.** A pure
  function in `app/services/simulation/evidence_digest_surface.py`
  consumes a PAS201 digest and emits a structured operator
  summary with stable contents on identical inputs.
* **The surface is environment-bounded by construction.** All
  three formatters refuse any digest whose `phase` is not
  `PAS201`, whose `allowed_environment` is not `SIMULATION_ONLY`,
  or whose `live_behavior_changed` is not `False`. Mismatches
  raise `EvidenceDigestSurfaceValidationError`.
* **Output is closed-vocabulary.** Operator highlights,
  `claimable_now`, and `not_claimable_yet` are passed through
  verbatim from the PAS201 digest (which itself draws them from
  closed PAS201 vocabularies). The surface adds no free-form
  text; only fixed structural labels and the digest's own
  tokens appear in rendered output.
* **Live-routing wording is impossible.** A defensive check
  enforces that no rendering can contain tokens like
  `live_routing_active`, `live_call_routed`,
  `strategy_deployed_live`, `real_lead_handled`, or
  `production_traffic_served`. Any attempt to emit one raises.
* **The Slack rendering is API-free.** `format_digest_for_slack`
  returns a string. It does not import `slack_sdk`, does not
  call any Slack endpoint, and does not send any message. The
  string is hard-capped at 4 000 characters so the renderer is
  concise by construction.
* **No external service imports.** PAS202 source imports nothing
  from `twilio`, `slack_sdk`, `openai`, `anthropic`, `dotenv`,
  `supabase`, or `app.engine.state_machine`.
* **No forbidden status literals.** The strings `APPROVED`,
  `APPLIED`, `AUTO_APPLIED`, `LIVE`, `DEPLOYED` never appear as
  string constants in PAS202 source. The readiness gate
  enforces this by AST string-constant scan.
* **No forbidden live-mutation identifiers.** Twelve identifier
  names — `apply_recommendation`, `deploy_strategy`,
  `switch_strategy_live`, `auto_apply`, `auto_promote`,
  `force_promote`, `live_apply`, `auto_deploy`,
  `route_lead_live`, `route_call_live`, `send_real_sms`,
  `send_real_call` — plus two messaging identifiers
  (`send_slack_message`, `post_to_slack`) are all absent from
  PAS202 source.
* **No PII in output.** Tests verify that none of the three
  renderings contains phone-shaped tokens or production-shaped
  brokerage UUIDs.
* **PAS201 digest is not mutated.** Tests verify that running
  all three formatters against a digest leaves the digest
  byte-for-byte unchanged.

## What PAS202 does not prove

The surface renders evidence; it does not generate evidence and
it does not act on it. The following remain out of scope:

* **PAS202 does not send a Slack message.** The Slack formatter
  returns a string for operators to copy-paste manually. An
  authenticated Slack-posting surface belongs to PAS203 or
  later.
* **PAS202 does not route a live call.** No part of PAS202
  touches the production engine, Twilio, Supabase, or any
  outbound integration.
* **PAS202 does not promote a strategy.** A `strong` digest
  rendered through PAS202 is human-readable evidence, not an
  action.
* **PAS202 does not validate against live-call performance.**
  Calibration of digest-strength against live outcomes is
  PAS202+'s next phase.
* **PAS202 does not generate new digest content.** Every field
  in the rendering comes from a closed PAS201 vocabulary or is
  a fixed structural label.

## How an operator should read digest output

### Plain-text rendering (default)

```
PAS201 evidence digest pas201-dgst-XXXX (strategy=callback_first, ...)
Evidence strength: strong
Recommended next action: review_digest_then_decide_pilot_step
Safety: outcome=clean, auto_fail_count=0
Lineage: intact=True
  recommendation_id        = pas195-rec-...
  review_id                = pas196-rev-...
  package_id               = pas197-pkg-...
  runtime_id               = pas198-rt-...
  inspection_id            = pas199-insp-...
  behavioral_evaluation_id = pas200-beval-...
Artifact integrity: 24/24
No live behavior anywhere in lineage: True
Operator highlights:
  - runtime_pass_rate_100_percent
  - safety_outcome_clean
  - ...
Claimable now:
  - synthetic_rehearsal_passed_for_strategy
  - operator_approved_strategy_for_manual_test
  - ...
Still not claimable:
  - live_call_routing_remains_out_of_scope
  - calibration_against_live_call_outcomes_pending
  - ...
```

Read top-down:

1. **Header** identifies the digest, strategy, and confirms
   `SIMULATION_ONLY`, `live_behavior_changed=False`.
2. **Evidence strength + next action** tells you the
   one-word verdict and the single closed-vocabulary action
   token PAS201 recommends.
3. **Safety + lineage + artifact integrity** are the gate
   checks — if any of these is off, the rest is suspect.
4. **Highlights** is the per-strategy structural signal.
5. **Claimable now / still not claimable** is the script for
   a demo or stakeholder review.

### Structured JSON (`--json`)

For programmatic consumption, audit handoff, or pipeline
integration. The schema is the keys named in
`OPERATOR_SUMMARY_REQUIRED_KEYS`.

### Slack-safe markdown (`--slack`)

Concise, single-message size, Slack-styled. **The operator must
paste it manually**; PAS202 does not authenticate to Slack and
does not POST anywhere.

### Writing the operator summary (`--write-summary`)

Writes the structured operator summary as JSON under
`reports/simulations/` for handoff to a teammate, auditor, or
investor. The file is read-only artefact data.

## Claimable today (with PAS202 merged)

* An operator can render any PAS201 evidence digest as plain
  text, structured JSON, or Slack-safe markdown — all
  deterministic, all bounded to `SIMULATION_ONLY`.
* The surface refuses any digest that is not
  `phase=PAS201`/`allowed_environment=SIMULATION_ONLY`/
  `live_behavior_changed=False`.
* All renderings are free of PII, free of production brokerage
  IDs, free of free-form prose, and free of live-routing
  wording.
* The Slack rendering is API-free: it returns a string, does
  not authenticate to Slack, does not POST anywhere.

## Still not claimable (PAS203+)

* PAS202 does not send a Slack message — even a
  properly-formatted one. An authenticated Slack-posting
  surface belongs to PAS203 or later.
* PAS202 does not validate the digest against live-call
  performance.
* PAS202 does not promote a strategy or route a live call.
* PAS202 does not generate new digest content.

## Future PAS203 path

PAS203 is the next bounded step: an authenticated Slack-posting
surface for the digest, gated by operator confirmation. Expected
shape:

1. A pure adapter that turns the PAS202 Slack rendering into a
   Slack message payload (still no live integration in the test
   suite).
2. A bounded operator command that, with explicit confirmation,
   posts the rendering to a designated read-only channel.
3. A readiness gate asserting the adapter cannot post outside
   the designated channel, cannot include PII, and cannot make
   live-routing claims.
4. Tests asserting the adapter remains structurally
   `SIMULATION_ONLY` and cannot trigger any production behaviour.

PAS203 is **not** PAS202's responsibility. PAS202 ships the
deterministic renderings; PAS203 ships the bounded outbound
surface that operators can opt into.

## Safety constraints (inherited + extended)

PAS202 inherits the full PAS193–PAS201 safety doctrine:

* No real leads, no real phone calls, no Twilio live calls.
* No outbound Slack messages, no Slack imports.
* No worker auto-start, no production brokerage mutation.
* No new SQL migration, no edits to
  `combined_supabase_migration.sql`.
* No secret-shaped tokens in source or in artefacts.
* No PII in renderings — no free-form text fields, no real
  user ids, no email addresses, no phone numbers, no production
  brokerage UUIDs.
* No autonomous-apply identifiers in PAS202 source — readiness
  gate enforces by AST scan.
* No forbidden status literals (`APPROVED`, `APPLIED`,
  `AUTO_APPLIED`, `LIVE`, `DEPLOYED`) in PAS202 source —
  readiness gate enforces by AST string-constant scan.
* No live-routing assertions in any rendering — a defensive
  check raises if a forbidden token would be emitted.
* Slack rendering is API-free: pure string output, hard-capped
  at 4 000 characters.
* Every input digest must carry `phase=PAS201`,
  `allowed_environment=SIMULATION_ONLY`,
  `live_behavior_changed=False`. PAS202 refuses anything else
  at the contract boundary.

## How to run

```
# Compile-check.
python -m compileall -q app/services/simulation scripts/pas202_*.py tests/mvp/test_pas202_evidence_digest_surface.py

# Unit + integration tests.
python -m pytest tests/mvp/test_pas202_evidence_digest_surface.py -q

# Read-only readiness gate.
python scripts/pas202_evidence_digest_surface_readiness_check.py --summary-only

# Render the digest as plain text (default).
python scripts/pas202_view_simulation_evidence_digest.py \
    --digest reports/simulations/pas201_simulation_evidence_digest_<ts>_<id>.json

# Render the structured operator summary as JSON.
python scripts/pas202_view_simulation_evidence_digest.py \
    --digest <path> --json

# Render the Slack-safe markdown (string only; no API call).
python scripts/pas202_view_simulation_evidence_digest.py \
    --digest <path> --slack

# Write the operator summary JSON to reports/simulations/.
python scripts/pas202_view_simulation_evidence_digest.py \
    --digest <path> --write-summary
```

When `--write-summary` is used, operator-summary artefacts land
under `reports/simulations/` with filenames of shape
`pas202_evidence_digest_operator_summary_<utc-timestamp>_<digest_id>.json`.

## Relationship to PAS201

PAS202 is purely additive over PAS201. The PAS202 readiness gate
enforces that every PAS193 through PAS201 carry-forward file
remains on disk and that the PAS202 surface neither imports nor
modifies any of them. The surface service consumes a PAS201
digest's `digest_id`, `strategy_id`, `evidence_strength`,
`operator_summary`, `claimable_now`, `not_claimable_yet`, and
artefact summaries; it produces only string and dict outputs. The
input digest is never mutated.
