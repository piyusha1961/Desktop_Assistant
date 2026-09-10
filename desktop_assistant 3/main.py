"""
main.py
-------
This is the file you RUN to start the assistant: `python main.py`

It builds the GUI (a simple chat-style window) using customtkinter, and
wires up:
    - a text box for typed commands (always available, most reliable)
    - a "Speak" button for voice commands (uses modules/voice.py)
    - a chat-style display showing the conversation history
    - a separate small window for sending email (needs to/subject/body,
      which doesn't fit well into a single typed command)

The GUI itself contains NO logic about what commands mean — it just sends
whatever text it receives to assistant_core.process_command() and displays
whatever comes back. This keeps the GUI code simple and swappable.
"""

import threading
import customtkinter as ctk

import assistant_core
from modules import voice, email_ops
import config

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AssistantApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(config.APP_NAME)
        self.geometry("500x650")
        self.minsize(420, 500)

        self._build_widgets()
        self._display_message("Assistant", "Hi! Type a command below, or click Speak. "
                                             "Try: 'what's the time', 'open notepad', "
                                             "'weather', 'wikipedia python'.")

    def _build_widgets(self):
        # --- Chat history display (read-only text box) ---
        self.chat_box = ctk.CTkTextbox(self, width=460, height=460, wrap="word")
        self.chat_box.pack(padx=15, pady=(15, 5), fill="both", expand=True)
        self.chat_box.configure(state="disabled")  # user shouldn't type directly into history

        # --- Status label (shows "Listening...", "Thinking...", etc.) ---
        self.status_label = ctk.CTkLabel(self, text="Ready", text_color="gray")
        self.status_label.pack(pady=(0, 5))

        # --- Bottom input row: text entry + Send + Speak buttons ---
        input_frame = ctk.CTkFrame(self, fg_color="transparent")
        input_frame.pack(padx=15, pady=(0, 10), fill="x")

        self.entry = ctk.CTkEntry(input_frame, placeholder_text="Type a command...")
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 8))
        self.entry.bind("<Return>", lambda event: self._handle_text_command())

        send_btn = ctk.CTkButton(input_frame, text="Send", width=70, command=self._handle_text_command)
        send_btn.pack(side="left", padx=(0, 8))

        speak_btn = ctk.CTkButton(input_frame, text="🎙 Speak", width=90, command=self._handle_voice_command)
        speak_btn.pack(side="left")

        # --- Extra action row: quick buttons for less "typeable" features ---
        action_frame = ctk.CTkFrame(self, fg_color="transparent")
        action_frame.pack(padx=15, pady=(0, 15), fill="x")

        email_btn = ctk.CTkButton(action_frame, text="✉ Send Email", command=self._open_email_dialog)
        email_btn.pack(side="left", padx=(0, 8))

        screenshot_btn = ctk.CTkButton(
            action_frame, text="📷 Screenshot",
            command=lambda: self._run_command("screenshot")
        )
        screenshot_btn.pack(side="left")

    # ---------- Core interaction handlers ----------

    def _display_message(self, sender: str, message: str):
        """Adds a line to the chat history box."""
        self.chat_box.configure(state="normal")
        self.chat_box.insert("end", f"{sender}: {message}\n\n")
        self.chat_box.configure(state="disabled")
        self.chat_box.see("end")  # auto-scroll to latest message

    def _run_command(self, command_text: str):
        """
        Shared logic: display the user's command, run it through the
        assistant's brain, display + speak the response.
        Runs in a background thread so the GUI never freezes while
        waiting on an API call.
        """
        self._display_message("You", command_text)
        self.status_label.configure(text="Thinking...")

        def worker():
            response = assistant_core.process_command(command_text)
            # Schedule GUI updates back on the main thread
            self.after(0, lambda: self._display_message("Assistant", response))
            self.after(0, lambda: self.status_label.configure(text="Ready"))
            voice.speak(response)

        threading.Thread(target=worker, daemon=True).start()

    def _handle_text_command(self):
        text = self.entry.get()
        if not text.strip():
            return
        self.entry.delete(0, "end")
        self._run_command(text)

    def _handle_voice_command(self):
        self.status_label.configure(text="Listening...")

        def worker():
            heard_text = voice.listen()
            if not heard_text:
                self.after(0, lambda: self.status_label.configure(text="Ready"))
                self.after(0, lambda: self._display_message(
                    "Assistant", "I couldn't hear anything clearly. Please try again or type instead."
                ))
                return
            self.after(0, lambda: self._run_command(heard_text))

        threading.Thread(target=worker, daemon=True).start()

    # ---------- Email dialog (separate small popup window) ----------

    def _open_email_dialog(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Send Email")
        dialog.geometry("380x320")
        dialog.grab_set()  # makes this popup modal (blocks main window until closed)

        ctk.CTkLabel(dialog, text="To:").pack(anchor="w", padx=15, pady=(15, 0))
        to_entry = ctk.CTkEntry(dialog, placeholder_text="recipient@example.com")
        to_entry.pack(padx=15, fill="x")

        ctk.CTkLabel(dialog, text="Subject:").pack(anchor="w", padx=15, pady=(10, 0))
        subject_entry = ctk.CTkEntry(dialog, placeholder_text="Subject")
        subject_entry.pack(padx=15, fill="x")

        ctk.CTkLabel(dialog, text="Message:").pack(anchor="w", padx=15, pady=(10, 0))
        body_box = ctk.CTkTextbox(dialog, height=120)
        body_box.pack(padx=15, pady=(0, 10), fill="both", expand=True)

        result_label = ctk.CTkLabel(dialog, text="", text_color="gray")
        result_label.pack(pady=(0, 5))

        def on_send():
            to_addr = to_entry.get().strip()
            subject = subject_entry.get().strip()
            body = body_box.get("1.0", "end").strip()

            if not to_addr or not subject or not body:
                result_label.configure(text="Please fill in all fields.", text_color="red")
                return

            result_label.configure(text="Sending...", text_color="gray")

            def worker():
                result = email_ops.send_email(to_addr, subject, body)
                dialog.after(0, lambda: result_label.configure(text=result, text_color="lightgreen"))
                dialog.after(0, lambda: self._display_message("Assistant", result))

            threading.Thread(target=worker, daemon=True).start()

        send_btn = ctk.CTkButton(dialog, text="Send", command=on_send)
        send_btn.pack(pady=(0, 15))


if __name__ == "__main__":
    app = AssistantApp()
    app.mainloop()
