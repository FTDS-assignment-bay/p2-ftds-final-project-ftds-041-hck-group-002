"""
Application logger configuration.
"""

from pathlib import Path
from loguru import logger

from config.config import settings

# Pastikan folder log ada
log_path = Path(settings.LOG_FOLDER)
log_path.mkdir(parents=True, exist_ok=True)

# Hapus logger bawaan
logger.remove()

# Tampilkan log di terminal
logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
    colorize=True,
)

# Simpan log ke file
logger.add(
    log_path / "etl.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level="INFO",
)

__all__ = ["logger"]