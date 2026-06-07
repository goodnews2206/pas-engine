# PAS211G.1 — Principal Contract + JWT Boundary Stub

First implementation step of the PAS211G plan. Builds the auth **boundary**
(principal contract + resolver + pure authz helpers) that PAS211G.2 (real JWT
verification) and PAS211G.3 (route enforcement) plug into — **without enforcing
anything on existing routes** and **without breaking any API-key flow**.

## What was implemented

- **Extended `Principal`** ([app/auth/principal.py](../app/auth/principal.py)) —
  additive fields `principal_type`, `permissions`, `auth_method`, `session_id`
  (all optional → PAS133A five-field construction and tests still work); new
  helpers `principal_id`, `is_brokerage_scoped`, `require_brokerage_id()`.
  New vocabularies: principal types (`ORVN_ADMIN`, `BROKER_OWNER`, `TEAM_LEAD`,
  `AGENT`, `INTEGRATION_FORWARDER`, `SLACK_OPERATOR`, `SYSTEM_WORKER`) and auth
  methods (`admin_key`, `brokerage_api_key`, `jwt`, `slack_signature`,
  `twilio_signature`, `system`).
- **Resolver boundary** ([app/auth/resolver.py](../app/auth/resolver.py)) —
  `resolve_principal_from_admin_key`, `resolve_principal_from_brokerage_api_key`,
  `resolve_principal_from_jwt_stub`, `resolve_principal_from_request`. Reuses the
  existing constant-time admin compare and the hash-aware brokerage lookup so it
  never drifts from production auth.
- **Pure authz helpers** ([app/auth/authz.py](../app/auth/authz.py)) —
  `has_permission`, `require_principal_type`, `require_brokerage_scope`,
  `AuthorizationError`. Deny-by-default; framework-free.
- **Config flags** ([app/config.py](../app/config.py)) — `JWT_AUTH_ENABLED`
  (default False), `JWT_ISSUER`, `JWT_AUDIENCE` (reserved for G.2),
  `ENABLE_LEGACY_API_KEY_AUTH` (default True). No JWT secret is required at
  startup.
- **Tests** — `tests/mvp/test_pas211g_1_principal_resolver.py` (18).

## What was intentionally NOT enforced yet

- **No production route uses the resolver.** `/admin/*`, `/portal/*`,
  `/ingest/lead`, `/outbound/*` keep their existing `require_admin` /
  `require_brokerage` / `X-API-Key` checks unchanged. Route migration is
  **PAS211G.3**.
- **No real JWT verification.** The JWT path is a stub (see below). Real HS256
  Supabase-token verification is **PAS211G.2**.
- No scoped Supabase client, no RLS activation, no RBAC enforcement on routes,
  no 2FA, no migration applied, no new dependency.

## Principal model

`Principal(user_id, email, role, brokerage_id, source, principal_type=,
permissions=, auth_method=, session_id=)` — frozen/immutable. `role` is the
PAS133A fine role; `principal_type` is the coarse PAS211G identity class. Both
are carried so legacy role helpers (`is_owner`, `is_legacy`, …) keep working
while PAS211G gates on `principal_type`. Helpers: `is_admin`,
`is_brokerage_user`, `is_brokerage_scoped`, `require_brokerage_id()`.

## Resolver boundary behaviour

| Input | Result |
|---|---|
| Valid `X-Admin-Key` (constant-time match) | `ORVN_ADMIN` principal (`auth_method=admin_key`, legacy source) |
| Invalid/empty admin key, or empty configured key | `None` |
| Valid `X-API-Key` → known non-demo brokerage | `BROKER_OWNER` (or `INTEGRATION_FORWARDER` on the `/ingest*` surface) |
| Unknown/empty key, or `demo` tenant | `None` |
| Bearer token, JWT disabled | `None` |
| Bearer token, JWT enabled (no impl) | `None` — **fail closed**, logged without the token value |
| `resolve_principal_from_request` | tries JWT → admin key → API key (surface-aware), first non-None wins, else `None` |

Legacy resolution is gated by `ENABLE_LEGACY_API_KEY_AUTH` (and the existing
`ENABLE_LEGACY_ADMIN_KEY_AUTH` / `ENABLE_LEGACY_BROKERAGE_KEY_AUTH`).

## Legacy API-key compatibility

`X-Admin-Key` and `X-API-Key` continue to authenticate every existing route
exactly as before (the resolver is additive scaffolding, not wired into
`require_admin`/`require_brokerage`). Tests assert `require_admin` and the
`/ingest/lead` API-key path are unchanged. Ingestion stays API-key
(`INTEGRATION_FORWARDER`) — the resolver models that surface explicitly so it can
stay API-key while portal/admin move to JWT later.

## JWT stub status

`resolve_principal_from_jwt_stub` is a **safe stub**: `None` when
`JWT_AUTH_ENABLED` is False; **`None` (fail closed)** when True-but-unimplemented.
It NEVER constructs a principal from an unverified token, and never logs the
token. PyJWT 2.12.1 happens to be importable in the current environment but is
**not declared in requirements.txt**, so PAS211G.1 does not depend on it — adding
the dependency (or choosing stdlib HS256) is a PAS211G.2 decision, documented
rather than taken here.

## How this prepares PAS211G.2 / G.3

- **G.2** swaps the stub body for real verification (HS256 via `SUPABASE_JWT_SECRET`,
  checking `JWT_ISSUER`/`JWT_AUDIENCE`), populating `Principal` from claims
  (`user_id`, `brokerage_id`, `role`, `permissions`, `session_id`). The boundary
  signature and call sites don't change.
- **G.3** converts `require_admin`/`require_brokerage` into FastAPI dependencies
  that call `resolve_principal_from_request` + the authz helpers, gating on
  `principal_type` and tenant scope — legacy keys still resolve to principals, so
  no flow breaks during the window.

## Paid-client readiness impact

Establishes the single seam through which all future auth flows — the
prerequisite for per-user identity, RBAC, and (with the scoped client in G.4–.5)
real RLS enforcement. On its own it changes no runtime behaviour, so it does not
move the readiness verdict; it unblocks the steps that do.

## Remaining gaps

Real JWT verification (G.2), route enforcement (G.3), scoped Supabase client +
RLS pilot (G.4–.5), admin per-operator identity + 2FA (G.6), legacy sunset (G.7).
Out of PAS211G scope: PII/retention (PAS211I), webhook hardening (PAS211J),
durable rate limiting + region/timezone (PAS211K/214P).
