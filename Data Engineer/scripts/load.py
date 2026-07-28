"""
Load module.

Responsible for loading and reading Pandas DataFrame
from PostgreSQL.
"""

import pandas as pd

from sqlalchemy.exc import SQLAlchemyError

from config.database import engine
from config.logger import logger


def load_dataframe(
    dataframe,
    schema: str,
    table: str,
    if_exists: str = "append",
    chunksize: int = 5000,
) -> None:
    """
    Load DataFrame into PostgreSQL.
    """

    logger.info(f"Loading dataframe to {schema}.{table}")

    try:

        dataframe.to_sql(
            name=table,
            schema=schema,
            con=engine,
            if_exists=if_exists,
            index=False,
            chunksize=chunksize,
            method="multi",
        )

        logger.success(
            f"{len(dataframe)} rows loaded into {schema}.{table}"
        )

    except SQLAlchemyError as e:

        logger.exception(e)

        raise


def read_dataframe(schema: str, table: str) -> pd.DataFrame:
    """
    Read PostgreSQL table into Pandas DataFrame.

    Parameters
    ----------
    schema : str
        Database schema.
    table : str
        Table name.

    Returns
    -------
    pd.DataFrame
    """

    logger.info(f"Reading data from {schema}.{table}")

    query = f"SELECT * FROM {schema}.{table}"

    try:

        dataframe = pd.read_sql(query, engine)

        logger.success(
            f"{len(dataframe)} rows read from {schema}.{table}"
        )

        return dataframe

    except Exception as e:

        logger.exception(e)

        raise