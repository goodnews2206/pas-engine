# PAS212 — Memory Candidate Pipeline

**Type:** Implementation + documentation. PAS212 rebuilds the **minimal** memory candidate pipeline needed to advance the *adaptive* doctrine pillar — **only** through human-approved candidate memory. No automatic approval, no automatic behaviour change, no embeddings, no vector DB, no external services, no web UI, no migration.

**Doctrine:** PAS should become *queryable, adaptive, and operationally intelligent.* PAS210 made it queryable on live data; PAS212 lays the **adaptive** foundation — but adaptation is gated behind explicit human approval and, in this checkpoint, changes nothing in the runtime.

---

## 1. Scope

**In scope (built):**
- A minimal, transcript-free **memory candidate model** (`candidate_contracts.py`).
- **Deterministic, conservative candidate generation** from already-committed lead/event data (`candidate_generation.py`).
- An **in-memory, tenant-scoped store** with an explicit **review/approval boundary** (`candidate_store.py`).
- Narrow tests for all of the above.

**Out of scope (deliberately not built):**
- Full PAS160–190 memory subsystem (28 corpus modules) — only the candidate→review core.
- Automatic learning / auto-approval.
- Embeddings, vector search, retrieval, injection into the live engine.
- PAS Brain UI.
- PAS213 ingestion.
- Database persistence (no `pas_memory_records` table; see §9).

Rebuilt **from the PAS209.5 recovery-corpus specification only** (docstrings, names, contracts) — not copied from bytecode. Module names are intentionally distinct (`candidate_contracts`/`candidate_generation`/`candidate_store`) to signal a fresh minimal pipeline, not a restore.

---

## 2. Data model

`MemoryCandidate` (frozen dataclass, `candidate_contracts.py`):

| Field | Meaning |
|---|---|
| `id` | Deterministic `mc_<sha256[:16]>` over (brokerage, subject, type, evidence) — regeneration is idempotent |
| `brokerage_id` | Tenant pin (mandatory; taken from the explicit argument only) |
| `subject_type` | `lead` \| `brokerage` \| `agent` \| `source` |
| `subject_id` | Id of the subject |
| `candidate_type` | See §3 |
| `proposed_memory` | Short human-readable summary (never raw transcript) |
| `evidence_refs` | Tuple of refs (`lead:…`, `event:…`); **required, non-empty** |
| `provenance` | How it was derived |
| `confidence` | 0.0–1.0 |
| `status` | `candidate` (default) \| `approved` \| `rejected` \| `archived` |
| `created_at` | ISO-8601 (injectable for deterministic tests) |
| `created_by_system` | `pas212.candidate_generation` |
| `reviewed_by` / `reviewed_at` | Set only on an explicit review decision |

`validate_candidate()` enforces: tenant present, valid subject/type/status, non-empty summary, **non-empty evidence**, confidence in range, and **no raw-transcript leak** (`transcript`/`turns`/`raw_text`/`utterance` tokens rejected). `make_candidate()` returns `None` rather than emit an invalid record.

---

## 3. Candidate types

Conservative, closed set (PAS212 examples), all deterministic and pure:

| Type | Trigger (from committed data) | Subject |
|---|---|---|
| `lead_fact` | A lead row carries ≥1 of intent/budget/timeline | lead |
| `callback_preference` | Lead has callback event(s) | lead |
| `repeated_objection_pattern` | ≥2 objection events for a lead | lead |
| `source_lead_quality_signal` | ≥3 leads from a source with a clearly strong/weak booking rate | source |
| `agent_followup_pattern` | An agent with ≥3 assigned leads all booking | agent |

Thresholds are intentionally high; weak signals produce nothing. Missing evidence (e.g. a lead with no id) produces nothing.

---

## 4. Approval boundary

- Generation emits **`candidate` status only** — never `approved`/`rejected`.
- `MemoryCandidateStore` transitions are **explicit and reviewer-stamped**: `approve()` / `reject()` / `archive()` require a non-empty `reviewer`; they record `reviewed_by` + `reviewed_at`.
- Only a `candidate` may be approved or rejected. A **rejected candidate can never be approved** and remains stored (auditable).
- **No live behaviour change.** The store imports nothing from the engine, brokerage config, Twilio, Cal.com, or any outbound surface (enforced by a test). Approving a candidate records a decision and **does not** alter prompts, flags, or call behaviour.
- **Tenant isolation.** Every read/transition is scoped by `brokerage_id`; a candidate under one brokerage is unreachable via another, and cross-tenant `add_candidates` is rejected.

---

## 5. Candidate generation summary

`generate_candidates(brokerage_id, *, leads=(), events=(), now=None)` runs all five generators, de-duplicates by id, and returns a deterministically ordered list. Inputs are passed in by the caller (no DB reads here), so the pipeline is pure and unit-testable. `brokerage_id` is the **only** tenant source — any `brokerage_id` on an input row is ignored/overwritten.

---

## 6. Storage approach

**In-memory, tenant-scoped, process-local** (`MemoryCandidateStore`). No database, no file, no migration. This satisfies PAS212's "implement a safe in-memory/file-free abstraction with tests first" path because the corpus `pas_memory_records` table (migrate_v10/v11) is **not** in the committed schema and a migration is not yet justified. Durable persistence is **PAS212B** (§9).

---

## 7. What is NOT implemented

- No DB table / migration (PAS212B).
- No retrieval or injection of approved memory into the live engine (PAS212C).
- No auto-approval, no auto-learning, no behaviour change of any kind.
- No embeddings / vector DB / external services / UI.
- No prompt-injection quarantine classifier (the corpus `classifier`/`governance` DANGEROUS path) — out of minimal scope; the contract still rejects transcript leaks.

---

## 8. Relationship to PAS300 / PAS301 memory ownership

PAS300/PAS301 define identity, session, and **workspace/memory ownership** (who owns and governs a brokerage's memory). PAS212 is the **mechanism** beneath that policy: candidates are tenant-pinned and human-approved, so when the PAS301 ownership/roles model is wired, "who may approve a candidate" maps cleanly onto the explicit `reviewer` on `approve()`/`reject()`. PAS212 deliberately stops at recording the decision; enforcing *which role* may review is a later integration with PAS301 auth.

---

## 9. Future steps

- **PAS212B — Durable persistence.** Propose (do not auto-apply) a `pas_memory_records` + review-audit table migration mirroring the in-memory contract (tenant `NOT NULL`, RLS), and swap the store backend. Migration SQL to be reviewed separately.
- **PAS212C — Governed retrieval + injection.** Only approved, governed candidates feed the runtime (operator-gated, still no autonomous change), with the prompt-injection quarantine path from the corpus `classifier`/`governance` spec.
- **PAS301 integration.** Bind `reviewer` to authenticated role/identity once PAS301 auth lands.

---

*End of PAS212. Minimal candidate pipeline only: deterministic generation + in-memory tenant-scoped store + explicit approval boundary. No DB/migration, no embeddings, no behaviour change, no PAS209/stash/`__pycache__` touched, no dependencies added.*
