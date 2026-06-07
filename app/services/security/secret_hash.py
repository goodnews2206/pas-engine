"""PAS211F — deterministic hashing for high-entropy credentials.

Brokerage API keys (`pas_` + ``secrets.token_urlsafe(32)``) and onboarding
invite keys (`orvn_` + …) are random ~256-bit tokens looked up by the value the
caller presents. The stored form must therefore be a deterministic,
collision-resistant hash so we can find the row by hashing the presented value
— a peppered SHA-256.

Why not bcrypt/argon2: those deliberately-slow KDFs exist for LOW-entropy
human passwords. These tokens are already high-entropy, so a fast keyed hash is
both sufficient and necessary (an exact-match indexed lookup needs determinism).
This module uses only the standard library — no new dependency.
"""
from __future__ import annotations

import hashlib
import hmac
from typing import Optional

from app.config import get_settings

_PREFIX = "sha256$"


def _pepper(pepper: Optional[str]) -> str:
    if pepper is not None:
        return pepper
    return get_settings().SECRET_HASH_PEPPER or ""


def hash_secret(raw: str, *, pepper: Optional[str] = None) -> str:
    """Deterministic peppered SHA-256 of a high-entropy secret.

    Returns ``"sha256$<hexdigest>"``; empty input → ``""``. The pepper is an
    optional deployment-wide secret (``SECRET_HASH_PEPPER``) so a stolen DB alone
    cannot be brute-forced/rainbow-tabled without it.
    """
    if not raw:
        return ""
    digest = hashlib.sha256((_pepper(pepper) + raw).encode("utf-8")).hexdigest()
    return _PREFIX + digest


def verify_secret(raw: str, stored_hash: str, *, pepper: Optional[str] = None) -> bool:
    """Constant-time check that ``raw`` hashes to ``stored_hash``."""
    if not raw or not stored_hash:
        return False
    return hmac.compare_digest(hash_secret(raw, pepper=pepper), stored_hash)


# Named aliases for call-site clarity (identical algorithm).
hash_api_key = hash_secret
hash_invite_key = hash_secret


__all__ = ("hash_secret", "verify_secret", "hash_api_key", "hash_invite_key")
