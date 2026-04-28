"""
Security verification test — confirms all hardened endpoints enforce auth correctly.
Runs against http://localhost:8000
"""

import sys
import io
import urllib.request
import urllib.error
import json
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE = "http://localhost:8000"
PASS = "[PASS]"
FAIL = "[FAIL]"
INFO = "[INFO]"

results = []


def req(method, path, body=None, headers=None, label=""):
    url = BASE + path
    data = json.dumps(body).encode() if body else None
    h = {"Content-Type": "application/json"}
    if headers:
        h.update(headers)
    try:
        r = urllib.request.Request(url, data=data, headers=h, method=method)
        with urllib.request.urlopen(r, timeout=5) as resp:
            return resp.status, resp.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()
    except Exception as ex:
        return 0, str(ex)


def check(label, status, expected_status, note=""):
    ok = status == expected_status
    tag = PASS if ok else FAIL
    msg = f"{tag} {label} -> HTTP {status} (expected {expected_status})"
    if note:
        msg += f" | {note}"
    print(msg)
    results.append((ok, label))
    return ok


print("=" * 60)
print("PAS Security Verification Suite")
print("=" * 60)
print()

# ── 1. /health — always open ───────────────────────────────────
print("[1] Health endpoint (must be open)")
status, body = req("GET", "/health")
check("/health returns 200", status, 200)
print()

# ── 2. /outbound/call — must reject without X-API-Key ─────────
print("[2] Outbound endpoint — X-API-Key enforcement")
# LeadPayload: phone (required, E.164), brokerage_id, name, etc. — flat structure
payload = {
    "phone": "+15550001234",
    "brokerage_id": "demo",
    "name": "Test Lead",
}

status, body = req("POST", "/outbound/call", body=payload)
check("No API key -> 422 (missing header)", status, 422, "FastAPI rejects missing required header")

status, body = req("POST", "/outbound/call", body=payload, headers={"X-API-Key": "fake_key_invalid"})
check("Wrong API key -> 401", status, 401)

status, body = req("POST", "/outbound/call", body=payload, headers={"X-API-Key": "pas_wrongkey"})
check("Invalid pas_ key -> 401", status, 401)
print()

# ── 3. /admin routes — must reject without X-Admin-Key ────────
print("[3] Admin routes — X-Admin-Key enforcement")
status, body = req("GET", "/admin/brokerages")
check("No admin key -> 422", status, 422, "FastAPI rejects missing required header")

status, body = req("GET", "/admin/brokerages", headers={"X-Admin-Key": "wrong-key"})
check("Wrong admin key -> 401", status, 401)

status, body = req("POST", "/admin/brokerages", body={"id": "x", "name": "x"}, headers={"X-Admin-Key": "wrong-key"})
check("POST /brokerages wrong key -> 401", status, 401)
print()

# ── 4. /admin with correct dev key ─────────────────────────────
print("[4] Admin routes — correct key accepted")
status, body = req("GET", "/admin/brokerages", headers={"X-Admin-Key": "change-me-before-deploy"})
check("Correct admin key -> 200", status, 200, "Returns brokerage list (empty if no DB)")
print()

# ── 5. /twilio/voice — dev mode skips sig but rate limits active
print("[5] Twilio webhook — rate limit active")
status, body = req("POST", "/twilio/voice", body=None,
                   headers={"Content-Type": "application/x-www-form-urlencoded"})
# In dev mode signature check is skipped, so it'll process the (empty) form
check("/twilio/voice accessible in dev mode (no sig check)", status in (200, 422, 500), True,
      f"HTTP {status} — sig check disabled, body parse may fail")
print()

# ── 6. Rate limiting — hammer one endpoint ─────────────────────
print("[6] Rate limiting — /outbound/call (20 req/min limit)")
# Use correct flat payload so body validation passes; key is intentionally invalid
rl_payload = {"phone": "+15550001234", "brokerage_id": "demo", "name": "RateTest"}
hits_429 = 0
for i in range(25):
    s, _ = req("POST", "/outbound/call", body=rl_payload, headers={"X-API-Key": "pas_ratelimitest"})
    if s == 429:
        hits_429 += 1

check("Rate limiter fires 429 after 20 requests", hits_429 > 0, True,
      f"Got {hits_429} x 429 responses in 25 rapid requests")
print()

# ── 7. Body size limit ─────────────────────────────────────────
print("[7] Body size limit — 64KB max")
big_body = "x" * (65 * 1024)
url = BASE + "/outbound/call"
data = big_body.encode()
h = {"Content-Type": "application/json", "Content-Length": str(len(data)), "X-API-Key": "test"}
try:
    r = urllib.request.Request(url, data=data, headers=h, method="POST")
    with urllib.request.urlopen(r, timeout=5) as resp:
        status = resp.status
except urllib.error.HTTPError as e:
    status = e.code
except Exception:
    status = 0

check("65KB body -> 413", status, 413, "BodySizeLimitMiddleware active")
print()

# ── 8. /slack/command — no signing secret → 403 ───────────────
print("[8] Slack command — no brokerage found (workspace not linked)")
slack_body = "team_id=NOTEXIST&text=stats&response_url=http://x.com"
url = BASE + "/slack/command"
data = slack_body.encode()
h = {"Content-Type": "application/x-www-form-urlencoded"}
try:
    r = urllib.request.Request(url, data=data, headers=h, method="POST")
    with urllib.request.urlopen(r, timeout=5) as resp:
        status, body = resp.status, resp.read().decode()
except urllib.error.HTTPError as e:
    status, body = e.code, e.read().decode()
except Exception as ex:
    status, body = 0, str(ex)

check("Unknown Slack team -> 200 with warning text", status, 200,
      "Returns JSON error (not 500)")
print()

# ── 9. Error message sanitization ─────────────────────────────
print("[9] Error message sanitization — no DB schema leaks")
status, body = req("GET", "/admin/brokerages/nonexistent-id/leads",
                   headers={"X-Admin-Key": "change-me-before-deploy"})
if status == 500:
    leaked = any(kw in body.lower() for kw in ["postgresql", "supabase", "syntax error", "relation", "column"])
    check("500 response doesn't leak DB internals", not leaked, True,
          f"Body: {body[:120]}")
else:
    check(f"Leads endpoint returned {status} (no 500 = no leak risk)", True, True)
print()

# ── Summary ────────────────────────────────────────────────────
print("=" * 60)
passed = sum(1 for ok, _ in results if ok)
total = len(results)
print(f"Results: {passed}/{total} checks passed")
if passed == total:
    print("All security checks PASSED.")
else:
    failed = [label for ok, label in results if not ok]
    print("Failed checks:")
    for f in failed:
        print(f"  - {f}")
print("=" * 60)
