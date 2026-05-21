# PAS195 — Simulation Evidence Recommendation Layer

## Purpose

PAS193 stood up a deterministic rehearsal layer. PAS194 turned it
into a strategy-comparison layer. PAS195 takes the next bounded
step: it reads a PAS194 comparison report and emits a single
**CANDIDATE** strategy recommendation for human operator review.

PAS195 does **not** apply the recommendation. It does **not**
switch live behaviour. It does **not** mutate Supabase, Twilio,
Slack, or any production state. Its only job is to convert
simulation evidence into a structured, signed-off-shape suggestion
that an operator can accept, reject, or escalate.

## What PAS195 proves

* **Evidence-driven recommendations exist.** A pure function in
  `app/services/simulation/recommendations.py` converts a PAS194
  comparison report into one structured recommendation carrying
  `recommendation_id`, `recommendation_type`,
  `recommended_strategy`, `rejected_strategy`,
  `confidence_level`, `evidence_summary`, `safety_notes`,
  `operator_required`, `status`.
* **Recommendations are bounded by safety.** A strategy is
  disqualified if any of its failure modes carry a PAS193 safety
  auto-fail code (`unsafe_claim`, `pii_leak`,
  `hallucinated_policy`, `agent_poaching`,
  `qualification_pressure`, `language_misclaim`,
  `empty_transcript`, `pii_pattern_in_utterance`,
  `supported_false_no_safe_handoff`). The disqualification stands
  regardless of how good its other metrics look.
* **Recommendations are bounded by threshold.** A strategy is
  only recommendable if its `pass_rate >= 0.95` (configurable
  via `--pass-rate-threshold`). Otherwise the recommendation
  is `recommendation_type: no_safe_promotion` and
  `recommended_strategy: None`.
* **Recommendations never autonomously apply.** Every output
  carries `status: "CANDIDATE"` and `operator_required: True`.
  The readiness gate enforces this by scanning the module surface
  for autonomous-apply identifiers (`apply_recommendation`,
  `deploy_strategy`, `switch_strategy_live`, `auto_apply`,
  `auto_promote`, `force_promote`, `live_apply`, `auto_deploy`)
  and failing if any appear.
* **Recommendations are deterministic.** `recommendation_id` is a
  stable hash of the comparison `report_id`, the recommendation
  type, the recommended and rejected strategies, and the
  pass-rate threshold. Same comparison + threshold → same id.
* **Ties surface explicitly.** When two safe strategies tie on
  composite (avg_score, pass_rate), `recommendation_type` is
  `ambiguous` and `evidence_summary.tied_safe_strategies` lists
  the tie. The recommendation engine never silently picks a
  winner.

## What PAS195 does not prove

PAS195 produces evidence-driven candidates. It does not produce
runtime behaviour. The following remain explicitly out of scope:

* **Live runtime application of the recommendation.** PAS195
  cannot switch the brokerage's active strategy. That is a future
  PAS197+ concern, gated on:
  1. PAS196 — operator review surface (Slack-driven
     accept/reject/escalate with an audit trail);
  2. PAS197 — a bounded runtime selector that consults an
     operator-approved recommendation rather than a raw simulation
     report.
* **Validation against the live state machine.** Recommendations
  still rest on PAS193's offline adapter and PAS194's offline
  comparison. Closing that gap is PAS198+ work.
* **Calibration against pilot outcomes.** PAS195 recommendations
  are produced from synthetic evidence. Whether the recommended
  strategy actually performs better on live calls is a separate
  question that requires PAS199 pilot-cohort instrumentation.

## How this upgrades the Speedrun claim

Before PAS195, the defensible claim was:

> "PAS rehearses lead conversations in simulation under multiple
> conversation strategies before handling real calls, and compares
> the outcomes."

After PAS195, the defensible upgrade is:

> "PAS rehearses lead conversations in simulation under multiple
> strategies, compares the outcomes, and surfaces a structured
> CANDIDATE recommendation for operator review — never applying
> the recommendation autonomously."

The "never applying autonomously" half is load-bearing: it is the
operating doctrine PAS195 enforces in code.

## Claimable today (with PAS195 merged)

* PAS converts simulation evidence into structured CANDIDATE
  recommendations.
* Recommendations are bounded by both safety auto-fail codes and
  a configurable pass-rate threshold.
* Recommendations are deterministic — the same comparison
  produces the same recommendation id.
* Recommendations always require operator review; PAS does not
  apply them autonomously.
* Recommendation outputs are inspectable JSON artefacts under
  `reports/simulations/`.

## Still not claimable (PAS196+ follow-ups)

* PAS exposes recommendations to operators through a review
  surface (PAS196 — Slack-driven accept/reject with audit trail).
* PAS runtime selects a strategy per lead based on an
  operator-approved recommendation (PAS197+).
* PAS recommendations are validated against the live state
  machine (PAS198+).
* PAS recommendations are calibrated against pilot outcomes
  (PAS199+).

## Future PAS196 path

PAS196 is the next bounded step: an operator review surface that
reads PAS195 recommendation artefacts and lets a human respond.
Its expected shape:

1. A Slack command (`/pas review-recommendations`) that lists
   currently-open PAS195 candidates by `recommendation_id`,
   strategy, confidence, and comparison `report_id`.
2. A Slack button or follow-up command that records `ACCEPTED`,
   `REJECTED`, or `ESCALATED` against a recommendation id, with
   the operator's user id and a timestamp.
3. A bounded ledger (operator-action log on disk, or a new
   Supabase table introduced via a small explicitly-approved
   migration) that captures the audit trail.
4. A read-only PAS196 readiness gate that asserts the operator
   review surface cannot trigger any live mutation by itself.

PAS196 is **not** PAS195's responsibility. PAS195 ships the
artefact shape; PAS196 ships the review surface.

## Safety constraints (inherited + extended)

PAS195 inherits the full PAS193/PAS194 safety doctrine and adds
the explicit autonomous-apply ban:

* No real leads, no real phone calls, no Twilio live calls.
* No Slack messages, no Slack imports.
* No worker auto-start, no production brokerage mutation.
* No new SQL migration, no edits to
  `combined_supabase_migration.sql`.
* No secret-shaped tokens in source or in artefacts.
* No PII-shaped tokens in recommendations.
* No production brokerage UUIDs anywhere.
* No autonomous-apply identifiers in PAS195 source — readiness
  gate enforces by AST scan.
* Every recommendation carries `status: "CANDIDATE"` and
  `operator_required: True`.

## How to run

```
# Compile-check.
python -m compileall -q app/services/simulation scripts/pas195_*.py tests/mvp/test_pas195_simulation_recommendations.py

# Unit + integration tests.
python -m pytest tests/mvp/test_pas195_simulation_recommendations.py -q

# Read-only readiness gate.
python scripts/pas195_simulation_recommendation_readiness_check.py --summary-only

# Generate a recommendation from a fresh PAS194 comparison.
python scripts/pas195_generate_simulation_recommendation.py

# Generate from an existing PAS194 comparison report on disk.
python scripts/pas195_generate_simulation_recommendation.py \
    --from-report reports/simulations/pas194_strategy_comparison_<ts>_<id>.json

# Stricter threshold (only recommend if pass_rate >= 1.0).
python scripts/pas195_generate_simulation_recommendation.py --pass-rate-threshold 1.0

# Stdout summary only; no JSON written.
python scripts/pas195_generate_simulation_recommendation.py --summary-only
```

Recommendations land under `reports/simulations/` with filenames
of shape `pas195_recommendation_<utc-timestamp>_<recommendation_id>.json`.

## Relationship to PAS194

PAS195 is purely additive over PAS194. The PAS195 readiness gate
enforces every PAS193 and PAS194 carry-forward file remains on
disk. The recommendation engine consumes the PAS194 comparison
report's `per_strategy_metrics`, `failure_modes_by_strategy`,
`worst_strategy`, `report_id`, and `generated_at` fields, and
emits a new artefact that references the source comparison by id.
