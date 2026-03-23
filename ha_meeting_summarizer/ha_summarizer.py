from transformers import pipeline
import openai
import os
from ha_meeting_summarizer.utils import get_logger

logger = get_logger()

class HASummarizer:
    """
    Meeting summarizer class:
    - Offline-first using Hugging Face
    - Optional online model using OpenAI GPT
    """
    def __init__(self, backend="offline", hf_model="facebook/bart-large-cnn",
                 openai_model="gpt-3.5-turbo", openai_api_key=None):
        self.backend = backend.lower()
        self.hf_model = hf_model
        self.openai_model = openai_model
        self.openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")

        if self.backend == "offline":
            try:
                logger.info(f"Loading offline Hugging Face model: {hf_model}")
                self.hf_summarizer = pipeline("summarization", model=hf_model)
            except Exception as e:
                logger.error(f"Failed to load Hugging Face model: {e}")
                raise RuntimeError(f"Cannot load offline model {hf_model}")
        elif self.backend == "online":
            if not self.openai_api_key:
                raise ValueError("OpenAI API key required for online backend")
            openai.api_key = self.openai_api_key
            logger.info(f"Using OpenAI model: {openai_model}")
        else:
            raise ValueError("Invalid backend. Choose 'offline' or 'online'.")

    def summarize_text(self, text, max_tokens=150):
        if not text:
            logger.warning("Empty text provided.")
            return ""
        if self.backend == "offline":
            try:
                result = self.hf_summarizer(text, max_length=max_tokens,
                                            min_length=40, do_sample=False)
                return result[0]["summary_text"]
            except Exception as e:
                logger.error(f"Hugging Face summarization failed: {e}")
                return "Error generating summary offline."
        elif self.backend == "online":
            try:
                response = openai.ChatCompletion.create(
                    model=self.openai_model,
                    messages=[
                        {"role": "system", "content": "You summarize meeting transcripts concisely."},
                        {"role": "user", "content": text}
                    ],
                    max_tokens=max_tokens,
                    temperature=0.5
                )
                return response["choices"][0]["message"]["content"].strip()
            except Exception as e:
                logger.error(f"OpenAI summarization failed: {e}")
                return "Error generating summary online."

    def summarize_file(self, file_path, max_tokens=150):
        if not os.path.exists(file_path):
            logger.error(f"File {file_path} not found.")
            return "File not found."
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
        return self.summarize_text(text, max_tokens=max_tokens)
