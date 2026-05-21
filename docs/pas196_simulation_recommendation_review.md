# PAS196 — Simulation Recommendation Review Surface

## Purpose

PAS195 emits CANDIDATE strategy recommendations from simulation
evidence. PAS196 gives an operator the structural means to act on
one — to **approve it for manual test**, **reject it**, or
**expire it** — without changing any live behaviour, mutating any
brokerage row, or touching Twilio, Slack, Supabase, or the live
state machine.

PAS196 is deliberately the smallest possible review surface:

* A pure function (`submit_review`) that validates an operator
  review action against a closed status machine and returns a
  bounded review envelope.
* A CLI that wraps that function.
* A readiness gate that asserts the surface cannot grow into a
  live-mutation path.

Nothing else. The review surface produces evidence of review. It
does not act on it.

## What PAS196 proves

* **A bounded status machine governs the recommendation
  lifecycle.** Four allowed statuses (`CANDIDATE`,
  `APPROVED_FOR_MANUAL_TEST`, `REJECTED`, `EXPIRED`) and four
  allowed transitions are enumerated in
  `app/services/simulation/recommendation_review.py`. Any other
  status value is structurally rejected.
* **Forbidden statuses are absent by construction.** The strings
  `APPROVED`, `APPLIED`, `AUTO_APPLIED`, `LIVE`, and `DEPLOYED`
  never appear as string constants in PAS196 source. The
  readiness gate enforces this via AST scan of string literals,
  matching exactly so that `APPROVED_FOR_MANUAL_TEST` (a distinct
  value) is unaffected.
* **No autonomous-apply code path can exist.** Identifier names
  that would signal a live mutation (`apply_recommendation`,
  `deploy_strategy`, `switch_strategy_live`, `auto_apply`,
  `auto_promote`, `force_promote`, `live_apply`, `auto_deploy`)
  are forbidden in PAS196 source and enforced by AST scan.
* **Review envelopes are bounded.** Every envelope carries
  exactly the eleven documented fields: `review_id`, `phase`,
  `recommendation_id`, `previous_status`, `new_status`,
  `actor_type`, `actor_id_token`, `reason_token`, `reviewed_at`,
  `operator_required`, `live_behavior_changed`. There is no
  `notes`, `comment`, `free_text`, or `operator_notes` field —
  reviews never carry free-form operator text, which keeps the
  ledger PII-free and machine-readable.
* **Actor identity is shape-bounded.** `actor_id_token` must
  match `^op_[a-z0-9]{4,32}$` for operators or be the literal
  `auto_expiry` for the automated-expiry actor. Real Slack user
  ids (e.g. `U01234567`) are structurally rejected.
* **Reasons are vocabulary-bounded.** `reason_token` is one of
  eight enumerated values; any other value is rejected. The
  vocabulary covers approval, four distinct rejection rationales,
  and three expiry rationales.
* **Reviews never change live behaviour.** Every envelope is
  stamped with `live_behavior_changed: False` and
  `operator_required: True`. The readiness gate's runtime smoke
  test exercises this on a synthetic recommendation.
* **Reviews are deterministic.** `review_id` is a stable
  SHA-256-derived hash of (recommendation_id, previous_status,
  new_status, actor_type, actor_id_token, reason_token,
  reviewed_at). Same inputs → same id, every call.

## What PAS196 does not prove

PAS196 ships the review surface. It does not ship the runtime
that consumes the review. The following remain out of scope:

* **PAS does not yet read review envelopes at runtime.**
  Approving a recommendation `APPROVED_FOR_MANUAL_TEST` in PAS196
  has no effect on which strategy the engine actually uses on a
  live call. That binding belongs to PAS197 — a bounded runtime
  selector that consults review envelopes and refuses to act on
  anything still in `CANDIDATE`.
* **The review surface is not yet a Slack command.** PAS196's
  CLI is the structural minimum. PAS198+ will add a Slack
  command (`/pas review-recommendations`) that calls the same
  bounded function, with the same actor / reason vocabulary,
  emitting the same envelopes. The Slack surface is a UX layer
  on top of PAS196; it is not PAS196 itself.
* **No persistent review ledger.** Review envelopes are written
  as discrete JSON files under `reports/simulations/`. There is
  no Supabase table, no migration, no cross-review query layer.
  Aggregating reviews across time is a PAS199+ concern.

## Claimable today (with PAS196 merged)

* PAS has a bounded operator-review surface for simulation
  strategy recommendations.
* Operators can record `APPROVED_FOR_MANUAL_TEST`, `REJECTED`,
  or `EXPIRED` against any CANDIDATE recommendation.
* The review surface cannot autonomously apply, deploy, or
  switch live behaviour — enforced structurally by the absence
  of forbidden status literals and identifiers, and by every
  envelope carrying `live_behavior_changed: False`.
* Reviews carry no PII or free-form operator text; both
  `actor_id_token` shape and `reason_token` vocabulary are
  bounded.
* Review envelopes are deterministic and hash-identified for
  audit.

## Still not claimable (PAS197+)

* PAS runtime selects a strategy per lead based on an
  operator-approved recommendation. (PAS197.)
* Operators review recommendations from a Slack command rather
  than the CLI. (PAS198.)
* The review history is queryable across time. (PAS199.)
* Reviews are validated against live-call outcomes. (PAS200+.)

## Future PAS197 path

PAS197 is the next bounded step: a runtime strategy selector that
reads PAS196 review envelopes. Its expected shape:

1. A pure function `select_strategy_for_lead(lead_context,
   review_index)` that returns either an approved strategy id
   from an `APPROVED_FOR_MANUAL_TEST` envelope, or the existing
   default (`balanced`) when no approved recommendation applies.
2. Hard refusal to act on `CANDIDATE` envelopes — only
   `APPROVED_FOR_MANUAL_TEST` is consulted. `REJECTED` and
   `EXPIRED` envelopes are ignored.
3. A "manual test only" runtime gate that requires the lead to
   be flagged as a manual-test lead before the approved strategy
   is consulted. Live leads continue to use the default until a
   later PAS phase explicitly broadens scope.
4. A PAS197 readiness gate that asserts the selector cannot read
   anything stronger than `APPROVED_FOR_MANUAL_TEST` and cannot
   switch behaviour for non-manual-test leads.

PAS197 is **not** PAS196's responsibility. PAS196 ships the
review record shape; PAS197 ships the runtime that respects it.

## Safety constraints (inherited + extended)

PAS196 inherits the full PAS193–PAS195 safety doctrine and adds
explicit status-and-identifier bans:

* No real leads, no real phone calls, no Twilio live calls.
* No Slack messages, no Slack imports.
* No worker auto-start, no production brokerage mutation.
* No new SQL migration, no edits to
  `combined_supabase_migration.sql`.
* No secret-shaped tokens in source or in artefacts.
* No PII in review envelopes — no free-form text fields, no real
  user ids, no email addresses, no phone numbers.
* No autonomous-apply identifiers in PAS196 source — readiness
  gate enforces by AST scan.
* No forbidden status literals (`APPROVED`, `APPLIED`,
  `AUTO_APPLIED`, `LIVE`, `DEPLOYED`) in PAS196 source —
  readiness gate enforces by AST string-constant scan.
* Every review envelope carries `operator_required: True` and
  `live_behavior_changed: False`.

## How to run

```
# Compile-check.
python -m compileall -q app/services/simulation scripts/pas196_*.py tests/mvp/test_pas196_simulation_recommendation_review.py

# Unit + integration tests.
python -m pytest tests/mvp/test_pas196_simulation_recommendation_review.py -q

# Read-only readiness gate.
python scripts/pas196_simulation_recommendation_review_readiness_check.py --summary-only

# Approve a recommendation for manual test.
python scripts/pas196_review_simulation_recommendation.py \
    --recommendation reports/simulations/pas195_recommendation_<ts>_<id>.json \
    --action approve-manual-test \
    --actor-id-token op_yourtoken \
    --reason-token operator_approved_for_manual_test

# Reject a recommendation as unsafe.
python scripts/pas196_review_simulation_recommendation.py \
    --recommendation reports/simulations/pas195_recommendation_<ts>_<id>.json \
    --action reject \
    --actor-id-token op_yourtoken \
    --reason-token operator_rejected_unsafe

# Expire a recommendation automatically.
python scripts/pas196_review_simulation_recommendation.py \
    --recommendation reports/simulations/pas195_recommendation_<ts>_<id>.json \
    --action expire \
    --actor-id-token auto_expiry \
    --actor-type automated_expiry \
    --reason-token candidate_expired_age
```

Review envelopes land under `reports/simulations/` with filenames
of shape `pas196_recommendation_review_<utc-timestamp>_<review_id>.json`.

## Relationship to PAS195

PAS196 is purely additive over PAS195. The PAS196 readiness gate
enforces that every PAS193, PAS194, and PAS195 carry-forward file
remains on disk and that the PAS196 surface does not import or
modify any of them. The review service consumes a PAS195
recommendation's `recommendation_id` and `status` fields and emits
a new artefact that references the source recommendation by id.

A PAS195 recommendation never changes in place. Review state lives
in the PAS196 envelope. The history of any one recommendation is
reconstructable by joining its `recommendation_id` across PAS195
recommendation files and PAS196 review files.
