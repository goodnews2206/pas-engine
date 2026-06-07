"""PAS213 — digital lead ingestion route.

Narrow, explicit endpoint: ``POST /ingest/lead``. Tenant is resolved from the
brokerage ``X-API-Key`` (the existing safe token pattern, reused — no auth
rewrite). The route validates the tenant, then hands the raw payload to the
ingestion service. It never dials, never mutates other surfaces.
"""
import logging
from typing import Any, Dict, Optional

from fastapi import APIRouter, Header, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.db.brokerage_store import get_brokerage_by_api_key
from app.services.ingestion.lead_ingestion import ingest_digital_lead
from app.utils.rate_limiter import client_ip, rate_limit

logger = logging.getLogger("pas.routes.ingestion")

router = APIRouter()


class DigitalLeadIn(BaseModel):
    # Tenant is resolved from X-API-Key; brokerage_id (if sent) is only
    # cross-checked against the key owner by the service.
    brokerage_id: Optional[str] = None
    source: str = "manual"
    external_lead_id: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    message: Optional[str] = None
    budget: Optional[str] = None
    timeline: Optional[str] = None
    intent: Optional[str] = None
    property_location: Optional[str] = None
    received_at: Optional[str] = None
    raw_source_label: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


@router.post("/lead")
async def ingest_lead(
    payload: DigitalLeadIn,
    request: Request,
    x_api_key: str = Header(..., description="Brokerage API key — pas_xxx"),
):
    # Anti-abuse rate limit (consistent with /outbound and /twilio).
    rate_limit(f"ingest:{client_ip(request)}", max_requests=60, window_seconds=60)

    # Tenant from auth only — fail closed on an unknown / demo key.
    brokerage = get_brokerage_by_api_key(x_api_key)
    if not brokerage or not brokerage.get("id") or brokerage.get("id") == "demo":
        return JSONResponse({"status": "failed", "error": "unauthorized"}, status_code=401)

    result = ingest_digital_lead(payload.model_dump(exclude_none=True), brokerage=brokerage)

    status_map = {"ingested": 201, "duplicate": 200, "rejected": 422, "failed": 400}
    code = status_map.get(result.get("status"), 400)
    logger.info(
        "digital lead | brokerage=%s | status=%s | source=%s",
        brokerage["id"], result.get("status"), result.get("source"),
    )
    return JSONResponse(result, status_code=code)
