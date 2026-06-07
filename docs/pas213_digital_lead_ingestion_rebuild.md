# PAS213 — Digital Lead Ingestion Rebuild

**Type:** Implementation + documentation. PAS213 rebuilds the **minimal** digital lead ingestion path so brokerages can send non-voice leads (website forms, portal/lead-form notifications, manual entry) into PAS and have them become safe, tenant-scoped operational records — without relying on Twilio voice flows.

Rebuilt **from the PAS209.5 recovery-corpus specification only** (not copied from bytecode). Distinct, minimal module names signal a fresh rebuild, not a restore of the PAS160–169 subsystem.

---

## 1. Scope

**In scope (built):**
- A digital lead **contract** (`lead_contracts.py`) + pure **normalizers** (`lead_normalizers.py`).
- Deterministic, tenant-scoped **dedupe** (`lead_dedupe.py`, process-local v1).
- A service-first **ingestion service** (`lead_ingestion.py`) with injectable DB/event deps.
- A narrow **route** `POST /ingest/lead` (`app/routes/lead_ingestion.py`), wired in `main.py`.

**Out of scope (deliberately not built):**
- Gmail OAuth / inbox scanning / any external service.
- Source-specific parsers (Zillow/Realtor/Facebook email bodies) → **PAS213B**.
- Durable (DB-backed) dedupe + pending-call queueing → **PAS213C**.
- Web UI, CORS, broad auth rewrite, CRM replacement.
- Automatic memory approval, outbound automation, any behaviour change outside the ingestion path.

---

## 2. Ingestion contract

Input payload (`DigitalLeadIn` / accepted keys): `source` (required), `external_lead_id`, `name`, `phone`, `email`, `message`, `budget`, `timeline`, `intent`, `property_location`, `received_at`, `raw_source_label`, `metadata`, and `brokerage_id` (accepted **only** for an auth cross-check — never trusted as the tenant). Unknown keys are preserved into `metadata`.

Canonical `NormalizedLead` carries **no `brokerage_id`** (tenant comes from auth). `source` ∈ `{website_form, zillow, realtor_com, facebook, manual, email_forwarder}`; unknown → `manual` + warning (raw label preserved). **`phone` is required** (the leads table and call paths are phone-keyed); email-only leads are deferred to PAS213B.

---

## 3. Normalization rules

- **Phone:** strip formatting; 10 digits → `+1XXXXXXXXXX`; 11 digits starting `1` → `+1…`; leading `+` preserved; ≥8 digits → best-effort `+…`; otherwise invalid → lead **rejected**.
- **Email:** trimmed, lowercased, basic shape-checked; invalid → dropped (not fatal).
- **Name:** whitespace-collapsed.
- **Unknown fields + explicit `metadata`:** preserved under `NormalizedLead.metadata`.
- Pure functions, **never raise**; a malformed payload yields a structural `failed` envelope.

---

## 4. Dedupe rules

Deterministic key (no randomness/timestamp in the primary path):
- **Preferred:** `tenant | source | ext:external_lead_id`.
- **Fallback:** `tenant | contact:(phone|email) | (msg:<hash> if message else day:<received_at[:10]>)`.

Idempotent: a repeated identical submission under the same tenant returns `duplicate` and is written once. **No cross-tenant dedupe** — `brokerage_id` is in the key *and* the store is bucketed per tenant. Process-local v1 surfaces the structural warning `lead_dedupe_store_is_process_local` (durable store = PAS213C).

---

## 5. Tenant safety

- Tenant is resolved from the brokerage **`X-API-Key`** (the existing safe token pattern, reused — no auth rewrite). The route fails closed (401) on an unknown/`demo` key.
- The service takes the **authenticated brokerage** and uses its id as the only tenant source. A payload `brokerage_id` that differs from the authenticated tenant is **rejected** (`tenant_mismatch`); it is never silently overridden or inferred.
- Empty/`demo` tenant → `failed: tenant_unresolved` (fail closed).
- The emitted event payload carries **no raw phone/email** (only `has_email`/`has_message` flags + structural facts) — no secrets/PII in logs.

---

## 6. Route / service summary

- **Service:** `ingest_digital_lead(payload, *, brokerage, dedupe_store=, lead_writer=, event_sink=)` → validate tenant → reject mismatch → normalize → dedupe → upsert lead (via `lead_memory.upsert_lead` by default) → emit `lead.ingested` event → return a **source-transparent** envelope (`status`, `source_mode="digital_ingestion"`, `brokerage_id`, `dedupe_key`, `source`, `lead_created`, `warnings`). Dependencies are injectable for testing without a DB.
- **Route:** `POST /ingest/lead` (`X-API-Key`), IP rate-limited (60/min, consistent with `/outbound`, `/twilio`), maps service status → HTTP (`ingested`→201, `duplicate`→200, `rejected`→422, `failed`→400, unauthorized→401).
- **No outbound call.** The ingestion modules import nothing from Twilio / Cal.com / the call engine; ingestion never dials. Deferred pending-call enqueue is PAS213C.

---

## 7. What is NOT implemented

- No durable dedupe / pending-call queue (process-local v1 only).
- No source-specific email parsing or forwarder signature verification.
- No automatic outbound call, no memory approval, no behaviour change elsewhere.
- No email-only leads (phone required in v1).

---

## 8. Future steps

- **PAS213B — Email forwarder + source-specific adapters.** A signed forwarder endpoint (`X-PAS-Webhook-Secret` / HMAC, per the corpus `security` spec) and per-provider parsers (Zillow/Realtor/Facebook), projecting onto this same `NormalizedLead`. Still no Gmail/OAuth/inbox scanning.
- **PAS213C — Durable dedupe + safe deferred queueing.** Supabase-backed dedupe (replacing the process-local registry) and, only if the durable pending-call path is rebuilt and proven safe, optional deferred call enqueue — never a direct dial from ingestion.

---

## 9. PAS213B — durable persistence, dedupe & event logging

PAS213 was service-first and test-safe but its dedupe was **process-local** — a
restart lost the seen-key set, so a re-posted form after a redeploy could create
a second operational record. PAS213B upgrades ingestion to be **durable enough
for a paying brokerage** without widening any boundary: no Gmail/OAuth, no inbox
scanning, no external vendors, no CRM writeback, no outbound call, no auth
rewrite, no new dependency.

> Note: §8 originally pencilled "PAS213B" as the email forwarder. That work is
> re-tagged **PAS214** below; PAS213B is the durability checkpoint that landed.

### 9.1 Durable persistence decision

The normalized lead already persists to the existing **`leads`** table via
`lead_memory.upsert_lead` (tenant-scoped, `UNIQUE(brokerage_id, phone_number)`),
which is exactly what the **PAS210 / PAS206 read-only snapshot adapter** reads to
build operational intelligence. That write path is durable and unchanged — so
digital leads already land where the snapshot bridge can see them. PAS213B keeps
it as the default writer; no change to the `leads` schema was needed.

### 9.2 Durable dedupe strategy

Dedupe moves from in-memory to a dedicated **`lead_ingestion_dedupe`** ledger
(`SupabaseLeadDedupeStore`, now the service default):

- **Restart-survival:** the seen-key set lives in Postgres, not process memory.
- **Tenant-scoped:** `brokerage_id` is part of `UNIQUE(brokerage_id, dedupe_key)`
  and every read filters on it → **no cross-tenant dedupe**, ever.
- **Key preference unchanged** from PAS213: `external_lead_id` preferred, else a
  `contact | (message-hash | received-day)` fallback (deterministic, PII-free
  `dl_<sha>` token).
- **Race backstop:** the `UNIQUE` constraint rejects a concurrent duplicate
  registration, which the store swallows — race-safe to the extent the existing
  check-then-write DB pattern allows (the same pattern `lead_memory` uses).
- **Fails open, never silent-drops:** on any DB error (including *table not yet
  created because the migration is unapplied*), `is_duplicate` returns False and
  the lead is still persisted + evented. A rare duplicate is acceptable; a lost
  lead is not. The dedupe key is registered **after** the lead write so a write
  failure cannot strand a key and drop a legitimate retry.
- Injecting the process-local `LeadDedupeStore` still works (and still surfaces
  `lead_dedupe_store_is_process_local`) for unit tests.

### 9.3 Migration status

**Created, NOT applied:** `scripts/migrate_v8_digital_ingestion_dedupe.sql`
(additive, idempotent `CREATE TABLE IF NOT EXISTS` + indexes + RLS-enable,
following the existing `migrate_v*.sql` convention). It must be applied by an
operator in the Supabase SQL editor, exactly like every prior migration. Until
then, durable dedupe degrades safely (§9.2). The table stores **no raw PII** —
only the opaque dedupe-key token, the source label, and an optional vendor
`external_lead_id`.

### 9.4 Event logging behaviour

Ingestion now emits the full lifecycle through the existing durable
`pas_events` sink (`event_logger.log_event_bg`), all **PII-free**:

| event | when | payload (structural only) |
|-------|------|---------------------------|
| `lead.ingested` | new lead persisted | source, raw_source_label, external_lead_id, dedupe_key, has_email, has_message, lead_created |
| `lead.duplicate` | dedupe hit | source, raw_source_label, external_lead_id, dedupe_key |
| `lead.rejected` | normalization failure or `tenant_mismatch` | reason, errors / claimed_brokerage_id, source |

No phone / email / name / message text ever enters a payload. `tenant_unresolved`
emits **nothing** — with no tenant there is nothing to scope an event to.

### 9.5 What remains for PAS213C / PAS214

- **PAS213C** — apply `migrate_v8`, then optional safe deferred call enqueue
  (still never a direct dial from ingestion) and dedupe `hit_count`/`last_seen_at`
  bumping on repeat hits.
- **PAS214** — email-forwarder endpoint (signed `X-PAS-Webhook-Secret` / HMAC)
  and per-provider source adapters projecting onto this same `NormalizedLead`.
  Still no Gmail/OAuth/inbox scanning.

---

*End of PAS213B. Durable lead persistence + dedupe + lifecycle events on top of
PAS213, within the same boundaries: durable `lead_ingestion_dedupe` ledger
(migration proposal only — not applied), durable `pas_events` lifecycle logging,
tenant isolation preserved, PII-free events, no outbound dial, no Gmail/OAuth, no
external services, no new dependencies, no behaviour change outside ingestion.
PAS209 / parked stash / `__pycache__` untouched. Corpus used as spec only.*
