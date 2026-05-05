"""
PAS Configuration — All env vars in one place.
Copy .env.example to .env and fill in values.
"""

from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Twilio (voice calls — optional in simulation/demo mode)
    TWILIO_ACCOUNT_SID: str = ""
    TWILIO_AUTH_TOKEN: str = ""
    TWILIO_PHONE_NUMBER: str = ""

    # Deepgram (STT — optional in simulation/demo mode)
    DEEPGRAM_API_KEY: str = ""

    # ElevenLabs (TTS — optional in simulation/demo mode)
    ELEVENLABS_API_KEY: str = ""
    ELEVENLABS_VOICE_ID: str = "21m00Tcm4TlvDq8ikWAM"  # Rachel — professional, warm

    # LLM provider selection — "anthropic" (default) or "openai".
    # PAS routes objection handling through whichever is configured.
    LLM_PROVIDER: str = "anthropic"

    # Anthropic (objection handling — optional, has safe fallback)
    ANTHROPIC_API_KEY: str = ""

    # OpenAI (alternative LLM provider — optional, has safe fallback)
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4.1-mini"

    # Supabase (persistence — optional, logs a warning when missing)
    SUPABASE_URL: str = ""
    SUPABASE_SERVICE_KEY: str = ""

    # Cal.com (booking — optional, returns simulated booking when missing)
    CALCOM_API_KEY: str = ""
    CALCOM_EVENT_TYPE_ID: int = 0

    # Notifications
    RESEND_API_KEY: str = ""          # resend.com — leave blank to disable email
    FROM_EMAIL: str = "alex@orvnlabs.com"

    # Admin
    ADMIN_API_KEY: str = ""           # set a strong secret — required to use /admin/* routes

    # Twilio Browser Calling (for the website "Talk to Alex" demo widget)
    TWILIO_API_KEY_SID: str = ""
    TWILIO_API_SECRET: str = ""
    TWILIO_TWIML_APP_SID: str = ""

    # App
    BASE_URL: str = "http://localhost:8000"
    ENVIRONMENT: str = "development"

    # Auth — Supabase Auth + legacy key transition flags (PAS133).
    # SUPABASE_JWT_SECRET is the HS256 secret used by Supabase Auth to sign
    # access tokens. The PAS backend will use it to verify Bearer tokens
    # statelessly. Empty string means JWT verification is unavailable —
    # legacy key auth still works while these flags are on.
    SUPABASE_JWT_SECRET: str = ""

    # Legacy auth flags. Default True so PAS133A is a no-op for behaviour;
    # PAS133B reads them from resolve_principal(); PAS133D flips them off
    # in production after the dashboard has fully migrated.
    ENABLE_LEGACY_ADMIN_KEY_AUTH: bool = True
    ENABLE_LEGACY_BROKERAGE_KEY_AUTH: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
