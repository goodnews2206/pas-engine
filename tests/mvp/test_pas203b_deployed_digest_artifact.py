"""
PAS203-B — Deployed evidence digest artifact tests.

Coverage:

  * At least one PAS201 digest artefact is committed under
    reports/simulations/.
  * That artefact parses, carries phase=PAS201,
    allowed_environment=SIMULATION_ONLY,
    live_behavior_changed=False.
  * That artefact carries no PII / production brokerage UUIDs /
    secret-shaped tokens.
  * On a clean checkout the PAS203 Slack route returns the real
    PAS202 Slack-safe digest rendering — not the missing-digest
    fallback — when handed the committed reports/simulations/
    directory.
  * The fallback still fires when handed an empty directory.
  * The readiness gate runs clean (verdict=READY).
"""

from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys
import tempfile

import pytest


_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


from app.services.slack.simulation_digest_intent import (  # noqa: E402
    DIGEST_FILENAME_PREFIX,
    DIGEST_FILENAME_SUFFIX,
    MISSING_DIGEST_FALLBACK_MESSAGE,
    find_latest_digest_path,
    load_digest,
    try_route_simulation_digest,
)


REPORTS_DIR = _REPO_ROOT / "reports" / "simulations"


# Reuse the loader's strict filename regex via a local copy so the
# test does not depend on a private import. Must match the
# pattern declared in simulation_digest_intent.py.
_DIGEST_FILENAME_RE = re.compile(
    r"^pas201_simulation_evidence_digest_"
    r"[0-9TZ]{8,32}_"
    r"pas201-dgst-[0-9a-f]{8,32}"
    r"\.json$"
)


def _committed_digest_files():
    if not REPORTS_DIR.is_dir():
        return []
    return [
        p for p in REPORTS_DIR.iterdir()
        if p.is_file() and _DIGEST_FILENAME_RE.match(p.name)
    ]


# ──────────────────────────────────────────────────────────────────
# Artefact presence + safety
# ──────────────────────────────────────────────────────────────────

def test_reports_simulations_directory_exists_in_repo():
    assert REPORTS_DIR.is_dir(), (
        f"reports/simulations/ must exist in the repo so the deployed "
        f"PAS203 Slack surface has a directory to read"
    )


def test_at_least_one_pas201_digest_artifact_is_committed():
    files = _committed_digest_files()
    assert files, (
        "at least one PAS201 digest artefact "
        "(pas201_simulation_evidence_digest_<ts>_pas201-dgst-<id>.json) "
        "must be committed under reports/simulations/"
    )


def test_committed_digest_parses_and_carries_pas201_contract():
    files = _committed_digest_files()
    assert files
    digest = json.loads(files[0].read_text(encoding="utf-8"))
    assert digest["phase"] == "PAS201"
    assert digest["allowed_environment"] == "SIMULATION_ONLY"
    assert digest["live_behavior_changed"] is False


_PII_PATTERNS = (
    re.compile(r"\b\d{3}[\s.\-]\d{3}[\s.\-]\d{4}\b"),
    re.compile(r"\(\d{3}\)\s*\d{3}[\s.\-]?\d{4}"),
    re.compile(r"\+\d[\d\s.\-]{6,14}\d"),
    re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}"),
    re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
)

_PROD_ID_PATTERNS = (
    re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"),
    re.compile(r"brokerage_id\s*=\s*[\"']?[0-9a-fA-F\-]{8,}[\"']?"),
)

_SECRET_PATTERNS = (
    re.compile(r"AKIA[0-9A-Z]{12,}"),
    re.compile(r"xox[bp]-[0-9A-Za-z\-]{10,}"),
    re.compile(r"sk_(live|test)_[A-Za-z0-9]{16,}"),
    re.compile(r"\bAC[0-9a-fA-F]{32}\b"),
    re.compile(r"\bSK[0-9a-fA-F]{32}\b"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
)


def test_committed_digest_carries_no_pii():
    files = _committed_digest_files()
    assert files
    text = files[0].read_text(encoding="utf-8")
    for pat in _PII_PATTERNS:
        assert not pat.search(text), (
            f"committed digest carries PII-shaped token "
            f"matching {pat.pattern!r}"
        )


def test_committed_digest_carries_no_production_brokerage_ids():
    files = _committed_digest_files()
    assert files
    text = files[0].read_text(encoding="utf-8")
    for pat in _PROD_ID_PATTERNS:
        assert not pat.search(text), (
            f"committed digest carries production brokerage UUID "
            f"matching {pat.pattern!r}"
        )


def test_committed_digest_carries_no_secret_shapes():
    files = _committed_digest_files()
    assert files
    text = files[0].read_text(encoding="utf-8")
    for pat in _SECRET_PATTERNS:
        assert not pat.search(text), (
            f"committed digest carries secret-shaped token "
            f"matching {pat.pattern!r}"
        )


def test_committed_digest_filename_matches_loader_regex():
    files = _committed_digest_files()
    assert files
    # Filename shape is what the PAS203 loader scans for; this
    # assertion guards against accidentally renaming the file in a
    # way that hides it from production.
    for fp in files:
        assert fp.name.startswith(DIGEST_FILENAME_PREFIX)
        assert fp.name.endswith(DIGEST_FILENAME_SUFFIX)


# ──────────────────────────────────────────────────────────────────
# Loader integration
# ──────────────────────────────────────────────────────────────────

def test_pas203_loader_finds_committed_digest():
    latest = find_latest_digest_path(REPORTS_DIR)
    assert latest is not None
    assert _DIGEST_FILENAME_RE.match(latest.name)


def test_pas203_loader_accepts_committed_digest():
    latest = find_latest_digest_path(REPORTS_DIR)
    assert latest is not None
    digest = load_digest(latest)
    assert digest["phase"] == "PAS201"
    assert digest["allowed_environment"] == "SIMULATION_ONLY"
    assert digest["live_behavior_changed"] is False


# ──────────────────────────────────────────────────────────────────
# Slack route — real digest vs. fallback
# ──────────────────────────────────────────────────────────────────

def test_slack_route_returns_real_digest_against_committed_reports_dir():
    out = try_route_simulation_digest("simulation digest", REPORTS_DIR)
    assert out is not None
    # The committed digest has digest_id pas201-dgst-d438476edaca2e11;
    # PAS202's Slack formatter embeds it as a literal in the output.
    # We assert the marker rather than the specific id so the test
    # remains stable if a future bootstrap digest replaces this one.
    assert "*PAS201 digest*" in out
    assert "pas201-dgst-" in out
    assert "SIMULATION_ONLY" in out
    assert out != MISSING_DIGEST_FALLBACK_MESSAGE


def test_slack_route_returns_fallback_when_reports_dir_empty():
    with tempfile.TemporaryDirectory() as tmp:
        out = try_route_simulation_digest(
            "simulation digest", pathlib.Path(tmp),
        )
        assert out == MISSING_DIGEST_FALLBACK_MESSAGE


def test_slack_route_returns_fallback_when_reports_dir_missing():
    with tempfile.TemporaryDirectory() as tmp:
        out = try_route_simulation_digest(
            "simulation digest", pathlib.Path(tmp) / "nope",
        )
        assert out == MISSING_DIGEST_FALLBACK_MESSAGE


def test_slack_route_with_non_matching_text_returns_none():
    # Sanity check — non-digest text still falls through to the
    # rest of the dispatcher (PAS191 / LLM).
    out = try_route_simulation_digest("stats", REPORTS_DIR)
    assert out is None


# ──────────────────────────────────────────────────────────────────
# Readiness gate
# ──────────────────────────────────────────────────────────────────

_GATE = _REPO_ROOT / "scripts" / "pas203b_deployed_digest_readiness_check.py"


def test_readiness_gate_runs_clean_summary_only():
    proc = subprocess.run(
        [sys.executable, str(_GATE), "--summary-only"],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "verdict=READY" in proc.stdout


def test_readiness_gate_json_envelope_valid():
    proc = subprocess.run(
        [sys.executable, str(_GATE), "--summary-only", "--json"],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert proc.returncode == 0
    payload_str = proc.stdout[proc.stdout.find("{"):]
    payload = json.loads(payload_str)
    assert payload["phase"] == "PAS203-B"
    assert payload["verdict"] == "READY"
    assert payload["ready"] is True
    assert payload["fail_count"] == 0
    assert payload["check_count"] > 0
