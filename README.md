# Home Assistant Meeting Summarizer

Offline-first, production-ready meeting summarizer for Home Assistant. Summarizes transcripts locally with Hugging Face, with optional OpenAI GPT. Features configurable models, logging, error handling, examples, and tests. Inspired by Liquid4All’s project.

---

## Features
- Offline-first summarization using Hugging Face transformers
- Optional online summarization with OpenAI GPT
- Summarizes text strings or meeting transcript files
- Ready for Home Assistant automations
- Configurable models and backends
- Logging, error handling, and unit tests included

---

## Installation

Clone or upload this project folder to your system.

Install dependencies:

```bash
pip install -r requirements.txt
````

For online GPT models, set your OpenAI API key:

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

---

## Usage

### Offline summarization (default)

```python
from ha_meeting_summarizer.ha_summarizer import HASummarizer

summarizer = HASummarizer()  # defaults to offline Hugging Face
summary = summarizer.summarize_file("examples/sample_meeting.txt")
print(summary)
```

### Online summarization (optional)

```python
summarizer_online = HASummarizer(
    backend="online",
    openai_model="gpt-4",
    openai_api_key="YOUR_API_KEY"
)
summary_online = summarizer_online.summarize_file("examples/sample_meeting.txt")
print(summary_online)
```

---

## Testing

Run the included tests using pytest:

```bash
pytest tests/
```

* Tests cover offline summarization, empty text, and missing file handling.
* Online tests are optional since they require an OpenAI API key.

---

## Dependencies

* `transformers>=4.40.0` (offline summarization)
* `torch>=2.0.0` (required for transformers)
* `openai>=0.27.0` (online summarization)
* `pytest>=7.0.0` (testing)

---

## Project Structure

```text
ha-meeting-summarizer/
├── README.md
├── requirements.txt
├── ha_meeting_summarizer/
│   ├── __init__.py
│   ├── ha_summarizer.py
│   └── utils.py
├── examples/
│   ├── sample_meeting.txt
│   └── run_example.py
└── tests/
    └── test_ha_summarizer.py
```

---

## Acknowledgements

This project was inspired by [Liquid4All’s Home Assistant Meeting Summarization example](https://github.com/Liquid4All/cookbook/tree/pau/examples/home-assistant/examples/meeting-summarization).

