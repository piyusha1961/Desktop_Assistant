"""
chatbot.py
----------
BONUS FEATURE: AI Chatbot integration.

Whenever the command router (assistant_core.py) doesn't recognize a command
as one of the fixed features (time, weather, email, etc.), it falls back to
this module — so the assistant can still give a sensible answer instead of
just saying "I don't understand."

This example uses Anthropic's Claude API. You can swap this for any LLM
provider (OpenAI, Gemini, etc.) — the pattern (send text, get text back)
stays the same. You'll need your own API key (see README for how to get one
and where to put it in your .env file).
"""

import requests
import config


def ask_ai(question: str) -> str:
    """
    Sends the user's question to an AI API and returns its text response.
    Falls back to a friendly message if no API key is configured or if
    the request fails for any reason (never crashes the app).
    """
    if not config.AI_API_KEY:
        return (
            "I don't have a fixed command for that, and the AI chatbot "
            "feature isn't set up yet. Add AI_API_KEY to your .env file "
            "to enable it (see README)."
        )

    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": config.AI_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": "claude-sonnet-4-6",
                "max_tokens": 300,
                "messages": [{"role": "user", "content": question}],
            },
            timeout=15,
        )
        data = response.json()

        if response.status_code != 200:
            return f"AI service error: {data.get('error', {}).get('message', 'unknown error')}"

        # The response content is a list of blocks; we join any text blocks
        reply = "".join(
            block.get("text", "") for block in data.get("content", []) if block.get("type") == "text"
        )
        return reply.strip() or "The AI didn't return a text response."

    except requests.exceptions.RequestException as e:
        return f"Network error contacting the AI service: {e}"
