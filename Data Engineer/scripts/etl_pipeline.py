"""
Pipeline module.

Responsible for orchestrating the ETL workflow.
"""

from config.logger import logger

from scripts.clean import clean_data
from scripts.export import export_dataset
from scripts.extract import extract_data
from scripts.load import load_dataframe
from scripts.transform import transform_data
from scripts.validate import validate_data


def run_extract():
    """Extract data from source."""
    logger.info("Step 1/7 : Extract")
    return extract_data()


def run_load_raw(df):
    """Load raw data into PostgreSQL."""
    logger.info("Step 2/7 : Load Raw")

    load_dataframe(
        dataframe=df,
        schema="raw",
        table="sales",
        if_exists="replace"
    )


def run_validate(df):
    """Validate extracted data."""
    logger.info("Step 3/7 : Validate")

    df, validation = validate_data(df)

    logger.info(f"Validation Summary: {validation}")

    return df


def run_clean(df):
    """Clean dataset."""
    logger.info("Step 4/7 : Clean")
    return clean_data(df)


def run_transform(df):
    """Feature engineering."""
    logger.info("Step 5/7 : Transform")
    return transform_data(df)


def run_load_analytics(df):
    """Load transformed data into analytics schema."""
    logger.info("Step 6/7 : Load Analytics")

    load_dataframe(
        dataframe=df,
        schema="analytics",
        table="sales",
        if_exists="replace"
    )


def run_export():
    """Export analytics dataset."""
    logger.info("Step 7/7 : Export")
    export_dataset()


def run_pipeline():
    """Run complete ETL pipeline."""

    logger.info("=" * 60)
    logger.info("START ETL PIPELINE")
    logger.info("=" * 60)

    df = run_extract()

    run_load_raw(df)

    df = run_validate(df)

    df = run_clean(df)

    df = run_transform(df)

    run_load_analytics(df)

    run_export()

    logger.success("=" * 60)
    logger.success("ETL PIPELINE FINISHED")
    logger.success("=" * 60)