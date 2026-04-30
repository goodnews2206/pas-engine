import asyncio
import logging
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from app.services.llm.claude_client import handle_objection
from app.services.booking.calcom_client import book_appointment
from app.utils.slot_formatter import format_slot_for_speech

logger = logging.getLogger("pas.engine")


class State(str, Enum):
    GREETING = "GREETING"
    INTENT = "INTENT"
    BUDGET = "BUDGET"
    TIMELINE = "TIMELINE"
    BOOKING = "BOOKING"
    OBJECTION = "OBJECTION"
    CLOSING = "CLOSING"
    DONE = "DONE"


HARD_OBJECTIONS = [
    "not interested", "already have an agent",
    "have a realtor", "remove me", "stop calling",
    "waste of time", "don't need"
]

STATE_ORDER = [
    State.GREETING,
    State.INTENT,
    State.BUDGET,
    State.TIMELINE,
    State.BOOKING,
    State.CLOSING,
    State.DONE,
]


@dataclass
class LeadData:
    phone_number: str = ""
    email: str = ""
    name: str = ""
    intent: str = ""
    budget: str = ""
    timeline: str = ""
    property_interest: str = ""
    source: str = "inbound"
    booking_confirmed: bool = False
    booking_url: str = ""
    booking_slot: str = ""


@dataclass
class EngineState:
    current: State = State.GREETING
    previous: Optional[State] = None
    lead: LeadData = field(default_factory=LeadData)
    attempt_count: int = 0
    transcript_log: list = field(default_factory=list)
    outcome: str = "not_booked"
    objection_count: dict = field(default_factory=dict)
    states_visited: list = field(default_factory=lambda: ["GREETING"])


class PASEngine:
    MAX_ATTEMPTS = 2

    # Set by process_input when the lead asks to speak to a human.
    # The websocket handler reads this and initiates a Twilio warm transfer.
    pending_transfer: bool = False
    assigned_agent_id: Optional[str] = None

    def __init__(self, call_sid: str, lead_context: dict = None, brokerage: dict = None):
        self.call_sid = call_sid
        self.state = EngineState()
        self.start_time = datetime.now(timezone.utc)
        self.is_outbound = bool(lead_context)

        # Brokerage identity — fully white-labelled per tenant
        brokerage = brokerage or {}
        self.brokerage_id = brokerage.get("id", "demo")
        self.brokerage_name = brokerage.get("name", "ORVN Realty")
        self.agent_name = brokerage.get("agent_name", "Alex")
        self.featured_properties: list = brokerage.get("featured_properties") or []

        # Self-training config — Claude-generated overrides replace defaults when present
        training = brokerage.get("training_config") or {}
        self.trained_booking_prompt: str = training.get("booking_prompt", "")
        self.trained_objection_prompt: str = training.get("objection_system_prompt", "")
        self.training_version: int = brokerage.get("training_version", 0)

        # Brokerage operational config — controls call behaviour per tenant
        self.transfer_enabled: bool = brokerage.get("transfer_enabled", True)
        self.booking_enabled: bool = brokerage.get("booking_enabled", True)
        self.ai_disclosure_enabled: bool = brokerage.get("ai_disclosure_enabled", True)
        self.max_objection_attempts: int = brokerage.get("max_objection_attempts", 2)

        # Lead context — from outbound form data or inbound memory lookup
        if lead_context:
            self.state.lead.name = lead_context.get("name", "")
            self.state.lead.email = lead_context.get("email", "")
            self.state.lead.intent = lead_context.get("intent", "")
            self.state.lead.budget = lead_context.get("budget", "")
            self.state.lead.timeline = lead_context.get("timeline", "")
            self.state.lead.property_interest = lead_context.get("property_interest", "")
            self.state.lead.source = lead_context.get("source", "outbound")

        _default_booking = (
            "Great. I can book you in for a property viewing with one of our agents — "
            "would you like me to do that now?"
        )
        self.prompts = {
            State.INTENT: "Are you looking to buy, sell, or rent?",
            State.BUDGET: "Got it — what price range are you working with?",
            State.TIMELINE: "Perfect. How soon are you looking to make a move?",
            # Use trained prompt if available — otherwise default
            State.BOOKING: self.trained_booking_prompt or _default_booking,
        }

    # ───────────── PUBLIC ─────────────

    def get_greeting(self) -> str:
        disclosure = "Just so you know, this call may be recorded for quality purposes. " if self.ai_disclosure_enabled else ""
        name = self.state.lead.name
        returning = self.state.lead.source == "returning"

        if returning and name:
            intent = self.state.lead.intent
            context = f" Last time we spoke, you were interested in {intent}." if intent else ""
            return (
                f"Hi {name}, this is {self.agent_name} from {self.brokerage_name}. "
                f"{disclosure}"
                f"Great to hear from you again.{context} "
                "How can I help you today?"
            )

        if self.is_outbound:
            name_part = f", is this {name}?" if name else "?"
            return (
                f"Hi{name_part} This is {self.agent_name} calling from {self.brokerage_name}. "
                f"{disclosure}"
                "You recently submitted an inquiry about a property — "
                "do you have 2 minutes?"
            )

        return (
            f"Hi, this is {self.agent_name} from {self.brokerage_name}. "
            f"{disclosure}"
            "You recently inquired about a property — do you have a quick moment?"
        )

    async def process_input(self, transcript: str):
        self._log("lead", transcript)

        if self._is_ai_question(transcript):
            return self._handle_ai_question(), False

        if self._is_transfer_request(transcript):
            return self._handle_transfer_request(), False

        if self._is_question(transcript):
            return (
                "Great question — our agent will walk you through that in detail during the viewing. "
                "Quick one first — " + self._current_question(),
                False
            )

        if self._is_hard_objection(transcript):
            return await self._handle_objection(transcript)

        handler = self._get_handler(self.state.current)
        response, advance = await handler(transcript)

        if advance:
            self._advance_state()

        self._log("pas", response)
        return response, self.state.current == State.DONE

    # ───────────── HANDLERS ─────────────

    def _get_handler(self, state):
        return {
            State.GREETING: self._handle_greeting,
            State.INTENT: self._handle_intent,
            State.BUDGET: self._handle_budget,
            State.TIMELINE: self._handle_timeline,
            State.BOOKING: self._handle_booking,
            State.CLOSING: self._handle_closing,
        }.get(state, self._handle_done)

    async def _handle_greeting(self, text):
        lowered = text.lower()

        confusion = [
            "didn't sign up", "did not sign up",
            "didn't inquire", "did not inquire",
            "wrong number", "not me", "i didn't", "i never"
        ]
        if any(c in lowered for c in confusion):
            self.state.outcome = "not_booked"
            self.state.current = State.DONE
            return (
                "My apologies — you may have been referred through a partner site. "
                "No worries at all. Have a great day.",
                True
            )

        # Answering machine detected by Twilio machine_detection
        if "machine" in lowered or "voicemail" in lowered:
            self.state.outcome = "not_booked"
            self.state.current = State.DONE
            return (
                f"Hi, this is Alex from ORVN Realty calling for "
                f"{self.state.lead.name or 'you'}. "
                "We'd love to book a property viewing — please call us back or visit orvnlabs.com.",
                True
            )

        if any(w in lowered for w in ["no", "busy", "not now", "call back"]):
            self.state.outcome = "not_booked"
            self.state.current = State.DONE
            return "No problem — I'll follow up later. Have a great day!", True

        # For outbound/returning calls with pre-filled data, skip ahead to the
        # first unanswered question so the caller isn't asked what we already know.
        lead = self.state.lead
        if lead.intent and lead.budget and lead.timeline:
            return self.prompts[State.BOOKING], True
        if lead.intent and lead.budget:
            return self.prompts[State.TIMELINE], True
        if lead.intent:
            return self.prompts[State.BUDGET], True
        return self.prompts[State.INTENT], True

    async def _handle_intent(self, text):
        lowered = text.lower()

        if any(w in lowered for w in ["buy", "purchase", "own", "looking", "moving"]):
            self.state.lead.intent = "buying"
        elif any(w in lowered for w in ["sell", "listing"]):
            self.state.lead.intent = "selling"
        elif any(w in lowered for w in ["rent", "lease"]):
            self.state.lead.intent = "renting"
        else:
            return self._retry("Just to confirm — buy, sell, or rent?")

        return self.prompts[State.BUDGET], True

    async def _handle_budget(self, text):
        budget = self._extract_budget(text)
        if budget:
            self.state.lead.budget = budget
            self.state.attempt_count = 0
            return self.prompts[State.TIMELINE], True

        if self.state.attempt_count >= self.MAX_ATTEMPTS:
            self.state.lead.budget = "not specified"
            self.state.attempt_count = 0
            return self.prompts[State.TIMELINE], True

        return self._retry("Even a rough range helps — what budget are you working with?")

    async def _handle_timeline(self, text):
        timeline = self._extract_timeline(text)
        self.state.lead.timeline = timeline or "unspecified"
        self.state.attempt_count = 0

        # Tease featured properties if any are loaded for this brokerage
        booking_prompt = self.prompts[State.BOOKING]
        if self.featured_properties:
            prop = self.featured_properties[0]
            addr = prop.get("address", "a property")
            price = prop.get("price", "")
            price_str = f" listed at {price}" if price else ""
            booking_prompt = (
                f"We actually have a great listing — {addr}{price_str} — "
                f"that sounds like it could be a strong match. "
                "I can book you in to view it with one of our agents. Would that work?"
            )

        return booking_prompt, True

    async def _handle_booking(self, text):
        if not self.booking_enabled:
            self.state.outcome = "not_booked"
            return (
                "Sounds great — one of our agents will reach out to you shortly "
                "to discuss next steps. Have a great day!",
                True,
            )

        lowered = text.lower()

        # Soft objections at booking stage
        if any(p in lowered for p in [
            "do i have to", "commit", "what does that involve",
            "is it free", "no obligation", "cost", "charge"
        ]):
            return (
                "No commitment at all — the viewing is completely free. "
                "Our agent will show you the property and answer any questions. "
                "Shall I go ahead and book it?",
                False
            )

        if any(w in lowered for w in ["yes", "sure", "okay", "yeah", "go ahead", "do it", "please"]):
            result = await book_appointment(
                phone=self.state.lead.phone_number,
                name=self.state.lead.name or "Lead",
                email=self.state.lead.email,
                notes=(
                    f"{self.state.lead.intent}, "
                    f"{self.state.lead.budget}, "
                    f"{self.state.lead.timeline}"
                    + (f", {self.state.lead.property_interest}" if self.state.lead.property_interest else "")
                ),
                brokerage_id=self.brokerage_id,
                call_sid=self.call_sid,
            )

            if result.get("success"):
                self.state.outcome = "booked"
                self.state.lead.booking_confirmed = True
                self.state.lead.booking_slot = result.get("slot", "")

                slot_text = format_slot_for_speech(self.state.lead.booking_slot)

                # Fire-and-forget notifications
                asyncio.create_task(self._send_booking_notifications(slot_text))

                confirm_channel = (
                    "by email and text" if self.state.lead.email else "by text"
                )
                return (
                    f"Perfect — you're booked for a property viewing on {slot_text}. "
                    f"You'll receive a confirmation {confirm_channel} shortly. "
                    "Is there anything specific you'd like the agent to know before the viewing?",
                    True
                )
            else:
                self.state.outcome = "not_booked"
                return (
                    "Our calendar is a little full right now, but one of our agents will "
                    "call you back within the hour to lock in a time.",
                    True
                )

        if any(w in lowered for w in ["no", "not now", "later", "not yet"]):
            self.state.outcome = "not_booked"
            return (
                "No worries at all. I'll have an agent follow up with you — "
                "feel free to reach out anytime.",
                True
            )

        return self._retry("Just a quick yes or no — shall I book the viewing?")

    async def _handle_closing(self, text):
        # Capture any final notes the lead shares before the call ends
        if text.strip():
            self.state.lead.property_interest = (
                (self.state.lead.property_interest + " | " + text.strip())
                if self.state.lead.property_interest else text.strip()
            )
        return (
            "Got it — I'll pass that along to your agent. "
            "Looking forward to finding you the perfect property. Have a great day!",
            True
        )

    async def _handle_done(self, text):
        return "", True

    # ───────────── NOTIFICATIONS ─────────────

    async def _send_booking_notifications(self, slot_text: str):
        from app.services.notifications.sms_client import send_booking_confirmation_sms
        from app.services.notifications.email_client import send_booking_confirmation_email

        phone = self.state.lead.phone_number
        name = self.state.lead.name or "there"

        if phone:
            await send_booking_confirmation_sms(phone, name, slot_text)

        if self.state.lead.email:
            await send_booking_confirmation_email(
                to=self.state.lead.email,
                name=name,
                slot_readable=slot_text,
                intent=self.state.lead.intent,
                budget=self.state.lead.budget,
                timeline=self.state.lead.timeline,
            )

    # ───────────── OBJECTION ─────────────

    def _classify_objection(self, text: str) -> str:
        lowered = text.lower()
        if "remove me" in lowered or "stop calling" in lowered:
            return "remove"
        if "agent" in lowered or "realtor" in lowered:
            return "has_agent"
        if "not interested" in lowered:
            return "not_interested"
        return "other"

    async def _handle_objection(self, text):
        category = self._classify_objection(text)
        self.state.objection_count[category] = (
            self.state.objection_count.get(category, 0) + 1
        )

        # Any "remove/stop" category ends the call immediately, no second chance.
        # For all other categories, end after max_objection_attempts total objections.
        total_objections = sum(self.state.objection_count.values())
        if category == "remove" or total_objections >= self.max_objection_attempts:
            self.state.outcome = "not_booked"
            self.state.current = State.DONE
            return "Understood — I won't contact you again. Take care.", True

        self.state.previous = self.state.current
        response = await handle_objection(
            objection=text,
            current_state=self.state.previous.value,
            lead_context=self.state.lead.__dict__,
            # Inject trained system prompt if this brokerage has been self-trained
            system_prompt_override=self.trained_objection_prompt or None,
        )
        return response, False

    # ───────────── UTILS ─────────────

    def _current_question(self) -> str:
        return self.prompts.get(self.state.current, "how can I help?")

    def _is_transfer_request(self, text: str) -> bool:
        if not self.transfer_enabled:
            return False
        lowered = text.lower()
        triggers = [
            "speak to a human", "speak to someone", "talk to a person",
            "talk to an agent", "speak to a real person", "human please",
            "transfer me", "connect me", "speak to a real",
            "can i talk to", "let me speak to", "i want to speak to",
            "i'd like to speak", "get me an agent", "i need a person",
        ]
        return any(t in lowered for t in triggers)

    def _handle_transfer_request(self) -> str:
        self.pending_transfer = True
        self.state.outcome = "transferred"
        return (
            "Of course — let me connect you with one of our agents right now. "
            "Please hold for just a moment."
        )

    def _is_ai_question(self, text: str) -> bool:
        lowered = text.lower()
        triggers = [
            "are you ai", "are you an ai", "is this ai", "are you a bot",
            "are you a robot", "are you real", "am i talking to a person",
            "is this a real person", "are you a real person", "is this automated",
            "are you human", "is this a machine", "who am i speaking to",
            "what are you", "is this a human", "are you actually a person",
        ]
        return any(t in lowered for t in triggers)

    def _handle_ai_question(self) -> str:
        redirect = "Quick one while I have you — " + self._current_question()
        return (
            "Yes — I'm an AI assistant with ORVN Realty. "
            "I handle the initial matching so you're only connected with an agent "
            "who's the right fit for what you're looking for. "
            "You'll be working with a real person for the viewing itself. "
            f"{redirect}"
        )

    def _is_hard_objection(self, text):
        return any(w in text.lower() for w in HARD_OBJECTIONS)

    def _is_question(self, text: str) -> bool:
        lowered = text.lower()
        return (
            "?" in text or
            any(q in lowered for q in [
                "can you", "could you", "what", "why", "how",
                "is it", "are there", "does that", "do i have to"
            ])
        )

    def _advance_state(self):
        idx = STATE_ORDER.index(self.state.current)
        if idx + 1 < len(STATE_ORDER):
            self.state.current = STATE_ORDER[idx + 1]
            state_name = self.state.current.value
            if state_name not in self.state.states_visited:
                self.state.states_visited.append(state_name)
            self.state.attempt_count = 0
            self._skip_if_prefilled()

    def _skip_if_prefilled(self):
        """For outbound calls with form data: skip states we already have answers for."""
        lead = self.state.lead
        if self.state.current == State.INTENT and lead.intent:
            self._advance_state()
        elif self.state.current == State.BUDGET and lead.budget:
            self._advance_state()
        elif self.state.current == State.TIMELINE and lead.timeline:
            self._advance_state()

    def _retry(self, prompt):
        self.state.attempt_count += 1
        variations = [prompt, "Just a ballpark is fine.", "Even an estimate works."]
        if self.state.attempt_count <= self.MAX_ATTEMPTS:
            return variations[min(self.state.attempt_count - 1, len(variations) - 1)], False
        self.state.attempt_count = 0
        return prompt, True

    def _extract_budget(self, text):
        lowered = text.lower()
        word_map = {
            "half a million": "$500k",
            "two fifty": "$250k",
            "three fifty": "$350k",
            "four fifty": "$450k",
            "a million": "$1m",
        }
        for k, v in word_map.items():
            if k in lowered:
                return v
        patterns = [r"\$?[\d,]+(?:\.\d+)?(?:k|m)?", r"[\d,]+\s*-\s*[\d,]+"]
        for p in patterns:
            match = re.search(p, lowered)
            if match:
                return match.group(0)
        return None

    def _extract_timeline(self, text):
        match = re.search(
            r"(?:a\s+)?(?:few|couple\s+of)?\s*\d*\s*(days?|weeks?|months?|years?)",
            text.lower()
        )
        return match.group(0) if match else None

    def _log(self, speaker, text):
        self.state.transcript_log.append({
            "speaker": speaker,
            "text": text,
            "state": self.state.current,
            "ts": datetime.now(timezone.utc).isoformat(),
        })

    # ───────────── RESULT ACCESSORS ─────────────

    def get_outcome(self) -> str:
        return self.state.outcome

    def get_full_transcript(self) -> str:
        return "\n".join(
            f"[{e['speaker']}] {e['text']}" for e in self.state.transcript_log
        )

    def get_metadata(self) -> dict:
        return {
            "lead": self.state.lead.__dict__,
            "final_state": self.state.current.value,
            "is_outbound": self.is_outbound,
            "duration_seconds": (datetime.now(timezone.utc) - self.start_time).seconds,
            "states_visited": self.state.states_visited,
            "objections_detected": [
                {"category": k, "count": v}
                for k, v in self.state.objection_count.items()
            ],
            "brokerage_id": self.brokerage_id,
        }