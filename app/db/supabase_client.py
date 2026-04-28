"""
Supabase Client — singleton pattern
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
    if _supabase is None:
        raise RuntimeError("Supabase not initialized. Call init_supabase() first.")
    return _supabase
