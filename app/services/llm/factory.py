"""
Provider factory.

Picks an LLM provider based on the LLM_PROVIDER env setting and falls back
to whichever provider has credentials. Returns None when no provider is
usable — callers must treat None as "use canned fallback response".
"""

import logging

from app.config import get_settings
from app.services.llm.anthropic_provider import AnthropicProvider
from app.services.llm.base import LLMProvider
from app.services.llm.openai_provider import OpenAIProvider

logger = logging.getLogger("pas.llm.factory")

_PROVIDER_CACHE: dict[str, LLMProvider] = {}


def _build(name: str) -> LLMProvider:
    if name in _PROVIDER_CACHE:
        return _PROVIDER_CACHE[name]
    if name == "openai":
        provider: LLMProvider = OpenAIProvider()
    else:
        provider = AnthropicProvider()
    _PROVIDER_CACHE[name] = provider
    return provider


def get_provider() -> LLMProvider | None:
    """
    Return the configured provider if available, otherwise the other one if
    it happens to have credentials, otherwise None.
    """
    preferred = (get_settings().LLM_PROVIDER or "anthropic").lower().strip()
    if preferred not in ("anthropic", "openai"):
        logger.warning(f"Unknown LLM_PROVIDER={preferred!r} — defaulting to anthropic")
        preferred = "anthropic"

    primary = _build(preferred)
    if primary.is_available:
        return primary

    secondary_name = "openai" if preferred == "anthropic" else "anthropic"
    secondary = _build(secondary_name)
    if secondary.is_available:
        logger.warning(
            f"Preferred provider {preferred!r} not configured — "
            f"falling back to {secondary_name!r}"
        )
        return secondary

    return None


def reset_cache() -> None:
    """Test/diagnostic hook — drop cached provider instances."""
    _PROVIDER_CACHE.clear()
