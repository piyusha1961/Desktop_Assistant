"""
music_ops.py
------------
Handles playing music. Two approaches are supported:

1. play_local(command_text) -> plays an mp3 file from a local "music" folder
   using the system's default media player (simplest, most reliable).

2. play_on_youtube(command_text) -> opens a YouTube search for the song
   in the browser (works even if you have no local mp3 files, good for demo).
"""

import os
import webbrowser

import config

# Folder where you should place a few sample .mp3 files for the demo
MUSIC_DIR = os.path.join(os.path.dirname(__file__), "..", "music")


def play_local(command_text: str) -> str:
    """
    Looks for an .mp3 file in the /music folder whose name is mentioned
    in the command, and plays it with the OS's default player.

    Example: "play believer" -> looks for "believer.mp3" in /music
    """
    query = command_text.lower().replace("play", "").strip()

    if not os.path.isdir(MUSIC_DIR):
        return "No 'music' folder found. Create one and add some .mp3 files."

    for filename in os.listdir(MUSIC_DIR):
        if filename.lower().endswith(".mp3") and query in filename.lower():
            filepath = os.path.join(MUSIC_DIR, filename)
            try:
                os.startfile(filepath)  # Windows only
                return f"Playing {filename}"
            except Exception as e:
                return f"Found the file but couldn't play it: {e}"

    return f"Couldn't find a song matching '{query}' in the music folder."


def play_on_youtube(command_text: str) -> str:
    """
    Fallback / simpler option: opens a YouTube search for the requested
    song directly in the browser. No local files needed.
    """
    query = command_text.lower().replace("play", "").strip()

    if not query:
        return "What song would you like to play?"

    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    return f"Searching YouTube for: {query}"
