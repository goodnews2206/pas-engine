"""
Onboarding — public endpoint for brokerages to claim their invite key.

No auth required (the key itself is the credential).
POST /onboarding/claim  → validates key, marks used, returns api_key
"""

import logging

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel

from app.db.invite_store import claim_invite_key
from app.utils.rate_limiter import client_ip, rate_limit

router = APIRouter()
logger = logging.getLogger("pas.onboarding")


class ClaimRequest(BaseModel):
    key: str
    email: str = ""


@router.post("/claim")
async def claim_key(body: ClaimRequest, request: Request):
    """
    Consume a one-time invite key issued by the ORVN admin.

    Returns the brokerage's api_key on success — this is the credential
    used for all subsequent /portal/* requests. Store it securely.
    """
    # PAS211D: this endpoint is unauthenticated by design (the key is the
    # credential) and returns a brokerage api_key on success, so throttle it to
    # blunt brute-force enumeration of the invite-key space.
    rate_limit(f"onboarding_claim:{client_ip(request)}", max_requests=10, window_seconds=60)

    if not body.key or not body.key.startswith("orvn_"):
        raise HTTPException(status_code=400, detail="Invalid invite key format.")

    brokerage = claim_invite_key(body.key, used_by_email=body.email)
    if not brokerage:
        raise HTTPException(
            status_code=400,
            detail="Invite key is invalid, expired, already used, or revoked.",
        )

    logger.info(f"Onboarding claimed | brokerage={brokerage.get('id')} | email={body.email}")
    return {
        "status": "claimed",
        "brokerage_id": brokerage.get("id"),
        "brokerage_name": brokerage.get("name"),
        "api_key": brokerage.get("api_key"),
        "note": "Use the api_key as X-API-Key header for all /portal/* requests. Store it securely.",
    }
