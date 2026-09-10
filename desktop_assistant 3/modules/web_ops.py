"""
web_ops.py
----------
This module handles everything that needs INTERNET (but not login/auth):
    1. google_search(query)   -> opens a Google search in the browser
    2. wiki_search(query)     -> fetches a short Wikipedia summary as TEXT
    3. get_weather(city)      -> fetches live weather using OpenWeatherMap API

WHY ERROR HANDLING MATTERS HERE:
Anything that depends on the internet can fail (no wifi, wrong city name,
API key not set up yet). Each function below uses try/except so a single
failed API call never crashes your whole assistant — it just returns a
friendly error message instead.
"""

import webbrowser
import requests
import wikipedia

import config


def google_search(command_text: str) -> str:
    """
    Extracts the search term from the command and opens a Google search
    for it in the default browser.

    Example: "search python tutorials" -> searches "python tutorials"
    """
    query = command_text.lower()
    for trigger in ["search for", "search", "google"]:
        query = query.replace(trigger, "")
    query = query.strip()

    if not query:
        return "What would you like me to search for?"

    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching Google for: {query}"


def wiki_search(command_text: str) -> str:
    """
    Extracts the topic from the command and returns a short Wikipedia
    summary (2 sentences) as text, which the GUI can display and speak.

    Example: "wikipedia albert einstein" -> summary of Albert Einstein
    """
    query = command_text.lower().replace("wikipedia", "").strip()

    if not query:
        return "What topic should I look up on Wikipedia?"

    try:
        summary = wikipedia.summary(query, sentences=2)
        return f"According to Wikipedia: {summary}"
    except wikipedia.exceptions.DisambiguationError as e:
        # Happens when the topic is ambiguous (e.g. "Mercury" -> planet or element?)
        options = ", ".join(e.options[:5])
        return f"That topic is a bit ambiguous. Did you mean one of: {options}?"
    except wikipedia.exceptions.PageError:
        return f"I couldn't find a Wikipedia page for '{query}'."
    except Exception as e:
        return f"Something went wrong searching Wikipedia: {e}"


def get_weather(command_text: str = "") -> str:
    """
    Fetches current weather for a city using the OpenWeatherMap API.

    If the user mentioned a city in their command (e.g. "weather in Pune"),
    that city is used. Otherwise it falls back to config.DEFAULT_CITY.
    """
    city = config.DEFAULT_CITY
    command_text = command_text.lower()
    if " in " in command_text:
        city = command_text.split(" in ")[-1].strip()

    if not config.OPENWEATHER_API_KEY:
        return (
            "Weather feature isn't set up yet. Add your free OpenWeatherMap "
            "API key to the .env file (see README)."
        )

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": config.OPENWEATHER_API_KEY,
        "units": "metric",  # gives temperature in Celsius
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        if response.status_code != 200:
            # e.g. city name typed wrong, or API key invalid
            return f"Couldn't get weather for '{city}': {data.get('message', 'unknown error')}"

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        return (
            f"Weather in {city.title()}: {description}, {temp}°C "
            f"(feels like {feels_like}°C), humidity {humidity}%"
        )
    except requests.exceptions.RequestException as e:
        return f"Network error while fetching weather: {e}"
