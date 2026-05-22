# PAS198 — Bounded Manual-Test Runtime

## Purpose

PAS197 ships a structured **manual-test package** that asserts an
operator-approved (recommendation, review) pair is ready for
manual inspection. PAS198 takes the next bounded step: it
**executes** the package's recommended strategy against the closed
PAS193 scenario catalogue inside a strictly `SIMULATION_ONLY`
runtime, and emits an inspectable runtime artefact carrying a
transcript bundle, runtime evaluation, capability summary, and
safety outcome.

PAS198 is the smallest possible execution layer:

* A pure function (`execute_manual_test_runtime`) that validates
  the package against a strict contract.
* A bounded output carrying closed-vocabulary execution status,
  safety outcome, capability markers, and safety markers — and
  nothing else free-form.
* A CLI that wraps the function and writes the runtime artefact
  to `reports/simulations/`.
* A readiness gate that asserts the runtime can never be anything
  other than `SIMULATION_ONLY`.

PAS198 does **not** select a strategy at runtime for live calls.
PAS198 does **not** route a live call. PAS198 does **not** deploy
anything. Its only output is an inspectable JSON file flagged
`status: "EXECUTED"`,
`allowed_environment: "SIMULATION_ONLY"`,
`live_behavior_changed: false`.

## What PAS198 proves

* **A bounded runtime consumes a PAS197 package.** A pure
  function in `app/services/simulation/manual_test_runtime.py`
  consumes a `READY_FOR_MANUAL_TEST` / `SIMULATION_ONLY`
  package, validates it, and emits a single runtime artefact.
  Any contract violation raises
  `ManualTestRuntimeValidationError` and the CLI exits 2.
* **The contract chains correctly.** The runtime requires
  `package.status == "READY_FOR_MANUAL_TEST"`,
  `package.allowed_environment == "SIMULATION_ONLY"`,
  `package.live_behavior_changed is False`,
  `package.package_id` non-empty, and
  `package.strategy_id` non-empty and drawn from the
  PAS194 `STRATEGY_IDS` catalogue. Mismatches at any joint are
  refused.
* **The runtime is environment-bounded by construction.** The
  fields `allowed_environment` and `live_behavior_changed` on
  the runtime artefact are fixed at `"SIMULATION_ONLY"` and
  `False` respectively by the service. The caller cannot
  override them. The readiness gate's runtime smoke test
  exercises this on a synthetic package.
* **The runtime reuses PAS193 / PAS194 with no relaxation.**
  Transcripts are built by PAS194's `run_scenario_under_strategy`
  using the package's `strategy_id` against the PAS193 closed
  scenario catalogue. Scoring is PAS193's `score_conversation`
  unchanged. Safety auto-fails remain absolute: if any scenario
  trips a safety auto-fail the runtime halts at that scenario and
  carries `execution_status = "halted_on_safety"`.
* **The transcript bundle is structured.** Each entry carries
  `scenario_id`, `scenario_type`, `supported`, `turns`,
  conversation-level `capability_markers`, and conversation-level
  `safety_markers`. Each turn carries `sequence_id`, `actor`
  (drawn from the closed `{agent, lead}` vocabulary),
  `agent_action`, `text`, per-turn `capability_markers`, and
  per-turn `safety_markers`. Sequence IDs are deterministic
  integers starting at 1.
* **Runtime evaluation is deterministic.** Per scenario, the
  evaluation records `qualification_captured`, `objection_handled`,
  `callback_captured`, `booking_attempted`,
  `unsafe_output_detected`, `hallucinated_policy_detected`,
  `pii_leak_detected`, `transcript_integrity_valid`, plus
  `score`, `passed`, and `failure_reasons`. Aggregate
  `runtime_score` (`pass_rate`, `average_score`) and
  `capability_summary` (rates for the four capabilities) are
  computed from the per-scenario rows. Same inputs → same numbers
  every call.
* **`runtime_id` is deterministic.** `runtime_id` is a stable
  SHA-256-derived hash of (`package_id`, `executed_strategy`,
  `executed_scenarios`). The same package executed against the
  same catalogue produces the same `runtime_id` every call.
* **Forbidden status literals are absent.** The strings
  `APPROVED`, `APPLIED`, `AUTO_APPLIED`, `LIVE`, and `DEPLOYED`
  never appear as string constants in PAS198 source. The
  readiness gate enforces this by AST string-constant scan.
  `READY_FOR_MANUAL_TEST` and `EXECUTED` (distinct values) are
  unaffected.
* **Forbidden live-mutation identifiers are absent.**
  `apply_recommendation`, `deploy_strategy`,
  `switch_strategy_live`, `auto_apply`, `auto_promote`,
  `force_promote`, `live_apply`, `auto_deploy`,
  `route_lead_live`, `route_call_live`, `send_real_sms`, and
  `send_real_call` are all absent from PAS198 source. The
  readiness gate enforces this by AST identifier scan.
* **No external service imports.** PAS198 source imports nothing
  from `twilio`, `slack_sdk`, `openai`, `anthropic`, `dotenv`,
  `supabase`, or `app.engine.state_machine`. The readiness gate
  enforces this by AST import scan.

## What PAS198 does not prove

PAS198 ships the runtime. It does not ship anything that consumes
the runtime artefact at production scale. The following remain
out of scope:

* **The runtime does not route a live call.** Executing a PAS198
  runtime against `callback_first` does not cause PAS to use
  `callback_first` on any real lead. The production engine
  continues to use its default strategy until a later phase
  explicitly broadens scope.
* **There is no Slack surface for runtime invocation.** Operators
  invoke the runtime via CLI and inspect the runtime JSON file
  directly. A Slack command surface mirroring PAS196's review
  shape will be added in PAS199 or later.
* **There is no calibration loop.** Runtime outcomes in
  simulation are not yet shown to predict live-call outcomes.
  Calibration belongs to PAS200+.
* **The runtime does not select a strategy per lead.** Strategy
  selection by lead profile belongs to a later phase, gated on
  the manual-test runtime and on calibration evidence.

## Claimable today (with PAS198 merged)

* PAS can execute an operator-approved strategy against a closed,
  deterministic synthetic catalogue and emit a bounded inspectable
  runtime artefact.
* Runtime artefacts are structurally bounded to `SIMULATION_ONLY`
  and carry `live_behavior_changed: False`.
* Runtime artefacts carry no PII and no free-form operator text;
  every descriptive field is drawn from a closed vocabulary.
* Safety auto-fails halt the manual test, are surfaced in
  `safety_outcome`, and prevent quiet promotion: the runtime
  cannot ship a "looked fine on the surface" verdict while a
  safety violation fired underneath.
* Runtime artefacts are deterministic and hash-identified for
  audit; the same package always yields the same `runtime_id`.
* PAS197 packages that are rejected, expired, or
  `live_behavior_changed: true` are refused at the runtime
  boundary.

## Still not claimable (PAS199+)

* Operators trigger the manual-test runtime from a Slack command
  and review the runtime artefact in Slack. (PAS199.)
* Runtime outcomes are validated against live-call performance.
  (PAS200+.)
* The PAS engine selects a strategy per lead based on
  runtime + calibration evidence. (Later phase.)

## Future PAS199 path

PAS199 is the next bounded step: a Slack operator surface for
PAS198 runs, mirroring the PAS196 review pattern. Expected
shape:

1. A Slack command that surfaces eligible PAS197 packages and
   accepts an operator action (`run_manual_test`) bound to a
   package id.
2. A bounded action handler that invokes the PAS198 runtime in
   the same `SIMULATION_ONLY` mode the CLI uses today and
   posts a structured summary back to Slack.
3. A persistence layer that records the runtime invocation
   (operator actor token, package id, runtime id) without
   mutating any production brokerage row.
4. A PAS199 readiness gate asserting the Slack handler cannot
   bypass the PAS198 contract (no `force_run`, no
   `auto_promote`, no live-routing identifiers).

PAS199 is **not** PAS198's responsibility. PAS198 ships the
runtime that consumes the package; PAS199 ships the operator
surface that triggers it.

## Safety constraints (inherited + extended)

PAS198 inherits the full PAS193–PAS197 safety doctrine:

* No real leads, no real phone calls, no Twilio live calls.
* No Slack messages, no Slack imports.
* No worker auto-start, no production brokerage mutation.
* No new SQL migration, no edits to
  `combined_supabase_migration.sql`.
* No secret-shaped tokens in source or in artefacts.
* No PII in runtime artefacts — no free-form text fields, no real
  user ids, no email addresses, no phone numbers; transcripts are
  the canned PAS193 adapter lines only.
* No autonomous-apply identifiers in PAS198 source — readiness
  gate enforces by AST scan.
* No forbidden status literals (`APPROVED`, `APPLIED`,
  `AUTO_APPLIED`, `LIVE`, `DEPLOYED`) in PAS198 source —
  readiness gate enforces by AST string-constant scan.
* Every runtime artefact carries `status: "EXECUTED"`,
  `allowed_environment: "SIMULATION_ONLY"`, and
  `live_behavior_changed: False`.
* `execution_status` is drawn from the closed vocabulary
  `{completed, halted_on_safety, halted_on_empty_transcript}`.
* `safety_outcome.outcome` is drawn from the closed vocabulary
  `{clean, auto_fail}`.
* `actor` is drawn from the closed vocabulary `{agent, lead}`.
* `capability_markers` and `safety_markers` are drawn from
  closed vocabularies declared in `manual_test_runtime.py`.

## How to run

```
# Compile-check.
python -m compileall -q app/services/simulation scripts/pas198_*.py tests/mvp/test_pas198_manual_test_runtime.py

# Unit + integration tests.
python -m pytest tests/mvp/test_pas198_manual_test_runtime.py -q

# Read-only readiness gate.
python scripts/pas198_manual_test_runtime_readiness_check.py --summary-only

# Execute a PAS197 manual-test package in the bounded runtime.
python scripts/pas198_run_manual_test_runtime.py \
    --package reports/simulations/pas197_manual_test_package_<ts>_<id>.json

# Stdout summary only; no JSON written.
python scripts/pas198_run_manual_test_runtime.py \
    --package <path> --summary-only
```

Runtime artefacts land under `reports/simulations/` with filenames
of shape
`pas198_manual_test_runtime_<utc-timestamp>_<runtime_id>.json`.

## Relationship to PAS197

PAS198 is purely additive over PAS197. The PAS198 readiness gate
enforces that every PAS193, PAS194, PAS195, PAS196, and PAS197
carry-forward file remains on disk and that the PAS198 surface
neither imports nor modifies any of them. The runtime service
consumes a PAS197 package's `package_id`, `status`,
`allowed_environment`, `live_behavior_changed`, and `strategy_id`.
It emits a new artefact that references the source `package_id`.

A PAS197 package and a PAS198 runtime artefact never change in
place. Each PAS198 runtime is a distinct, hash-identified,
immutable artefact that asserts a bounded synthetic rehearsal of
the package's recommended strategy was executed at the time the
runtime was generated.
