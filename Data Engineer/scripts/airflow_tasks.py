"""
Airflow task module.

Contains task wrappers used by Airflow.
"""

from config.logger import logger

from scripts.extract import extract_data
from scripts.validate import validate_data
from scripts.clean import clean_data
from scripts.transform import transform_data
from scripts.load import load_dataframe, read_dataframe
from scripts.export import export_dataset


def task_extract_load_raw():
    """
    Extract CSV then load into raw schema.
    """

    logger.info("Airflow : Extract + Load Raw")

    df = extract_data()

    load_dataframe(
        dataframe=df,
        schema="raw",
        table="sales",
        if_exists="replace",
    )


def task_validate():
    """
    Validate raw dataset.
    """

    logger.info("Airflow : Validate")

    df = read_dataframe(
        schema="raw",
        table="sales",
    )

    validate_data(df)


def task_analytics_pipeline():
    """
    Clean → Transform → Load Analytics → Export
    """

    logger.info("Airflow : Analytics Pipeline")

    df = read_dataframe(
        schema="raw",
        table="sales",
    )

    df = clean_data(df)

    df = transform_data(df)

    load_dataframe(
        dataframe=df,
        schema="analytics",
        table="sales",
        if_exists="replace",
    )

    export_dataset()