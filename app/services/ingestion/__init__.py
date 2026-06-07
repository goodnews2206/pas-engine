"""app.services.ingestion — PAS213 minimal digital lead ingestion.

Rebuilt minimally from the PAS209.5 recovery-corpus *specification* (not copied
from bytecode): a service-first path that turns non-voice inbound leads
(website forms, portal/lead-form notifications, manual entry) into safe,
tenant-scoped operational records + events.

Doctrine carried from the corpus:
  * Tenant scope is resolved from auth, never trusted from a public payload.
  * Pure normalizers that never raise; deterministic, cross-tenant-safe dedupe.
  * No outbound call from ingestion; no Gmail/OAuth/inbox scanning.

Durable dedupe/queueing and source-specific adapters (email forwarder) are
deferred — see docs/pas213_digital_lead_ingestion_rebuild.md.
"""
