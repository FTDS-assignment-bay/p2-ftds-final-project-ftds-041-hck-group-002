"""
Transformation module.

Responsible for creating general business features.
"""

import pandas as pd

from config.logger import logger


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create business features.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """

    logger.info("Starting feature engineering...")

    # -----------------------------
    # Date Features
    # -----------------------------
    df["year"] = df["date"].dt.year

    df["month"] = df["date"].dt.month

    df["quarter"] = df["date"].dt.quarter

    df["week_of_year"] = (
        df["date"]
        .dt
        .isocalendar()
        .week
        .astype(int)
    )

    df["day_of_week"] = df["date"].dt.day_name()

    # -----------------------------
    # Weekend Flag
    # -----------------------------
    df["weekend_flag"] = (
        df["date"]
        .dt
        .dayofweek
        .isin([5, 6])
        .astype(int)
    )

    # -----------------------------
    # Revenue
    # -----------------------------
    df["revenue"] = (
        df["units_sold"] *
        df["price_unit"]
    ).round(2)

    logger.success("Feature engineering completed.")

    return df