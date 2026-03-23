"""
Generate a sample audio file for HA Meeting Summarizer examples.

This script uses pyttsx3 (offline TTS) to produce a .wav file from text.

Usage:
    python examples/generate_sample_audio.py
"""

import pyttsx3
from pathlib import Path

# Ensure the examples folder exists
examples_dir = Path("examples")
examples_dir.mkdir(exist_ok=True)

# Output audio file
audio_file = examples_dir / "sample_meeting.wav"

# Text for audio
audio_text = """
Today we had our team meeting on Jan 13, 2025.
Alice went over the Q2 roadmap and highlighted the key priorities.
Bob talked about ongoing marketing campaigns and suggested increasing social media posts.
Carol provided updates on engineering projects and confirmed deadlines are on track.
Dave asked about the budget for new hires.
The team agreed to review the budget next week and follow up as needed.
"""

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)   # Adjust speech speed
engine.setProperty('volume', 1.0) # Max volume

# Generate the audio file
engine.save_to_file(audio_text, str(audio_file))
engine.runAndWait()

print(f"Sample audio file created at {audio_file.resolve()}")
