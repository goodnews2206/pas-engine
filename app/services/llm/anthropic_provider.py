"""Anthropic (Claude) implementation of LLMProvider."""

import logging

import anthropic

from app.config import get_settings
from app.services.llm.base import LLMProvider

logger = logging.getLogger("pas.llm.anthropic")

DEFAULT_MODEL = "claude-sonnet-4-20250514"


class AnthropicProvider(LLMProvider):
    name = "anthropic"

    def __init__(self, model: str | None = None):
        self._model = model or DEFAULT_MODEL
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

    async def chat(
        self,
        system: str,
        user: str,
        max_tokens: int,
        temperature: float,
    ) -> str:
        client = self._get_client()
        response = await client.messages.create(
            model=self._model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return response.content[0].text.strip()
