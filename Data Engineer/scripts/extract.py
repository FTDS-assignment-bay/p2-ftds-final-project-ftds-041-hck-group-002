"""
Extract module.

Responsible for reading the raw CSV file and
returning it as a Pandas DataFrame.
"""

from pathlib import Path

import pandas as pd

from config.config import settings


def extract_data() -> pd.DataFrame:
    """
    Read source CSV file.

    Returns
    -------
    pd.DataFrame
        Raw dataset.
    """

    file_path = Path(settings.SOURCE_FILE)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Source file not found: {file_path}"
        )

    df = pd.read_csv(file_path)

    return df