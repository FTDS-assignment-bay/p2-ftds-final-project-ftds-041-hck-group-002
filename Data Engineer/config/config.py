"""
Application configuration module.

Load environment variables from .env and expose
them through a single settings object.
"""

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv

# Root directory (Data Engineer/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env
load_dotenv(BASE_DIR / ".env")


@dataclass(frozen=True)
class Settings:
    """Application settings."""

    # Database
    DB_HOST: str = os.getenv("DB_HOST", "")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_NAME: str = os.getenv("DB_NAME", "")
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")

    # Schemas
    SCHEMA_RAW: str = os.getenv("SCHEMA_RAW", "raw")
    SCHEMA_STAGING: str = os.getenv("SCHEMA_STAGING", "staging")
    SCHEMA_ANALYTICS: str = os.getenv("SCHEMA_ANALYTICS", "analytics")

    # ETL
    SOURCE_FILE: str = os.getenv("SOURCE_FILE", "data/FMCG_2022_2024.csv")
    OUTPUT_FOLDER: str = os.getenv("OUTPUT_FOLDER", "output/")
    LOG_FOLDER: str = os.getenv("LOG_FOLDER", "logs/")


settings = Settings()