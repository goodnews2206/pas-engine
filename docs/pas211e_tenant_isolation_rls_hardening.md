# PAS211E — Tenant Isolation / RLS Hardening

Hardens PAS multi-tenant isolation so brokerage data is protected by **more than
one layer of application discipline**, and lays the database-level RLS backstop.
Focused on tenant isolation only — **not** JWT/RBAC, secrets encryption,
onboarding, UI, performance, or prompt-injection (those remain PAS211G/F/etc.).

## PAS211C findings addressed

| Finding | Status |
|---|---|
| Intelligence queries fail OPEN when `brokerage_id` omitted (return global stream) | **Fixed** — fail-closed |
| `agent_store.get/update/delete_agent` operate by global PK, no tenant predicate | **Fixed** — optional tenant predicate, wired into portal |
| `booking_store.get_booking/update_booking_status` by global PK | **Fixed** — optional tenant predicate |
| RLS enabled on tables but **zero policies** | **Migration proposal added** (`migrate_v9`, not applied) |
| Service-role key bypasses RLS (app-only scoping) | **Documented**; backstop is forward-looking until PAS211G |

## Tenant isolation model — before → after

**Before:** isolation was *single-layer* — every query had to remember an
`.eq("brokerage_id", …)`. Some shared helpers returned the **global** event
stream when the filter was omitted, and several store helpers mutated/read by
global id with no tenant predicate. The database offered no backstop (RLS
enabled, no policies; service-role bypass).

**After:** isolation is *defense-in-depth at the app layer*, plus a documented
DB backstop proposal:
- Shared intelligence reads **fail closed**: no tenant scope ⇒ empty result,
  never a cross-tenant read, unless an admin route explicitly opts in.
- Tenant-owned store helpers carry a `brokerage_id` predicate when called from
  tenant-facing routes, so a cross-tenant id reads as `None` and a cross-tenant
  write changes nothing.
- A `migrate_v9` RLS-policy proposal exists for the eventual JWT-scoped client.

## Intelligence fail-closed changes

`app/services/intelligence/queries.py` — `recent_events`, `events_for_call`,
`callback_events`, `fetch_call_and_lead_context` now take `allow_global=False`.
A new `_tenant_scope_ok` guard returns an **empty** result (and logs a warning)
unless the caller passes a `brokerage_id` **or** explicitly `allow_global=True`.

- **Portal callers** ([app/routes/portal.py](../app/routes/portal.py)) already
  pass `brokerage["id"]` → scoped, unchanged.
- **Admin callers** ([app/routes/events.py](../app/routes/events.py)) now pass
  `allow_global=True` — their cross-tenant view is intentional and now explicit.
- **Workflow runtime** ([app/services/workflows/runtime.py](../app/services/workflows/runtime.py))
  derives `allow_global = (audience == "admin")` and threads it through
  `fetch_workflow_events`, so the admin workflow view keeps working while the
  portal workflow view stays tenant-scoped.

## Stores hardened

| Helper | Change |
|---|---|
| `agent_store.get_agent(agent_id, brokerage_id=None)` | scoped lookup → `None` cross-tenant |
| `agent_store.update_agent(... , brokerage_id=None)` | `brokerage_id` predicate on the UPDATE |
| `agent_store.delete_agent(... , brokerage_id=None)` | `brokerage_id` predicate on the DELETE |
| `agent_store.set_agent_status(... , brokerage_id=None)` | threads predicate through `update_agent` |
| `booking_store.get_booking(booking_id, brokerage_id=None)` | scoped lookup → `None` cross-tenant |
| `booking_store.update_booking_status(... , brokerage_id=None)` | `brokerage_id` predicate on the UPDATE |

The `brokerage_id` parameter is **optional** so admin/internal callers (which are
legitimately cross-tenant, e.g. `agents.py` under `X-Admin-Key`, the websocket
transfer path) are unchanged. Tenant-facing portal routes now pass it, adding a
DB-layer predicate **on top of** the existing app-level ownership check.

## RLS migration proposal summary

`scripts/migrate_v9_tenant_rls_policies.sql` — **proposal, NOT applied.**

- Additive + idempotent: re-asserts `ENABLE ROW LEVEL SECURITY` and creates
  tenant policies guarded by `pg_policies` existence checks (no `DROP POLICY`,
  no destructive SQL).
- Per tenant-owned table (`leads`, `calls`, `bookings`, `agents`,
  `training_logs`, `lead_ingestion_dedupe`): `FOR ALL TO authenticated USING /
  WITH CHECK (brokerage_id = auth.jwt() ->> 'brokerage_id')`.
- `pas_events`: SELECT-only tenant read (events are written by the backend
  service role). `brokerages`: self-read by `id`.
- Order-independent vs `migrate_v8` (the dedupe-table policy is guarded on the
  table's existence).

## Service-role limitations (read this)

PAS talks to Supabase exclusively with the **service-role key**
([app/db/supabase_client.py](../app/db/supabase_client.py)), which has
`BYPASSRLS`. **Therefore the `migrate_v9` policies do not constrain the running
application today** — they only take effect for a **non-service, JWT-scoped**
client carrying a `brokerage_id` claim.

| Aspect | Today | Needed for true RLS enforcement |
|---|---|---|
| Tenant-facing reads | service-role + app-level `brokerage_id` filter | JWT-scoped (`authenticated`) Supabase client |
| Tenant claim | none | `brokerage_id` claim minted at login |
| Backstop | none in DB (policies inert under service role) | `migrate_v9` policies become effective |
| Admin/worker spans tenants | service-role (correct) | stays service-role (BYPASSRLS) |

Introducing the scoped client + minting the JWT claim is **PAS211G**. Until then,
isolation is **app-layer only** — now two-layered (fail-closed queries + store
predicates) but still dependent on correct app code; the DB cannot yet stop a
mistake on the service-role path.

## Remaining gaps (deferred)

- **PAS211G** — JWT/RBAC + a JWT-scoped Supabase client so `migrate_v9` policies
  actually enforce; per-operator admin identity (replaces the single admin key).
- **PAS211F** — secrets-at-rest encryption + rotate live credentials.
- **PAS211I** — PII minimization in logs/`pas_events`; retention/deletion/export.
- **PAS211J** — Twilio webhook URL-pin + replay protection.
- **PAS211K / PAS214P** — durable/shared rate limiting; region/timezone.
- `call_logger` outcome/finalize still write by `call_sid` (Twilio-trusted SID,
  no tenant context at that layer) — left as-is; revisit with PAS211J.

## Paid-client readiness impact

PAS211E removes the most likely cross-tenant **leak paths** (fail-open shared
queries) and the most dangerous **cross-tenant mutation** surfaces
(agent/booking by global id), and ships the RLS-policy backstop as a reviewable,
not-yet-applied migration. Isolation is now genuinely two-layered at the app
level.

It does **not** by itself make the database enforce isolation — that requires the
PAS211G JWT-scoped client. Net: this is a necessary, material step toward
paid-client readiness; combined with PAS211D it closes the acute "any caller can
reach another tenant's data through a forgotten filter or a global-id helper"
class of risk, but the **Conditionally Ready** verdict stands until PAS211G (real
RLS enforcement) and the PAS211F secrets items land.
