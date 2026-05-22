# PAS201 — Simulation Evidence Digest

## Purpose

PAS193–PAS200 each ship one bounded artefact in the simulation
chain:

* PAS195 — strategy recommendation
* PAS196 — operator review of that recommendation
* PAS197 — manual-test package
* PAS198 — bounded manual-test runtime
* PAS199 — lineage inspection
* PAS200 — deterministic behavioural evaluation

PAS201 takes the next bounded step: it **joins** all six into a
single operator-readable digest with a deterministic
evidence-strength rating. The digest is the artefact an operator
hands to a demo audience, an investor, or a teammate to make the
case "this strategy survived our offline rehearsal — here's the
chain". The digest is strictly read-only and `SIMULATION_ONLY`.
PAS201 never re-executes a runtime, re-runs an inspection,
promotes a strategy, or touches production.

PAS201 is the smallest possible operator-facing digest layer:

* A pure function (`build_evidence_digest`) that validates every
  join in the six-artefact lineage and emits a single bounded
  digest.
* A deterministic four-valued evidence-strength scorer
  (`strong` / `moderate` / `weak` / `blocked`).
* Closed-vocabulary `operator_summary` (highlights +
  recommended_next_action), `claimable_now`, and
  `not_claimable_yet`.
* A CLI that wraps the service.
* A readiness gate that asserts the digest can never be anything
  other than `SIMULATION_ONLY`.

PAS201 does **not** select a strategy. PAS201 does **not** route a
live call. PAS201 does **not** deploy anything. PAS201 does
**not** generate any new evidence — it consumes what PAS193–PAS200
already produced. Its only output is an inspectable JSON file
flagged
`phase: "PAS201"`,
`allowed_environment: "SIMULATION_ONLY"`,
`live_behavior_changed: false`.

## What PAS201 proves

* **The six-artefact lineage joins cleanly.** A pure function in
  `app/services/simulation/evidence_digest.py` validates every
  join — `review.recommendation_id == recommendation.recommendation_id`,
  `package.recommendation_id / review_id / strategy_id` match
  recommendation+review, `runtime.package_id / executed_strategy`
  match package, `inspection.lineage_summary.{recommendation_id,
  review_id, package_id, runtime_id, strategy_id}` match the
  upstream artefacts, and `behavioral_evaluation.runtime_id +
  inspection_id` match runtime and inspection. Any mismatch
  raises `EvidenceDigestValidationError` and the CLI exits 2.
* **The digest is environment-bounded by construction.** The
  fields `allowed_environment` and `live_behavior_changed` on the
  digest are fixed at `"SIMULATION_ONLY"` and `False` by the
  service. The caller cannot override them.
* **Evidence strength is deterministic.** `evidence_strength` is
  drawn from `{strong, moderate, weak, blocked}` by closed rule:
  - `blocked` if the runtime's safety outcome is not `clean`,
    if the inspection's lineage is broken, if either the
    inspection's or the behavioural evaluation's artefact
    integrity has any False entry, if the digest's own
    artefact-integrity block has any False entry, or if any
    artefact in the chain carries `live_behavior_changed=True`.
  - `strong` if `runtime.runtime_score.pass_rate >= 0.95`
    (and not blocked).
  - `moderate` if `runtime.runtime_score.pass_rate >= 0.75`
    (and not blocked).
  - `weak` otherwise (and not blocked).
* **Operator summary is closed-vocabulary.**
  `operator_summary.highlights` is drawn from
  `OPERATOR_HIGHLIGHTS` (19 tokens — pass-rate band, safety
  outcome, lineage status, artefact-integrity status, behavioural
  flag echoes, no-live-behavior-change confirmation).
  `operator_summary.recommended_next_action` is drawn from
  `OPERATOR_NEXT_ACTIONS` (4 tokens, one per evidence-strength
  value). No free-form text.
* **`claimable_now` and `not_claimable_yet` are bounded.** Both
  lists are drawn from closed vocabularies (8 and 5 tokens
  respectively). `claimable_now` lists only what the chain
  actually supports — strong chains earn the
  `synthetic_rehearsal_passed_for_strategy` token; blocked chains
  are restricted to the safety-orthogonal subset
  (`no_live_behavior_changed`, `no_pii_in_simulation_artifacts`).
  `not_claimable_yet` always lists the structural gaps that
  remain — live call routing, calibration against live outcomes,
  automated promotion, real lead exposure, Slack runtime
  surface.
* **`digest_id` is deterministic.** `digest_id` is a stable
  SHA-256 hash of `(recommendation_id, review_id, package_id,
  runtime_id, inspection_id, behavioral_evaluation_id)`. Same
  six-artefact chain produces the same `digest_id` every call.
* **The digest carries no free-form text.** Every field is
  either a structural value (id, integer count, float rate), a
  closed-vocabulary token, or a list of those. There is no
  `notes`, `comment`, `headline`, `operator_notes`, or
  `free_text` field on the digest.
* **Forbidden status literals are absent.** The strings
  `APPROVED`, `APPLIED`, `AUTO_APPLIED`, `LIVE`, `DEPLOYED`
  never appear as string constants in PAS201 source. The
  readiness gate enforces this by AST string-constant scan.
* **Forbidden live-mutation identifiers are absent.** Twelve
  identifier names — `apply_recommendation`, `deploy_strategy`,
  `switch_strategy_live`, `auto_apply`, `auto_promote`,
  `force_promote`, `live_apply`, `auto_deploy`,
  `route_lead_live`, `route_call_live`, `send_real_sms`,
  `send_real_call` — are all absent from PAS201 source. The
  readiness gate enforces this by AST identifier scan.
* **No external service imports.** PAS201 source imports nothing
  from `twilio`, `slack_sdk`, `openai`, `anthropic`, `dotenv`,
  `supabase`, or `app.engine.state_machine`.

## What PAS201 does not prove

The digest summarises evidence; it does not generate evidence and
it does not act on it. The following remain out of scope:

* **The digest does not run a manual test.** PAS201 reads
  what PAS198 already executed. It cannot re-execute a strategy
  and it cannot generate a new transcript.
* **The digest does not route a live call.** No part of PAS201
  touches the production engine, Twilio, Supabase, or Slack.
* **The digest does not promote a strategy.** A `strong` digest
  is operator-readable evidence, not an automated action.
* **The digest does not validate against live-call performance.**
  Calibration belongs to PAS202+.
* **The digest does not replace human review.** It is an
  artefact for human consumption; the decision-of-record is
  still the operator's.
* **The digest does not modify any upstream artefact.** PAS195–
  PAS200 artefacts are read, never mutated.

## How to use the digest

### In a demo

1. Run the simulation chain end-to-end on the strategy you want
   to demo (PAS193 → PAS194 → PAS195 → PAS196 → PAS197 → PAS198 →
   PAS199 → PAS200). All six artefacts land under
   `reports/simulations/`.
2. Build the digest:
   ```
   python scripts/pas201_build_simulation_evidence_digest.py \
       --recommendation        reports/simulations/pas195_recommendation_<ts>_<id>.json \
       --review                reports/simulations/pas196_recommendation_review_<ts>_<id>.json \
       --package               reports/simulations/pas197_manual_test_package_<ts>_<id>.json \
       --runtime               reports/simulations/pas198_manual_test_runtime_<ts>_<id>.json \
       --inspection            reports/simulations/pas199_runtime_inspection_<ts>_<id>.json \
       --behavioral-evaluation reports/simulations/pas200_behavioral_evaluation_<ts>_<id>.json
   ```
3. The summary printout (one block per source artefact +
   evidence strength + claimable / not-claimable list) is the
   talking script. The JSON artefact is the receipt.

### In an investor or stakeholder review

* Pair the digest's `evidence_strength`,
  `operator_summary.highlights`, and `not_claimable_yet` list
  with a single sentence: *"This is what we can defend in
  simulation today; this is what we cannot yet claim about live
  behaviour."*
* The digest is hash-identified, so a saved artefact is
  re-verifiable — re-running PAS201 against the same six
  artefacts produces the same `digest_id`.

### As an audit handoff

* Pass the digest plus the six source artefacts. Anyone with
  access to PAS201 + the six files can independently
  reconstruct the same digest byte-for-byte (modulo the
  `generated_at` timestamp).

## Claimable today (with PAS201 merged)

* An operator can join PAS195 + PAS196 + PAS197 + PAS198 +
  PAS199 + PAS200 into a single bounded, hash-identified
  evidence digest for audit, demo, or investor review.
* The digest refuses broken lineages: any mismatch in the six-
  artefact joins is surfaced as a validation error.
* Evidence strength is computed deterministically from the
  closed rule set; same six artefacts always yield the same
  strength.
* The digest carries no PII, no production brokerage IDs, no
  free-form operator text, no LLM-derived signals.
* The digest's `claimable_now` list never asserts live routing
  activity; `not_claimable_yet` always reminds the reader that
  live call routing, calibration, and automated promotion
  remain out of scope.

## Still not claimable (PAS202+)

* PAS validates digest strength against live-call performance
  (calibration). (PAS202+.)
* The PAS engine consumes a digest to choose a strategy per
  lead. (Later phase, gated on calibration evidence.)
* Operators trigger or distribute digests from Slack. (Later
  operator-surface phase.)
* Digests are used to gate any automatic promotion or
  deployment. (Outside PAS201's scope by construction — a
  digest is evidence, not an action.)

## Future PAS202 path

PAS202 is the next bounded step: a calibration layer that ties
PAS201 digest strength to whatever live-call evidence the PAS
engine already records. Expected shape:

1. A read-only ingestion of historical live-call outcomes,
   strictly bounded to whatever the engine already records (no
   new PII surfaces, no new schemas).
2. A pure comparator that maps PAS201 `evidence_strength` per
   strategy to live-call outcome distributions for matching
   lead segments.
3. A calibration report under `reports/simulations/` that
   records, per strategy, how well synthetic digest strength
   predicted live outcomes — without ever causing the engine
   to switch strategy.
4. A PAS202 readiness gate asserting the calibration layer
   cannot bypass the PAS201 contract (no LLM-based scoring, no
   Slack imports, no Twilio imports, no migrations).

PAS202 is **not** PAS201's responsibility. PAS201 ships the
six-artefact join + deterministic strength scorer; PAS202 ships
the calibration that contextualises the digest against live
evidence.

## Safety constraints (inherited + extended)

PAS201 inherits the full PAS193–PAS200 safety doctrine:

* No real leads, no real phone calls, no Twilio live calls.
* No Slack messages, no Slack imports.
* No worker auto-start, no production brokerage mutation.
* No new SQL migration, no edits to
  `combined_supabase_migration.sql`.
* No secret-shaped tokens in source or in artefacts.
* No PII in digest artefacts — no free-form text fields, no
  real user ids, no email addresses, no phone numbers.
* No autonomous-apply identifiers in PAS201 source — readiness
  gate enforces by AST scan.
* No forbidden status literals (`APPROVED`, `APPLIED`,
  `AUTO_APPLIED`, `LIVE`, `DEPLOYED`) in PAS201 source —
  readiness gate enforces by AST string-constant scan.
* Every digest artefact carries `phase: "PAS201"`,
  `allowed_environment: "SIMULATION_ONLY"`, and
  `live_behavior_changed: False`.
* `evidence_strength` drawn from the closed
  `EVIDENCE_STRENGTH_VALUES` vocabulary
  (`{strong, moderate, weak, blocked}`).
* `operator_summary.highlights` drawn from the closed
  `OPERATOR_HIGHLIGHTS` vocabulary.
* `operator_summary.recommended_next_action` drawn from the
  closed `OPERATOR_NEXT_ACTIONS` vocabulary.
* `claimable_now` drawn from the closed `CLAIMABLE_NOW_VOCAB`
  vocabulary; it never asserts live routing activity.
* `not_claimable_yet` drawn from the closed
  `NOT_CLAIMABLE_YET_VOCAB` vocabulary; every token names a gap
  (`*_out_of_scope` or `*_pending`).

## How to run

```
# Compile-check.
python -m compileall -q app/services/simulation scripts/pas201_*.py tests/mvp/test_pas201_evidence_digest.py

# Unit + integration tests.
python -m pytest tests/mvp/test_pas201_evidence_digest.py -q

# Read-only readiness gate.
python scripts/pas201_evidence_digest_readiness_check.py --summary-only

# Build the digest (the operator-facing command).
python scripts/pas201_build_simulation_evidence_digest.py \
    --recommendation        <pas195 path> \
    --review                <pas196 path> \
    --package               <pas197 path> \
    --runtime               <pas198 path> \
    --inspection            <pas199 path> \
    --behavioral-evaluation <pas200 path>
```

Digest artefacts land under `reports/simulations/` with filenames
of shape
`pas201_simulation_evidence_digest_<utc-timestamp>_<digest_id>.json`.

## Relationship to PAS195–PAS200

PAS201 is purely additive over PAS200. The PAS201 readiness gate
enforces that every PAS193, PAS194, PAS195, PAS196, PAS197,
PAS198, PAS199, and PAS200 carry-forward file remains on disk and
that the PAS201 surface neither imports nor modifies any of them.
The digest service consumes the six source artefacts; it never
re-runs anything in the simulation engine.

A digest is an immutable, hash-identified, operator-facing
summary. Source artefacts and the digest never change in place.
Each PAS201 digest is a distinct artefact that asserts the
six-artefact lineage was consistent, the evidence strength was
*X*, and the listed claims were the ones the chain actually
supported at the time the digest was generated.
