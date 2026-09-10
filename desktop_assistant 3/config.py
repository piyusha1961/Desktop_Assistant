"""
config.py
---------
Central place for all settings, API keys, and constants used across the project.

WHY THIS FILE EXISTS:
Instead of typing API keys or passwords directly inside your feature code
(bad practice — risky if you ever share/upload your code), we load them from
a separate .env file that never gets shared/uploaded (see .env.example).

HOW TO USE:
1. Copy ".env.example" to a new file named ".env" in the same folder.
2. Fill in your own keys/passwords inside .env.
3. Never delete the .env from your local machine, but never upload/share it either.
"""

import os
from dotenv import load_dotenv

# Load variables from the .env file into the environment
load_dotenv()

# ---- API Keys / Secrets (read from .env) ----
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS", "")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD", "")
AI_API_KEY = os.getenv("AI_API_KEY", "")

# ---- App constants ----
APP_NAME = "PyAssist - Desktop Assistant"
DEFAULT_CITY = "Aurangabad"

# Folder where screenshots will be saved
SCREENSHOT_DIR = os.path.join(os.path.expanduser("~"), "PyAssist_Screenshots")

# Common applications this assistant knows how to open.
# KEY = what the user says/types (lowercase)
# VALUE = the actual command used to launch it on Windows.
# NOTE: paths may differ on your machine — adjust as needed (see README).
APP_PATHS = {
    "calculator": "Calculator",
    "whatsapp": "WhatsApp",
    "notes": "Notes",
    "vs code": "Visual Studio Code",
    "vscode": "Visual Studio Code",
    "safari": "Safari",
}

# Common websites this assistant knows how to open.
SITE_PATHS = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "wikipedia": "https://wikipedia.org",
    "instagram": "https://instagram.com",
}
