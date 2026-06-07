"""
Demo Call API — lets website visitors call PAS from a browser.

Flow:
  1. Browser fetches GET /demo/token  → gets a short-lived Twilio Access Token
  2. Browser SDK (Twilio.js) uses the token to place a call
  3. Twilio calls POST /demo/call     → this webhook returns TwiML connecting to PAS
  4. WebSocket opens, PASEngine runs with demo brokerage config

Setup required (one-time, in Twilio console):
  - Create an API Key: console.twilio.com/project/api-keys
    → set TWILIO_API_KEY_SID and TWILIO_API_SECRET in Railway
  - Create a TwiML App: console.twilio.com/voice/twiml/apps
    → set Voice Request URL to: https://your-railway-url/demo/call
    → set TWILIO_TWIML_APP_SID in Railway
"""

import logging
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import JSONResponse
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant
from twilio.twiml.voice_response import VoiceResponse, Connect, Stream
from twilio.request_validator import RequestValidator

from app.config import get_settings
from app.db.brokerage_store import get_brokerage_by_id
from app.db.call_logger import create_call_record
from app.utils.call_store import active_calls
from app.utils.rate_limiter import client_ip, rate_limit

router = APIRouter()
logger = logging.getLogger("pas.demo")


def _demo_cors_origin(settings) -> str:
    """PAS211D: only the wide-open `*` in development. In any other environment
    restrict the demo token's CORS to the configured site origin so an arbitrary
    third-party page can't mint billable Twilio voice tokens via the browser."""
    if settings.is_development:
        return "*"
    return (settings.BASE_URL or "").split(",")[0].strip() or "null"


@router.get("/token")
async def get_demo_token(request: Request):
    """
    Returns a 5-minute Twilio Access Token for the browser SDK.

    PAS211D: this mints a *billable* live Twilio voice grant, so it is disabled
    in production unless explicitly re-enabled (ENABLE_DEMO_ENDPOINTS), is
    per-IP rate limited, and its CORS is restricted to the site origin outside
    development.
    """
    settings = get_settings()
    cors_origin = _demo_cors_origin(settings)

    if not settings.demo_endpoints_allowed:
        # Don't advertise the capability in production.
        raise HTTPException(status_code=404, detail="Not found")

    # Throttle anonymous token minting (each token can place a billable call).
    rate_limit(f"demo_token:{client_ip(request)}", max_requests=10, window_seconds=60)

    if not all([settings.TWILIO_API_KEY_SID, settings.TWILIO_API_SECRET, settings.TWILIO_TWIML_APP_SID]):
        logger.warning("Demo calling requested but TWILIO_API_KEY_SID / TWILIO_API_SECRET / TWILIO_TWIML_APP_SID not configured")
        response = JSONResponse(
            status_code=503,
            content={"error": "Demo calling is not configured yet. Contact ORVN."}
        )
        response.headers["Access-Control-Allow-Origin"] = cors_origin
        return response

    token = AccessToken(
        settings.TWILIO_ACCOUNT_SID,
        settings.TWILIO_API_KEY_SID,
        settings.TWILIO_API_SECRET,
        identity="web_demo",
        ttl=300,  # 5 minutes — enough for one demo call
    )
    token.add_grant(VoiceGrant(outgoing_application_sid=settings.TWILIO_TWIML_APP_SID))

    logger.info("Demo token issued for browser call")
    response = JSONResponse(content={"token": token.to_jwt(), "ttl": 300})
    response.headers["Access-Control-Allow-Origin"] = cors_origin
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    return response


@router.options("/token")
async def demo_token_preflight():
    """Handle CORS preflight from the website."""
    cors_origin = _demo_cors_origin(get_settings())
    response = Response(status_code=204)
    response.headers["Access-Control-Allow-Origin"] = cors_origin
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


@router.post("/call")
async def demo_call_webhook(request: Request):
    """
    TwiML webhook — Twilio calls this when the browser SDK connects.
    Set this URL as the Voice Request URL in your Twilio TwiML App.

    Returns TwiML that streams audio into the PAS WebSocket handler,
    using the demo brokerage config (ORVN Realty defaults).
    """
    settings = get_settings()
    form = await request.form()
    form_dict = dict(form)

    # Verify the request came from Twilio
    if settings.ENVIRONMENT != "development":
        validator = RequestValidator(settings.TWILIO_AUTH_TOKEN)
        proto = request.headers.get("X-Forwarded-Proto", request.url.scheme)
        host = request.headers.get("X-Forwarded-Host", request.headers.get("host", request.url.netloc))
        url = f"{proto}://{host}{request.url.path}"
        sig = request.headers.get("X-Twilio-Signature", "")
        if not validator.validate(url, form_dict, sig):
            logger.warning("Rejected forged demo call webhook")
            return Response(status_code=403)

    call_sid = form_dict.get("CallSid", "demo_unknown")
    logger.info(f"[{call_sid}] Demo call initiated from browser")

    # Use the demo brokerage — falls back to safe defaults if Supabase is unavailable
    brokerage = get_brokerage_by_id("demo")
    active_calls[call_sid] = {
        "brokerage": brokerage,
        "lead": {"source": "web_demo"},
    }

    await create_call_record(
        call_sid=call_sid,
        phone_number="web_demo",
        email="",
        source="web_demo",
        brokerage_id=brokerage.get("id", "demo"),
    )

    ws_base = settings.BASE_URL.replace("https://", "wss://").replace("http://", "ws://")
    stream_url = f"{ws_base}/ws/media-stream/{call_sid}"

    response = VoiceResponse()
    connect = Connect()
    stream = Stream(url=stream_url)
    stream.parameter(name="callSid", value=call_sid)
    stream.parameter(name="caller", value="web_demo")
    connect.append(stream)
    response.append(connect)

    logger.info(f"[{call_sid}] Demo TwiML returned | stream={stream_url}")
    return Response(content=str(response), media_type="application/xml")
