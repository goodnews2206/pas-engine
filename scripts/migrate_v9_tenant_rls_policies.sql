-- ─────────────────────────────────────────────────────────────────
-- PAS — Migration v9 (PAS211E)
-- Tenant-scoped Row-Level Security POLICIES.
-- Run in Supabase SQL Editor → Run All. Safe to re-run (guarded CREATEs).
--
-- STATUS: PROPOSAL — NOT auto-applied by any code path. Apply by hand, like
-- every prior migrate_v*.sql.
--
-- ┌─ READ THIS FIRST — service-role limitation ─────────────────────┐
-- │ PAS currently talks to Supabase with the SERVICE-ROLE key        │
-- │ (app/db/supabase_client.py). The service role has BYPASSRLS, so  │
-- │ these policies DO NOT constrain the running application today.    │
-- │ Tenant isolation is, for now, enforced in application code        │
-- │ (every query carries an `.eq("brokerage_id", …)` predicate;       │
-- │ PAS211E hardened the remaining store helpers + made the shared    │
-- │ intelligence queries fail-closed).                                │
-- │                                                                   │
-- │ These policies are the DATABASE-LEVEL backstop that becomes       │
-- │ effective ONLY once tenant-facing reads are moved onto a NON-     │
-- │ service, JWT-scoped Supabase client (the `authenticated` role     │
-- │ carrying a `brokerage_id` claim). Wiring that scoped client +     │
-- │ minting the JWT claim is PAS211G (auth/JWT/RBAC). Until then,      │
-- │ applying this migration is safe and additive but changes no       │
-- │ runtime behaviour — do not mistake "policies exist" for           │
-- │ "service-role access is constrained". It is not.                  │
-- └───────────────────────────────────────────────────────────────────┘
--
-- This migration is ADDITIVE ONLY:
--   - No table/column/constraint/index is dropped or altered.
--   - It (re)enables RLS (idempotent) and creates tenant policies guarded by
--     pg_policies existence checks (no DROP POLICY — re-running is a no-op).
--
-- Policy intent (per tenant-owned table): a principal may see/modify only rows
-- whose `brokerage_id` equals the `brokerage_id` claim in its JWT. The claim is
-- expected to be minted by PAS211G when a brokerage user authenticates.
--   USING       → controls which existing rows are visible / mutable.
--   WITH CHECK  → controls which rows may be written (no cross-tenant inserts).
--
-- The `authenticated` role is Supabase Auth's logged-in role. `anon` gets no
-- policy here → no anonymous access. The service role keeps full access
-- (BYPASSRLS) for backend jobs that legitimately span tenants (admin, workers).
-- ─────────────────────────────────────────────────────────────────


-- ── Re-assert RLS is enabled (idempotent, additive) ─────────────
ALTER TABLE leads                  ENABLE ROW LEVEL SECURITY;
ALTER TABLE calls                  ENABLE ROW LEVEL SECURITY;
ALTER TABLE bookings               ENABLE ROW LEVEL SECURITY;
ALTER TABLE agents                 ENABLE ROW LEVEL SECURITY;
ALTER TABLE pas_events             ENABLE ROW LEVEL SECURITY;
ALTER TABLE training_logs          ENABLE ROW LEVEL SECURITY;
ALTER TABLE brokerages             ENABLE ROW LEVEL SECURITY;
-- lead_ingestion_dedupe is created by migrate_v8 (also unapplied); guard it so
-- v9 can run before or after v8 without error.


-- ── Tenant policies (guarded so re-runs are no-ops; NO DROP) ─────
DO $$
BEGIN
    -- Tables whose tenant column is `brokerage_id`.
    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE schemaname='public' AND tablename='leads' AND policyname='leads_tenant_isolation') THEN
        CREATE POLICY leads_tenant_isolation ON leads
            FOR ALL TO authenticated
            USING (brokerage_id = (auth.jwt() ->> 'brokerage_id'))
            WITH CHECK (brokerage_id = (auth.jwt() ->> 'brokerage_id'));
    END IF;

    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE schemaname='public' AND tablename='calls' AND policyname='calls_tenant_isolation') THEN
        CREATE POLICY calls_tenant_isolation ON calls
            FOR ALL TO authenticated
            USING (brokerage_id = (auth.jwt() ->> 'brokerage_id'))
            WITH CHECK (brokerage_id = (auth.jwt() ->> 'brokerage_id'));
    END IF;

    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE schemaname='public' AND tablename='bookings' AND policyname='bookings_tenant_isolation') THEN
        CREATE POLICY bookings_tenant_isolation ON bookings
            FOR ALL TO authenticated
            USING (brokerage_id = (auth.jwt() ->> 'brokerage_id'))
            WITH CHECK (brokerage_id = (auth.jwt() ->> 'brokerage_id'));
    END IF;

    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE schemaname='public' AND tablename='agents' AND policyname='agents_tenant_isolation') THEN
        CREATE POLICY agents_tenant_isolation ON agents
            FOR ALL TO authenticated
            USING (brokerage_id = (auth.jwt() ->> 'brokerage_id'))
            WITH CHECK (brokerage_id = (auth.jwt() ->> 'brokerage_id'));
    END IF;

    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE schemaname='public' AND tablename='training_logs' AND policyname='training_logs_tenant_isolation') THEN
        CREATE POLICY training_logs_tenant_isolation ON training_logs
            FOR ALL TO authenticated
            USING (brokerage_id = (auth.jwt() ->> 'brokerage_id'))
            WITH CHECK (brokerage_id = (auth.jwt() ->> 'brokerage_id'));
    END IF;

    -- pas_events is an observability stream: read-scoped to the tenant, but the
    -- backend writes events via the service role (BYPASSRLS), so a tenant
    -- principal gets SELECT-only here. No WITH CHECK / no tenant inserts.
    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE schemaname='public' AND tablename='pas_events' AND policyname='pas_events_tenant_read') THEN
        CREATE POLICY pas_events_tenant_read ON pas_events
            FOR SELECT TO authenticated
            USING (brokerage_id = (auth.jwt() ->> 'brokerage_id'));
    END IF;

    -- brokerages: a tenant principal may see only its own row (keyed by id).
    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE schemaname='public' AND tablename='brokerages' AND policyname='brokerages_self_read') THEN
        CREATE POLICY brokerages_self_read ON brokerages
            FOR SELECT TO authenticated
            USING (id = (auth.jwt() ->> 'brokerage_id'));
    END IF;

    -- lead_ingestion_dedupe only exists once migrate_v8 is applied. Guard on the
    -- table's presence so v9 is order-independent vs v8.
    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='lead_ingestion_dedupe')
       AND NOT EXISTS (SELECT 1 FROM pg_policies WHERE schemaname='public' AND tablename='lead_ingestion_dedupe' AND policyname='lead_ingestion_dedupe_tenant_isolation') THEN
        EXECUTE $p$
            CREATE POLICY lead_ingestion_dedupe_tenant_isolation ON lead_ingestion_dedupe
                FOR ALL TO authenticated
                USING (brokerage_id = (auth.jwt() ->> 'brokerage_id'))
                WITH CHECK (brokerage_id = (auth.jwt() ->> 'brokerage_id'))
        $p$;
    END IF;
END $$;


-- ── Verification (reference — not executed) ─────────────────────
-- List the tenant policies created by this migration:
--   SELECT tablename, policyname FROM pg_policies
--   WHERE schemaname='public' AND policyname LIKE '%tenant%'
--      OR policyname IN ('pas_events_tenant_read','brokerages_self_read')
--   ORDER BY tablename;
--
-- IMPORTANT: these constrain only the `authenticated` role. Confirm with the
-- security team that PAS211G has (a) introduced a JWT-scoped Supabase client for
-- tenant-facing reads and (b) mints a `brokerage_id` claim, BEFORE relying on
-- these policies as an isolation control. Under the service-role key they are
-- inert by design.
