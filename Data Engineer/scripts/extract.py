"""
Extract module.

Responsible for reading the raw CSV file
and returning it as a Pandas DataFrame.
"""

from pathlib import Path

import pandas as pd

from config.logger import logger


# Root project directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Dataset location
DATA_PATH = PROJECT_ROOT / "data" / "FMCG_2022_2024.csv"


def extract_data() -> pd.DataFrame:
    """
    Read source CSV file.

    Returns
    -------
    pd.DataFrame
        Raw dataset.
    """

    logger.info(f"Reading dataset: {DATA_PATH}")

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Source file not found:\n{DATA_PATH}"
        )

    df = pd.read_csv(DATA_PATH)

    logger.success(f"{len(df)} rows extracted.")

    return df