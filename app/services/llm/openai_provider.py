"""
OpenAI implementation of LLMProvider.

The openai SDK is imported lazily so that PAS keeps booting on environments
where the package is not yet installed (e.g. existing Railway deploy that
hasn't picked up the new requirement). is_available reports False in that
case and the caller falls back to the canned response path.
"""

import logging

from app.config import get_settings
from app.services.llm.base import LLMProvider

logger = logging.getLogger("pas.llm.openai")

DEFAULT_MODEL = "gpt-4.1-mini"


class OpenAIProvider(LLMProvider):
    name = "openai"

    def __init__(self, model: str | None = None):
        self._model = model or get_settings().OPENAI_MODEL or DEFAULT_MODEL
        self._client = None

    @property
    def is_available(self) -> bool:
        if not get_settings().OPENAI_API_KEY:
            return False
        try:
            import openai  # noqa: F401
        except ImportError:
            logger.warning("openai package not installed — OpenAI provider unavailable")
            return False
        return True

    def _get_client(self):
        if self._client is None:
            try:
                from openai import AsyncOpenAI
            except ImportError as e:
                raise RuntimeError(
                    "openai package not installed — add `openai` to requirements.txt"
                ) from e
            key = get_settings().OPENAI_API_KEY
            if not key:
                raise RuntimeError("OPENAI_API_KEY not configured")
            self._client = AsyncOpenAI(api_key=key)
        return self._client

    async def chat(
        self,
        system: str,
        user: str,
        max_tokens: int,
        temperature: float,
    ) -> str:
        client = self._get_client()
        response = await client.chat.completions.create(
            model=self._model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        return (response.choices[0].message.content or "").strip()
