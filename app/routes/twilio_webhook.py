"""
Twilio Webhook Routes
POST /twilio/voice  — called by Twilio on inbound AND outbound call answer
POST /twilio/status — called by Twilio when call ends (duration/status finalisation)
"""

import logging
from fastapi import APIRouter, HTTPException, Request, Response
from twilio.request_validator import RequestValidator
from twilio.twiml.voice_response import VoiceResponse, Connect, Stream

from app.config import get_settings
from app.db.call_logger import create_call_record
from app.db.brokerage_store import get_brokerage_by_phone
from app.utils.call_store import pending_leads, active_calls
from app.utils.rate_limiter import rate_limit, client_ip

router = APIRouter()
logger = logging.getLogger("pas.twilio_webhook")
settings = get_settings()


def _verify_twilio(request: Request, form_data: dict) -> bool:
    """
    Validate the X-Twilio-Signature header to confirm the request
    genuinely came from Twilio and has not been tampered with.
    Uses the Twilio auth token as the HMAC key.
    """
    validator = RequestValidator(settings.TWILIO_AUTH_TOKEN)
    # Reconstruct the URL Twilio signed — respect reverse-proxy headers
    proto = request.headers.get("X-Forwarded-Proto", request.url.scheme)
    host = request.headers.get("X-Forwarded-Host", request.headers.get("host", request.url.netloc))
    url = f"{proto}://{host}{request.url.path}"
    signature = request.headers.get("X-Twilio-Signature", "")
    return validator.validate(url, form_data, signature)


@router.post("/voice")
async def incoming_call(request: Request):
    form_data = await request.form()
    form_dict = dict(form_data)

    # Rate limit: 60 webhook hits/min per IP (Twilio CDN IPs are consistent)
    rate_limit(f"twilio_voice:{client_ip(request)}", max_requests=60, window_seconds=60)

    # Verify the request genuinely came from Twilio. RN-2 (PAS211A): the seam is
    # require_twilio_signature, which is True in every non-development env, so a
    # forged webhook can never be silently accepted in production.
    if settings.require_twilio_signature and not _verify_twilio(request, form_dict):
        logger.warning(f"Rejected forged Twilio voice webhook from {client_ip(request)}")
        raise HTTPException(status_code=403, detail="Invalid Twilio signature.")

    call_sid = form_data.get("CallSid", "unknown")
    caller = form_data.get("From", "unknown")
    callee = form_data.get("To", "unknown")
    direction = form_data.get("Direction", "inbound")
    answered_by = form_data.get("AnsweredBy", "")  # from machine_detection

    def _mask(phone: str) -> str:
        return phone[:3] + "****" + phone[-3:] if len(phone) > 6 else "***"

    logger.info(f"Call webhook | SID={call_sid} | dir={direction} | from={_mask(caller)} | to={_mask(callee)}")

    # For outbound, the lead is the party we dialled (To)
    lead_phone = callee if direction == "outbound-api" else caller

    # Answering machine — leave a short voicemail and end
    if answered_by in ("machine_start", "fax"):
        logger.info(f"[{call_sid}] Answering machine detected — leaving voicemail")
        twiml = VoiceResponse()
        twiml.pause(length=2)
        twiml.say(
            "Hi, this is Alex from ORVN Realty. We'd love to book you in for a property "
            "viewing — please call us back or visit orvnlabs.com. Have a great day!",
            voice="Polly.Joanna"
        )
        pending_leads.pop(lead_phone, None)
        return Response(content=str(twiml), media_type="application/xml")

    # Identify which brokerage owns this Twilio number
    brokerage = get_brokerage_by_phone(callee if direction == "outbound-api" else lead_phone)
    if not brokerage["active"] and direction == "outbound-api":
        logger.info(f"[{call_sid}] Brokerage {brokerage['id']} is paused — dropping outbound call")
        twiml = VoiceResponse()
        twiml.hangup()
        return Response(content=str(twiml), media_type="application/xml")

    # Pick up outbound lead context that was stored by /outbound/call
    lead_context = pending_leads.pop(lead_phone, None)
    if lead_context:
        active_calls[call_sid] = {"lead": lead_context, "brokerage": brokerage}
        logger.info(f"[{call_sid}] Outbound context loaded for {lead_phone}")
    else:
        active_calls[call_sid] = {"lead": None, "brokerage": brokerage}

    # Persist call record
    await create_call_record(
        call_sid=call_sid,
        phone_number=lead_phone,
        email=lead_context.get("email", "") if lead_context else "",
        source=lead_context.get("source", "inbound") if lead_context else "inbound",
        brokerage_id=brokerage["id"],
    )

    # Build WebSocket stream URL
    ws_base = settings.BASE_URL.replace("https://", "wss://").replace("http://", "ws://")
    stream_url = f"{ws_base}/ws/media-stream/{call_sid}"

    response = VoiceResponse()
    connect = Connect()
    stream = Stream(url=stream_url)
    stream.parameter(name="callSid", value=call_sid)
    stream.parameter(name="caller", value=lead_phone)
    connect.append(stream)
    response.append(connect)

    logger.info(f"[{call_sid}] Returning TwiML | stream_url={stream_url}")
    return Response(content=str(response), media_type="application/xml")


@router.post("/status")
async def call_status(request: Request):
    form_data = await request.form()
    form_dict = dict(form_data)

    # RN-2 (PAS211A): enforce in every non-development env (see /voice above).
    if settings.require_twilio_signature and not _verify_twilio(request, form_dict):
        logger.warning(f"Rejected forged Twilio status webhook from {client_ip(request)}")
        raise HTTPException(status_code=403, detail="Invalid Twilio signature.")

    call_sid = form_data.get("CallSid", "unknown")
    call_status = form_data.get("CallStatus", "unknown")
    duration = form_data.get("CallDuration", "0")

    logger.info(f"Call status | SID={call_sid} | status={call_status} | duration={duration}s")

    # Clean up active call context
    active_calls.pop(call_sid, None)

    from app.db.call_logger import finalize_call_on_hangup
    await finalize_call_on_hangup(
        call_sid=call_sid,
        duration_seconds=int(duration),
        raw_status=call_status,
    )
    return Response(status_code=204)
