"""
PAS Configuration — All env vars in one place.
Copy .env.example to .env and fill in values.
"""

import os
from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings


# PAS211A — values of ENVIRONMENT that count as production.
_PRODUCTION_ENV_VALUES = {"production", "prod"}

# PAS211A — deployment-platform env vars whose mere presence implies a hosted,
# production-like runtime. If any is set but ENVIRONMENT is not production, the
# deployment is almost certainly mis-configured (dev defaults on a real host).
_PRODUCTION_INDICATOR_VARS = (
    "RENDER",
    "VERCEL",
    "FLY_APP_NAME",
    "HEROKU_APP_NAME",
    "DYNO",
    "RAILWAY_ENVIRONMENT",
    "RAILWAY_PROJECT_ID",
    "RAILWAY_SERVICE_ID",
    "KUBERNETES_SERVICE_HOST",
)


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

    # ── PAS211G.1 — principal resolver boundary ─────────────────────
    # JWT verification is SCAFFOLDING ONLY in PAS211G.1. While JWT_AUTH_ENABLED
    # is False (default) the resolver's JWT path returns None (no Bearer auth).
    # When an operator flips it True before PAS211G.2 wires real verification,
    # the JWT path FAILS CLOSED (still returns None) — it must never grant access
    # without a verified token. No JWT secret is required at startup either way.
    JWT_AUTH_ENABLED: bool = False
    JWT_ISSUER: str = ""        # reserved for PAS211G.2 verification
    JWT_AUDIENCE: str = ""      # reserved for PAS211G.2 verification

    # Master switch for the legacy X-Admin-Key / X-API-Key resolver paths. Kept
    # True so existing API-key flows are unchanged in PAS211G.1.
    ENABLE_LEGACY_API_KEY_AUTH: bool = True

    # ── PAS211D — critical security fix pack 1 ──────────────────────
    # Demo / simulation endpoints (/simulate-call, /demo/token) are developer +
    # sales tools, not paid-client surfaces. They stay available outside
    # production; in production they are disabled (404) unless an operator
    # explicitly opts back in here. Closes the anonymous-exposure holes from
    # the PAS211C audit while keeping local/dev usable.
    ENABLE_DEMO_ENDPOINTS: bool = False

    # Only honour X-Forwarded-For for per-IP rate limiting when the deployment
    # explicitly declares it sits behind a trusted reverse proxy. Default off so
    # a client cannot spoof the header to mint unlimited rate-limit buckets.
    TRUST_PROXY_HEADERS: bool = False

    # ── PAS211F — secrets at rest ───────────────────────────────────
    # When enabled, newly created/rotated brokerage API keys and invite keys are
    # stored HASHED (api_key_hash / key_hash) and the plaintext column is left
    # empty; lookups hash the presented value. DEFAULT OFF — turn on only AFTER
    # applying scripts/migrate_v10_secrets_encryption_rotation.sql (which adds
    # api_key_hash). Pre-existing plaintext keys keep working via a legacy
    # fallback during the compatibility phase.
    SECRETS_HASHING_ENABLED: bool = False

    # Optional deployment-wide pepper mixed into credential hashes so a stolen
    # database alone cannot be brute-forced without it. Rotate via key_version.
    SECRET_HASH_PEPPER: str = ""

    # ── PAS211H — prompt & memory injection safety ──────────────────
    # Self-training distils call transcripts into a persisted
    # OBJECTION_SYSTEM_PROMPT. PAS211H sanitizes/delimits transcript input AND
    # denylist-validates the generated prompt before saving. This flag is the
    # operator kill-switch: set False to stop persisting generated system prompts
    # entirely (training still computes insights; the prompt is just not saved).
    SELF_TRAINING_PROMPT_PERSIST_ENABLED: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True

    # ── PAS211A — production config + signature guards ──────────────

    @property
    def is_production(self) -> bool:
        return (self.ENVIRONMENT or "").strip().lower() in _PRODUCTION_ENV_VALUES

    @property
    def is_development(self) -> bool:
        return (self.ENVIRONMENT or "").strip().lower() == "development"

    @property
    def demo_endpoints_allowed(self) -> bool:
        """PAS211D: demo/simulation routes are open outside production; in
        production they require an explicit ENABLE_DEMO_ENDPOINTS opt-in. Keeps
        local/dev usable while closing the production exposure."""
        return (not self.is_production) or self.ENABLE_DEMO_ENDPOINTS

    @property
    def require_twilio_signature(self) -> bool:
        """RN-2: Twilio signature verification is skipped ONLY in explicit
        development. Any non-development environment (incl. production) enforces
        it, so a forged webhook can never be silently accepted in production."""
        return not self.is_development

    def production_indicators(self) -> List[str]:
        """Deployment signals suggesting a production-like host. Read live from
        os.environ so a mis-set ENVIRONMENT is caught even with cached settings."""
        found = [v for v in _PRODUCTION_INDICATOR_VARS if os.environ.get(v)]
        base = (self.BASE_URL or "").strip().lower()
        if base.startswith("https://") and "localhost" not in base and "127.0.0.1" not in base:
            found.append("BASE_URL(https)")
        return found

    def looks_like_production(self) -> bool:
        return bool(self.production_indicators())

    def validate_runtime_security(self) -> None:
        """RN-1: fail fast when a production-like deployment is running with a
        non-production ENVIRONMENT. Dev defaults on a real host would silently
        disable Twilio signature enforcement, weaken admin-key checks, and expose
        /docs. Local development (no indicators) is unaffected."""
        if self.looks_like_production() and not self.is_production:
            indicators = ", ".join(self.production_indicators())
            raise RuntimeError(
                "PAS refused to start: production deployment indicators detected "
                f"({indicators}) but ENVIRONMENT={self.ENVIRONMENT!r}. Set "
                "ENVIRONMENT=production to enforce signature verification and "
                "admin-key checks, or remove the deployment indicators for local "
                "development."
            )


@lru_cache()
def get_settings() -> Settings:
    return Settings()
