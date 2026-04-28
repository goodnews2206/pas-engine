"""
PAS Configuration — All env vars in one place.
Copy .env.example to .env and fill in values.
"""

from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Twilio
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_PHONE_NUMBER: str

    # Deepgram
    DEEPGRAM_API_KEY: str

    # ElevenLabs
    ELEVENLABS_API_KEY: str
    ELEVENLABS_VOICE_ID: str = "21m00Tcm4TlvDq8ikWAM"  # Rachel — professional, warm

    # Anthropic
    ANTHROPIC_API_KEY: str

    # Supabase
    SUPABASE_URL: str
    SUPABASE_SERVICE_KEY: str

    # Cal.com
    CALCOM_API_KEY: str
    CALCOM_EVENT_TYPE_ID: int  # get from Cal.com dashboard

    # Notifications
    RESEND_API_KEY: str = ""          # resend.com — leave blank to disable email
    FROM_EMAIL: str = "alex@orvnlabs.com"

    # Admin
    ADMIN_API_KEY: str = ""           # set a strong secret — required to use /admin/* routes

    # App
    BASE_URL: str  # e.g. https://your-app.up.railway.app
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
