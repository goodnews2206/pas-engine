"""
Claude API Wrapper — Objection Handling ONLY

Constraints:
- max_tokens: 100
- temperature: 0.2
- 2 sentences max
- Always steers back toward booking
"""

import logging

import anthropic

from app.config import get_settings

logger = logging.getLogger("pas.llm")
settings = get_settings()

client = anthropic.AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)

OBJECTION_SYSTEM_PROMPT = """You are a professional real estate AI assistant handling a live phone call.
Your ONLY job is to respond to objections and steer the conversation back toward booking a consultation.

Rules:
- Respond in 1-2 sentences maximum
- Be warm, direct, and non-pushy
- Acknowledge the objection briefly, then pivot back
- Never argue or pressure
- End with a soft question that reopens the conversation

Output ONLY the response text. No preamble. No explanation."""


async def handle_objection(
    objection: str,
    current_state: str,
    lead_context: dict,
    system_prompt_override: str = None,
) -> str:
    """
    Takes the lead's objection and returns a short rebuttal.
    Falls back to a safe default if Claude fails.
    """
    context_str = ""
    if lead_context.get("intent"):
        context_str = f"They're interested in {lead_context['intent']}."
    if lead_context.get("budget"):
        context_str += f" Budget: {lead_context['budget']}."

    user_prompt = (
        f"Lead said: \"{objection}\"\n"
        f"Conversation stage: {current_state}\n"
        f"{context_str}\n\n"
        "Respond to this objection and guide them back toward scheduling a consultation."
    )

    try:
        response = await client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=100,
            temperature=0.2,
            system=system_prompt_override or OBJECTION_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}]
        )
        text = response.content[0].text.strip()
        logger.info(f"Claude objection response: {text!r}")
        return text

    except Exception as e:
        logger.error(f"Claude API error: {e}")
        # Safe fallback — keeps conversation alive
        return (
            "I completely understand — there's no pressure at all. "
            "Would it be okay if I just asked one more quick question before you go?"
        )
