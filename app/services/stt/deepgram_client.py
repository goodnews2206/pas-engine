"""
Deepgram Streaming STT Client
Handles: mulaw 8kHz audio from Twilio → real-time transcription
"""

import asyncio
import json
import logging
from contextlib import asynccontextmanager
from typing import Callable, Awaitable

import websockets

from app.config import get_settings

logger = logging.getLogger("pas.stt")
settings = get_settings()

# Deepgram streaming endpoint — optimized for telephony
DEEPGRAM_URL = (
    "wss://api.deepgram.com/v1/listen"
    "?model=nova-2-phonecall"
    "&encoding=mulaw"
    "&sample_rate=8000"
    "&channels=1"
    "&punctuate=true"
    "&interim_results=true"
    "&endpointing=300"        # 300ms silence = end of utterance
    "&utterance_end_ms=1000"  # flush after 1s of silence
)


class DeepgramStreamClient:
    """
    Context manager that opens a WebSocket to Deepgram.
    Yields a connection object you can call .send(audio_bytes) on.
    Transcripts are delivered via the callback passed to connect().
    """

    @asynccontextmanager
    async def connect(self, on_transcript: Callable[[str, bool], Awaitable[None]]):
        headers = {"Authorization": f"Token {settings.DEEPGRAM_API_KEY}"}

        async with websockets.connect(DEEPGRAM_URL, extra_headers=headers) as ws:
            logger.info("Deepgram WebSocket connected")

            # Listener task — reads transcripts from Deepgram
            async def _listen():
                try:
                    async for message in ws:
                        await _process_message(message, on_transcript)
                except websockets.ConnectionClosed:
                    logger.info("Deepgram connection closed")
                except Exception as e:
                    logger.error(f"Deepgram listener error: {e}", exc_info=True)

            listener_task = asyncio.create_task(_listen())

            # Wrap ws in a simple sender interface
            class DGConnection:
                async def send(self, audio_bytes: bytes):
                    try:
                        await ws.send(audio_bytes)
                    except Exception as e:
                        logger.warning(f"Deepgram send error: {e}")

                async def finish(self):
                    """Tell Deepgram we're done sending audio."""
                    try:
                        await ws.send(json.dumps({"type": "CloseStream"}))
                    except Exception:
                        pass

            try:
                yield DGConnection()
            finally:
                await DGConnection().finish()
                listener_task.cancel()
                try:
                    await listener_task
                except asyncio.CancelledError:
                    pass


async def _process_message(raw: str, callback: Callable[[str, bool], Awaitable[None]]):
    """Parse Deepgram response and invoke callback with transcript + finality."""
    try:
        data = json.loads(raw)
        result_type = data.get("type")

        if result_type == "Results":
            channel = data.get("channel", {})
            alts = channel.get("alternatives", [])
            if not alts:
                return

            transcript = alts[0].get("transcript", "").strip()
            is_final = data.get("is_final", False)
            speech_final = data.get("speech_final", False)

            if transcript:
                # speech_final = true means utterance boundary detected
                await callback(transcript, is_final or speech_final)

        elif result_type == "UtteranceEnd":
            # Force final processing
            await callback("", True)

    except (json.JSONDecodeError, KeyError) as e:
        logger.warning(f"Failed to parse Deepgram message: {e}")
