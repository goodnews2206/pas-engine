"""
Simple in-process rate limiter.
Uses a sliding window per key (IP or brokerage_id).
No external dependencies — pure stdlib.
"""
import time
from collections import defaultdict
from fastapi import HTTPException, Request

# { key -> [timestamp, timestamp, ...] }
_windows: dict[str, list[float]] = defaultdict(list)


def rate_limit(key: str, max_requests: int, window_seconds: int = 60):
    """
    Raises HTTP 429 if `key` has made more than `max_requests`
    in the last `window_seconds`. Call this at the top of any endpoint.
    """
    now = time.monotonic()
    bucket = _windows[key]
    # Evict timestamps outside the sliding window
    _windows[key] = [t for t in bucket if now - t < window_seconds]
    if len(_windows[key]) >= max_requests:
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded — max {max_requests} requests per {window_seconds}s.",
        )
    _windows[key].append(now)


def client_ip(request: Request) -> str:
    """Extract real client IP, respecting reverse-proxy forwarding."""
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"
