import logging
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv(".env")

class Settings(BaseSettings):
    # API
    APP_NAME: str = os.getenv("APP_NAME", "ChatBot-LangChain")
    APP_ENV: str = os.getenv("APP_ENV", "local")
    FAST_API_PORT: int = int(os.getenv("FAST_API_PORT", "8080"))
    FAST_API_HOST: str = os.getenv("FAST_API_HOST", "0.0.0.0")

    # Api Keys
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    GROQ_MODEL_NAME: str = os.getenv("GROQ_MODEL_NAME", "llama-3.3-70b-specdec")

    # Performance
    GUNICORN_WORKERS: int = int(os.getenv("GUNICORN_WORKERS", "2"))
    GUNICORN_THREADS: int = int(os.getenv("GUNICORN_THREADS", "6"))

settings = Settings()