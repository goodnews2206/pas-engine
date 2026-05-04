"""Quick ElevenLabs voice test — generates a sample greeting and saves to test_voice.mp3"""
import asyncio
import sys
import os
sys.path.insert(0, ".")

from app.services.tts.elevenlabs_client import synthesize_speech

async def main():
    print("Testing ElevenLabs voice...")
    text = (
        "Hi there! This is Alex from ORVN Realty. "
        "I'm calling about your recent interest in one of our properties. "
        "Do you have a moment to chat?"
    )
    audio = await synthesize_speech(text)
    if audio:
        with open("test_voice.mp3", "wb") as f:
            f.write(audio)
        size_kb = len(audio) / 1024
        print(f"Success! Audio generated: {size_kb:.1f} KB -> test_voice.mp3")
        print("Open test_voice.mp3 to hear Alex's voice.")
    else:
        print("Failed — no audio returned. Check ELEVENLABS_API_KEY and VOICE_ID.")

asyncio.run(main())
