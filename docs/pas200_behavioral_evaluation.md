# PAS200 — Deterministic Behavioural Runtime Evaluation

## Purpose

PAS198 ships a bounded simulation-only runtime that records what
happened during a synthetic rehearsal (pass/fail, capability
markers, safety auto-fails). PAS199 ships an inspection surface
that audits the four-artefact lineage. PAS200 takes the next
bounded step: it evaluates **how** the synthetic conversation
behaved — not just whether it passed.

PAS200 reads PAS198 transcripts and (optionally) PAS199
inspections, then emits a structured behavioural-quality
artefact carrying deterministic structural scores for five
behavioural dimensions, closed-vocabulary per-turn annotations,
and closed-vocabulary aggregate flags. The evaluation is strictly
read-only and `SIMULATION_ONLY`. PAS200 never re-executes a
runtime, never promotes a strategy, and never touches production
systems.

PAS200 is the smallest possible behavioural-evaluation layer:

* A pure function (`build_behavioral_evaluation`) that validates
  the runtime against a strict contract and emits a single
  evaluation artefact.
* Five deterministic structural scorers
  (`score_pressure`, `score_pacing`, `score_continuity`,
  `score_trust`, `score_friction`) that derive their values from
  agent-action plan structure, turn ordering, acknowledgement
  patterns, and the PAS198 safety markers — no LLM, no
  embeddings, no learning, no probability.
* A bounded `annotate_turns(entry)` helper that emits
  closed-vocabulary per-turn annotations referencing
  `sequence_id`.
* A CLI that wraps the service.
* A readiness gate that asserts the evaluation can never be
  anything other than `SIMULATION_ONLY`.

PAS200 does **not** select a strategy. PAS200 does **not** route
a live call. PAS200 does **not** deploy anything. PAS200 does
**not** re-execute a runtime. Its only output is an inspectable
JSON file flagged
`phase: "PAS200"`,
`allowed_environment: "SIMULATION_ONLY"`,
`live_behavior_changed: false`.

## What PAS200 proves

* **Deterministic behavioural evaluation exists.** A pure function
  in `app/services/simulation/behavioral_evaluation.py` consumes a
  PAS198 runtime and emits an evaluation artefact whose
  `behavioral_evaluation_id` is a stable SHA-256 hash of
  `runtime_id × inspection_id_or_blank × transcript_hash`. Same
  input runtime produces the same evaluation, including the same
  identifier, every call.
* **The evaluation is environment-bounded by construction.** The
  fields `allowed_environment` and `live_behavior_changed` on
  the evaluation artefact are fixed at `"SIMULATION_ONLY"` and
  `False` by the service. The caller cannot override them. The
  readiness gate's runtime smoke test exercises this on a
  synthetic runtime.
* **Five behavioural dimensions are scored structurally.** All
  five scorers are deterministic functions of agent-action plan
  structure, turn ordering, and safety markers:
  - `pressure_score` (0..1) reflects early-booking, repeated-
    booking, stacked-qualification, and pre-greet escalation
    signals.
  - `pacing_score` (0..1) rewards a `greet`-first opening,
    discovery before commitment, a `close` ending, and the
    absence of stacked qualification.
  - `continuity_score` (0..1) measures (agent, lead) pairing
    density and penalises in-conversation `greet` resets.
  - `trust_score` (0..1) rewards `greet`-first openings,
    acknowledgement before qualification, and a trust-preserving
    action ratio. It is penalised by any active safety marker.
  - `friction_score` (0..1) responds to safety markers, repeated
    objection-handling, stacked qualification, and
    pressure-immediately-followed-by-disengagement sequences.
* **Per-turn annotations are closed-vocabulary and deterministic.**
  `annotate_turns(entry)` returns records of
  `{scenario_id, sequence_id, actor, agent_action, annotations[]}`,
  with each annotation drawn from `TURN_ANNOTATIONS`:
  `EARLY_ESCALATION`, `STACKED_QUALIFICATION`, `CONTEXT_RESET`,
  `ACKNOWLEDGMENT_PRESENT`, `CALLBACK_CONTINUITY`,
  `HIGH_PRESSURE_SEQUENCE`, `SOFT_DISCOVERY`,
  `TRUST_PRESERVING_LANGUAGE`, `HESITATION_AFTER_PUSH`,
  `NATURAL_TRANSITION`. No free-form text. No probabilistic
  weighting.
* **Aggregate behavioural flags are closed-vocabulary.**
  `behavioral_flags` are drawn from `BEHAVIORAL_FLAGS` and surface
  composite findings such as `high_pressure_strategy`,
  `low_trust_strategy`, `good_pacing_observed`,
  `early_escalation_observed`, `callback_continuity_observed`,
  `high_friction_observed`, `low_friction_observed`, and so on.
* **Artefact integrity is recorded as boolean checks.** Nine
  integrity booleans confirm the runtime status, environment,
  bundle non-emptiness, scenario coverage, sequence-id
  referential consistency, score bounds, and closed-vocabulary
  compliance of annotations and flags.
* **PAS199 inspection cross-reference is optional but strict.**
  If an inspection is supplied, the evaluation validates that
  `inspection.lineage_summary.runtime_id == runtime.runtime_id`
  and that the inspection itself is `SIMULATION_ONLY` and
  `live_behavior_changed=False`. Mismatches raise
  `BehavioralEvaluationValidationError`.
* **Forbidden status literals are absent.** The strings
  `APPROVED`, `APPLIED`, `AUTO_APPLIED`, `LIVE`, and `DEPLOYED`
  never appear as string constants in PAS200 source. The
  readiness gate enforces this by AST string-constant scan.
* **Forbidden live-mutation identifiers are absent.**
  `apply_recommendation`, `deploy_strategy`,
  `switch_strategy_live`, `auto_apply`, `auto_promote`,
  `force_promote`, `live_apply`, `auto_deploy`,
  `route_lead_live`, `route_call_live`, `send_real_sms`, and
  `send_real_call` are all absent from PAS200 source. The
  readiness gate enforces this by AST identifier scan.
* **No external service imports.** PAS200 source imports nothing
  from `twilio`, `slack_sdk`, `openai`, `anthropic`, `dotenv`,
  `supabase`, or `app.engine.state_machine`.

## What PAS200 does not prove

PAS200 ships behavioural evaluation. It does not ship anything
that interprets, promotes, or optimises behaviour based on the
evaluation. The following remain out of scope:

* **PAS200 does not optimise conversations.** Scores are read,
  not acted on. No part of PAS200 modifies a strategy plan.
* **PAS200 does not retrain or auto-promote strategies.** A
  high `trust_score` does not cause PAS to use a strategy on
  any real call.
* **PAS200 does not score live brokerages.** Every score is
  derived from synthetic PAS193 catalogue conversations.
* **PAS200 does not infer psychology using LLMs.** All scoring
  is deterministic and structural. The evaluation refuses
  probabilistic or model-derived signals.
* **PAS200 does not validate real-world success.** Calibration
  of behavioural scores against live-call outcomes belongs to
  PAS201+.
* **PAS200 does not replace human review.** The evaluation is
  inspectable evidence, not an action.
* **PAS200 does not modify PAS execution behaviour.** PAS198 and
  PAS199 artefacts are read; never mutated.

## Claimable today (with PAS200 merged)

* An operator can run PAS200 against any PAS198 runtime artefact
  and inspect a bounded, hash-identified behavioural evaluation
  carrying five structural scores, per-turn annotations, and
  aggregate flags — all drawn from closed vocabularies.
* The evaluation refuses any runtime that is not `EXECUTED`,
  `SIMULATION_ONLY`, and `live_behavior_changed=False`.
* The evaluation refuses any PAS199 inspection whose
  `lineage_summary.runtime_id` does not match the input runtime.
* Per-turn annotations reference real `sequence_id` values from
  the input runtime — integrity is asserted by the evaluation
  itself and re-checked by every test run.
* Evaluation outputs are deterministic and hash-identified for
  audit; the same runtime always yields the same
  `behavioral_evaluation_id`.
* The evaluation carries no PII, no production brokerage IDs,
  no free-form operator text.
* Safety violations recorded by PAS198 propagate into PAS200 as
  reduced `trust_score` and elevated `friction_score` — they are
  never silently dropped.

## Still not claimable (PAS201+)

* PAS validates behavioural scores against live-call performance
  (calibration). (PAS201+.)
* The PAS engine consumes a behavioural evaluation to choose a
  strategy per lead. (Later phase, gated on calibration
  evidence.)
* Operators trigger evaluations from Slack. (Later phase.)
* Behavioural scores are turned into automated alerts on live
  conversations. (Outside PAS200's scope by construction.)

## Future PAS201 path

PAS201 is the next bounded step: a calibration layer that ties
PAS200 behavioural scores to whatever live-call evidence the PAS
engine already records. Expected shape:

1. A read-only ingestion of historical live-call outcomes,
   strictly bounded to whatever the engine already records (no
   new PII surfaces, no new schemas).
2. A pure comparator that maps PAS200 behavioural scores per
   strategy to live-call outcome distributions for matching
   lead segments.
3. A calibration report under `reports/simulations/` that
   records, per strategy and per behavioural dimension, how
   well synthetic structural scoring predicted live outcomes —
   without ever causing the engine to switch strategy.
4. A PAS201 readiness gate asserting the calibration layer
   cannot bypass the PAS200 contract (no LLM-based scoring, no
   Slack imports, no Twilio imports, no migrations).

PAS201 is **not** PAS200's responsibility. PAS200 ships the
deterministic structural scoring; PAS201 ships the calibration
that contextualises it.

## Safety constraints (inherited + extended)

PAS200 inherits the full PAS193–PAS199 safety doctrine:

* No real leads, no real phone calls, no Twilio live calls.
* No Slack messages, no Slack imports.
* No worker auto-start, no production brokerage mutation.
* No new SQL migration, no edits to
  `combined_supabase_migration.sql`.
* No secret-shaped tokens in source or in artefacts.
* No PII in evaluation artefacts — no free-form text fields, no
  real user ids, no email addresses, no phone numbers.
* No autonomous-apply identifiers in PAS200 source — readiness
  gate enforces by AST scan.
* No forbidden status literals (`APPROVED`, `APPLIED`,
  `AUTO_APPLIED`, `LIVE`, `DEPLOYED`) in PAS200 source —
  readiness gate enforces by AST string-constant scan.
* Every evaluation artefact carries `phase: "PAS200"`,
  `allowed_environment: "SIMULATION_ONLY"`, and
  `live_behavior_changed: False`.
* All scores live in `[0.0, 1.0]`.
* Per-turn annotations drawn from the closed `TURN_ANNOTATIONS`
  vocabulary.
* Aggregate flags drawn from the closed `BEHAVIORAL_FLAGS`
  vocabulary.
* Actor labels drawn from `{agent, lead}` (PAS198 vocabulary).
* No LLM, no embeddings, no vector DB, no external vendor calls,
  no probabilistic grading.

## How to run

```
# Compile-check.
python -m compileall -q app/services/simulation scripts/pas200_*.py tests/mvp/test_pas200_behavioral_evaluation.py

# Unit + integration tests.
python -m pytest tests/mvp/test_pas200_behavioral_evaluation.py -q

# Read-only readiness gate.
python scripts/pas200_behavioral_evaluation_readiness_check.py --summary-only

# Evaluate a PAS198 runtime (PAS199 inspection optional).
python scripts/pas200_evaluate_runtime_behavior.py \
    --runtime reports/simulations/pas198_manual_test_runtime_<ts>_<id>.json

python scripts/pas200_evaluate_runtime_behavior.py \
    --runtime    reports/simulations/pas198_manual_test_runtime_<ts>_<id>.json \
    --inspection reports/simulations/pas199_runtime_inspection_<ts>_<id>.json
```

Evaluation artefacts land under `reports/simulations/` with
filenames of shape
`pas200_behavioral_evaluation_<utc-timestamp>_<behavioral_evaluation_id>.json`.

## Relationship to PAS198 / PAS199

PAS200 is purely additive over PAS199. The PAS200 readiness gate
enforces that every PAS193, PAS194, PAS195, PAS196, PAS197,
PAS198, and PAS199 carry-forward file remains on disk and that
the PAS200 surface neither imports nor modifies any of them. The
evaluation service consumes a PAS198 runtime artefact's
`runtime_id`, `transcript_bundle`, and contract fields; if a
PAS199 inspection is supplied, the service also cross-references
`inspection.lineage_summary.runtime_id`. PAS200 produces a new
artefact that references the source `runtime_id` and (optionally)
`inspection_id` — neither input is ever mutated.

A PAS198 runtime, a PAS199 inspection, and a PAS200 behavioural
evaluation never change in place. Each PAS200 evaluation is a
distinct, hash-identified, immutable artefact that asserts the
behavioural quality of the source runtime at the time the
evaluation was generated.
