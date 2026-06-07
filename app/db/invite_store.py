"""
Invite / Onboarding Key Store

Flow:
  1. Admin creates brokerage via POST /admin/brokerages
  2. Admin generates an invite key via POST /admin/brokerages/{id}/invite
  3. Brokerage receives the invite key (email / copy-paste)
  4. Brokerage calls POST /onboarding/claim with the key
  5. System returns the brokerage's api_key and marks key as used
  6. Brokerage uses api_key for all future /portal/* calls

Key rules:
  - Single-use (used=true after claim)
  - Expiry (configurable, default 7 days)
  - Revocable (admin can invalidate before use)
  - Scoped to one brokerage
"""

import logging
import secrets
from datetime import datetime, timedelta, timezone
from typing import Optional

from app.config import get_settings
from app.db.supabase_client import get_supabase

logger = logging.getLogger("pas.invites")

_KEY_TTL_DAYS = 7


def generate_invite_key(brokerage_id: str, created_by: str = "admin", ttl_days: int = _KEY_TTL_DAYS) -> dict:
    """Create a new invite key for a brokerage. Revokes any previous unused key."""
    db = get_supabase()
    now = datetime.now(timezone.utc)
    expires = (now + timedelta(days=ttl_days)).isoformat()
    key = "orvn_" + secrets.token_urlsafe(32)

    # Revoke any previous active keys for this brokerage
    try:
        db.table("onboarding_keys").update({"revoked": True}).eq(
            "brokerage_id", brokerage_id
        ).eq("used", False).eq("revoked", False).execute()
    except Exception as e:
        logger.warning(f"Could not revoke old keys for {brokerage_id}: {e}")

    payload = {
        "key": key,
        "brokerage_id": brokerage_id,
        "created_by": created_by,
        "expires_at": expires,
        "used": False,
        "revoked": False,
        "created_at": now.isoformat(),
    }

    # PAS211F: store the hash (key_hash/key_lookup columns added in migrate_v7)
    # and clear the plaintext key once hashing is enabled. The raw key is still
    # returned (once) to the caller.
    if get_settings().SECRETS_HASHING_ENABLED:
        from app.services.security.secret_hash import hash_invite_key
        key_hash = hash_invite_key(key)
        payload["key_hash"] = key_hash
        payload["key_lookup"] = key_hash
        payload["key"] = ""

    db.table("onboarding_keys").insert(payload).execute()
    logger.info(f"Invite key generated | brokerage={brokerage_id} | expires={expires}")
    return {
        "key": key,
        "brokerage_id": brokerage_id,
        "expires_at": expires,
        "ttl_days": ttl_days,
    }


def get_invite_status(brokerage_id: str) -> Optional[dict]:
    """Return the current invite key record for a brokerage (most recent)."""
    try:
        db = get_supabase()
        result = (
            db.table("onboarding_keys")
            .select("id, brokerage_id, expires_at, used, used_at, used_by_email, revoked, created_at")
            .eq("brokerage_id", brokerage_id)
            .order("created_at", desc=True)
            .limit(1)
            .execute()
        )
        return result.data[0] if result.data else None
    except Exception as e:
        logger.error(f"get_invite_status failed for {brokerage_id}: {e}")
        return None


def revoke_invite_key(brokerage_id: str) -> bool:
    """Revoke all unused keys for a brokerage."""
    try:
        db = get_supabase()
        db.table("onboarding_keys").update({"revoked": True}).eq(
            "brokerage_id", brokerage_id
        ).eq("used", False).execute()
        logger.info(f"Invite key(s) revoked | brokerage={brokerage_id}")
        return True
    except Exception as e:
        logger.error(f"revoke_invite_key failed for {brokerage_id}: {e}")
        return False


def claim_invite_key(key: str, used_by_email: str = "") -> Optional[dict]:
    """
    Validate and consume an invite key.
    Returns the brokerage record (including api_key) if valid.
    Returns None if the key is invalid, expired, used, or revoked.
    """
    try:
        db = get_supabase()

        # PAS211F: hashed lookup first (keys issued after activation store only
        # the hash), with a legacy plaintext fallback for keys issued before.
        record = None
        if get_settings().SECRETS_HASHING_ENABLED:
            try:
                from app.services.security.secret_hash import hash_invite_key
                hk = hash_invite_key(key)
                hres = db.table("onboarding_keys").select("*").eq("key_hash", hk).limit(1).execute()
                if hres.data:
                    record = hres.data[0]
            except Exception as e:
                logger.warning(f"Hashed invite lookup unavailable; trying legacy: {e}")
        if record is None:
            result = db.table("onboarding_keys").select("*").eq("key", key).limit(1).execute()
            record = result.data[0] if result.data else None

        if not record:
            logger.warning(f"Invite key not found: {key[:12]}...")
            return None

        now = datetime.now(timezone.utc)

        if record.get("used"):
            logger.warning(f"Invite key already used: {key[:12]}...")
            return None
        if record.get("revoked"):
            logger.warning(f"Invite key revoked: {key[:12]}...")
            return None
        if record.get("expires_at") and now.isoformat() > record["expires_at"]:
            logger.warning(f"Invite key expired: {key[:12]}...")
            return None

        # Mark key as used — target by primary key id (the plaintext `key` may be
        # cleared once hashing is enabled).
        db.table("onboarding_keys").update({
            "used": True,
            "used_at": now.isoformat(),
            "used_by_email": used_by_email,
        }).eq("id", record["id"]).execute()

        # Return the brokerage (including api_key)
        brokerage_result = db.table("brokerages").select("*").eq(
            "id", record["brokerage_id"]
        ).limit(1).execute()

        if not brokerage_result.data:
            return None

        brokerage = brokerage_result.data[0]
        logger.info(f"Invite key claimed | brokerage={record['brokerage_id']} | email={used_by_email}")
        return brokerage

    except Exception as e:
        logger.error(f"claim_invite_key failed: {e}")
        return None
