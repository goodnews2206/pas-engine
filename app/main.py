"""
PAS (Performative AI SuperStaff) - Main Entry Point
ORVN Labs | Production MVP
"""

import logging
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware

from app.routes.twilio_webhook import router as twilio_router
from app.routes.websocket_handler import router as ws_router
from app.routes.outbound import router as outbound_router
from app.routes.slack_command import router as slack_router
from app.routes.admin import router as admin_router
from app.routes.agents import router as agents_router
from app.routes.portal import router as portal_router
from app.routes.demo import router as demo_router
from app.db.supabase_client import init_supabase
from app.config import get_settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("pas.main")

MAX_BODY_SIZE = 64 * 1024  # 64 KB — enough for any legitimate PAS payload


class BodySizeLimitMiddleware(BaseHTTPMiddleware):
    """Reject requests with bodies larger than MAX_BODY_SIZE to prevent memory exhaustion."""
    async def dispatch(self, request: Request, call_next):
        content_length = request.headers.get("content-length")
        if content_length and int(content_length) > MAX_BODY_SIZE:
            return Response(content="Request body too large.", status_code=413)
        return await call_next(request)


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    logger.info("PAS Engine starting up...")

    # Warn loudly about weak admin key — do not block startup, but be impossible to miss
    if not settings.ADMIN_API_KEY:
        logger.critical("SECURITY: ADMIN_API_KEY is not set — /admin routes are locked but should be configured before deploying.")
    elif settings.ADMIN_API_KEY in ("change-me-before-deploy", "admin", "secret", "password"):
        logger.critical(f"SECURITY: ADMIN_API_KEY is set to a weak default value '{settings.ADMIN_API_KEY}' — change it immediately.")

    if settings.ENVIRONMENT == "development":
        logger.warning("SECURITY: Running in DEVELOPMENT mode — Twilio signature verification is DISABLED.")

    try:
        init_supabase()
    except Exception as e:
        logger.warning(f"Supabase unavailable — DB logging disabled: {e}")
    yield
    logger.info("PAS Engine shutting down.")


app = FastAPI(
    title="PAS — Performative AI SuperStaff",
    description="Real-time voice orchestration engine for real estate lead qualification",
    version="1.0.0-mvp",
    lifespan=lifespan,
    # Disable /docs and /redoc in production — don't expose the API schema publicly
    docs_url="/docs" if __import__("os").getenv("ENVIRONMENT", "development") == "development" else None,
    redoc_url=None,
)

# Body size limit must be first so it runs before any route handler
app.add_middleware(BodySizeLimitMiddleware)

settings = get_settings()
_allowed_origins = (
    ["*"]
    if settings.ENVIRONMENT == "development"
    else [o.strip() for o in settings.BASE_URL.split(",") if o.strip()]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["Content-Type", "X-Admin-Key", "X-API-Key"],
)

app.include_router(twilio_router, prefix="/twilio", tags=["Twilio"])
app.include_router(ws_router, prefix="/ws", tags=["WebSocket"])
app.include_router(outbound_router, prefix="/outbound", tags=["Outbound"])
app.include_router(slack_router, prefix="/slack", tags=["Slack"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(agents_router, prefix="/admin", tags=["Agents"])
app.include_router(portal_router, prefix="/portal", tags=["Portal"])
app.include_router(demo_router, prefix="/demo", tags=["Demo"])

# Serve the brokerage client dashboard at /dashboard
_dashboard_dir = os.path.join(os.path.dirname(__file__), "static", "dashboard")
if os.path.isdir(_dashboard_dir):
    app.mount("/dashboard", StaticFiles(directory=_dashboard_dir, html=True), name="dashboard")


@app.get("/health")
async def health():
    return {"status": "operational", "system": "PAS MVP"}
