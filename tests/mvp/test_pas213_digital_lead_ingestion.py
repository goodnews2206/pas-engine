"""PAS213 — digital lead ingestion tests (service-first + narrow route).

Covers: valid ingest, empty rejected, normalization, same-tenant dedupe,
no cross-tenant dedupe, external_lead_id dedupe, missing tenant fails closed,
event emitted, no outbound call (import scan), raw metadata preserved, source
labels handled.
"""
import ast
import inspect

import pytest

from app.services.ingestion import lead_contracts as lc
from app.services.ingestion import lead_ingestion as svc
from app.services.ingestion import lead_normalizers as norm
from app.services.ingestion.lead_dedupe import LeadDedupeStore
from app.services.ingestion.lead_ingestion import ingest_digital_lead

BRK_A = {"id": "brk-A"}
BRK_B = {"id": "brk-B"}


class _Recorder:
    def __init__(self):
        self.writes = []
        self.events = []

    def writer(self, brokerage_id, phone, updates):
        self.writes.append((brokerage_id, phone, dict(updates)))

    def sink(self, event_type, **kw):
        self.events.append((event_type, kw))


def _ingest(payload, brokerage=BRK_A, store=None, rec=None):
    rec = rec or _Recorder()
    store = store or LeadDedupeStore()
    res = ingest_digital_lead(
        payload, brokerage=brokerage, dedupe_store=store,
        lead_writer=rec.writer, event_sink=rec.sink,
    )
    return res, rec, store


# 1. valid lead ingests
def test_valid_lead_ingests():
    res, rec, _ = _ingest({"source": "website_form", "phone": "212-555-1234", "name": "Marcus", "intent": "buying"})
    assert res["status"] == "ingested"
    assert res["lead_created"] is True
    assert res["brokerage_id"] == "brk-A"
    assert rec.writes and rec.writes[0][0] == "brk-A" and rec.writes[0][1] == "+12125551234"


# 2. empty / meaningless lead rejected (no usable phone)
def test_empty_lead_rejected():
    res, rec, _ = _ingest({"source": "website_form", "name": "No Phone"})
    assert res["status"] == "rejected"
    assert "missing_or_invalid_phone" in res["errors"]
    assert rec.writes == []


# 3. normalization works
def test_normalization():
    assert norm.normalize_phone("(212) 555-1234") == "+12125551234"
    assert norm.normalize_phone("+44 20 7946 0000") == "+442079460000"
    assert norm.normalize_email("  John@Example.COM ") == "john@example.com"
    assert norm.normalize_email("not-an-email") == ""
    assert norm.normalize_name("  marcus   lee ") == "marcus lee"


# 4. dedupe same tenant works (idempotent repeat)
def test_dedupe_same_tenant():
    store = LeadDedupeStore()
    rec = _Recorder()
    p = {"source": "zillow", "phone": "2125551234", "message": "interested in 123 Main"}
    r1, _, _ = _ingest(p, store=store, rec=rec)
    r2, _, _ = _ingest(p, store=store, rec=rec)
    assert r1["status"] == "ingested"
    assert r2["status"] == "duplicate"
    assert r2["dedupe_key"] == r1["dedupe_key"]
    assert len(rec.writes) == 1  # written once


# 5. dedupe does not cross tenants
def test_dedupe_does_not_cross_tenants():
    store = LeadDedupeStore()
    p = {"source": "zillow", "phone": "2125551234", "message": "interested"}
    r_a, _, _ = _ingest(p, brokerage=BRK_A, store=store)
    r_b, _, _ = _ingest(p, brokerage=BRK_B, store=store)
    assert r_a["status"] == "ingested"
    assert r_b["status"] == "ingested"  # different tenant → not a duplicate
    assert r_a["dedupe_key"] != r_b["dedupe_key"]


# 6. external_lead_id dedupe works
def test_external_lead_id_dedupe():
    store = LeadDedupeStore()
    p1 = {"source": "realtor_com", "phone": "2125551234", "external_lead_id": "RC-999"}
    p2 = {"source": "realtor_com", "phone": "3105550000", "external_lead_id": "RC-999"}  # diff contact, same ext id
    r1, _, _ = _ingest(p1, store=store)
    r2, _, _ = _ingest(p2, store=store)
    assert r1["status"] == "ingested"
    assert r2["status"] == "duplicate"


# 7. missing tenant fails closed
def test_missing_tenant_fails_closed():
    res, rec, _ = _ingest({"source": "manual", "phone": "2125551234"}, brokerage={"id": ""})
    assert res["status"] == "failed" and res["error"] == "tenant_unresolved"
    assert rec.writes == []
    # demo tenant also fails closed
    res2, _, _ = _ingest({"source": "manual", "phone": "2125551234"}, brokerage={"id": "demo"})
    assert res2["status"] == "failed"


def test_tenant_mismatch_rejected():
    res, rec, _ = _ingest({"source": "manual", "phone": "2125551234", "brokerage_id": "brk-EVIL"})
    assert res["status"] == "failed" and res["error"] == "tenant_mismatch"
    assert rec.writes == []


# 8. event emitted if event store available
def test_event_emitted():
    res, rec, _ = _ingest({"source": "facebook", "phone": "2125551234", "email": "a@b.com"})
    assert res["status"] == "ingested"
    assert rec.events and rec.events[0][0] == "lead.ingested"
    ev_kw = rec.events[0][1]
    assert ev_kw["brokerage_id"] == "brk-A"
    assert ev_kw["event_source"] == "digital_ingestion"
    # no raw PII in event payload
    payload = ev_kw["payload"]
    assert "phone" not in payload and "email" not in payload
    assert payload["has_email"] is True


# 9. no direct outbound call (import scan of ingestion modules)
def test_ingestion_has_no_outbound_or_engine_imports():
    for mod in (svc, norm, lead_contracts_mod()):
        tree = ast.parse(inspect.getsource(mod))
        imported = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported += [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom):
                imported.append(node.module or "")
        joined = " ".join(imported)
        for bad in ("twilio", "calcom", "state_machine", "websocket_handler", "outbound"):
            assert bad not in joined, f"{mod.__name__} must not import {bad}"


def lead_contracts_mod():
    return lc


# 10. raw metadata preserved safely (unknown keys + explicit metadata)
def test_raw_metadata_preserved():
    env = norm.normalize_digital_lead({
        "source": "website_form", "phone": "2125551234",
        "metadata": {"campaign": "spring"}, "utm_term": "condo",
    })
    assert env["status"] == "ok"
    lead = env["lead"]
    assert lead.metadata["campaign"] == "spring"
    assert lead.metadata["utm_term"] == "condo"  # unknown key preserved


# 11. source labels handled
@pytest.mark.parametrize("source", list(lc.ALL_SOURCES))
def test_known_source_labels_handled(source):
    res, _, _ = _ingest({"source": source, "phone": "2125551234"})
    assert res["status"] == "ingested" and res["source"] == source


def test_unknown_source_mapped_to_manual_with_warning():
    env = norm.normalize_digital_lead({"source": "tiktok", "phone": "2125551234"})
    assert env["lead"].source == lc.SOURCE_MANUAL
    assert "unknown_source_mapped_to_manual" in env["lead"].warnings
    # raw label is preserved
    assert env["lead"].raw_source_label == "tiktok"


def test_process_local_warning_surfaced():
    res, _, _ = _ingest({"source": "manual", "phone": "2125551234"})
    assert "lead_dedupe_store_is_process_local" in res["warnings"]


# narrow route-level smoke test (auth + source transparency)
def test_route_ingests_with_valid_key(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.lead_ingestion as route_mod
    from app.main import app

    monkeypatch.setattr(route_mod, "get_brokerage_by_api_key", lambda k: {"id": "brk-A"})
    captured = {}

    def _fake_ingest(payload, brokerage):
        captured["c"] = (payload, brokerage)
        return {
            "status": "ingested",
            "source_mode": "digital_ingestion",
            "brokerage_id": brokerage["id"],
            "source": payload.get("source"),
        }

    monkeypatch.setattr(route_mod, "ingest_digital_lead", _fake_ingest)
    with TestClient(app) as client:
        resp = client.post("/ingest/lead", headers={"X-API-Key": "pas_x"},
                           json={"source": "website_form", "phone": "2125551234"})
    assert resp.status_code == 201
    assert resp.json()["source_mode"] == "digital_ingestion"
    assert captured["c"][1]["id"] == "brk-A"


def test_route_rejects_unknown_key(monkeypatch):
    from fastapi.testclient import TestClient
    import app.routes.lead_ingestion as route_mod
    from app.main import app

    monkeypatch.setattr(route_mod, "get_brokerage_by_api_key", lambda k: None)
    with TestClient(app) as client:
        resp = client.post("/ingest/lead", headers={"X-API-Key": "bad"},
                           json={"source": "manual", "phone": "2125551234"})
    assert resp.status_code == 401
