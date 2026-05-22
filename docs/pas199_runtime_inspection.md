# PAS199 — Operational Runtime Inspection Surface

## Purpose

PAS198 ships a bounded simulation-only runtime that consumes a
PAS197 manual-test package and produces a structured runtime
artefact. PAS199 takes the next bounded step: it makes the full
PAS lineage —

    PAS195 recommendation
        -> PAS196 review
            -> PAS197 package
                -> PAS198 runtime

— **operationally inspectable and auditable** as a single,
bounded JSON artefact. The inspection is strictly read-only. It
never executes a strategy, never re-runs a simulation, never
mutates anything.

PAS199 is the smallest possible inspection layer:

* A pure function (`build_inspection`) that validates every join
  in the four-artefact lineage and emits a single structured
  inspection artefact.
* A bounded read-only `replay_transcript(runtime, scenario_id)`
  helper that re-projects a PAS198 transcript by sequence id,
  actor, capability marker, and safety marker.
* A pure `compare_runtimes(runtime_a, runtime_b)` helper that
  produces a deterministic delta (score, capability, safety,
  transcript size, flipped scenarios).
* A CLI that wraps all three and writes the inspection artefact
  to `reports/simulations/`.
* A readiness gate that asserts the inspection can never be
  anything other than `SIMULATION_ONLY`.

PAS199 does **not** select a strategy at runtime. PAS199 does
**not** route a live call. PAS199 does **not** deploy anything.
PAS199 does **not** re-execute a runtime — it reads what PAS198
already produced. Its only output is an inspectable JSON file
flagged
`phase: "PAS199"`,
`allowed_environment: "SIMULATION_ONLY"`,
`live_behavior_changed: false`.

## What PAS199 proves

* **The four-artefact lineage is verifiable end-to-end.** A pure
  function in `app/services/simulation/runtime_inspection.py`
  consumes a PAS195 recommendation, PAS196 review, PAS197
  package, and PAS198 runtime, validates every join, and emits a
  single inspection artefact. Any contract violation raises
  `RuntimeInspectionValidationError` and the CLI exits 2.
* **The lineage contract chains correctly.** The inspection
  requires
  `review.recommendation_id == recommendation.recommendation_id`,
  `package.recommendation_id == recommendation.recommendation_id`,
  `package.review_id == review.review_id`,
  `package.strategy_id == recommendation.recommended_strategy`,
  `runtime.package_id == package.package_id`, and
  `runtime.executed_strategy == package.strategy_id`. A break at
  any joint is refused at construction time. The
  `artifact_integrity` block of the output records every join
  check as a boolean for audit.
* **The inspection is environment-bounded by construction.** The
  fields `allowed_environment` and `live_behavior_changed` on
  the inspection artefact are fixed at `"SIMULATION_ONLY"` and
  `False` by the service. The caller cannot override them.
* **Transcript replay is read-only and deterministic.**
  `replay_transcript(runtime, scenario_id)` returns a bounded
  record of `sequence_ids`, `actors`, per-turn
  `capability_markers`, and per-turn `safety_markers`. It never
  executes anything; it only re-projects what PAS198 already
  recorded. Same runtime + same `scenario_id` produce the same
  replay every call. Unknown `scenario_id` raises.
* **Runtime comparison is deterministic.**
  `compare_runtimes(runtime_a, runtime_b)` produces a bounded
  delta: `pass_rate_delta`, `average_score_delta`, per-capability
  rate deltas, safety auto-fail count delta + outcome change
  flag, transcript size deltas, and the sorted list of scenarios
  whose `passed` flag flipped between A and B. The function
  refuses non-`EXECUTED` or non-`SIMULATION_ONLY` runtimes on
  either side.
* **`inspection_id` is deterministic.** `inspection_id` is a
  stable SHA-256-derived hash of `(recommendation_id, review_id,
  package_id, runtime_id, compared_runtime_id_or_blank)`. Same
  lineage produces the same `inspection_id` every call.
* **The inspection artefact carries no free-form text.** Every
  field is either a structural value (id, integer count, float
  rate), a closed-vocabulary token (actor / capability marker /
  safety marker / execution status / safety outcome), or a list
  of those. There is no `notes`, `comment`, `operator_notes`, or
  `free_text` field on the inspection.
* **Forbidden status literals are absent.** The strings
  `APPROVED`, `APPLIED`, `AUTO_APPLIED`, `LIVE`, and `DEPLOYED`
  never appear as string constants in PAS199 source. The
  readiness gate enforces this by AST string-constant scan.
  Distinct values like `READY_FOR_MANUAL_TEST`,
  `APPROVED_FOR_MANUAL_TEST`, and `EXECUTED` are unaffected.
* **Forbidden live-mutation identifiers are absent.**
  `apply_recommendation`, `deploy_strategy`,
  `switch_strategy_live`, `auto_apply`, `auto_promote`,
  `force_promote`, `live_apply`, `auto_deploy`,
  `route_lead_live`, `route_call_live`, `send_real_sms`, and
  `send_real_call` are all absent from PAS199 source. The
  readiness gate enforces this by AST identifier scan.
* **No external service imports.** PAS199 source imports nothing
  from `twilio`, `slack_sdk`, `openai`, `anthropic`, `dotenv`,
  `supabase`, or `app.engine.state_machine`. The readiness gate
  enforces this by AST import scan.

## What PAS199 does not prove

PAS199 ships the inspection surface. It does not ship anything
that triggers, executes, or promotes runtimes based on the
inspection. The following remain out of scope:

* **The inspection does not run a manual test.** PAS199 reads
  what PAS198 already executed. It cannot re-execute a strategy
  and it cannot generate a new transcript.
* **The inspection does not route a live call.** No part of
  PAS199 touches the production engine, Twilio, Supabase, or
  Slack.
* **The inspection does not auto-promote a strategy.** An
  inspection that records `safety_outcome.outcome == "clean"` and
  `pass_rate == 1.0` does not cause PAS to use that strategy on
  any real call. Promotion of a strategy to production runtime
  remains a later phase, gated on calibration evidence.
* **The inspection does not validate runtime outcomes against
  live-call performance.** Calibration belongs to PAS200+.

## Claimable today (with PAS199 merged)

* An operator can join a PAS195 recommendation, PAS196 review,
  PAS197 package, and PAS198 runtime into a single bounded,
  hash-identified inspection artefact for audit.
* The inspection refuses broken lineages: any mismatch in the
  recommendation / review / package / runtime joins is surfaced
  as a validation error, not silently glossed over.
* An operator can replay any PAS198 transcript by `scenario_id`
  and inspect the deterministic sequence of agent / lead turns,
  capability markers, and safety markers.
* An operator can diff two PAS198 runtimes and see the delta in
  pass rate, average score, per-capability rate, safety auto-fail
  count, transcript size, and the per-scenario `passed`-flag
  flips.
* The inspection artefact is bounded to `SIMULATION_ONLY` and
  carries `live_behavior_changed: false` by construction.
* The inspection carries no PII, no production brokerage IDs,
  and no free-form operator text.

## Still not claimable (PAS200+)

* PAS validates runtime outcomes against live-call performance
  (calibration). (PAS200+.)
* PAS routes a real lead to a manually-tested strategy. (Later
  phase, gated on calibration evidence.)
* Operators trigger or promote runtimes from Slack. (Later
  operator-surface phase.)

## Future PAS200 path

PAS200 is the next bounded step: a calibration layer that ties
PAS198 simulation outcomes to whatever live-call evidence the
PAS engine carries. Expected shape:

1. A read-only ingestion of historical live-call outcomes,
   strictly bounded to whatever the engine already records (no
   new PII surfaces, no new schemas).
2. A pure comparator that maps PAS199 inspection summaries to
   the matching live-call population segments.
3. A calibration report under `reports/simulations/` that
   records, per strategy, how well simulation evaluation
   predicted live outcomes — without ever causing the engine
   to switch strategy.
4. A PAS200 readiness gate asserting the calibration layer
   cannot bypass the PAS199 contract (no live-mutation
   identifiers, no Slack imports, no Twilio imports, no
   migrations).

PAS200 is **not** PAS199's responsibility. PAS199 ships the
inspection surface; PAS200 ships the calibration that
contextualises it.

## Safety constraints (inherited + extended)

PAS199 inherits the full PAS193–PAS198 safety doctrine:

* No real leads, no real phone calls, no Twilio live calls.
* No Slack messages, no Slack imports.
* No worker auto-start, no production brokerage mutation.
* No new SQL migration, no edits to
  `combined_supabase_migration.sql`.
* No secret-shaped tokens in source or in artefacts.
* No PII in inspection artefacts — no free-form text fields, no
  real user ids, no email addresses, no phone numbers.
* No autonomous-apply identifiers in PAS199 source — readiness
  gate enforces by AST scan.
* No forbidden status literals (`APPROVED`, `APPLIED`,
  `AUTO_APPLIED`, `LIVE`, `DEPLOYED`) in PAS199 source —
  readiness gate enforces by AST string-constant scan.
* Every inspection artefact carries `phase: "PAS199"`,
  `allowed_environment: "SIMULATION_ONLY"`, and
  `live_behavior_changed: False`.
* Replay actors drawn from `{agent, lead}`.
* Replay capability markers drawn from
  `{qualification_captured, appointment_attempted,
    callback_captured, objection_handled, conversation_completed}`.
* Replay safety markers drawn from the closed PAS198 safety
  vocabulary.

## How to run

```
# Compile-check.
python -m compileall -q app/services/simulation scripts/pas199_*.py tests/mvp/test_pas199_runtime_inspection.py

# Unit + integration tests.
python -m pytest tests/mvp/test_pas199_runtime_inspection.py -q

# Read-only readiness gate.
python scripts/pas199_runtime_inspection_readiness_check.py --summary-only

# Inspect a complete lineage (PAS195 -> PAS196 -> PAS197 -> PAS198).
python scripts/pas199_inspect_runtime_lineage.py \
    --recommendation reports/simulations/pas195_recommendation_<ts>_<id>.json \
    --review         reports/simulations/pas196_recommendation_review_<ts>_<id>.json \
    --package        reports/simulations/pas197_manual_test_package_<ts>_<id>.json \
    --runtime        reports/simulations/pas198_manual_test_runtime_<ts>_<id>.json

# Inspect a lineage AND diff against a second PAS198 runtime.
python scripts/pas199_inspect_runtime_lineage.py \
    --recommendation <path> --review <path> \
    --package <path> --runtime <path> \
    --compare-runtime reports/simulations/pas198_manual_test_runtime_<ts>_<id>.json
```

Inspection artefacts land under `reports/simulations/` with
filenames of shape
`pas199_runtime_inspection_<utc-timestamp>_<inspection_id>.json`.

## Relationship to PAS198

PAS199 is purely additive over PAS198. The PAS199 readiness gate
enforces that every PAS193, PAS194, PAS195, PAS196, PAS197, and
PAS198 carry-forward file remains on disk and that the PAS199
surface neither imports nor modifies any of them. The inspection
service consumes only the four input artefacts; it does not
re-run anything in the simulation engine.

A PAS198 runtime and a PAS199 inspection artefact never change in
place. Each PAS199 inspection is a distinct, hash-identified,
immutable artefact that asserts the four-artefact lineage was
consistent at the time the inspection was generated.
