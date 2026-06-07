# PAS213B.1 — Durable Dedupe Migration: Apply / Verify Runbook

**Migration:** `scripts/migrate_v8_digital_ingestion_dedupe.sql`
**Creates:** table `lead_ingestion_dedupe` (+ one partial index, RLS enabled)
**Status:** PROPOSAL — **not** applied, **not** auto-applied by any code path.
**Owner action:** an operator applies it by hand in the Supabase SQL editor,
exactly like every prior `scripts/migrate_v*.sql`.

> This runbook is the safe, reviewable procedure to turn on **durable**
> cross-restart dedupe for digital lead ingestion. It changes **no product
> scope** and adds **no dependency**. It is a prerequisite step before a paying
> brokerage's digital leads flow through PAS in production.

---

## 1. Purpose

PAS213B wired a durable dedupe store (`SupabaseLeadDedupeStore`) that reads/writes
a `lead_ingestion_dedupe` ledger so a re-posted form, a forwarder loop, or a
manual re-send does **not** create a second operational record — and that this
holds **across process restarts / redeploys**. The store is already the runtime
default. The only missing piece is the backing table. This migration creates it.

---

## 2. When to apply

- **Before** onboarding any paying brokerage whose digital leads must be
  de-duplicated reliably (i.e. before real customer data flows through
  `POST /ingest/lead`).
- It is a plain additive `CREATE TABLE IF NOT EXISTS` that takes **no lock on any
  existing table**, so it is safe to run online; a maintenance window is **not**
  required. Pick any low-traffic moment.
- Idempotent: re-running it is a no-op, so it is safe to apply more than once.

---

## 3. Prerequisites

- Supabase project for the target environment (staging first, then production).
- **Service-role / SQL-editor access** to that project (the same access used for
  every prior `migrate_v*.sql`).
- The base schema already present (it is, on `main`): `brokerages`, `leads`,
  `pas_events`. This migration references **none of them via FK** — `lead_id` is a
  nullable `UUID` soft reference (no FK), mirroring the `pas_events` / `audit_log`
  precedent. There is **no `auth.users` dependency** (unlike `migrate_v7.sql`).
- No new environment variables. No new code deploy is required — the app already
  ships the durable store.

---

## 4. Exact SQL to apply

Apply the committed file verbatim — do not retype:

```
scripts/migrate_v8_digital_ingestion_dedupe.sql
```

It creates exactly:

- `lead_ingestion_dedupe` (`id`, `brokerage_id`, `dedupe_key`, `source`,
  `external_lead_id`, `lead_id`, `hit_count`, `first_seen_at`, `last_seen_at`)
- `UNIQUE (brokerage_id, dedupe_key)` — tenant-scoped, the race backstop
- partial index `lead_ingestion_dedupe_ext_idx`
- `ENABLE ROW LEVEL SECURITY` (no anon policies; writes via the service-role
  backend client — parity with `leads` / `calls` / `pas_events` / `audit_log`)

---

## 5. Pre-apply checks

1. Confirm you are connected to the **intended** environment (staging vs prod).
2. Confirm the table does not already exist (expect **empty / no row**):

   ```sql
   SELECT to_regclass('public.lead_ingestion_dedupe');  -- expect NULL pre-apply
   ```

3. Confirm the base tables exist (sanity):

   ```sql
   SELECT to_regclass('public.leads'), to_regclass('public.pas_events');
   ```

4. Confirm the file on disk matches what you intend to run (review the diff /
   open the committed file). Do not paste ad-hoc SQL.

---

## 6. Apply steps

1. Open **Supabase Studio → SQL Editor** for the target project.
2. Paste the **entire** contents of
   `scripts/migrate_v8_digital_ingestion_dedupe.sql`.
3. **Run All.**
4. Expect success with no destructive notices (only `CREATE TABLE` / `CREATE
   INDEX` / `ALTER TABLE ... ENABLE ROW LEVEL SECURITY`).

---

## 7. Post-apply verification SQL

```sql
-- 7.1 Table exists
SELECT to_regclass('public.lead_ingestion_dedupe');           -- expect a row

-- 7.2 Tenant-scoped UNIQUE present
SELECT conname FROM pg_constraint
WHERE conrelid = 'lead_ingestion_dedupe'::regclass AND contype = 'u';
-- expect one unique constraint over (brokerage_id, dedupe_key)

-- 7.3 Columns are exactly the structural / non-PII set
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'lead_ingestion_dedupe'
ORDER BY ordinal_position;
-- expect: id, brokerage_id, dedupe_key, source, external_lead_id,
--         lead_id, hit_count, first_seen_at, last_seen_at
-- expect NO phone / email / name / message column

-- 7.4 Secondary index present
SELECT indexname FROM pg_indexes
WHERE tablename = 'lead_ingestion_dedupe';
-- expect lead_ingestion_dedupe_ext_idx (+ the unique + pkey indexes)

-- 7.5 RLS enabled
SELECT relrowsecurity FROM pg_class
WHERE oid = 'public.lead_ingestion_dedupe'::regclass;            -- expect true
```

---

## 8. Test with a sample duplicate lead (post-apply)

Use a **staging** brokerage API key. Send the **same** payload twice:

```bash
# First submission → 201 Created, status "ingested"
curl -sS -X POST "$BASE_URL/ingest/lead" \
  -H "X-API-Key: $STAGING_KEY" -H "Content-Type: application/json" \
  -d '{"source":"website_form","phone":"212-555-0199","external_lead_id":"RUNBOOK-1"}'

# Identical second submission → 200 OK, status "duplicate"
curl -sS -X POST "$BASE_URL/ingest/lead" \
  -H "X-API-Key: $STAGING_KEY" -H "Content-Type: application/json" \
  -d '{"source":"website_form","phone":"212-555-0199","external_lead_id":"RUNBOOK-1"}'
```

Expected:
- First response `status: "ingested"`, second `status: "duplicate"` with the same
  `dedupe_key`.
- Ledger has exactly one row for that key:

  ```sql
  SELECT brokerage_id, dedupe_key, source, external_lead_id, hit_count
  FROM lead_ingestion_dedupe
  WHERE external_lead_id = 'RUNBOOK-1';                         -- expect 1 row
  ```

- `pas_events` shows a `lead.ingested` then a `lead.duplicate` for that tenant
  (PII-free payloads).

Cleanup (staging only, optional): delete the test ledger row + the test lead.
**Never run cleanup against production customer data.**

---

## 9. Rollback / disable strategy

The runtime **fails open**: if the table is absent or unreachable, ingestion
keeps working and no lead is lost (only durable dedupe is inactive). So:

- **Preferred "disable":** do nothing destructive. If durable dedupe must be
  turned off, revert at the **application layer** (inject the process-local
  `LeadDedupeStore`, or a code revert) — this keeps the ledger and its history.
- **Hard rollback (last resort, destructive):** the table has **no inbound FK**,
  so dropping it cascades nothing, but it **permanently loses the dedupe
  history**:

  ```sql
  DROP TABLE IF EXISTS lead_ingestion_dedupe;   -- destructive: loses the ledger
  ```

  After a drop the app reverts to fail-open behavior automatically. Do **not**
  drop on production unless you have accepted the loss of dedupe state.

---

## 10. Expected app behavior

### Before migration (current production state)
- `POST /ingest/lead` works; leads persist to `leads`; events to `pas_events`.
- Durable dedupe is **inactive** (fails open): `is_duplicate` returns False and
  `register` is a swallowed no-op (table missing). Server logs a warning naming
  this file.
- Same-phone repeats still collapse in the `leads` table
  (`UNIQUE(brokerage_id, phone_number)` + merge), but the API returns `ingested`
  each time and **no `lead.duplicate` event fires**. Different-phone /
  same-`external_lead_id` repeats are **not** suppressed.
- **No lead is ever lost.**

### After migration
- Durable dedupe is **active**: an identical resubmission returns `duplicate`,
  emits `lead.duplicate`, and is not written again — and this **survives
  restarts/redeploys**.
- Tenant isolation preserved: `UNIQUE(brokerage_id, dedupe_key)` means a key seen
  under one tenant can never suppress another tenant's lead.

---

## 11. Safety notes for paid-client deployment

- **Staging first.** Apply + run §8 on staging, confirm `ingested` → `duplicate`,
  then apply to production.
- **Additive & idempotent.** No existing table/column/constraint/index is dropped
  or altered; re-running is safe.
- **No PII at rest in the ledger.** Only an opaque `dl_<sha>` dedupe token, the
  closed-vocab `source`, and an optional vendor `external_lead_id`. Name / phone
  / email / message are never written here.
- **RLS enabled**, no anon policies — same posture as `leads` / `pas_events`.
- **No new dependency, no code deploy, no env var** required to apply.
- **Fail-open guarantee** means an aborted or delayed apply never drops a paying
  client's lead — it only defers durable duplicate suppression.
- Apply via the same audited path as prior migrations; do not paste ad-hoc DDL.
