# Desktop_Assistant
IRIS - A desktop assistant 

# 🤖 IRIS – AI Voice-Controlled Desktop Assistant

> A smart Python-based desktop assistant designed to automate everyday computer tasks using voice commands and a modern graphical user interface.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

---

## 📌 About the Project

**IRIS (AI Voice-Controlled Desktop Assistant)** is a Python-based automation application designed to simplify everyday computer operations.

The assistant allows users to interact with their computer using **voice commands and a graphical user interface**. IRIS can perform various tasks such as opening applications, launching websites, searching Google and Wikipedia, providing weather updates, telling the date and time, taking screenshots, playing music, and more.

The main objective of the project is to reduce manual effort and improve productivity by integrating multiple desktop automation features into a single intelligent assistant.

---

# 🎯 Problem Statement

Users perform several repetitive tasks while using a computer, such as opening applications, visiting websites, searching for information, checking the weather, taking screenshots, and managing basic system operations.

Performing these tasks manually requires multiple clicks and keyboard interactions, which can be time-consuming.

The proposed system, **IRIS**, addresses this problem by providing a centralized desktop assistant that accepts voice or text commands and automatically performs the requested operations.

---

# 🎯 Objectives

* Develop a user-friendly graphical interface for a desktop assistant.
* Implement speech-to-text functionality for voice commands.
* Implement text-to-speech functionality for assistant responses.
* Automate the opening of desktop applications.
* Open websites through user commands.
* Perform Google and Wikipedia searches.
* Provide weather information using APIs.
* Display the current date and time.
* Capture and save screenshots.
* Play music from the user's system.
* Provide basic system information.
* Improve productivity through desktop automation.

---

# ✨ Features

## 🎤 Voice Commands

IRIS can accept voice commands from the user.

Example:

```text
Open Chrome
```

---

## 💻 Application Launcher

The assistant can open supported desktop applications.

Examples:

```text
Open Chrome
Open Calculator
Open VS Code
Open Notepad
```

---

## 🌐 Website Launcher

IRIS can open commonly used websites.

Examples:

```text
Open YouTube
Open Google
Open Gmail
Open LinkedIn
Open GitHub
```

---

## 🔍 Smart Search

The assistant can perform searches using:

* Google Search
* Wikipedia Search

Example:

```text
Search Artificial Intelligence
```

---

## 🌦️ Weather Information

IRIS can provide weather information such as:

* Temperature
* Humidity
* Weather condition
* Wind speed

---

## 🕒 Date and Time

The assistant can provide the current:

* Time
* Date
* Day

---

## 📸 Screenshot Capture

Users can capture and automatically save screenshots.

---

## 🎵 Music Control

IRIS can play music from a selected music directory.

---

## 🔋 System Information

The assistant can provide basic system information such as:

* Battery percentage
* CPU usage
* RAM usage
* Disk usage

---

## 🔔 Reminder System

Users can create simple reminders and receive notifications.

---

# 🖥️ User Interface

IRIS uses a modern GUI built with **CustomTkinter**.

The interface includes:

* Assistant title and branding
* Assistant status indicator
* Conversation/output area
* Start Listening button
* Clear conversation button
* Screenshot button
* Exit button

Example interface flow:

```text
┌─────────────────────────────────────────────┐
│                  I R I S                    │
│              Desktop Assistant              │
│                                             │
│              ● Ready to assist              │
│                                             │
│  IRIS: Hello! How can I help you today?     │
│                                             │
│       🎤 Start Listening   Clear            │
│                                             │
│       📸 Screenshot        Exit             │
└─────────────────────────────────────────────┘
```

---

# 🏗️ Project Architecture

```text
User
 │
 ├── Voice Command
 │
 └── Text Command
        │
        ▼
Command Processing System
        │
        ▼
   ┌─────────────────────┐
   │   IRIS Assistant    │
   └─────────────────────┘
        │
        ├── Application Module
        ├── Browser Module
        ├── Search Module
        ├── Weather Module
        ├── Screenshot Module
        ├── Music Module
        ├── Reminder Module
        └── System Information Module
        │
        ▼
   Response Generation
        │
        ▼
 Text-to-Speech + GUI Output
```

---

# 📁 Project Structure

```text
DesktopAssistant/
│
├── main.py                    # Application entry point
├── config.py                  # Configuration and settings
├── requirements.txt           # Required Python packages
├── README.md                  # Project documentation
│
├── gui/
│   ├── __init__.py
│   └── interface.py           # CustomTkinter GUI
│
├── core/
│   ├── __init__.py
│   ├── assistant.py           # Main assistant controller
│   ├── commands.py            # Command processing
│   ├── speech.py              # Speech-to-text
│   └── voice.py               # Text-to-speech
│
├── modules/
│   ├── __init__.py
│   ├── apps.py                # Application launcher
│   ├── browser.py             # Website launcher
│   ├── search.py              # Google and Wikipedia search
│   ├── weather.py             # Weather information
│   ├── screenshot.py          # Screenshot functionality
│   ├── music.py               # Music control
│   ├── reminder.py            # Reminder system
│   ├── datetime_module.py     # Date and time
│   └── system.py              # System information
│
├── assets/
│   └── ...
│
└── screenshots/
    └── ...
```

---

# 🛠️ Technology Stack

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Main programming language |
| CustomTkinter     | Graphical User Interface  |
| SpeechRecognition | Voice command recognition |
| pyttsx3           | Text-to-speech            |
| Requests          | API communication         |
| Wikipedia         | Wikipedia search          |
| PyAutoGUI         | Screenshot automation     |
| Webbrowser        | Opening websites          |
| OS / Subprocess   | Application management    |
| Datetime          | Date and time operations  |
| Psutil            | System information        |
| Pygame            | Music functionality       |

---

# 📦 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/DesktopAssistant.git
```

Navigate to the project folder:

```bash
cd DesktopAssistant
```

---

## 2️⃣ Create a Virtual Environment (Recommended)

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

Or install the packages manually:

```bash
pip install customtkinter
pip install SpeechRecognition
pip install pyttsx3
pip install wikipedia
pip install requests
pip install pyautogui
pip install pillow
pip install pygame
pip install psutil
```

---

# ▶️ Running the Application

Run the following command from the project directory:

### macOS / Linux

```bash
python3 main.py
```

### Windows

```bash
python main.py
```

---

# 🗣️ Example Commands

| Command                           | Action                       |
| --------------------------------- | ---------------------------- |
| Open Chrome                       | Opens Google Chrome          |
| Open YouTube                      | Opens YouTube                |
| Search Python                     | Searches Google              |
| Wikipedia Artificial Intelligence | Searches Wikipedia           |
| What is the time?                 | Displays current time        |
| What is today's date?             | Displays current date        |
| Take a screenshot                 | Captures the screen          |
| Play music                        | Starts music                 |
| What's the weather?               | Displays weather information |
| Battery status                    | Displays battery information |
| Exit                              | Closes the assistant         |

---

# 🔑 API Configuration

Some features, such as weather information, require an API key.

Create or update the `config.py` file:

```python
WEATHER_API_KEY = "YOUR_API_KEY"
DEFAULT_CITY = "Mumbai"
```

> ⚠️ **Never upload your personal API keys directly to a public GitHub repository.**

For better security, environment variables can be used in future versions.

---

# 🧩 Development Phases

### ✅ Phase 1 — GUI Development

* CustomTkinter interface
* IRIS branding
* Status indicator
* Conversation area
* Functional GUI buttons

### 🔄 Phase 2 — Voice Recognition

* Microphone input
* Speech-to-text conversion
* Voice command detection

### 🔄 Phase 3 — Text-to-Speech

* Assistant voice responses
* pyttsx3 integration

### 🔄 Phase 4 — Application Automation

* Open desktop applications
* Application command processing

### 🔄 Phase 5 — Website Automation

* Open commonly used websites
* Browser integration

### 🔄 Phase 6 — Search Module

* Google Search
* Wikipedia Search

### 🔄 Phase 7 — Weather Integration

* Weather API
* Temperature and humidity information

### 🔄 Phase 8 — Screenshot and Music

* Screenshot capture
* Music functionality

### 🔄 Phase 9 — Reminder and System Information

* Reminder notifications
* Battery information
* CPU and RAM usage

### 🔄 Phase 10 — Final Integration

* Connect all modules
* Error handling
* Testing
* GUI improvements
* Documentation

---

# 🚀 Future Enhancements

Future versions of IRIS may include:

* 🤖 AI chatbot integration
* 🧠 Natural Language Processing
* 📧 Email automation
* 📅 Calendar integration
* 📄 PDF reading and summarization
* 📂 Smart file search
* 🏠 Smart home automation
* 🔐 Face recognition login
* ☁️ Cloud synchronization
* 🌙 Advanced theme customization

---

# 🧠 Concepts Demonstrated

This project demonstrates the practical use of:

* Python Programming
* Object-Oriented Programming
* Modular Programming
* GUI Development
* Speech Recognition
* Text-to-Speech
* API Integration
* Desktop Automation
* Error Handling
* File Handling
* Event-Driven Programming

---

# 🧪 Project Status

🚧 **Currently Under Development**

The project is being developed using a modular approach, where each feature is implemented and tested independently before final integration.

---

# 👩‍💻 Author

**Piyusha Ghadigaonkar**

Electronics and Computer Science Engineering Student

---

# 📄 License

This project is developed for **educational and academic purposes** as part of a Python Programming Mini Project.

---

⭐ If you found this project interesting, feel free to star the repository!

