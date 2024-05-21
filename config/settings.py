# config/settings.py

import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    TARGET_CHAT_ID = os.getenv("TARGET_CHAT_ID")

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GOOGLE_GENERATIVE_MODULE = os.getenv("GOOGLE_GENERATIVE_MODULE")
    GOOGLE_PROMPT_COMMAND = os.getenv("GOOGLE_PROMPT_COMMAND")

    SUMMARY_API_URL = os.getenv("SUMMARY_API_URL")
    SUMMARY_API_KEY = os.getenv("SUMMARY_API_KEY")
    SUMMARY_API_HOST = os.getenv("SUMMARY_API_HOST")
