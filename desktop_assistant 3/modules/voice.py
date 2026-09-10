"""
voice.py
--------
Handles converting SPEECH -> TEXT (so the assistant can "listen") and
TEXT -> SPEECH (so the assistant can "talk back").

Two separate libraries are used because they do opposite jobs:
    - speech_recognition : microphone audio -> text   (needs internet)
    - pyttsx3             : text -> spoken audio        (works OFFLINE)

WHY THIS MATTERS FOR YOUR DEMO:
Because speech_recognition needs internet and a working mic (which can be
flaky in an exam hall), ALWAYS keep a typed-text input option in your GUI
as a backup. Never make voice the ONLY way to give a command.
"""

import speech_recognition as sr
import pyttsx3

# pyttsx3 engine is created ONCE and reused (creating it repeatedly can
# cause audio glitches or errors on some systems)
_engine = pyttsx3.init()
_engine.setProperty("rate", 175)  # speaking speed; adjust to taste


def speak(text: str) -> None:
    """Speaks the given text out loud using the offline TTS engine."""
    try:
        _engine.say(text)
        _engine.runAndWait()
    except Exception as e:
        print(f"[voice.py] Couldn't speak text: {e}")


def listen() -> str:
    """
    Listens to the microphone for a few seconds and converts speech to text.

    Returns the recognized text in lowercase, or an empty string if
    nothing could be understood (caller should handle that gracefully).
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("[voice.py] Adjusting for background noise...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("[voice.py] Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

        # Sends the audio to Google's free speech recognition service
        text = recognizer.recognize_google(audio)
        return text.lower()

    except sr.WaitTimeoutError:
        return ""  # user didn't say anything in time
    except sr.UnknownValueError:
        return ""  # audio was captured but not understood
    except sr.RequestError as e:
        print(f"[voice.py] Speech recognition service error: {e}")
        return ""
    except Exception as e:
        print(f"[voice.py] Microphone error (is one connected?): {e}")
        return ""
