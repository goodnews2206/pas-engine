"""
Outbound Call Trigger
POST /outbound/call — accepts a lead payload (from ad form, CRM webhook, etc.)
                      and immediately dials the lead via Twilio.

Payload fields:
  phone      (required) — E.164 format, e.g. +12125551234
  name       (optional) — lead's first name for personalised greeting
  email      (optional) — for post-booking email confirmation
  intent     (optional) — buy | sell | rent  (skips that question if known)
  budget     (optional) — e.g. "$400k–$600k"  (skips budget question if known)
  timeline   (optional) — e.g. "3 months"     (skips timeline question if known)
  source     (optional) — facebook_ad | crm | website | referral  (for analytics)
  property_interest (optional) — free-text note passed to Cal.com booking
"""

import logging

from fastapi import APIRouter, Header, HTTPException, Request
from pydantic import BaseModel, field_validator
from twilio.rest import Client

from app.config import get_settings
from app.db.brokerage_store import get_brokerage_by_api_key, get_brokerage_by_id
from app.utils.call_store import pending_leads
from app.utils.rate_limiter import client_ip, rate_limit

router = APIRouter()
logger = logging.getLogger("pas.outbound")


class LeadPayload(BaseModel):
    phone: str
    brokerage_id: str = "demo"   # which brokerage is triggering this call
    name: str = ""
    email: str = ""
    intent: str = ""
    budget: str = ""
    timeline: str = ""
    source: str = "outbound"
    property_interest: str = ""

    @field_validator("phone")
    @classmethod
    def must_be_e164(cls, v: str) -> str:
        v = v.strip()
        if not v.startswith("+") or not v[1:].isdigit():
            raise ValueError("phone must be E.164 format, e.g. +12125551234")
        return v

    @field_validator("intent")
    @classmethod
    def normalise_intent(cls, v: str) -> str:
        mapping = {"buy": "buying", "buying": "buying",
                   "sell": "selling", "selling": "selling",
                   "rent": "renting", "renting": "renting"}
        return mapping.get(v.lower().strip(), v.lower().strip())


@router.post("/call")
async def trigger_outbound_call(
    request: Request,
    payload: LeadPayload,
    x_api_key: str = Header(..., description="Brokerage API key — pas_xxx"),
):
    """
    Stores lead context then dials the lead.
    Requires X-API-Key header matching the brokerage's api_key.
    When Twilio answers, it hits POST /twilio/voice where we pick up the context.
    """
    settings = get_settings()

    # Rate limit: 20 calls per minute per IP to prevent abuse
    rate_limit(f"outbound:{client_ip(request)}", max_requests=20, window_seconds=60)

    # Authenticate brokerage by API key — brokerage_id in body must match key owner
    brokerage = get_brokerage_by_api_key(x_api_key)
    if not brokerage:
        raise HTTPException(status_code=401, detail="Invalid API key.")
    if brokerage["id"] != payload.brokerage_id:
        raise HTTPException(status_code=403, detail="API key does not belong to this brokerage.")
    # get_brokerage_by_api_key already fetched the row; re-use it
    if not brokerage["active"]:
        raise HTTPException(status_code=409, detail="PAS is paused for this brokerage. Resume it first.")

    # Use brokerage's dedicated Twilio number, fall back to default
    from_number = brokerage.get("twilio_phone") or settings.TWILIO_PHONE_NUMBER

    # Store context — consumed by /twilio/voice when the call connects
    pending_leads[payload.phone] = payload.model_dump()
    logger.info(f"Outbound call queued | phone={payload.phone} | brokerage={payload.brokerage_id} | source={payload.source}")

    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        call = client.calls.create(
            to=payload.phone,
            from_=from_number,
            url=f"{settings.BASE_URL}/twilio/voice",
            status_callback=f"{settings.BASE_URL}/twilio/status",
            status_callback_method="POST",
            machine_detection="Enable",          # skip answering machines
            machine_detection_timeout=4,
        )
        logger.info(f"Twilio call created | sid={call.sid} | to={payload.phone}")
        return {"status": "dialing", "call_sid": call.sid, "phone": payload.phone}

    except Exception as e:
        # Clean up so stale context doesn't linger
        pending_leads.pop(payload.phone, None)
        logger.error(f"Failed to create outbound call: {e}")
        raise HTTPException(status_code=502, detail=f"Twilio error: {e}")
