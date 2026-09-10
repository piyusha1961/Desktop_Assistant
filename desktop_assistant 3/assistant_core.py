"""
assistant_core.py
------------------
This is the "BRAIN" of the assistant. It does NOT do any actual work itself —
it just reads the user's command text, decides WHICH feature module should
handle it (based on keywords), and calls that module's function.

This keeps the code clean: the GUI doesn't need to know HOW weather or email
works, and the feature modules don't need to know anything about the GUI.
This separation is called "modular design" — mention this in your report.

HOW IT DECIDES (in order, first match wins):
    "time"                -> system_ops.get_time()
    "date"                -> system_ops.get_date()
    "screenshot"           -> system_ops.take_screenshot()
    "open <app/site>"      -> system_ops.open_app() then open_site()
    "weather"              -> web_ops.get_weather()
    "wikipedia"            -> web_ops.wiki_search()
    "search" / "google"    -> web_ops.google_search()
    "play"                 -> music_ops.play_on_youtube()
    "email"                -> handled specially (needs to/subject/body)
    anything else          -> chatbot.ask_ai()  (bonus AI fallback)
"""

from modules import system_ops, web_ops, music_ops, chatbot


def process_command(command_text: str) -> str:
    """
    Takes raw command text (from typing OR from voice-to-text) and returns
    the assistant's text response, ready to be displayed and/or spoken.
    """
    if not command_text or not command_text.strip():
        return "I didn't catch that. Could you type or say that again?"

    text = command_text.lower().strip()

    # --- Offline / system features (checked first: fastest, most reliable) ---
    if "time" in text:
        return system_ops.get_time()

    if "date" in text:
        return system_ops.get_date()

    if "screenshot" in text:
        return system_ops.take_screenshot()

    if text.startswith("open") or " open " in text:
        # Try apps first, then websites
        app_result = system_ops.open_app(text)
        if "don't recognize" not in app_result:
            return app_result
        return system_ops.open_site(text)

    # --- Online / API-based features ---
    if "weather" in text:
        return web_ops.get_weather(text)

    if "wikipedia" in text:
        return web_ops.wiki_search(text)

    if "search" in text or "google" in text:
        return web_ops.google_search(text)

    if "play" in text:
        return music_ops.play_on_youtube(text)

    # --- Bonus: anything unrecognized goes to the AI chatbot ---
    return chatbot.ask_ai(command_text)
