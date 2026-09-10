# PyAssist — Desktop Assistant (Python Mini Project)

A GUI-based desktop assistant that automates everyday tasks: opening apps/
websites, checking time/date/weather, searching Google/Wikipedia, taking
screenshots, sending email, playing music, and (bonus) answering open-ended
questions via an AI chatbot.

## Project Structure

```
desktop_assistant/
├── main.py               # GUI entry point — RUN THIS FILE
├── assistant_core.py      # command router ("brain")
├── config.py              # settings + loads API keys from .env
├── .env.example           # template for your secret keys (copy to .env)
├── requirements.txt        # Python packages needed
├── modules/
│   ├── system_ops.py       # time, date, open apps/sites, screenshot (offline)
│   ├── web_ops.py           # Google/Wikipedia search, weather (needs internet)
│   ├── email_ops.py         # send email via Gmail SMTP
│   ├── music_ops.py         # play music (local or YouTube)
│   ├── voice.py              # speech-to-text + text-to-speech
│   └── chatbot.py            # bonus: AI chatbot fallback
└── music/                  # (optional) put .mp3 files here for local playback
```

## Setup Instructions

### 1. Install Python
Make sure you have Python 3.9+ installed. Check with:
```
python --version
```

### 2. Install dependencies
From inside the `desktop_assistant` folder, run:
```
pip install -r requirements.txt
```

**Note on PyAudio (needed for microphone input):**
PyAudio sometimes fails to install directly via pip on Windows. If it fails, run:
```
pip install pipwin
pipwin install pyaudio
```

### 3. Set up your API keys
1. Copy `.env.example` and rename the copy to `.env`
2. Fill in your keys:
   - **OPENWEATHER_API_KEY** — free at https://openweathermap.org/api (takes a few minutes to activate after signup)
   - **EMAIL_ADDRESS** / **EMAIL_APP_PASSWORD** — your Gmail + an App Password from https://myaccount.google.com/apppasswords (requires 2-Step Verification turned on)
   - **AI_API_KEY** — only needed for the bonus chatbot feature; optional

You can skip any of these — the app won't crash, it'll just tell you that feature isn't set up yet.

### 4. Run the assistant
```
python main.py
```

## How to Use

- Type a command in the box and press Enter / click Send, OR click **🎙 Speak** to give a voice command.
- Try commands like:
  - `what's the time`
  - `what's the date`
  - `open notepad`
  - `open youtube`
  - `weather in Pune`
  - `wikipedia albert einstein`
  - `search python tutorials`
  - `play believer` (if you added an mp3, or it searches YouTube)
  - `screenshot`
  - Anything else → gets forwarded to the AI chatbot (if configured)
- Click **✉ Send Email** to open a small form (To / Subject / Message) and send an email.

## Known Limitations (worth mentioning in your report)

- Voice recognition (`speech_recognition`) requires an internet connection.
- `open_app()` paths in `config.py` are set for Windows; adjust `APP_PATHS` if you're on macOS/Linux, or if an app isn't found on your specific machine.
- Weather, search, Wikipedia, and the AI chatbot all require an active internet connection.
- The command router uses keyword matching, not full natural language understanding — it recognizes specific trigger words (time, date, weather, open, etc.) rather than free-form conversation, except for the AI chatbot fallback.

## Customization Ideas (for the bonus marks / extra polish)

- Add more entries to `APP_PATHS` / `SITE_PATHS` in `config.py`.
- Add a "reminder" feature using Python's `schedule` library + desktop notifications (`plyer` or `win10toast`).
- Swap `chatbot.py` to use a different AI provider if preferred.
