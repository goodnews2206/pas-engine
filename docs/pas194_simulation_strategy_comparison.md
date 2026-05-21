# PAS194 — Simulation Strategy Comparison

## Purpose

PAS193 stood up a deterministic rehearsal layer that could replay
a fixed scenario catalogue under a single PAS conversation
policy. PAS194 upgrades that into a **comparison** layer: the
same scenario catalogue is replayed under five distinct
conversation strategies, scored, and compared. Strategy trade-offs
are now inspectable artefacts rather than implicit assumptions.

## What PAS194 proves

* **PAS can run the same scenario set under multiple strategies.**
  Five strategy profiles (`conservative`, `balanced`, `assertive`,
  `callback_first`, `booking_first`) are defined under
  `app/services/simulation/strategies.py`. Each carries an
  inspectable tone, qualification depth, booking pressure,
  callback preference, objection style, and safety notes.
* **Strategy-aware execution is deterministic.** The comparison
  engine in `app/services/simulation/comparison.py` consumes the
  PAS193 transcript primitives and produces the same outcome for
  the same `(strategy, scenario, seed)` triple every run.
* **Strategy trade-offs are surfaced, not hidden.** When a
  strategy is structurally unsafe for a given scenario type — e.g.
  `assertive` pushing an appointment on `already_has_agent` is
  `agent_poaching`, `booking_first` pushing on
  `language_unsupported` is `language_misclaim` — the comparison
  engine forces the auto-fail safety invariant from PAS193's
  scorer rather than masking it.
* **Best- and worst-performing strategies are computed
  deterministically.** Ranking is composite: pass-rate first,
  then average score. Ties break by `strategy_id` lexicographic
  order, so the report's `best_strategy` and `worst_strategy`
  fields are reproducible.
* **Per-scenario winners are tracked.** The report identifies
  which strategies achieved the top score on each scenario, so
  the operator can see "for X scenario type, strategies A and B
  tie; for Y, only strategy C wins." This is the building block
  for strategy-routing in PAS195.
* **Reports are isolated and inspectable.** Comparison reports
  are written under `reports/simulations/` with a stable
  `report_id` of shape `pas194-cmp-<16 hex>`.

## What PAS194 does not prove

PAS194 proves that strategy comparison **exists** and is
**deterministic**. The following remain explicitly out of scope:

* **Live-call equivalence.** Strategies are modifiers over the
  PAS193 offline action plan. They have not yet been validated
  against the real state machine. PAS195 will route the same
  strategy surface through a stub-transport version of
  `app.engine.state_machine` so comparison-layer rankings can be
  shown to predict live call flow.
* **LLM-graded response wording.** The adapter still emits canned
  PAS-shaped lines. PAS194's comparison is about action policy,
  not language.
* **Calibration against production outcomes.** Pass rates and
  booking rates are computed against the synthetic catalogue.
  They are not yet shown to predict pilot pass rates. Calibration
  is PAS195 / PAS196.
* **Optimal strategy selection at runtime.** PAS194 produces the
  evidence for routing decisions; it does not yet wire that
  evidence into a runtime selector. That is PAS197 candidate work.

## How this upgrades the Speedrun claim

Before PAS194, the public claim was:

> "PAS rehearses lead conversations in simulation before handling
> real calls."

After PAS194, the defensible upgrade is:

> "PAS rehearses lead conversations in simulation under multiple
> conversation strategies before handling real calls, and compares
> the outcomes so the brokerage can see which strategy fits which
> lead profile."

Note the explicit boundary: the claim is about **comparison**, not
about **optimal selection at runtime**. PAS195+ closes that gap.

## Claimable today (with PAS194 merged)

* PAS has a deterministic, multi-strategy rehearsal comparison
  layer.
* Five named strategies are inspectable: `conservative`,
  `balanced`, `assertive`, `callback_first`, `booking_first`.
* Strategy trade-offs are surfaced as safety auto-fails — pushing
  an appointment on an already-represented lead loses the
  rehearsal under `assertive` / `booking_first`.
* Per-scenario winners are computed and reported.
* Comparison reports carry a stable hash-identified `report_id`
  for audit.

## Still not claimable (PAS195+ follow-ups)

* PAS rehearsal strategies are validated against the live state
  machine.
* PAS selects a strategy per lead at runtime based on
  comparison-layer evidence.
* PAS strategy comparison scores predict pilot performance.
* PAS strategies vary not just action policy but also wording.

## Safety constraints

PAS194 inherits the full PAS193 safety doctrine and adds nothing
that could relax it:

* No real leads, no real phone calls, no Twilio live calls.
* No Slack messages, no Slack imports.
* No worker auto-start.
* No production brokerage mutation, no Supabase writes.
* No new SQL migration.
* No `combined_supabase_migration.sql` edits or commits on this
  branch.
* No secret-shaped tokens in source or reports.
* No PII-shaped tokens in transcripts or reports.
* No production brokerage UUIDs anywhere in the artefact set.
* Deterministic per-strategy plan modifiers — same input, same
  output.
* Reports written only under `reports/simulations/`.

## How to run

From the repo root:

```
# Compile-check everything PAS194 touches.
python -m compileall -q app/services/simulation scripts/pas194_compare_simulation_strategies.py scripts/pas194_strategy_comparison_readiness_check.py tests/mvp/test_pas194_strategy_comparison.py

# Unit + integration tests.
python -m pytest tests/mvp/test_pas194_strategy_comparison.py -q

# Read-only readiness gate.
python scripts/pas194_strategy_comparison_readiness_check.py --summary-only

# Default — all 5 strategies x full 20-scenario catalogue.
python scripts/pas194_compare_simulation_strategies.py

# Restrict to safe strategies (skip the strategies that trigger
# safety auto-fails by design).
python scripts/pas194_compare_simulation_strategies.py --strategies conservative,balanced,callback_first

# Stdout summary only, no JSON written.
python scripts/pas194_compare_simulation_strategies.py --summary-only

# Strict mode — exit non-zero if any (strategy, scenario)
# auto-failed. Useful in CI for the safe-strategy subset.
python scripts/pas194_compare_simulation_strategies.py --strategies conservative,balanced,callback_first --strict
```

Comparison reports land under `reports/simulations/` with
filenames of shape
`pas194_strategy_comparison_<utc-timestamp>_<report_id>.json`.

## Relationship to PAS193

PAS194 is purely additive over PAS193. The PAS194 readiness gate
enforces that every PAS193 carry-forward file is still present and
that nothing in PAS194's source surface imports Twilio, Slack,
OpenAI, Anthropic, Supabase, dotenv, or the live state machine.

PAS194 does not modify PAS193's adapter, scorer, or report
builder. The comparison engine composes with PAS193 by importing
the action vocabulary tables in-package — `_AGENT_LINES`,
`_ACTION_PLAN_BY_TYPE`, `_ACTION_CAPABILITIES` — and passes the
constructed conversation through PAS193's `score_conversation`
unchanged. Auto-fail safety invariants therefore remain the single
source of truth.

## Open follow-ups (PAS195 candidates)

* Route every strategy through a stub-transport version of
  `app.engine.state_machine` so the comparison surface matches
  the live engine's call flow.
* Add an LLM-graded wording rubric per strategy, so the comparison
  scores reflect both action policy and language.
* Add per-lead strategy routing at runtime, gated on the
  comparison report's per-scenario winners.
* Add longitudinal comparison: track best/worst strategy trends
  across batches and surface regressions to the operator
  dashboard.
