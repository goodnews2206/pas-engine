"""Anthropic (Claude) implementation of LLMProvider."""

import logging

import anthropic

from app.config import get_settings
from app.services.llm.base import LLMProvider

logger = logging.getLogger("pas.llm.anthropic")

DEFAULT_MODEL = "claude-sonnet-4-20250514"

# Maps a PAS purpose label → the Claude tier used historically for that task.
# Keeps the cost/quality profile of the original direct-Anthropic call sites
# (Haiku for cheap classification/summary, Sonnet for objection + training).
_PURPOSE_MODEL_MAP = {
    "objection": "claude-sonnet-4-20250514",
    "summary": "claude-haiku-4-5-20251001",
    "slack_intent": "claude-haiku-4-5-20251001",
    "training": "claude-sonnet-4-20250514",
}


class AnthropicProvider(LLMProvider):
    name = "anthropic"

    def __init__(self, model: str | None = None):
        # Explicit model override wins over purpose-based selection.
        self._model_override = model
        self._client: anthropic.AsyncAnthropic | None = None

    @property
    def is_available(self) -> bool:
        return bool(get_settings().ANTHROPIC_API_KEY)

    def _get_client(self) -> anthropic.AsyncAnthropic:
        if self._client is None:
            key = get_settings().ANTHROPIC_API_KEY
            if not key:
                raise RuntimeError("ANTHROPIC_API_KEY not configured")
            self._client = anthropic.AsyncAnthropic(api_key=key)
        return self._client

    def _resolve_model(self, purpose: str | None) -> str:
        if self._model_override:
            return self._model_override
        if purpose and purpose in _PURPOSE_MODEL_MAP:
            return _PURPOSE_MODEL_MAP[purpose]
        return DEFAULT_MODEL

    async def chat(
        self,
        system: str,
        user: str,
        max_tokens: int,
        temperature: float,
        purpose: str | None = None,
    ) -> str:
        client = self._get_client()
        response = await client.messages.create(
            model=self._resolve_model(purpose),
            max_tokens=max_tokens,
            temperature=temperature,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return response.content[0].text.strip()
