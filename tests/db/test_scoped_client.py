"""
Tests for the PAS211G.4 scoped Supabase client factory
(app/db/supabase_client.get_scoped_supabase) and the inert-seam guarantees.

Pure unit tests — no network, no live Supabase, no .env, no real credentials.
The supabase client constructs offline; we only assert it is built with the
ANON key and carries the Bearer access token (so RLS would evaluate auth.jwt()).
"""

import inspect
import os
import sys
import types

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)

import pytest

import app.db.supabase_client as sc

# JWT-shaped, test-local fakes (supabase-py validates the key matches a JWT
# regex; anon keys / access tokens are JWTs). These are NOT real credentials.
FAKE_ANON = "eyJhbGc.eyJyb2xlIjoiYW5vbiJ9.anon-sig"
FAKE_SERVICE = "eyJhbGc.eyJyb2xlIjoic2VydmljZSJ9.service-sig"
FAKE_TOKEN = "eyJhbGc.eyJzdWIiOiJ1LTEifQ.user-sig"
URL = "https://example.supabase.co"


def _patch_settings(monkeypatch, *, url=URL, anon=FAKE_ANON, service=FAKE_SERVICE):
    fake = types.SimpleNamespace(
        SUPABASE_URL=url,
        SUPABASE_ANON_KEY=anon,
        SUPABASE_SERVICE_KEY=service,
    )
    monkeypatch.setattr(sc, "get_settings", lambda: fake)
    return fake


# ───────────── fail-closed paths ─────────────

def test_empty_token_fails_closed(monkeypatch):
    _patch_settings(monkeypatch)
    with pytest.raises(RuntimeError):
        sc.get_scoped_supabase("")
    with pytest.raises(RuntimeError):
        sc.get_scoped_supabase(None)  # type: ignore[arg-type]


def test_missing_anon_key_fails_closed(monkeypatch):
    _patch_settings(monkeypatch, anon="")
    with pytest.raises(RuntimeError):
        sc.get_scoped_supabase(FAKE_TOKEN)


def test_missing_url_fails_closed(monkeypatch):
    _patch_settings(monkeypatch, url="")
    with pytest.raises(RuntimeError):
        sc.get_scoped_supabase(FAKE_TOKEN)


# ───────────── happy path ─────────────

def test_factory_builds_client_with_anon_key_and_bearer(monkeypatch):
    _patch_settings(monkeypatch)
    client = sc.get_scoped_supabase(FAKE_TOKEN)
    assert client is not None
    # Built with the ANON key, never the service-role key.
    assert client.supabase_key == FAKE_ANON
    assert client.supabase_key != FAKE_SERVICE
    # Bearer token attached so PostgREST runs as the authenticated user (RLS).
    assert client.postgrest.session.headers.get("Authorization") == f"Bearer {FAKE_TOKEN}"


def test_factory_never_returns_service_client(monkeypatch):
    # Even if the global service client is initialised, the factory must build a
    # fresh anon-keyed client — never hand back the service-role singleton.
    _patch_settings(monkeypatch)
    monkeypatch.setattr(sc, "_supabase", object())  # stand-in service singleton
    client = sc.get_scoped_supabase(FAKE_TOKEN)
    assert client is not sc._supabase
    assert client.supabase_key == FAKE_ANON


# ───────────── source-level guards ─────────────

def test_scoped_factory_does_not_reference_service_key():
    src = inspect.getsource(sc.get_scoped_supabase)
    assert "SUPABASE_SERVICE_KEY" not in src
    assert "SUPABASE_ANON_KEY" in src


def test_service_role_path_still_exists():
    assert hasattr(sc, "get_supabase") and callable(sc.get_supabase)
    assert hasattr(sc, "init_supabase") and callable(sc.init_supabase)


# ───────────── inert-seam guards: nothing uses the factory yet ─────────────

def _py_files(root):
    for dirpath, _dirs, files in os.walk(root):
        if "__pycache__" in dirpath:
            continue
        for f in files:
            if f.endswith(".py"):
                yield os.path.join(dirpath, f)


def _repo_path(*parts):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", *parts))


def test_no_route_uses_scoped_factory():
    for path in _py_files(_repo_path("app", "routes")):
        with open(path, encoding="utf-8") as fh:
            assert "get_scoped_supabase" not in fh.read(), f"{path} references the scoped factory"


def test_no_store_or_service_uses_scoped_factory():
    # The only file allowed to define/mention it is supabase_client.py itself.
    for sub in ("services",):
        for path in _py_files(_repo_path("app", sub)):
            with open(path, encoding="utf-8") as fh:
                assert "get_scoped_supabase" not in fh.read(), f"{path} references the scoped factory"
    for path in _py_files(_repo_path("app", "db")):
        if os.path.basename(path) == "supabase_client.py":
            continue
        with open(path, encoding="utf-8") as fh:
            assert "get_scoped_supabase" not in fh.read(), f"{path} references the scoped factory"


def test_main_does_not_use_scoped_factory():
    with open(_repo_path("app", "main.py"), encoding="utf-8") as fh:
        assert "get_scoped_supabase" not in fh.read()
