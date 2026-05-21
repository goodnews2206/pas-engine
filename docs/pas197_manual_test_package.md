# PAS197 — Approved Strategy Manual-Test Package

## Purpose

PAS196 lets an operator transition a PAS195 CANDIDATE
recommendation to `APPROVED_FOR_MANUAL_TEST`. PAS197 takes the
next bounded step: it converts the approved review into a
structured **manual-test package** that the operator can inspect
before any future runtime work touches the strategy in question.

PAS197 is the artefact layer for manual test review. It does
not run the manual test; it only assembles the package the
operator inspects.

The package is the smallest possible inspectable artefact:

* A pure function (`build_manual_test_package`) that validates the
  (recommendation, review) pair against a strict contract.
* A bounded output carrying closed-vocabulary test steps, success
  metrics, rollback notes, and safety notes — and nothing else.
* A CLI that wraps the function.
* A readiness gate that asserts the package can never be anything
  other than SIMULATION_ONLY.

PAS197 does **not** select a strategy at runtime. PAS197 does
**not** route a live call. PAS197 does **not** deploy anything.
Its only output is an inspectable JSON file flagged
`status: "READY_FOR_MANUAL_TEST"`,
`allowed_environment: "SIMULATION_ONLY"`,
`live_behavior_changed: false`.

## What PAS197 proves

* **A bounded artefact represents an approved strategy.** A
  pure function in `app/services/simulation/manual_test_package.py`
  consumes a PAS195 CANDIDATE recommendation and a PAS196
  APPROVED_FOR_MANUAL_TEST review, validates the pair, and emits
  a single package. Validation is strict: any contract violation
  raises `ManualTestPackageValidationError` and the CLI exits 2.
* **The contract chains correctly.** The package requires
  `recommendation.status == "CANDIDATE"`,
  `recommendation.operator_required is True`,
  `recommendation.recommended_strategy` to be a non-empty string,
  `review.new_status == "APPROVED_FOR_MANUAL_TEST"`,
  `review.live_behavior_changed is False`, and
  `review.recommendation_id == recommendation.recommendation_id`.
  Mismatches at any of these joints are refused.
* **The package is environment-bounded by construction.** The
  fields `allowed_environment` and `live_behavior_changed` are
  fixed at `"SIMULATION_ONLY"` and `False` respectively by the
  service. The caller cannot override them. The readiness gate's
  runtime smoke test exercises this on a synthetic pair.
* **Test plan, success metrics, rollback notes, and safety notes
  are vocabulary-bounded.** Each is a list drawn from a closed
  tuple defined in the service module. There is no free-form
  text field on the package. PII and operator commentary cannot
  end up in a PAS197 artefact.
* **The package is deterministic.** `package_id` is a stable
  SHA-256-derived hash of (recommendation_id, review_id,
  strategy_id, status, allowed_environment). The same approved
  pair produces the same `package_id` every call.
* **Forbidden status literals are absent.** The strings
  `APPROVED`, `APPLIED`, `AUTO_APPLIED`, `LIVE`, and `DEPLOYED`
  never appear as string constants in PAS197 source. The
  readiness gate enforces this by AST scan, matching exactly so
  `APPROVED_FOR_MANUAL_TEST` and `READY_FOR_MANUAL_TEST` (distinct
  values) are unaffected.
* **Forbidden live-mutation identifiers are absent.**
  `apply_recommendation`, `deploy_strategy`, `switch_strategy_live`,
  `auto_apply`, `auto_promote`, `force_promote`, `live_apply`,
  `auto_deploy` are all absent from PAS197 source. The readiness
  gate enforces this by AST identifier scan.

## What PAS197 does not prove

PAS197 ships the package. It does not ship anything that consumes
the package at runtime. The following remain out of scope:

* **The package does not select a runtime strategy.** Generating
  a PAS197 package for `callback_first` does not cause PAS to use
  `callback_first` on any call. The runtime engine continues to
  use the default strategy until a later phase explicitly broadens
  scope.
* **There is no live-test runtime.** PAS197 packages are
  inspected; they are not yet executed against any harness. A
  bounded manual-test runtime that consumes a package and emits
  a fresh transcript belongs to PAS198.
* **There is no Slack review surface for packages.** Operators
  read packages as JSON files. A Slack command surface mirroring
  PAS196's review-action shape will be added in PAS199 or later.
* **There is no calibration loop.** Packages emitted in
  simulation are not yet shown to predict live-call outcomes.

## Claimable today (with PAS197 merged)

* PAS produces a bounded inspectable artefact for each operator-
  approved simulation strategy.
* Packages are structurally bounded to SIMULATION_ONLY and carry
  `live_behavior_changed: False`.
* Packages carry no PII or free-form operator text; every
  descriptive field is drawn from a closed vocabulary.
* Packages cannot be issued for rejected, expired, or unreviewed
  recommendations — the contract refuses every off-path input
  pair.
* Packages are deterministic and hash-identified for audit.

## Still not claimable (PAS198+)

* PAS has a bounded manual-test runtime that consumes a package
  and emits a transcript. (PAS198.)
* Operators review packages from a Slack command. (PAS199.)
* Package outcomes are validated against live-call performance.
  (PAS200+.)
* PAS runtime selects a strategy per lead. (Later phase, gated on
  the manual-test runtime and on calibration evidence.)

## Future PAS198 path

PAS198 is the next bounded step: a manual-test runtime that
consumes a PAS197 package and runs the recommended strategy
against the synthetic catalogue, then writes a transcript. Its
expected shape:

1. A CLI that accepts `--package <path>` and refuses anything
   that is not a `status: READY_FOR_MANUAL_TEST,
   allowed_environment: SIMULATION_ONLY` package.
2. A pure runner that calls into PAS194's strategy-aware
   transcript builder using the package's `strategy_id`. The
   runner reuses PAS193's scoring with no relaxation.
3. A transcript artefact under `reports/simulations/` that
   references the package's `package_id` and records the manual-
   test outcome.
4. A PAS198 readiness gate asserting the runner cannot run
   against anything other than the SIMULATION_ONLY environment
   and cannot bypass scoring auto-fails.

PAS198 is **not** PAS197's responsibility. PAS197 ships the
package shape; PAS198 ships the runtime that consumes it.

## Safety constraints (inherited + extended)

PAS197 inherits the full PAS193–PAS196 safety doctrine:

* No real leads, no real phone calls, no Twilio live calls.
* No Slack messages, no Slack imports.
* No worker auto-start, no production brokerage mutation.
* No new SQL migration, no edits to
  `combined_supabase_migration.sql`.
* No secret-shaped tokens in source or in artefacts.
* No PII in packages — no free-form text fields, no real user
  ids, no email addresses, no phone numbers.
* No autonomous-apply identifiers in PAS197 source — readiness
  gate enforces by AST scan.
* No forbidden status literals (`APPROVED`, `APPLIED`,
  `AUTO_APPLIED`, `LIVE`, `DEPLOYED`) in PAS197 source —
  readiness gate enforces by AST string-constant scan.
* Every package carries `status: "READY_FOR_MANUAL_TEST"`,
  `allowed_environment: "SIMULATION_ONLY"`, and
  `live_behavior_changed: False`.

## How to run

```
# Compile-check.
python -m compileall -q app/services/simulation scripts/pas197_*.py tests/mvp/test_pas197_manual_test_package.py

# Unit + integration tests.
python -m pytest tests/mvp/test_pas197_manual_test_package.py -q

# Read-only readiness gate.
python scripts/pas197_manual_test_package_readiness_check.py --summary-only

# Build a manual-test package from an approved (recommendation,
# review) pair on disk.
python scripts/pas197_create_manual_test_package.py \
    --recommendation reports/simulations/pas195_recommendation_<ts>_<id>.json \
    --review         reports/simulations/pas196_recommendation_review_<ts>_<id>.json

# Stdout summary only; no JSON written.
python scripts/pas197_create_manual_test_package.py \
    --recommendation <path> --review <path> --summary-only
```

Packages land under `reports/simulations/` with filenames of
shape `pas197_manual_test_package_<utc-timestamp>_<package_id>.json`.

## Relationship to PAS196

PAS197 is purely additive over PAS196. The PAS197 readiness gate
enforces that every PAS193, PAS194, PAS195, and PAS196 carry-
forward file remains on disk and that the PAS197 surface neither
imports nor modifies any of them. The package service consumes a
PAS195 recommendation's `recommendation_id`, `status`,
`operator_required`, and `recommended_strategy`, plus a PAS196
review's `review_id`, `recommendation_id`, `new_status`, and
`live_behavior_changed`. It emits a new artefact that references
both source IDs.

A PAS195 recommendation and a PAS196 review never change in place.
A PAS197 package is a distinct, hash-identified, immutable artefact
that asserts the join of (recommendation, review) was operator-
approved at the time the package was created.
