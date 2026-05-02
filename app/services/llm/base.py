"""
LLM provider interface.

PAS treats every LLM (Claude, OpenAI, anything else) as a replaceable provider
behind this single interface. Callers MUST NOT import a vendor SDK directly —
go through `app.services.llm.factory.get_provider()` instead.
"""

from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """Minimal chat interface every PAS LLM provider must implement."""

    name: str = "base"

    @property
    @abstractmethod
    def is_available(self) -> bool:
        """True if this provider has the credentials it needs to make a call."""

    @abstractmethod
    async def chat(
        self,
        system: str,
        user: str,
        max_tokens: int,
        temperature: float,
        purpose: str | None = None,
    ) -> str:
        """
        Return a single completion string. Raise on transport / API errors.

        `purpose` is an optional hint the provider may use to pick a tier-
        appropriate model (e.g. cheap/fast for "summary", strong for
        "training"). Providers may ignore it. Recognised values used by
        PAS today: "objection", "summary", "training", "slack_intent".
        """
