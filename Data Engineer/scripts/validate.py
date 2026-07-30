"""
Validation module.

Responsible for validating extracted data before cleaning.
"""

from typing import Dict, Tuple

import pandas as pd

from config.logger import logger


def validate_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict]:
    """
    Validate dataset before cleaning.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset.

    Returns
    -------
    Tuple[pd.DataFrame, Dict]
        Original DataFrame and validation summary.
    """

    logger.info("Starting data validation...")

    # Missing Values
    missing = df.isnull().sum().sum()

    if missing > 0:
        logger.warning(f"Missing values found: {missing}")
    else:
        logger.info("No missing values found.")

    # Duplicate Rows
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        logger.warning(f"Duplicate rows found: {duplicates}")
    else:
        logger.info("No duplicate rows found.")

    # Promotion Flag Validation
    valid_flag = set(df["promotion_flag"].unique())

    promotion_flag_valid = valid_flag.issubset({0, 1})

    if promotion_flag_valid:
        logger.info("Promotion flag is valid.")
    else:
        logger.warning("Promotion flag contains invalid values.")

    # Negative Value Validation
    negative_stock = (df["stock_available"] < 0).sum()
    negative_delivered = (df["delivered_qty"] < 0).sum()
    negative_units = (df["units_sold"] < 0).sum()
    negative_delivery_days = (df["delivery_days"] < 0).sum()

    negative_checks = {
        "stock_available": negative_stock,
        "delivered_qty": negative_delivered,
        "units_sold": negative_units,
        "delivery_days": negative_delivery_days,
    }

    for column, count in negative_checks.items():

        if count > 0:
            logger.warning(f"{column} contains {count} negative values.")
        else:
            logger.info(f"{column} validation passed.")

    validation_result = {
        "missing_values": missing,
        "duplicates": duplicates,
        "negative_stock": negative_stock,
        "negative_delivered_qty": negative_delivered,
        "negative_units_sold": negative_units,
        "negative_delivery_days": negative_delivery_days,
        "promotion_flag_valid": promotion_flag_valid,
    }

    logger.success("Validation completed.")

    return df, validation_result