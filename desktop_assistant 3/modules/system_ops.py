"""
system_ops.py
--------------
This module handles everything that talks directly to the OPERATING SYSTEM
(no internet needed). This is the safest, most reliable part of the whole
project — great to build and test FIRST.

Features covered:
    1. get_time()          -> tells current time
    2. get_date()           -> tells current date
    3. open_app(name)       -> launches an installed application
    4. open_site(name)      -> opens a website in the default browser
    5. take_screenshot()    -> captures the screen and saves it as an image
"""

import os
import subprocess
import webbrowser
import platform
from datetime import datetime

import pyautogui

import config


def get_time() -> str:
    """Returns the current time as a friendly string, e.g. '03:45 PM'."""
    now = datetime.now().strftime("%I:%M %p")
    return f"The current time is {now}"


def get_date() -> str:
    """Returns today's date as a friendly string, e.g. 'Monday, 03 August 2026'."""
    today = datetime.now().strftime("%A, %d %B %Y")
    return f"Today's date is {today}"


def open_app(command_text: str) -> str:
    """
    Tries to find a known application name inside the user's command text
    and launch it using macOS's 'open -a' command.
    """
    command_text = command_text.lower()

    for app_name, mac_app_name in config.APP_PATHS.items():
        if app_name in command_text:
            try:
                subprocess.run(["open", "-a", mac_app_name], check=True)
                return f"Opening {app_name}..."
            except subprocess.CalledProcessError:
                return (
                    f"I couldn't find '{mac_app_name}' on this Mac. "
                    f"Check the exact app name in your Applications folder."
                )
            except Exception as e:
                return f"Something went wrong while opening {app_name}: {e}"

    return "I don't recognize that application."

def open_site(command_text: str) -> str:
    """
    Tries to find a known website name inside the user's command text
    and open it in the default browser.

    Example: command_text = "open youtube" -> matches "youtube" in config.SITE_PATHS
    """
    command_text = command_text.lower()

    for site_name, url in config.SITE_PATHS.items():
        if site_name in command_text:
            webbrowser.open(url)
            return f"Opening {site_name}..."

    return "I don't recognize that website. Try: youtube, google, gmail, github, wikipedia."


def take_screenshot() -> str:
    """
    Captures the current screen and saves it as a PNG file with a
    timestamped filename, so repeated screenshots never overwrite each other.
    """
    try:
        os.makedirs(config.SCREENSHOT_DIR, exist_ok=True)

        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(config.SCREENSHOT_DIR, filename)

        screenshot = pyautogui.screenshot()
        screenshot.save(filepath)

        return f"Screenshot saved to {filepath}"
    except Exception as e:
        return f"Couldn't take a screenshot: {e}"
