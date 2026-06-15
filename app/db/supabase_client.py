"""
Supabase clients.

Two distinct access paths — DO NOT confuse them:

* ``get_supabase()`` — the global **service-role** client (``SUPABASE_SERVICE_KEY``).
  It has ``BYPASSRLS``: row-level security policies do NOT constrain it. Every
  current route/store/worker/webhook uses this path, and that remains correct
  for machine/internal/cross-tenant work (admin provisioning, ingestion,
  webhooks, background jobs, audit/event writers).

* ``get_scoped_supabase(access_token)`` — a per-request **RLS-aware** client built
  from ``SUPABASE_ANON_KEY`` + a *verified* user access token. PostgREST then runs
  as the ``authenticated`` role so RLS (``auth.jwt() ->> 'brokerage_id'``) applies
  at the database. PAS211G.4 adds this factory as an inert seam — NO route or
  store calls it yet; wiring it (and applying the RLS migration) is a later,
  separately-audited checkpoint.
"""

import logging
from supabase import create_client, Client

from app.config import get_settings

logger = logging.getLogger("pas.db")

_supabase: Client | None = None


def init_supabase():
    global _supabase
    settings = get_settings()
    _supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_KEY)
    logger.info("Supabase client initialized")


def get_supabase() -> Client:
    """Return the global SERVICE-ROLE client (bypasses RLS). Unchanged."""
    if _supabase is None:
        raise RuntimeError("Supabase not initialized. Call init_supabase() first.")
    return _supabase


def get_scoped_supabase(access_token: str) -> Client:
    """Build a per-request, RLS-aware Supabase client for a verified user.

    PAS211G.4 — inert seam. Constructs a fresh client with the **anon** key (NOT
    the service-role key) and attaches the caller's *already-verified* Supabase
    access token, so PostgREST sends ``Authorization: Bearer <token>`` and the
    database evaluates RLS as the ``authenticated`` role. Construction makes no
    network call.

    Fails CLOSED — raises rather than degrading to service-role access — when:
      * ``access_token`` is empty/missing (no identity to scope to), or
      * ``SUPABASE_URL`` / ``SUPABASE_ANON_KEY`` is not configured.

    It NEVER falls back to ``get_supabase()`` and NEVER uses the service-role
    key. No route or store calls this yet.
    """
    if not access_token:
        raise RuntimeError(
            "get_scoped_supabase requires a verified access token — refusing to "
            "build a tenant-scoped client without one (fail closed)."
        )

    settings = get_settings()
    url = settings.SUPABASE_URL or ""
    anon_key = settings.SUPABASE_ANON_KEY or ""
    if not url:
        raise RuntimeError("SUPABASE_URL is not configured — cannot build scoped client.")
    if not anon_key:
        raise RuntimeError(
            "SUPABASE_ANON_KEY is not configured — cannot build an RLS-aware "
            "scoped client (fail closed; will not use the service-role key)."
        )

    client = create_client(url, anon_key)
    # Run subsequent PostgREST requests as the authenticated user so RLS applies.
    client.postgrest.auth(access_token)
    return client
