"""
Audio Utilities
"""
import audioop
import struct


def pcm_to_mulaw(pcm_bytes: bytes, sample_width: int = 2) -> bytes:
    """Convert raw PCM bytes to mulaw."""
    return audioop.lin2ulaw(pcm_bytes, sample_width)


def mulaw_to_pcm(mulaw_bytes: bytes, sample_width: int = 2) -> bytes:
    """Convert mulaw bytes to raw PCM."""
    return audioop.ulaw2lin(mulaw_bytes, sample_width)


def encode_mulaw_for_twilio(mulaw_bytes: bytes) -> str:
    """Base64-encode mulaw audio for Twilio Media Stream payload."""
    import base64
    return base64.b64encode(mulaw_bytes).decode("utf-8")
