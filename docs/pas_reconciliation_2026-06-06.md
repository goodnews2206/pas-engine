# PAS — Repository State & Launch Readiness Reconciliation

**Date:** 2026-06-06
**Author role:** Lead Architect / Technical Auditor
**Type:** Documentation only — no code changed, no files restored, no caches deleted
**Scope of evidence:** Git history, working tree, source imports, full test run, and the standing JSON reports in the repository root.

---

## 0. Why this document exists

The working assumption coming into this review was that checkpoints **PAS160–PAS168 were complete** and that **PAS169 (crypto verification readiness)** was the sole remaining launch blocker.

A full reconciliation of the repository against that assumption shows it is **no longer accurate**. The prior reports describe a system that is not present in version control. This document records the verified reality so that future planning starts from source-of-truth rather than from stale reports.

> This is a documentation artifact only. It does not restore files, delete stale bytecode, modify code, touch PAS209, touch any parked stash, or implement PAS210.

---

## 1. Headline conclusions

1. **PAS160–169 cannot currently be treated as real committed work.** There are no PAS160–169 commits in git history, and the files those checkpoints were said to deliver are absent from both the committed tree and the working directory. They existed only as local, never-committed files and have since been removed; the only residue is stale compiled bytecode under `__pycache__`.

2. **PAS169 is no longer the launch blocker, because the code it audited is absent.** `pas169_launch_readiness_report.json` reports `verdict: READY` over a set of files (encrypted email-forwarder secret store, crypto round-trip gate, memory review modules) that are not in the repository. The verdict cannot be reproduced. The blocker is moot; the real blocker is provenance reconciliation.

3. **PAS today is a working voice MVP plus two demo-grade layers.** The committed reality is: (a) a functional Twilio voice-call qualification engine, (b) a simulation + proactive + intelligence + Slack-operator analytics stack that runs on synthetic scenarios and hardcoded demo snapshots, and (c) a Next.js product/UX prototype driven entirely by mock data with no backend calls.

4. **The highest-leverage next checkpoint is PAS210 — Live Operational Snapshot Bridge:** point the already-built proactive/intelligence/Slack stack at real per-tenant Supabase data instead of the hardcoded demo snapshot.

5. **PAS210 must be preceded by provenance reconciliation:** decide whether the lost, never-committed PAS160–169 work is recoverable (and recommit it) or formally retire it, and fix two runtime-breaking imports.

---

## 2. Repository reality (verified)

| Signal | Finding | How verified |
|---|---|---|
| Real repository | `pas-engine/pas-engine/` (the outer folder is a wrapper holding `AlexCallWidget.jsx` and `.env.backup.outer`) | directory + `git` inspection |
| Commit count | 141 | `git rev-list --count HEAD` |
| Current branch | `pas301-identity-ownership-session-workspace-lifecycle` = `main` + 4 PAS301–303 doc files | `git diff --stat main HEAD` → 4 docs, 2150 insertions |
| Working tree | Clean (no uncommitted changes) at time of audit | `git status --short` empty |
| Checkpoints present in git | PAS125, PAS145, **PAS190–209**, **PAS300–303** | `git log --all` checkpoint grep |
| Checkpoints **absent** from git | **PAS160–169** (and the PAS170–189 lineage referenced by readiness gates) | same |
| Test result | **1193 passed, 8 failed** (7m35s) | `python -m pytest tests` |

---

## 3. The PAS160–169 mismatch

### 3.1 What the prior reports claim

Three standing reports in the repository root assert success over the PAS160–169 lineage:

- `pas169_launch_readiness_report.json` (generated 2026-05-17) — `verdict: READY`, `blocker_count: 0`, 47/47 checks PASS. It asserts the presence of, among others:
  - `app/services/ingestion/email_forwarder_secret_store.py`
  - `app/routes/email_ingestion.py`
  - `app/services/memory/review.py`, `review_stats.py`, `operator_console.py`
  - `scripts/pas169_crypto_roundtrip_check.py`, `scripts/pas169_launch_readiness_check.py`
  - prior-phase scripts `scripts/pas160_*` … `scripts/pas168_*`
- `security_audit_report.json` (2026-05-09) — `CRITICAL: 0`, `HIGH: 0`.
- `integrity_check_report.json` (2026-05-09) — 15/15 passed (replay, contract normalization).

### 3.2 What the repository actually contains

Every PAS160–169 file named above is **missing from both `HEAD` and the working tree**, and **was never committed** to git:

```
app/routes/email_ingestion.py                              => NEVER COMMITTED, not on disk
app/services/ingestion/email_forwarder_secret_store.py     => NEVER COMMITTED, not on disk
app/services/memory/review.py                              => NEVER COMMITTED, not on disk
app/services/security/rate_limit.py                        => NEVER COMMITTED, not on disk
scripts/pas169_launch_readiness_check.py                   => NEVER COMMITTED, not on disk
```

Verified via `git log --all -- <path>` (no history) and `git cat-file -e HEAD:<path>` (not in HEAD).

### 3.3 Stale bytecode is the only residue

Thirteen service directories contain **only** `__pycache__` bytecode and **no source files**:

`ingestion, memory, outbound, callbacks, worker, monitoring, operator, optimization, replay, learning, brokerage, security, tenant`

Example surviving artifacts with no corresponding source:
- `app/services/security/__pycache__/` → `rate_limit.pyc`, `api_key_rotation.pyc`, `https_enforcement.pyc`, `operator_auth.pyc`, `cors_policy.pyc`, …
- `app/services/tenant/__pycache__/` → `tenant_visibility_service.pyc`, `tenant_incident_projection.pyc`, `tenant_audit_dashboard.pyc`, …

**Conclusion:** the PAS160–169 operational MVP (lead/email ingestion, encrypted secret store, memory-candidate review, security controls, tenant isolation) was developed locally, produced the May 2026 reports, and was deleted without ever entering version control. **It cannot currently be treated as real committed work.**

> Per the constraints of this task, this report does **not** investigate the `backups/` directory or attempt recovery, and does **not** delete the stale bytecode. Both are deferred to the provenance-reconciliation action (Section 9).

---

## 4. What is actually committed and working

### 4.1 Voice call engine — present, imports resolve, README matches
- `app/engine/state_machine.py` — 950-line qualification FSM (GREETING → INTENT → BUDGET → TIMELINE → BOOKING → CLOSING → DONE), Claude-backed objection handling with safe fallback, PAS128 callback-capture subflow, warm transfer, outbound prefill-skip.
- `app/routes/twilio_webhook.py`, `outbound.py`, `websocket_handler.py` — Twilio signature verification, answering-machine detection, media-stream STT→engine→TTS pipeline, fire-and-forget post-call tasks.
- Booking `app/services/booking/calcom_client.py`; STT `app/services/stt/deepgram_client.py`; TTS `app/services/tts/elevenlabs_client.py`; notifications (Slack/SMS/email).
- The core engine imports only modules that exist; it does **not** import any of the 13 empty directories.

### 4.2 Data layer — present, multi-tenant by application-layer scoping
- `app/db/` (11 modules): leads (`lead_memory.py`), calls, bookings, agents, events (`pas_events`, append-only), brokerages, errors, invites, audit_log.
- Schema `scripts/schema.sql` + migrations `migrate_v2.sql … migrate_v7.sql`.
- Tenancy enforced via explicit `brokerage_id` filters in query code. RLS is `ENABLE`d on tables but **no policies are defined**, and all access uses the Supabase **service key** (which bypasses RLS).

### 4.3 Analytics stack (PAS190–209) — real logic, synthetic input
- Simulation (`app/services/simulation/`, 14 files), proactive observer (`app/services/proactive/`), intelligence/leakage (`app/services/intelligence/`), Slack operator (`app/services/slack/`, 10 files + 12 read-only intents).
- The logic is real and deterministic, but it operates on **20 hand-authored scenarios** and a **hardcoded demo snapshot**, and self-marks output `SIMULATION_ONLY` / `live_behavior_changed: False`. The Supabase snapshot adapter (PAS206) exists but is **not** the default provider.

### 4.4 Product/UX prototype (PAS300–303)
- `web/` — Next.js 15 / React 19, 16 operational surfaces, 111 components, driven entirely by `web/lib/demo/` mock data. **Zero backend calls** (`fetch`/`axios`/HTTP) found.

---

## 5. Missing subsystems (relative to doctrine)

| Doctrine area | State in repository |
|---|---|
| Lead ingestion (email/webhook), dedup, validation, queueing | **Absent.** `app/services/ingestion/` empty. Only ingestion path is the live Twilio voice webhook. |
| Memory candidate generation + review/approval | **Absent as a subsystem.** `app/services/memory/` empty. Lead *facts* persist via `app/db/lead_memory.py`, but no candidate generation or approval workflow exists in the tree. |
| Proactive → live data | Defaults to `build_demo_snapshot()`; PAS206 adapter not wired as default. |
| Web → backend | Prototype is 100% mock data; no integration. |
| Auth (PAS301–303) | Design docs only; `app/auth/principal.py` defines JWT roles but no route validates a token. Legacy API-key auth is what runs. |
| Audit logging | Table + `audit_log.py` exist but are not called by the running app. |
| Background workers | `PENDING_CALLS_WORKER_ENABLED` referenced; no worker started at boot. |

---

## 6. Failing readiness checks

The full test run is **1193 passed, 8 failed**. All 8 failures are **readiness-gate self-checks**, not logic bugs. They fail because prior-phase readiness scripts are missing from disk:

```
FAILED tests/mvp/test_pas191_slack_natural_language_commands.py::test_readiness_gate_exits_ready
FAILED tests/mvp/test_pas191_slack_natural_language_commands.py::test_readiness_gate_json_mode_emits_valid_envelope
FAILED tests/mvp/test_pas191_slack_natural_language_commands.py::test_pas186_carry_forward_ready
FAILED tests/mvp/test_pas191_slack_natural_language_commands.py::test_pas187_carry_forward_ready
FAILED tests/mvp/test_pas191_slack_natural_language_commands.py::test_pas188_carry_forward_ready
FAILED tests/mvp/test_pas191_slack_natural_language_commands.py::test_pas189_carry_forward_ready
FAILED tests/mvp/test_pas191_slack_natural_language_commands.py::test_pas190_carry_forward_ready
FAILED tests/mvp/test_pas192_slack_operator_experience.py::test_pas191_readiness_gate_still_ready
```

Representative error: `[BLOCK] prior_phase:scripts/pas179_controlled_learning_readiness_check.py — missing — PAS191 must not delete.` (and pas180, pas181, pas182, … "and 18 more").

**Interpretation:** the test suite is independently corroborating Section 3 — a large body of prior-phase checkpoint scripts (PAS179–PAS190) was deleted, and the gates that assert their continued presence now fail.

---

## 7. Security gaps

**Present and sound:** Twilio (HMAC-SHA1) and Slack (HMAC-SHA256 + timestamp) signature verification; request body-size limit; per-IP rate limiting on calls/webhooks; weak-admin-key rejection in production; suppressed httpx logging to avoid key leakage; PII sanitization in the portal/intelligence layer; secret-redaction logic in `audit_log._redact()`.

**Gaps:**
1. **The security-hardening checkpoint (PAS169) is not in the tree.** Encrypted secret store, crypto round-trip gate, and the security-control modules (`rate_limit`, `api_key_rotation`, `https_enforcement`, `operator_auth`) survive only as stale `.pyc`. The "READY" verdict cannot be reproduced.
2. **Two runtime-breaking lazy imports:** `app/routes/slack_command.py:159` imports `app.services.security.rate_limit` and `:694` imports `app.services.operator.circuit_breaker_policy` — both empty directories. Boot survives (lazy imports), but those Slack code paths raise `ImportError` when exercised.
3. **Tenant isolation is application-layer only.** RLS enabled but no policies; service key bypasses RLS. A single missing `brokerage_id` filter in a future query would cross tenants.
4. **Plaintext secrets at rest:** `brokerages.api_key` and `brokerages.slack_signing_secret` are unencrypted (encryption was the deleted PAS169).
5. **Audit trail not wired** — no tamper-evident mutation record today.

---

## 8. Launch readiness & doctrine alignment

### 8.1 Launch readiness
- **Voice MVP:** runnable; the README's own "Definition of Done" checklist is entirely unchecked — no evidence of a verified end-to-end real call in this tree. *Demo-ready, not launch-verified.*
- **Analytics stack:** not launchable as operational intelligence — self-declared `SIMULATION_ONLY` on demo snapshots.
- **Web product:** not launchable as a product — no backend integration.
- **Security:** the hardening that would gate a launch is missing; two Slack paths throw at runtime.

**Verdict: NOT launch-ready.** The "PAS169 is the only blocker" framing is invalid; the true blockers are provenance reconciliation and the demo→live data bridge.

### 8.2 Doctrine alignment — *"queryable, adaptive, operationally intelligent"*

| Pillar | Alignment | Why |
|---|---|---|
| Queryable | Partial | Intelligence/leakage/event-query helpers and 12 Slack read-only intents are real, but they query demo snapshots and `pas_events`; the "PAS Brain" web surface is mock. |
| Adaptive | Not yet (sim-only) | Simulation strategies + `self_trainer.py` exist, but everything is `live_behavior_changed: False`. |
| Operationally intelligent | Partial | The proactive observer computes 10 real attention signals, but defaults to a hardcoded 2-lead demo snapshot. |
| Multi-tenant | Aligned at app layer, fragile below | Correct `brokerage_id` scoping; no RLS depth. |
| First-contact / booking | Aligned (voice), absent (digital) | Voice qualification + Cal.com booking real; email/web/form ingestion absent. |

**Reading:** PAS has built the *instruments* of an operationally intelligent company, but they are wired to rehearsal data. The gap to doctrine is one integration seam, not a missing capability set.

---

## 9. Recommended next checkpoint — PAS210 (Live Operational Snapshot Bridge)

**Goal.** Make the existing proactive + intelligence + Slack stack run on real per-tenant Supabase data instead of `build_demo_snapshot()`. Promote the committed PAS206 `supabase_snapshot_adapter.py` to the default snapshot provider for the observer and the Slack "needs-attention" intent, scoped by `brokerage_id`, behind a feature flag, with the demo snapshot retained as explicit fallback.

**Why now.** Every required component already exists and is committed: the observer logic, the read-only adapter, the Slack surface, and the `pas_events`/`leads`/`calls`/`bookings` stream the voice engine already writes. The only thing between "rehearsal" and "real operational intelligence" is the default-provider seam.

**Dependencies.** Live event/lead/call/booking rows (already produced by the voice + simulate paths); committed PAS206 adapter; existing tenant scoping. No dependency on the missing ingestion/memory/security checkpoints.

**Risks.** Real data exercises shapes the demo snapshot never did → the observer's hardcoded thresholds need calibration; must preserve read-only / SIMULATION-safe guarantees; the two broken Slack imports must be fixed first or the Slack path will throw.

**Business value.** First moment PAS says something true about a brokerage's *own* pipeline — the demoable proof of doctrine.

**Technical value.** Establishes the live-data contract every other surface reuses and forces threshold calibration against reality, retiring the largest source of demo-only debt.

> This report does **not** implement PAS210.

---

## 10. Pre-PAS210 actions (provenance first)

1. **Reconcile provenance.** Determine whether the never-committed PAS160–169 work is recoverable (investigate `backups/`, the stale `.pyc` modules, and other machines) and either recommit it or formally retire it. Until then, treat `pas169_launch_readiness_report.json`, `security_audit_report.json`, and `integrity_check_report.json` as historical — they audit absent code.
2. **Fix the two runtime-breaking Slack imports** (`slack_command.py:159`, `:694`).
3. **Resolve the 8 failing readiness-gate tests** — restore the asserted scripts or update the gates to the real checkpoint set.
4. **Remove stale `__pycache__`** for the 13 empty service directories (deferred; not done here).
5. **Add RLS policies (or a documented decision not to)** and **encrypt `brokerages.api_key` / `slack_signing_secret`** at rest — the actual hardening the missing PAS169 was meant to deliver.
6. **Then proceed to PAS210.**

---

## 11. One-line reconciliation

> The prior reports no longer match the repository: PAS is a working voice MVP plus two demo-grade layers (analytics and UI), not a system one crypto-blocker from launch. PAS169 is moot because the code it audited is absent. The highest-leverage next move is to point the already-built operational-intelligence stack at live tenant data (PAS210) — but only after reconciling the lost, never-committed PAS160–169 work and fixing two runtime-breaking imports.

---

## 12. PAS210 — Live Operational Snapshot Bridge (completed)

The bridge identified throughout this report is now built. PAS210 is the **first
operational-intelligence bridge**: it points the already-committed PAS205
observer / PAS207 needs-attention surface at **real per-tenant Supabase data**
via the committed PAS206 read-only adapter, instead of the demo snapshot.

Properties (all by construction):
- **Read-only.** No writes, no scheduling, no outbound actions, no mutations.
- **Feature-flagged.** Single flag `PAS_LIVE_OPERATIONAL_SNAPSHOT_ENABLED`; unset
  or non-`"true"` → demo behaviour is byte-for-byte unchanged.
- **Tenant-scoped, fail-closed.** Live mode requires a non-empty `brokerage_id`;
  missing tenant → explicit *unavailable*, never inferred or cross-tenant.
- **No silent fallback / mixing.** A live-adapter failure returns an explicit,
  labelled *unavailable* state — never a silent demo blend.
- **Source-transparent.** Every result carries `source_mode` ∈ {demo, live,
  unavailable}; the event stream records it.

Implementation: `app/services/proactive/live_snapshot_bridge.py`, wired into the
PAS207 path in `app/routes/slack_command.py`. Observer, renderer, adapter, and
matcher logic are unchanged. This is the moment PAS can tell a brokerage
something **true about its own pipeline** — the doctrine's "queryable,
operationally intelligent" claim made real on live data, still strictly observe-only.

---

*End of reconciliation report. PAS210 (live snapshot bridge) completed read-only and feature-flagged; PAS160–169 recovery work and the deferred rebuilds (PAS211+) remain as separately tracked. No files restored, no caches deleted, PAS209 untouched, parked stash untouched.*
