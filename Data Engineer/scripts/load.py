"""
Load module.

Responsible for loading a Pandas DataFrame into PostgreSQL.
"""

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

    Parameters
    ----------
    dataframe : pd.DataFrame
        DataFrame to load.
    schema : str
        Target schema.
    table : str
        Target table.
    if_exists : str
        append / replace / fail
    chunksize : int
        Number of rows per batch.
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