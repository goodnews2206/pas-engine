# PAS211 — Minimal Runtime Security Recovery

**Type:** Specification — documentation only. No runtime code, tests, migrations, or security modules are restored here. This scopes the *smallest* set of security work needed to protect the functionality PAS has **today**, and explicitly retires the rest of the lost PAS169 suite.

**Framing:** This is **not** PAS169 reconstruction, not recovery archaeology, not an enterprise security platform. It is a runtime-protection checkpoint: *protect what exists.*

---

## 1. Executive Summary

The committed PAS runtime is **already protected by most of the controls it needs** — Twilio and Slack signature verification, admin/brokerage API-key auth, two in-process rate limiters, a body-size limit, a production CORS allow-list, and working API-key rotation. PAS209.7 already restored the one security module the live code imports (`rate_limit`).

Therefore "minimal recovery" is mostly **affirmation, not reconstruction.** The audit surfaces only **two genuinely missing runtime protections** that affect current functionality:

1. **Secrets are stored in plaintext at rest** (`brokerages.api_key`, `brokerages.slack_signing_secret`) — the one **critical** data-protection gap. PAS169's encrypted secret store is gone.
2. **An environment-default footgun:** `ENVIRONMENT` defaults to `"development"`, and every production guard (Twilio signature enforcement, weak-admin-key refusal, `/docs` exposure) keys off `ENVIRONMENT == "production"`. An unconfigured production deploy **silently disables** those guards.

Almost the entire recovered PAS-SECURITY corpus (api_key_rotation, redirect_validation, operator_auth, cors_policy, dependency_scanner, api_key_reveal, Merkle/audit chains) is **redundant or unused** against today's functionality and is **retired**. The recommendation is to **split PAS211**: a tiny PAS211A config-hardening pass now, and a scheduled PAS211B (at-rest secret encryption + RLS defense-in-depth) before a real brokerage's live PII flows through PAS.

---

## 2. Scope

**In scope:** protections for the *currently committed* surfaces — PAS210 live reads, the Slack operator surface, Twilio webhooks, Supabase access, and the admin/portal/outbound API surfaces.

**Out of scope (explicitly retired):** rebuilding all security modules, operator audit chains, Merkle inclusion proofs, checkpoint scaffolding, durable rate-limit RPC, dependency scanning, and any enterprise/unused feature. No dependencies added. PAS209, the parked stash, and `__pycache__` are untouched.

---

## 3. Current Security Surface (evidence)

| Control | Status today | Evidence |
|---|---|---|
| Twilio signature verification | Present; enforced in prod, disabled in dev | `twilio_webhook.py:47,124` (`_verify_twilio`); `demo.py:94` `RequestValidator` |
| Slack signature verification | Present (HMAC + timestamp); rejects if no secret | `slack_command.py:151-155` `_verify_slack_signature` |
| Admin auth (X-Admin-Key) | Present; weak-key refusal **in prod** | `admin.py:61-63` `require_admin`; `main.py:65` |
| Brokerage auth (X-API-Key) | Present | `portal.py:86` `require_brokerage`; `outbound.py:64` |
| Rate limiting (outbound/twilio/sim) | Present, in-process | `utils/rate_limiter.py` via `outbound.py:74` (20/min), `twilio_webhook.py:44` (60/min) |
| Rate limiting (Slack) | Present (PAS209.7 rebuild) | `services/security/rate_limit.py` via `slack_command.py:163` |
| Body-size limit | Present (middleware) | `main.py:119` `BodySizeLimitMiddleware` |
| CORS | Dev permissive; **prod allow-list** | `main.py:124-130` (`BASE_URL` origins in prod) |
| API-key rotation | **Present & wired** | `admin.py:269` → `brokerage_store.rotate_api_key` |
| Tenant scoping | App-layer `.eq("brokerage_id")`; **RLS enabled, no policies**; service key bypasses RLS | `supabase_client.py:18` (service key); per-query filters |
| Secrets at rest | **Plaintext** | `schema.sql:14-15` (`slack_signing_secret TEXT`, `api_key TEXT`) |
| `ENVIRONMENT` default | **`"development"`** | `config.py:56` |

---

## 4. Runtime Audit

### Task 1 — Security module → current relevance

| Security capability | Referenced today? | Critical? | Rebuild? | Retire? | Reason |
|---|---|---|---|---|---|
| `rate_limit` (Slack) | **Yes** (`slack_command.py:163`) | Yes | Done (PAS209.7) | No | Already restored, minimal in-process. |
| `utils/rate_limiter` | **Yes** (outbound/twilio/sim) | Yes | No (exists) | No | Committed and working. |
| Twilio signature | Yes | Yes | No (exists) | No | Enforced in prod. |
| Slack signature | Yes | Yes | No (exists) | No | Enforced; fail-closed on missing secret. |
| Admin/brokerage auth | Yes | Yes | No (exists) | No | `require_admin` / `require_brokerage`. |
| `api_key_rotation` (corpus) | **No** (superseded) | — | No | **Retire** | Rotation already exists via `brokerage_store.rotate_api_key`. |
| `api_key_reveal` (corpus) | No consumer | No | No | **Retire/Later** | Onboarding returns the key directly; no reveal surface. |
| `cors_policy` (corpus) | No (inline CORS) | No | No | **Retire** | Prod allow-list already handled in `main.py`. |
| `https_enforcement` (corpus) | No | No | No (later) | **Later** | Platform terminates TLS; app-layer header hardening is a later nicety. |
| `operator_auth` (corpus) | No | No | No | **Retire** | `require_admin` suffices; consolidation unneeded now. |
| `redirect_validation` (corpus) | **No surface** | No | No | **Retire** | No redirect endpoints exist (no open-redirect surface). |
| `dependency_scanner` (corpus) | No | No | No | **Retire** | Report-only ops tooling, not runtime protection. |
| `rate_limit_store` / `rate_limit_rpc` (corpus) | No | No | No (later) | **Later** | Durable/atomic backend only needed if multi-instance. |
| `error_safety` (corpus) | Partial (inline) | No | No (later) | **Later** | Uniform public error envelopes — incremental hardening. |
| Operator audit chain / Merkle (corpus) | No | No | No | **Retire** | Out of scope by rule; no current consumer. |
| At-rest secret encryption | No | **Yes** | **Later (PAS211B)** | No | Plaintext `api_key`/`signing_secret`; real data-protection gap. |
| RLS policies | No (enabled, empty) | High | Later (PAS211B) | No | App-layer only; service key bypasses RLS. |

---

## 5. Recovery Corpus Findings (Task 2)

The recovered `security/` corpus (PAS-SECURITY-01..04) maps as follows:
- **Already satisfied by committed code:** rate limiting (PAS209.7 + utils), API-key rotation (`brokerage_store`), CORS allow-list (inline).
- **No current runtime relevance → retire:** `api_key_rotation` (redundant), `redirect_validation` (no surface), `operator_auth` (require_admin suffices), `cors_policy` (inline), `dependency_scanner` (ops tooling), `api_key_reveal` (no consumer), Merkle/audit-chain (out of scope).
- **Deferred (genuine but not blocking today):** `https_enforcement`, `error_safety`, `rate_limit_store`/`rate_limit_rpc` (durable/shared limiting).
- **Doctrine-critical but represented only as the *idea*, not this module:** at-rest secret encryption — rebuild a **minimal** Fernet-column variant in PAS211B, **not** the full PAS167/168 kid-rotation envelope.

**Default stance honored:** do not rebuild by default. Only two small protections are recommended, and only one corpus idea (encryption) is carried forward in minimal form.

---

## 6. Required Now (Task 3 — smallest protective set)

Nothing from the corpus needs reconstruction. "Required now" is **two tiny config-hardening guards** that protect existing functionality at near-zero risk:

- **RN-1 — Production environment assertion (fail-fast).** Refuse to start (or loudly hard-warn) when production indicators are present (e.g. `BASE_URL` is an https domain / a `PORT` from the platform) but `ENVIRONMENT != "production"`. Closes the dev-default footgun that silently disables Twilio signature enforcement and exposes `/docs`.
- **RN-2 — No silent signature bypass in prod.** Make the Twilio (and Slack) "verification disabled" path explicit and impossible under `ENVIRONMENT == "production"`; ensure it can only be skipped under an explicit, logged dev flag.

These are small, isolated, and consistent with the read-only doctrine. Plus: **confirm and keep** the existing controls (signatures, auth, both rate limiters, body limit, CORS allow-list, rotation) — no rebuild required.

---

## 7. Required Later (PAS211B + beyond)

- **RL-1 (Critical, data protection) — At-rest secret encryption.** Encrypt `brokerages.api_key` and `slack_signing_secret` with a minimal Fernet column (decrypt-on-read seam), plaintext fallback during migration. Needs a migration + key management. Required **before** a real brokerage's secrets live in PAS.
- **RL-2 (High) — RLS policies.** Add per-tenant Row-Level Security as defense-in-depth beneath the app-layer `brokerage_id` filters.
- **RL-3 (Medium) — Durable/shared rate-limit store.** Only when PAS runs multi-instance; until then in-process is acceptable.
- **RL-4 (Medium) — Wire audit logging.** `audit_log` exists but is unwired; record mutations on admin/rotation paths.
- **RL-5 (Low) — `error_safety` + security headers / app-layer HTTPS.** Uniform public error envelopes; HSTS et al.

---

## 8. Retired Security Work (Task — do not rebuild)

`api_key_rotation` (redundant), `cors_policy` (inline), `operator_auth` (superseded), `redirect_validation` (no surface), `dependency_scanner` (ops tooling), `api_key_reveal` (no consumer), `rate_limit_rpc` (no durable store yet), and **all operator audit chains / Merkle inclusion proofs / checkpoint scaffolding**. These remain preserved in the PAS209.5 corpus as reference; they are **not reconstructed**.

---

## 9. Critical Risks (Task 4 — ranked, current functionality only)

| Rank | Risk | Affected surface | Mitigation |
|---|---|---|---|
| **Critical** | Plaintext secrets at rest (`api_key`, `slack_signing_secret`) | Supabase | RL-1 (PAS211B encryption) |
| **High** | `ENVIRONMENT` dev-default silently disables prod guards (Twilio sig, weak-admin refusal, `/docs` hidden) | Twilio, admin, API docs | RN-1 + RN-2 (PAS211A) |
| **High** | Tenant isolation app-layer only; RLS empty; service key bypasses RLS | All tenant data | RL-2 (RLS policies) |
| **Medium** | In-process rate limiting (per-instance, resets on restart) | outbound/twilio/slack | RL-3 (durable store, if multi-instance) |
| **Medium** | No audit trail of mutations | admin/rotation | RL-4 (wire `audit_log`) |
| **Low** | No app-layer HTTPS enforcement / security headers | all HTTP | RL-5 |
| **Low** | Minimal key reveal/rotation UX | onboarding/admin | optional |

---

## 10. Recommended Recovery Plan

1. **PAS211A (now, ~days, tiny):** RN-1 + RN-2 config-hardening guards; affirm existing controls; **retire** the redundant corpus modules in §8 by decision (no code). Read-only-safe, no migration.
2. **PAS211B (scheduled, before live customer PII):** RL-1 at-rest secret encryption (minimal Fernet column) + RL-2 RLS policies. Requires one migration + key management; sequence ahead of onboarding a real brokerage's secrets.
3. **Later/opportunistic:** RL-3, RL-4, RL-5 as PAS scales past single-instance / needs audit/compliance.

---

## 11. PAS212 Impact

PAS212 (Memory Candidate Pipeline) is unaffected by **PAS211A** and can follow it immediately — RN-1/RN-2 are config guards that don't touch the memory path. **PAS211B** (encryption + RLS) is independent of PAS212 and can run **in parallel**; it is a prerequisite for *live customer data*, not for the memory rebuild or the demo. No conflict either way.

---

## 12. Final Recommendation

### Task 6 — What should PAS211 be?
**C — Split into PAS211A / PAS211B.**
- **Why not A (doc-only):** the dev-default footgun (RN-1/RN-2) is a real, cheap-to-fix runtime exposure; leaving it purely documented wastes a near-zero-cost win.
- **Why not B (implement everything now):** at-rest encryption + RLS (RL-1/RL-2) need a migration and key management and shouldn't be rushed; bundling them with the tiny config guards over-scopes the checkpoint.
- **Why C:** PAS211A delivers the small, safe, high-value runtime guards immediately; PAS211B schedules the genuinely important data-protection work (encryption + RLS) deliberately, before any real brokerage's secrets/PII flow through PAS. This is the honest "protect what exists" outcome — minimal rebuild, maximal protection-per-effort.

### Task 7 — Does PAS212 remain the correct next checkpoint?
**Yes.** After PAS211A, **PAS212 (Memory Candidate Pipeline)** remains the correct next *growth* checkpoint per the PAS209.6 sequence. PAS211B (encryption/RLS) is a data-protection prerequisite for going *live with a real customer's data* and can proceed in parallel with PAS212 without conflict — it does not displace PAS212 in the build order, but it must land before a paying brokerage's secrets are stored.

---

## PAS211A — Implementation note (completed)

**Status: implemented.** The two Required-Now config-hardening guards are live; no corpus modules were rebuilt, no migration, no encryption, no RLS.

- **RN-1 — Production config guard (implemented).** `app/config.py` adds production
  indicators (`RENDER`, `VERCEL`, `FLY_APP_NAME`, `HEROKU_APP_NAME`, `DYNO`,
  `RAILWAY_ENVIRONMENT`/`RAILWAY_PROJECT_ID`/`RAILWAY_SERVICE_ID`,
  `KUBERNETES_SERVICE_HOST`, and an `https://` non-localhost `BASE_URL`) plus
  `is_production` / `looks_like_production()` / `validate_runtime_security()`.
  `app/main.py` calls `validate_runtime_security()` at startup: a production-like
  host running with a non-production `ENVIRONMENT` now **fails fast** instead of
  silently running on dev defaults. Local development (no indicators) is unaffected.
- **RN-2 — Signature bypass blocked in production (implemented).** Twilio
  verification is now gated on `settings.require_twilio_signature` (True in every
  non-development environment) in both `/twilio/voice` and `/twilio/status`, so a
  forged webhook can never be silently accepted in production. Slack already fails
  closed on a missing signing secret (`slack_command.py:152-154`); a regression
  test now guards it. RN-1 additionally guarantees a production host can never be
  in the dev-bypass state.
- **Tests:** `tests/mvp/test_pas211a_production_config_guards.py` (12) — fail-fast
  on prod-indicator + non-production env, https-BASE_URL indicator, explicit
  `production`/`prod` allowed, dev preserved, Twilio `/voice` + `/status` reject
  unsigned requests in production, Slack fail-closed on missing secret.
- **PAS211B still pending:** at-rest secret encryption (RL-1, critical) and RLS
  policies (RL-2) remain the scheduled data-protection work before a real
  brokerage's secrets/PII flow through PAS. PAS211A did **not** touch encryption,
  RLS, memory, or ingestion.

---

*End of PAS211 specification + PAS211A implementation note. PAS211A added only config guards and tests; no migration, encryption, RLS, or restored corpus modules. PAS209 untouched, parked stash untouched, no `__pycache__` deleted, no dependencies added.*
