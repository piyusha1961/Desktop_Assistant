"""
email_ops.py
------------
Handles sending emails using Gmail's SMTP server.

IMPORTANT SETUP STEP (do this before demoing):
Gmail does NOT allow your normal password to be used by outside code anymore.
You must generate an "App Password" instead:
    1. Turn on 2-Step Verification on your Google account.
    2. Go to https://myaccount.google.com/apppasswords
    3. Generate a 16-character app password.
    4. Put it in your .env file as EMAIL_APP_PASSWORD (see .env.example).
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import config


def send_email(to_address: str, subject: str, body: str) -> str:
    """
    Sends a plain-text email from the configured Gmail account to `to_address`.

    Returns a success or friendly error message (never raises/crashes).
    """
    if not config.EMAIL_ADDRESS or not config.EMAIL_APP_PASSWORD:
        return (
            "Email feature isn't set up yet. Add EMAIL_ADDRESS and "
            "EMAIL_APP_PASSWORD to your .env file (see README)."
        )

    try:
        msg = MIMEMultipart()
        msg["From"] = config.EMAIL_ADDRESS
        msg["To"] = to_address
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Gmail's SMTP server, using an encrypted (TLS) connection
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # upgrade the connection to be encrypted
            server.login(config.EMAIL_ADDRESS, config.EMAIL_APP_PASSWORD)
            server.send_message(msg)

        return f"Email sent successfully to {to_address}"

    except smtplib.SMTPAuthenticationError:
        return (
            "Email login failed. Double-check EMAIL_ADDRESS and "
            "EMAIL_APP_PASSWORD in your .env file — remember it must be an "
            "App Password, not your normal Gmail password."
        )
    except Exception as e:
        return f"Something went wrong sending the email: {e}"
