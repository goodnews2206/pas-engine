"""
ElevenLabs TTS Client
Input: text string
Output: mulaw-encoded audio bytes (8kHz, compatible with Twilio Media Streams)

Note: ElevenLabs outputs mp3 by default. Twilio needs mulaw 8kHz.
We use audioop (stdlib) to convert PCM → mulaw after decoding mp3 with pydub.
"""

import io
import logging

import httpx
from pydub import AudioSegment

from app.config import get_settings

logger = logging.getLogger("pas.tts")
settings = get_settings()

ELEVENLABS_TTS_URL = (
    f"https://api.elevenlabs.io/v1/text-to-speech"
    f"/{settings.ELEVENLABS_VOICE_ID}"
    f"/stream"
)

# Pre-built fallback audio phrase (silence filler)
# In production: pre-synthesize this and store as bytes at startup
FALLBACK_TEXT = "One moment…"

_tts_cache: dict[str, bytes] = {}  # Simple in-process cache for repeated phrases


async def synthesize_speech(text: str) -> bytes:
    """
    Convert text to mulaw audio bytes for Twilio playback.
    Returns raw mulaw bytes (8kHz, mono).
    """
    if not text.strip():
        return b""

    # Cache hit
    if text in _tts_cache:
        logger.debug(f"TTS cache hit: {text[:40]!r}")
        return _tts_cache[text]

    headers = {
        "xi-api-key": settings.ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "text": text,
        "model_id": "eleven_turbo_v2",   # lowest latency model
        "voice_settings": {
            "stability": 0.45,
            "similarity_boost": 0.80,
            "style": 0.0,
            "use_speaker_boost": True
        },
        "output_format": "pcm_16000",   # PCM at 16kHz — we'll downsample
    }

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.post(
                f"https://api.elevenlabs.io/v1/text-to-speech/{settings.ELEVENLABS_VOICE_ID}",
                headers=headers,
                json={**payload, "output_format": "mp3_44100_128"}
            )
            resp.raise_for_status()
            mp3_bytes = resp.content

        # Convert mp3 → PCM → mulaw 8kHz
        mulaw_bytes = _convert_mp3_to_mulaw(mp3_bytes)
        _tts_cache[text] = mulaw_bytes
        logger.info(f"TTS synthesized {len(mulaw_bytes)} mulaw bytes for: {text[:50]!r}")
        return mulaw_bytes

    except httpx.HTTPError as e:
        logger.error(f"ElevenLabs TTS error: {e}")
        # Return empty — caller handles gracefully
        return b""


def _convert_mp3_to_mulaw(mp3_bytes: bytes) -> bytes:
    """
    mp3 → PCM 16-bit mono 8kHz → mulaw
    Uses pydub for decoding, audioop for mulaw encoding.
    """
    import audioop

    # Decode mp3
    audio = AudioSegment.from_mp3(io.BytesIO(mp3_bytes))

    # Normalize: mono, 8kHz, 16-bit
    audio = audio.set_channels(1).set_frame_rate(8000).set_sample_width(2)
    pcm_bytes = audio.raw_data

    # Encode to mulaw
    mulaw_bytes = audioop.lin2ulaw(pcm_bytes, 2)
    return mulaw_bytes


async def get_fallback_audio() -> bytes:
    """Pre-synthesized silence-filler. Call at startup to warm the cache."""
    return await synthesize_speech(FALLBACK_TEXT)
