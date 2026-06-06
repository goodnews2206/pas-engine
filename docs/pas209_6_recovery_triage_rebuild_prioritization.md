# PAS209.6 — Recovery Triage & Rebuild Prioritization

**Date:** 2026-06-06
**Type:** Triage / planning only — no source restored, no replacement modules written, no `__pycache__` deleted, PAS209 and the parked stash untouched, PAS210 not implemented, not pushed.
**Inputs:** recovery corpus `recovery/pas209_5_bytecode_corpus/` (216 modules, committed `c4fd2b4`); reconciliation report (`5042caa`); live import/router evidence from the committed tree.

---

## 1. Executive Summary

The PAS209.5 corpus preserves **216 source-less modules** spanning PAS141 → PAS190. Triaging them against the committed reality and the doctrine yields a sharp conclusion: **almost none of it is on the critical path.**

The committed live code touches the lost work in exactly **two places** — both lazy imports inside `app/routes/slack_command.py`:
- `from app.services.security.rate_limit import check_rate_limit` (line 159)
- `from app.services.operator.circuit_breaker_policy import …` (line 694)

These are the **only runtime blockers** and the **only Category A** work. Everything else recovered is additive and can be sequenced behind customer-facing operational proof.

PAS210 (Live Operational Snapshot Bridge) depends on **none** of the recovered subsystems for its data — it reads `pas_events` / `leads` / `calls` / `bookings` that the committed voice engine already writes, through the already-committed `app/services/proactive/supabase_snapshot_adapter.py`. Its only recovered-work prerequisite is the two-import repair, because the Slack surface that would expose it currently throws on those paths.

Net recommendation: **PAS209.7 (import repair) → PAS210 (snapshot bridge) → then** sequence security hardening, memory, ingestion, and worker durability as deliberate rebuilds — not restorations.

---

## 2. Triage Philosophy — recovery is not restoration

The corpus is a **reconstruction specification**, not source. There is no clean `.py` to drop back in; CPython-3.14 bytecode is not cleanly decompilable, and the only fidelity we have is docstrings + names + constants + disassembly. Therefore every "rebuild" is a **deliberate authoring task**, costed like new work, justified on present value — never on the fact that the code once existed (decision rule 2).

That reframing changes the math. Restoration would bias toward "bring it all back." Reconstruction forces the real question: *does this module move PAS toward being queryable, adaptive, and operationally intelligent for a real design partner — now?* If not, it waits or it dies. 216 modules of internal governance, simulation scaffolding, and checkpoint self-checks do not survive that test; a handful of doctrine-core and runtime-blocking modules do.

---

## 3. Category Definitions

- **A — Rebuild Immediately.** Critical to doctrine, launch, security, or PAS210 readiness. A runtime blocker or a hard prerequisite for the next shippable proof.
- **B — Rebuild Later.** Genuine doctrine/operational value, but not blocking the immediate operational proof. Sequenced deliberately after PAS210.
- **C — Retire / Do Not Rebuild.** Obsolete, superseded by committed code, redundant, simulation-only, or checkpoint-only scaffolding. Kept in the corpus as reference; not reconstructed.
- **D — Investigate Further.** Genuinely ambiguous; cannot be categorized without deeper disassembly review. (Used sparingly — most ambiguity resolved at the module level inside a subsystem.)

---

## 4. Subsystem Triage Table

| Subsystem | Cat | Appears to contain | Doctrine impact | Launch impact | PAS210 dep | Effort | Recommendation |
|---|---|---|---|---|---|---|---|
| security | **A** (rate_limit) / B (rest) | Per-tenant rate limiting, API-key rotation/reveal, HTTPS enforcement, operator auth, CORS/redirect guards | Med (trust) | High (hardening) | **Yes** (rate_limit only) | Low (rate_limit) / Med (rest) | Rebuild `rate_limit` now (A); rest in PAS211 (B) |
| operator | **A** (circuit_breaker_policy) / B / C | Circuit breaker, fleet status, incidents, Merkle audit chain, cutover approval | Med (ops intel) | Med | **Yes** (circuit_breaker_policy only) | Low (policy) / High (audit chain) | `circuit_breaker_policy` now (A); fleet/incidents B; Merkle audit chain C |
| ingestion | **B** | Email/lead webhook ingestion, dedupe, Fernet secret store, parser, normalizers, pending-call durability | High (first-contact, queryable) | Med | No | High | PAS213, after PAS210 (rules 6, 8) |
| memory | **B** | Candidate pipeline, classifier, review/approval, rollout ledger, tenant-scoped store, console | High (adaptive, memory) | Med | No | High | PAS212, after PAS210 (rule 7) |
| worker | **B** | Pending-call auto-dial worker, heartbeat monitor/service | Med (durability) | Med | No | Med | PAS214 |
| callbacks | **B** | Callback schedule service + durable store | Med (operational proof) | Med | No | Med | PAS214 (with worker) |
| tenant | **B** | Tenant visibility service, audit dashboard, incident projection | Med (queryable per-tenant) | Low | No | Med | Pair with operator B / PAS211+ |
| routes | **B** (paired) | Thin route shells for ingestion/operator/tenant/learning/security services | Mirrors their service | Low alone | Partial | Low each | Rebuild only the route whose service is rebuilt |
| brokerage | **C** | Config validator, onboarding templates, profile service | Low (dup of `db/brokerage_store`) | Low | No | Low | Retire; revisit `onboarding_templates` only if onboarding automation is needed |
| outbound | **C** | PAS163 dial adapter | Low (superseded) | Low | No | Low | Retire — committed `routes/outbound.py` + state machine already dial via Twilio |
| monitoring | **C** | Alert contracts, detectors, dispatcher, Slack transport | Low (superseded) | Low | No | Med | Retire — committed proactive observer (PAS205) covers attention signals |
| optimization | **C** | Scenario×strategy matrix, ranking, recommendations | Low (superseded) | Low | No | Med | Retire — committed `simulation/strategies` + `recommendations` cover this |
| replay | **C** | Event reader, reconstruction, evaluator | Low (superseded) | Low | No | Med | Retire — committed `intelligence/queries` + workflow runtime cover event reads |
| learning | **C** (defer) | Locked-by-default controlled learning, guardrails, manual-test harness, CANDIDATE-only recs | Med (adaptive, but internal) | Low | No | High | Retire-for-now; revisit only after memory proves value |
| scripts_readiness | **C** | 77 PAS144–190 readiness/security checker scripts | None | Low (gate self-checks) | No | High if rebuilt | Retire wholesale; relax the 8 failing gates instead (rules 3, 10) |
| simulation/slack residue | **C** | PAS142 runner, PAS143B behavior, PAS172 Slack employee-mode blocks | Low (sim-only) | Low | No | Low | Retire — superseded by committed simulation + slack stacks |

---

## 5. Category A — Rebuild Immediately

**Scope: 2 modules. The only runtime blockers and the only hard PAS210 prerequisite.**

1. **`app/services/security/rate_limit`** (PAS-SECURITY-02 — per-tenant/per-surface rate-limit service; doc indicates a DB-backed counter store with an in-process fallback).
   - Imported lazily at `slack_command.py:159` (`check_rate_limit`). Today this raises `ImportError` on the rate-limited Slack path.
   - Rebuild the **minimal** importable surface (`check_rate_limit` + its fallback store) — not the full PAS-SECURITY-02 suite.
2. **`app/services/operator/circuit_breaker_policy`** (PAS189 — advisory, read-through circuit-breaker policy).
   - Imported lazily at `slack_command.py:694`. Same failure mode.
   - "Advisory read-through" means a safe minimal shim (default-allow when no breaker state exists) restores the path without rebuilding the full PAS188 breaker.

**Why A and nothing else:** decision rules 5 and 9 — security/runtime blockers before growth. These two break a *currently committed, live-wired* router (`slack_router` is included in `main.py:138`). No other recovered module is referenced by committed code.

> Not in A: broader security hardening, the snapshot bridge's data deps (already committed), and all doctrine subsystems. They are real but not immediate blockers.

---

## 6. Category B — Rebuild Later

Sequenced **after** PAS210, in deliberate value order:

- **memory** (PAS212) — candidate pipeline → classifier → review/approval → store/queries. The "adaptive / memory-candidate generation" doctrine pillar. High effort (28 modules); rebuild the generation+review core first, defer rollout-ledger/governance extras.
- **ingestion** (PAS213) — email/lead webhook ingestion, dedupe, Fernet secret store, parser, normalizers. The digital first-contact path; unlocks non-voice lead sources for a design partner. High effort. Sequence after the live snapshot bridge unless a specific design partner needs email intake on day one (rule 8).
- **worker + callbacks** (PAS214) — pending-call auto-dial durability, heartbeat, durable callback scheduling. Operational durability under load.
- **security (remainder)** (PAS211) — `api_key_rotation`, `api_key_reveal`, `https_enforcement`, `operator_auth`, `cors_policy`, `redirect_validation`, `error_safety`. The real PAS-SECURITY-01/03/04 hardening; pre-design-partner, post-import-repair.
- **operator (fleet_status, incident_log) + tenant visibility** — operational-visibility surface that makes a tenant "queryable." Medium effort; pair routes with services.

---

## 7. Category C — Retire / Do Not Rebuild

- **scripts_readiness (77)** — checkpoint self-check scaffolding. Do **not** reconstruct; instead relax/redirect the 8 failing gate tests to the real committed checkpoint set (rules 3, 10).
- **simulation/slack residue, optimization, replay, monitoring** — superseded by the committed simulation, intelligence, and proactive-observer stacks. No customer-facing value to reconstructing internal duplicates (rule 4).
- **outbound dial adapter** — committed `routes/outbound.py` + state machine already place Twilio calls; the PAS163 adapter is redundant.
- **brokerage service extras** — overlap `app/db/brokerage_store.py`; revisit only if onboarding automation becomes a need.
- **learning** — locked-by-default, CANDIDATE-only, manual-test-harness governance. Doctrine-adjacent ("adaptive") but internal and heavy; retire-for-now and revisit only if memory rebuild proves the adaptive loop is wanted.
- **operator Merkle audit chain (PAS174–178)** — elaborate tamper-evidence governance with no near-term customer value.

Retired modules **remain in the corpus** as reference; "retire" means *not reconstructed*, not *deleted*.

---

## 8. Category D — Investigate Further

**None at subsystem level.** Ambiguity was resolvable at module granularity (e.g., `operator` splits cleanly into A/B/C). If, during PAS211/PAS212, a specific module's contract proves unclear from its artifact, escalate that single module to a focused disassembly review then — not the whole subsystem now.

---

## 9. PAS210 Dependency Analysis

**PAS210 — Live Operational Snapshot Bridge — DEPENDS ON (all already committed except the import repair):**
- `app/services/proactive/supabase_snapshot_adapter.py` (PAS206) — read-only Supabase reader, **committed**.
- `app/services/proactive/observer*.py` + `app/services/slack/proactive_digest_intent.py` — observer logic + Slack surface, **committed**.
- Live `pas_events` / `leads` / `calls` / `bookings` rows — **already produced** by the committed voice engine and `/simulate-call`.
- **Category A import repair (PAS209.7)** — required, because the Slack surface that exposes the digest currently throws on `security/rate_limit` and `operator/circuit_breaker_policy`.

**PAS210 does NOT depend on:** ingestion, memory, learning, monitoring, optimization, replay, outbound, brokerage, tenant, callbacks, worker, scripts_readiness, or the simulation/slack residue.

**Conclusion:** PAS210 is buildable today on committed data + the committed PAS206 adapter, gated only by the two-module Category A repair. Memory and ingestion are **not** prerequisites (rules 6, 7, 8).

---

## 10. Recommended Next Sequence

1. **PAS209.7 — Security Runtime Import Repair** *(Cat A; low effort).* Rebuild minimal `security/rate_limit` (`check_rate_limit` + fallback store) and `operator/circuit_breaker_policy` (advisory shim), or guard the two lazy imports. Fix the 8 failing readiness-gate tests by relaxing them to the committed set. Unblocks the live Slack surface and PAS210.
2. **PAS210 — Live Operational Snapshot Bridge.** Promote the committed PAS206 adapter to the default snapshot provider (flag-gated, per-tenant, read-only); first true operational proof on live call/event data.
3. **PAS211 — Minimal Runtime Security Recovery.** Rebuild the PAS-SECURITY-01/03/04 hardening (api-key rotation/reveal, HTTPS enforcement, operator auth, CORS/redirect guards). Pre-design-partner.
4. **PAS212 — Memory Candidate Pipeline Rebuild.** Candidate generation → review/approval → tenant-scoped store. The adaptive/memory doctrine pillar.
5. **PAS213 — Digital Lead Ingestion Rebuild.** Email/lead ingestion + dedupe + Fernet secret store. First non-voice contact path.
6. **PAS214 — Worker Durability / Operational Queueing.** Pending-call durability, heartbeat, durable callback scheduling.

*Adjustment vs. the proposed order:* sequence is unchanged; the evidence confirms PAS209.7 must strictly precede PAS210 (rule 11), and PAS211 (security hardening) is placed immediately after PAS210 and before memory/ingestion because runtime/security precedes growth (rule 5).

---

## 11. What NOT to do

- **Do not rebuild all 216 modules.** ~190 are Category C or deferred-B; wholesale reconstruction is internal archaeology (rules 2, 4).
- **Do not clean `__pycache__` before this triage's rebuilds are complete.** The corpus is committed, but the bytecode remains the disassembly source of record until each rebuilt module is verified.
- **Do not treat the May 2026 reports (`pas169_launch_readiness_report.json`, `security_audit_report.json`, `integrity_check_report.json`) as current source truth.** They audit absent code.
- **Do not ship/push PAS210 before the Category A import repair (PAS209.7).** The Slack exposure path throws until then.
- **Do not rebuild the 77 readiness scripts wholesale.** Relax the failing gates instead; rebuild a checker only if it protects current committed work.
- **Do not rebuild a subsystem just because its corpus artifact is rich** (memory and operator are large and well-documented — richness is not priority).

---

## 12. Final Recommendation

Build **PAS209.7 — Security Runtime Import Repair** next: reconstruct only the two modules the live Slack router actually imports (`security/rate_limit`, `operator/circuit_breaker_policy`) from their corpus artifacts, with safe fallbacks, and relax the 8 stale readiness-gate tests. This is low-effort, removes the only runtime blocker in committed code, and is the sole recovered-work prerequisite for PAS210. Immediately after, build **PAS210 — Live Operational Snapshot Bridge** on the call/event data the voice engine already produces and the committed PAS206 adapter — delivering the first real "queryable, operationally intelligent" proof on a tenant's own pipeline. Everything else recovered (memory, ingestion, broader security, worker durability) is genuine but additive and is sequenced deliberately afterward; the large remainder — readiness scaffolding, simulation/replay/optimization/monitoring duplicates, and obsolete adapters — is retired in place, preserved in the corpus but not reconstructed.

---

## PAS209.7 — Security Runtime Import Repair (note)

**Status: completed.** Category A repair executed with scope strictly limited to
the two runtime-breaking lazy imports in `app/routes/slack_command.py`.

- Implemented minimal source modules from the PAS209.5 corpus *as specification*
  (docstring + symbol names + constants; no bytecode copied):
  - `app/services/security/rate_limit.py` — exposes `check_rate_limit(...)` (the
    only imported symbol) plus the coherent minimal surface
    (`resolve_rate_limit_policy`, `build_rate_limit_bucket_key`,
    `rate_limit_public_error`, closed `ALLOWED_SURFACES` / `DEFAULT_POLICIES`).
    Uses a **process-local fixed-window** counter — no DB, no network, no new
    dependencies — with conservative per-surface defaults and **fail-open** on
    error. The original durable `rate_limit_store` (Supabase-backed) remains a
    deferred rebuild (PAS211).
  - `app/services/operator/circuit_breaker_policy.py` — exposes
    `should_block_new_outbound_for_brokerage(...)`. Advisory, read-only,
    **fail-open** (`False`) — PAS188's `circuit_breaker` ledger is absent, so the
    advisory policy correctly reports "do not block."
  - Re-established `app/services/security/__init__.py` and
    `app/services/operator/__init__.py` as packages.
- Added narrow tests: `tests/mvp/test_pas209_7_security_import_repair.py` (imports
  resolve, expected symbols exist, Slack lazy-import sites no longer throw,
  conservative/fail-open defaults correct, bucket key is a PII-free sha256).
- **Scope was limited to import repair.** No other security/operator modules were
  reconstructed. **Full runtime security recovery remains PAS211**; the broader
  operator surface (audit chain, fleet status, incidents) and the durable
  rate-limit store remain deferred per the table above.

---

## PAS210 — Live Operational Snapshot Bridge (note)

**Status: completed.** The highest-leverage checkpoint from this triage is built.

- New module `app/services/proactive/live_snapshot_bridge.py` bridges the PAS207
  needs-attention surface from the demo snapshot to **real per-tenant Supabase
  data** via the committed PAS206 adapter — read-only, feature-flagged, tenant
  scoped, fail-closed, source-transparent. Wired into `app/routes/slack_command.py`.
- Single flag: `PAS_LIVE_OPERATIONAL_SNAPSHOT_ENABLED` (literal `"true"` enables
  live; anything else preserves demo behaviour exactly).
- Confirms the dependency analysis above: PAS210 used **only** committed assets
  (PAS206 adapter + live `pas_events`/`leads`/`calls`/`bookings`) plus the
  PAS209.7 import repair. It did **not** require ingestion (PAS213), memory
  (PAS212), or broader security (PAS211) — those remain deferred as triaged.
- Tests: `tests/mvp/test_pas210_live_snapshot_bridge.py` (default-demo, live,
  brokerage required, fail-closed, adapter-failure, no-silent-mixing, source-mode
  transparency, demo preserved, tenant-scoped read). The PAS207 dispatcher
  precedence guard was updated to the new bridge call (precedence unchanged).

Next per the sequence above: **PAS211 — Minimal Runtime Security Recovery**.

---

*End of PAS209.6 triage + PAS209.7 repair note + PAS210 bridge note.*
