# PAS211G — Admin / JWT / RBAC + Scoped Client Plan

**Status: PLAN / SPEC ONLY.** No runtime code, no JWT implementation, no new
dependency, no migration, no Supabase policy created in this checkpoint. This is
the architecture that makes the PAS211E RLS policy proposal (`migrate_v9`)
actually enforce, and that takes PAS from "one shared admin key + one API key per
tenant" to per-user identity with roles — the prerequisite for paid-client
onboarding.

---

## 1. Executive summary

Today PAS has **two shared secrets** doing all the work: a single `ADMIN_API_KEY`
(all of `/admin/*`) and one `api_key` per brokerage (all of `/portal/*`,
`/ingest/lead`, `/outbound/*`). There is **no per-user identity, no JWT
enforcement, and no role layer** in the running app — `app/auth/principal.py`
defines a `Principal` dataclass + roles but **nothing constructs one** (the
resolver was always deferred to "PAS133B", which never shipped). Every DB call
uses the **service-role key**, which **bypasses RLS**, so the `migrate_v9`
tenant policies are inert.

PAS211G's job is to design — not yet build — the path to:
1. A **JWT validation boundary** that turns a Supabase Auth token into a
   `Principal`.
2. **Route-level RBAC** enforced from that `Principal`.
3. A **scoped (non-service-role) Supabase client** for tenant-facing reads so
   RLS finally bites.
4. A **compatibility window** so existing API-key ingestion/demo flows never
   break during the transition.

This document is the contract the implementation checkpoints (PAS211G.1–.7)
build against.

---

## 2. Current auth reality (audited)

| Surface | What exists today | Evidence |
|---|---|---|
| Admin auth | Single static `ADMIN_API_KEY`, constant-time compare (PAS211D), on all four `/admin` routers | `app/routes/admin.py` `require_admin` (`hmac.compare_digest`) |
| Brokerage auth | One static `api_key` per tenant (`pas_…`), exact-match lookup; PAS211F can hash it behind a flag | `app/routes/portal.py` `require_brokerage`; `app/db/brokerage_store.py get_brokerage_by_api_key` |
| Ingestion auth | `X-API-Key` → brokerage; tenant from auth only; payload `brokerage_id` mismatch rejected | `app/routes/lead_ingestion.py` |
| Slack | HMAC signature over `v0:ts:body` + 300s replay window + workspace `team_id` bind | `app/routes/slack_command.py` |
| Twilio | `RequestValidator` signature (enforced in every non-development env) | `app/routes/twilio_webhook.py`, `app/config.py require_twilio_signature` |
| Demo/sim | PAS211D: prod-gated (404 unless `ENABLE_DEMO_ENDPOINTS`), non-demo sim needs matching key | `app/routes/simulate.py`, `app/routes/demo.py` |
| Onboarding | One-time invite key (`orvn_…`), single-use + TTL + revocable, rate-limited (PAS211D) | `app/routes/onboarding.py`, `app/db/invite_store.py` |
| **JWT / Principal / RBAC** | **Scaffolding only — NOT enforced anywhere** | `app/auth/principal.py:8-10` ("nothing in the running app constructs Principals yet"); `SUPABASE_JWT_SECRET` declared in `app/config.py` and **never read** |
| Supabase client | **Service-role key only** (`BYPASSRLS`) — single global singleton | `app/db/supabase_client.py` |

**Direct answers to the task questions:**
- *What auth exists today?* Two shared static keys (admin + per-tenant) + signed webhooks (Slack/Twilio) + one-time invite keys.
- *What is scaffolding only?* The entire `app/auth/*` `Principal`/role layer; `SUPABASE_JWT_SECRET`; `ENABLE_LEGACY_*_AUTH` flags (inert — there is no JWT path to fall back from).
- *Where is JWT not enforced?* **Everywhere.** No route validates a Bearer token; `resolve_principal` does not exist.
- *Which routes use API keys?* `/portal/*`, `/ingest/lead`, `/outbound/*` (brokerage `X-API-Key`); `/admin/*`, `/admin/events/*` (`X-Admin-Key`).
- *Which routes should stay API-key short-term?* `/ingest/lead` and `/outbound/*` (machine-to-machine integration callers) and the demo/sim tools.
- *Which routes need user/session/JWT long-term?* `/portal/*` (human brokerage users) and `/admin/*` (ORVN operators) — both need per-user identity, roles, and 2FA.
- *Which paths legitimately require service-role?* Admin provisioning (create/rotate/delete brokerage), background workers, the event/audit writers, billing/system tasks, Twilio/Slack webhook handlers that write events for arbitrary tenants. (See §6 service-role table.)

---

## 3. Principal model (paid-client-ready)

Extends the existing `app/auth/principal.py` (`user_id`, `email`, `role`,
`brokerage_id`, `source`) with the fields RBAC needs (`permissions`,
`workspace_id`/`brokerage_id`, `session_id`). No code change here — this is the
target contract.

| Principal | Identity source | Tenant / workspace | Role(s) | Allowed operations | Data access | Service-role allowed? | 2FA later? |
|---|---|---|---|---|---|---|---|
| **ORVN admin** | Supabase Auth JWT, member of `admin_users` | none (cross-tenant) | `ORVN_ADMIN` | provision/rotate/deactivate brokerages, fleet ops, view all | All tenants (operational); PII via audited reads | Yes (admin provisioning runs as service-role on the backend) | **Yes (required)** |
| **Brokerage owner** | JWT, `brokerage_users.role='owner'` | one `brokerage_id` | `BROKER_OWNER` | full portal R/W, invite/seats, rotate own key, billing, integrations | Own tenant only, incl. PII | No (tenant-scoped client) | Yes (recommended) |
| **Team lead** | JWT, `brokerage_users.role='team_lead'` | one `brokerage_id` | `TEAM_LEAD` | portal R/W for the team, manage agents, view intelligence | Own tenant; PII yes | No | Optional |
| **Agent** | JWT, `brokerage_users.role='agent'` | one `brokerage_id` | `AGENT` | read assigned leads/calls, update own status, limited write | Own tenant, **own/assigned** records; PII limited | No | Optional |
| **Integration / forwarder** | Long-lived `X-API-Key` (machine) | one `brokerage_id` | `INTEGRATION_FORWARDER` | `POST /ingest/lead` (and future signed forwarder) only | Write-only ingestion to own tenant; **no read** of portal/admin | No | n/a (key rotation instead) |
| **Slack operator** | Slack-signed request → `team_id` → brokerage; operator user id from Slack payload (no PAS user yet) | one `brokerage_id` | `SLACK_OPERATOR` (maps to TEAM_LEAD-ish read + bounded mutations) | bounded Slack intents (pause/resume/push/remove, digests) | Own tenant; PII-free responses | No (reads scoped) | n/a (Slack workspace is the trust anchor) |
| **System worker** | No request principal; internal process w/ service-role | none / all | `SYSTEM_WORKER` | event/audit writes, training, reapers, snapshot reads | All tenants (by design) | **Yes (only path that should)** | n/a |

Notes:
- The existing role labels (`owner/agent/viewer/demo_viewer` + legacy) map onto
  this: `viewer`→read-only `AGENT`-minus-write; `demo_viewer`→demo tenant only;
  `admin_legacy`/`brokerage_legacy`→transition principals (see §7).
- `TEAM_LEAD` and `INTEGRATION_FORWARDER` and `SLACK_OPERATOR` are **new** role
  constants to add in PAS211G.1.

---

## 4. Route auth matrix

| Surface | Current auth | Target auth | Tenant source | Role requirement | Service-role allowed? | Readiness risk if unchanged |
|---|---|---|---|---|---|---|
| `/portal/*` | `X-API-Key` (owner-equiv) | **JWT** (Bearer) | JWT `brokerage_id` claim | `BROKER_OWNER` / `TEAM_LEAD` / `AGENT` | No → scoped client | **High** — no per-user identity, no least-privilege, shared key = full tenant access |
| `/ingest/lead` | `X-API-Key` | **API-key (kept)** + optional signed forwarder | key→`brokerage_id` | `INTEGRATION_FORWARDER` | No | Low — already tenant-pinned, fail-closed; keep machine auth |
| `/admin/*` | `X-Admin-Key` (one shared) | **JWT**, member of `admin_users` | none (cross-tenant) | `ORVN_ADMIN` | Yes (provisioning) | **High** — single shared key = whole-fleet compromise; no per-operator identity/2FA |
| `/admin/events/*`, `/admin/intelligence/*` | `X-Admin-Key` | **JWT** `ORVN_ADMIN` (+ optional brokerage scope) | none / optional `brokerage_id` | `ORVN_ADMIN` | Reads can move to scoped later | Medium — admin global reads explicit (PAS211E `allow_global`) |
| `/slack/command` | Slack HMAC + `team_id` | **unchanged** (signed webhook) | `team_id`→brokerage | `SLACK_OPERATOR` | No (reads scoped) | Low — signature + replay window already solid |
| `/twilio/*` | Twilio signature | **unchanged** (signed webhook) + PAS211J URL-pin/replay | webhook→brokerage by phone | n/a (machine) | Yes (writes events) | Medium — webhook hardening is PAS211J, not here |
| `/simulate-call` | PAS211D gate + demo-only/key | **unchanged** | body / matching key | demo or matching `INTEGRATION`/owner | No | Low — gated in prod |
| `/demo/token` | PAS211D gate + RL | **unchanged** | n/a | n/a | No | Low — gated in prod |
| `/outbound/*` | `X-API-Key` | **API-key (kept) → JWT optional** | key→`brokerage_id` | `BROKER_OWNER`/`INTEGRATION` | No | Medium — places real calls; keep key short-term, add JWT option |
| `/onboarding/claim` | invite key + RL | **unchanged** (bootstrap) | invite→brokerage | n/a (pre-auth bootstrap) | Service-role to read brokerage row | Low — single-use TTL'd + rate-limited |
| `/dashboard` (static), `/health` | none | none / JWT-gated SPA | n/a | n/a | No | Low |

---

## 5. RBAC model

Minimum role set + capability grid. `✓` = allowed, `own` = own-tenant only,
`—` = denied, `self` = own record only.

| Capability | ORVN_ADMIN | BROKER_OWNER | TEAM_LEAD | AGENT | INTEGRATION_FORWARDER | SYSTEM_WORKER |
|---|---|---|---|---|---|---|
| Read leads/calls/bookings | all | own | own | own (assigned) | — | all |
| Write/update tenant records | all | own | own | self/assigned | ingest-only (own) | all |
| Ingest digital lead | ✓ | own | own | — | own | ✓ |
| Invite users / manage seats | ✓ | own | — | — | — | — |
| Rotate API keys | all | own | — | — | — | — |
| View operational intelligence | all | own | own | limited | — | ✓ |
| View PII (phone/email/transcript) | audited | own | own | limited | — | ✓ |
| View/admin memory (PAS212) | all | own (approve) | own (propose) | — | — | ✓ |
| Manage billing / seats | ✓ | own | — | — | — | — |
| Manage integrations | ✓ | own | own | — | — | — |
| Access `/admin/*` surfaces | ✓ | — | — | — | — | n/a |

Enforcement principle: **deny by default**. A route declares the minimum role +
the tenant it operates on; the dependency rejects anything that isn't that role
*and* that tenant (`principal.brokerage_id == path/claim brokerage_id`).

---

## 6. Scoped Supabase client strategy

**Current limitation.** `app/db/supabase_client.py` builds ONE client with
`SUPABASE_SERVICE_KEY`. The service role has `BYPASSRLS`, so:
- `migrate_v9`'s `USING (brokerage_id = auth.jwt() ->> 'brokerage_id')` policies
  never apply to app queries — they're inert.
- Tenant isolation rests entirely on app-layer `.eq("brokerage_id", …)`
  discipline (hardened in PAS211E, but still single-layer at the DB).

**Target.** Two clients, chosen by call site:
1. **Scoped client** (`authenticated` role): created per-request from the user's
   Supabase JWT (or a minted token carrying the claims). RLS applies → the DB
   itself blocks cross-tenant rows. Used by **tenant-facing reads** (`/portal/*`,
   tenant intelligence, tenant memory reads).
2. **Service client** (existing): used ONLY by the legitimately cross-tenant
   paths below.

**JWT claims required** (minted by Supabase Auth + a custom-claims hook):
- `sub` / `user_id` — the principal identity.
- `brokerage_id` (a.k.a. `workspace_id`) — tenant scope; the RLS policies key on
  this.
- `role` — `owner|team_lead|agent|viewer` (admin handled via `admin_users`).
- `permissions` — optional fine-grained list for capabilities beyond role.
- `session_id` — optional, for revocation/audit.

**Operations that MUST remain service-role:**

| Path | Why service-role |
|---|---|
| Admin provisioning (create/rotate/deactivate brokerage) | Acts across tenants; pre-dates any tenant JWT |
| Onboarding `/claim` | Pre-auth bootstrap — reads the brokerage row before the user has a token |
| Background workers (training, reapers, snapshot/observer jobs) | No request principal; operate fleet-wide |
| Event/audit writers (`pas_events`, `audit_log`) | Must land even when no tenant row matches; observability stream |
| Twilio/Slack webhook handlers | Machine callers; write events/leads for the resolved tenant |

**Avoiding accidental service-role use in tenant-facing routes:**
- Provide `get_scoped_supabase(principal)` and make `get_supabase()` (service)
  **lint-flagged** in tenant route modules.
- A test (`test_no_service_role_in_tenant_routes`) greps `app/routes/portal.py`
  (and future tenant routes) for direct `get_supabase(` use.
- Route dependencies inject the scoped client; tenant stores accept a client
  parameter rather than importing the global singleton.

---

## 7. Migration path (phased)

| Phase | Deliverable | Risk | Gate to next |
|---|---|---|---|
| **PAS211G.1** | Auth inventory + finalize `Principal` contract: add `TEAM_LEAD`, `INTEGRATION_FORWARDER`, `SLACK_OPERATOR`, `permissions`, `session_id`; capability map as code constants. **No enforcement.** | None (types only) | Contract reviewed |
| **PAS211G.2** | JWT validation boundary: `resolve_principal(request)` verifies a Supabase JWT (`SUPABASE_JWT_SECRET`) → `Principal`; legacy key → synthetic principal behind `ENABLE_LEGACY_*`. Pure verification, not wired to routes. | Low | Unit-tested verifier |
| **PAS211G.3** | Route-level principal enforcement: convert `require_admin`/`require_brokerage` to resolve a `Principal` and assert role+tenant. API-key path still produces a legacy principal (compat). | Medium — touches live auth deps | Full suite green, no behavior change for valid keys |
| **PAS211G.4** | Scoped Supabase client prototype: `get_scoped_supabase(principal)`; tenant stores accept an injected client. Not yet default. | Medium | Prototype reads work |
| **PAS211G.5** | RLS enforcement pilot on **low-risk reads** (e.g. `/portal/bookings`, `/portal/leads` list): route uses scoped client; **apply `migrate_v9`**; verify cross-tenant returns empty at the DB. | High — first real RLS | Pilot read verified cross-tenant-safe |
| **PAS211G.6** | Admin per-operator identity (`admin_users` JWT) + 2FA groundwork (TOTP enrollment fields, step-up on sensitive ops). Retire shared `ADMIN_API_KEY` for humans. | High | Per-operator admin works; key kept for workers only |
| **PAS211G.7** | Legacy API-key compatibility window: announce, dual-run, then flip `ENABLE_LEGACY_BROKERAGE_KEY_AUTH=false` for portal (keep for ingestion). | Medium | All human users on JWT |

Sequencing rationale: types → verifier → enforcement (still key-compatible) →
scoped client → **one** low-risk RLS pilot before fleet-wide → admin/2FA →
legacy sunset. RLS is switched on for a single read first so a policy mistake
can't lock out the whole portal.

---

## 8. Compatibility strategy

PAS must not break existing API-key ingestion/demo flows while moving to JWT.

- **Stays API-key (indefinitely / long window):** `/ingest/lead`, `/outbound/*`
  (machine integration callers), and the internal/demo tools. Integration
  forwarders authenticate with a long-lived per-tenant key scoped to
  `INTEGRATION_FORWARDER` (ingest-only, no portal/admin) — ideally a **separate**
  key from the portal user key so revoking one doesn't break the other.
- **Moves to JWT first:** `/portal/*` (human users) then `/admin/*` (operators).
- **Legacy phase-out:** during PAS211G.3–.7 every `require_*` resolves a
  `Principal`; an API key yields a `brokerage_legacy`/`admin_legacy` principal
  (owner/admin-equivalent) so nothing breaks. Once the dashboard issues JWTs,
  flip `ENABLE_LEGACY_BROKERAGE_KEY_AUTH=false` for portal (keep it true for
  ingestion) and `ENABLE_LEGACY_ADMIN_KEY_AUTH=false` for human admin (keep the
  service key for workers).
- **Webhooks stay separate from user auth:** Slack (HMAC) and Twilio (signature)
  are **machine trust anchors**, never user JWTs. They resolve a tenant from
  `team_id`/phone and operate as a bounded `SLACK_OPERATOR` / machine principal.
  They are explicitly out of the JWT migration.

---

## 9. Tests needed (to be written in the implementation phases)

- JWT required on user routes — `/portal/*` without a valid Bearer → 401.
- API-key still accepted on ingestion — `/ingest/lead` with a valid key works
  (no regression) and is treated as `INTEGRATION_FORWARDER`.
- Service-role forbidden in tenant-facing routes — static check that
  `app/routes/portal.py` (and future tenant routes) don't call the service
  `get_supabase(` directly.
- Role cannot access higher-permission surfaces — `AGENT` → owner-only route
  (invite/rotate) → 403.
- Cross-tenant JWT rejected — a token with `brokerage_id=B` hitting a `…/{A}/…`
  resource → 403/404; and at the DB, the scoped client returns 0 rows.
- Scoped client receives `brokerage_id` claim — the per-request client is built
  with the principal's tenant claim.
- Admin routes require `ORVN_ADMIN` — non-admin JWT → 401/403 on `/admin/*`.
- Agent cannot access broker-only data — billing/seats/rotate → 403.
- Integration key cannot access portal/admin — an `INTEGRATION_FORWARDER` key on
  `/portal/*` or `/admin/*` → 403.

---

## 10. Service-role limitation summary

`migrate_v9` policies are **inert today** because every query uses the
service-role (`BYPASSRLS`) client. They become effective **only** once
tenant-facing reads run through a JWT-scoped `authenticated` client carrying a
`brokerage_id` claim (PAS211G.4–.5). Until then, tenant isolation is app-layer
only (two-layered after PAS211E, but the DB cannot stop a code mistake on the
service path). Admin/worker/webhook/billing paths intentionally keep
service-role.

---

## 11. Paid-client readiness impact & what is NOT implemented

**Impact:** this plan is the bridge from "shared keys" to "per-user identity +
real DB-enforced tenant isolation" — the remaining structural blocker (alongside
the operational tasks: applying `migrate_v9`/`v10`, rotating live `.env`
credentials, Slack-secret encryption) between **Conditionally Ready** and
**Ready** for paid-client real lead data.

**NOT implemented in PAS211G (spec only):** no JWT verification, no
`resolve_principal`, no route changes, no scoped client, no RBAC enforcement, no
2FA, no migration applied, no Supabase policy created, no dependency added. Those
land in PAS211G.1–.7. Webhook hardening is **PAS211J**; PII/retention is
**PAS211I**; durable/shared rate limiting + region/timezone is **PAS211K/214P**.
