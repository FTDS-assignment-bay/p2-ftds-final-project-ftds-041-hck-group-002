"""
Cleaning module.

Responsible for cleaning validated data.
"""

import pandas as pd

from config.logger import logger


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean validated dataset.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """

    logger.info("Starting data cleaning...")

    # -----------------------------
    # Convert Date
    # -----------------------------
    df["date"] = pd.to_datetime(df["date"])

    logger.info("Date converted to datetime.")

    # -----------------------------
    # Remove Leading / Trailing Spaces
    # -----------------------------
    object_columns = df.select_dtypes(include="object").columns

    for col in object_columns:
        df[col] = df[col].str.strip()

    logger.info("String columns cleaned.")

    # -----------------------------
    # Replace Negative Values with 0
    # -----------------------------
    numeric_columns = [
        "delivery_days",
        "stock_available",
        "delivered_qty",
        "units_sold",
    ]

    for col in numeric_columns:

        negative_count = (df[col] < 0).sum()

        if negative_count > 0:

            df.loc[df[col] < 0, col] = 0

            logger.info(
                f"{negative_count} negative values fixed in '{col}'."
            )

    logger.success("Data cleaning completed.")

    return df