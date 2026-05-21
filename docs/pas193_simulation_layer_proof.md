# PAS193 — Simulation Layer Proof

## Purpose

PAS193 stands up a deterministic, offline rehearsal layer for PAS
lead conversations. It exists to make one specific public claim
operationally defensible:

> "PAS rehearses lead conversations in simulation before handling
> real calls."

Before PAS193, that claim was strategic. With PAS193 merged, the
claim is backed by an inspectable artefact: a scenario catalogue,
a deterministic adapter, a scoring engine, a report model, a CLI
runner, and a readiness gate.

## What PAS193 proves

* **Rehearsal exists.** A closed, hand-authored catalogue of at
  least 20 real-estate lead scenarios lives under
  `app/services/simulation/scenarios.py`. Each scenario carries an
  intent, an initial message, a lead script, success and failure
  criteria, and an explicit `supported: True/False` flag.
* **Rehearsal is deterministic.** The adapter is a rule-based
  player with no randomness, no LLM, and no network. Same input
  produces the same transcript, action sequence, capability set,
  and score every run.
* **Outcomes are scored.** The scoring engine awards capability
  credit only when the adapter actually fired the relevant action
  (qualify, offer appointment, offer callback, handle objection,
  close). It auto-fails any rehearsal that emits an unsafe claim,
  a PII-shaped utterance, a hallucinated policy, an agent-poaching
  response, or a language misclaim.
* **Reports are produced.** Every batch emits a structured JSON
  report carrying pass rate, average score, booking-attempt rate,
  callback-capture rate, objection-handling rate, top failure
  modes, best- and worst-performing scenario types, and a stable
  `report_id` that is a hash of the scored scenario set and seed.
* **Reports are isolated.** Reports are written under
  `reports/simulations/`. The runner refuses to write outside
  that directory, and the readiness gate enforces it.
* **No live coupling.** Neither the adapter, the scorer, the
  report builder, the runner, nor the readiness gate imports
  Twilio, Slack, OpenAI, Anthropic, Supabase, `dotenv`, or
  `app.engine.state_machine`. Tests and the gate enforce this by
  static inspection.

## What PAS193 does not prove

PAS193 is the **proof of existence** for a rehearsal layer. It is
deliberately not the proof of fidelity. The following items are
explicitly out of scope and remain future PAS194 / PAS195 work:

* **State-machine equivalence.** PAS193 bypasses
  `app.engine.state_machine` because the live state machine binds
  to Twilio and Supabase. PAS194 will route the same scenario
  surface through the real state machine under a stub transport,
  so the rehearsal layer is provably exercising the same call
  flow as production.
* **LLM-driven response quality.** The adapter emits canned lines
  and never invokes an LLM. PAS193 proves the action sequence is
  right; it does not prove the wording is. Wording-quality scoring
  belongs to PAS194 (LLM-graded rubric under a closed prompt set)
  or PAS195 (live-call sample review).
* **Behavioural realism of the synthetic lead.** Lead utterances
  are scripted per scenario, not sampled from production
  transcripts. Realism comes from PAS195.
* **Outcome calibration against production.** PAS193 reports rates
  computed against a synthetic batch. It does not yet claim those
  rates are predictive of live-call performance. Calibration is
  PAS195.

## Claimable today (with PAS193 merged)

* PAS has a rehearsal layer.
* PAS rehearsals are deterministic and reproducible.
* PAS rehearsals are scored against capability and safety
  criteria with auto-fail invariants on safety violations.
* Each batch produces a structured, hash-identified report.
* The rehearsal layer is structurally incapable of placing a real
  call, sending a real message, or mutating a real brokerage row.

## Still not claimable (until PAS194 / PAS195)

* PAS rehearsals exercise the same state machine that handles
  live calls.
* PAS rehearses with LLM-graded response quality.
* PAS rehearsal scores predict live-call outcomes.
* PAS rehearses with utterances sampled from real lead behaviour.

## Safety constraints

The PAS193 doctrine, enforced by the readiness gate and tests:

* No real leads, no real phone calls, no Twilio live calls.
* No Slack messages, no Slack imports.
* No worker auto-start.
* No production brokerage mutation, no Supabase writes.
* No new SQL migration.
* No `combined_supabase_migration.sql` edits, no commits of that
  file on the PAS193 branch.
* No secrets in source or in reports.
* No PII-shaped tokens in scenarios, in transcripts, or in reports.
* No production brokerage UUIDs anywhere in the artefact set.
* Deterministic scoring — same input, same output.
* Reports written only under `reports/simulations/`.

## How to run

From the repo root:

```
# Compile-check everything PAS193 touches.
python -m compileall -q app/services/simulation scripts/pas193_run_simulation_batch.py scripts/pas193_simulation_layer_readiness_check.py tests/mvp/test_pas193_simulation_layer.py

# Unit + integration tests.
python -m pytest tests/mvp/test_pas193_simulation_layer.py -q

# Read-only readiness gate.
python scripts/pas193_simulation_layer_readiness_check.py --summary-only

# Default 20-scenario rehearsal batch.
python scripts/pas193_run_simulation_batch.py --count 20

# A larger batch (cycles through the catalogue).
python scripts/pas193_run_simulation_batch.py --count 100 --seed 42

# Stdout summary only, no JSON written.
python scripts/pas193_run_simulation_batch.py --count 20 --summary-only

# Strict mode — exit non-zero if any rehearsal auto-failed.
python scripts/pas193_run_simulation_batch.py --count 20 --strict
```

Reports land under `reports/simulations/` with filenames of shape
`pas193_simulation_batch_<utc-timestamp>_<report_id>.json`.

## Relationship to PAS191 / PAS192

PAS193 is additive over PAS192. It does not touch any PAS191 or
PAS192 surface. The PAS192 carry-forward is enforced by the PAS193
readiness gate: the gate checks that PAS192's Slack operator
modules, tests, and doc are still on disk and reachable.

## Open follow-ups (PAS194 candidates)

* Wire `app.engine.state_machine` into the rehearsal layer via a
  stub transport so PAS193 transcripts come from the real engine.
* Add an LLM-graded wording rubric under a closed prompt set.
* Add Spanish-language support so the language-unsupported
  scenario can flip to `supported: True`.
* Add longitudinal scoring: track best/worst trends across batches
  and surface regressions to the operator dashboard.
