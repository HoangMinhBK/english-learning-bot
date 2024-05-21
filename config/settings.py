# config/settings.py

import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    TARGET_CHAT_ID = os.getenv("TARGET_CHAT_ID")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
