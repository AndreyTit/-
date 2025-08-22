import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

TOKEN = os.getenv("BOT_TOKEN")
RECIPES_PATH = os.getenv("RECIPES_PATH")
EXTRAS_PATH = os.getenv("EXTRAS_PATH")  # Добавлено
