import os
import pytest
from ha_meeting_summarizer.ha_summarizer import HASummarizer

# Initialize offline summarizer
summarizer = HASummarizer()

# Optional: online summarizer (requires API key)
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    summarizer_online = HASummarizer(backend="online", openai_api_key=api_key)
else:
    summarizer_online = None


def test_offline_text_summary():
    text = "Alice and Bob discussed the Q2 roadmap and assigned tasks to the marketing and engineering teams."
    summary = summarizer.summarize_text(text)
    assert isinstance(summary, str)
    assert len(summary) > 0
    assert "roadmap" in summary or "tasks" in summary


def test_offline_file_summary(tmp_path):
    file_path = tmp_path / "meeting.txt"
    file_path.write_text("Marketing and engineering teams discussed the project deadlines.")
    summary = summarizer.summarize_file(str(file_path))
    assert isinstance(summary, str)
    assert len(summary) > 0


def test_offline_audio_summary():
    audio_path = "examples/sample_meeting.wav"
    if os.path.exists(audio_path):
        summary = summarizer.summarize_audio(audio_path)
        assert isinstance(summary, str)
        assert len(summary) > 0
    else:
        pytest.skip("No sample audio file available.")


@pytest.mark.skipif(summarizer_online is None, reason="OpenAI API key not set")
def test_online_text_summary():
    text = "Alice and Bob discussed the Q2 roadmap and assigned tasks to the marketing and engineering teams."
    summary = summarizer_online.summarize_text(text)
    assert isinstance(summary, str)
    assert len(summary) > 0
