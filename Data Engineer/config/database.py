"""
Database connection module.

Create a reusable SQLAlchemy Engine.
"""

import pandas as pd

from sqlalchemy import create_engine, text

from config.config import settings


def get_database_url() -> str:
    """
    Build PostgreSQL connection URL.
    """

    return (
        f"postgresql+psycopg2://"
        f"{settings.DB_USER}:"
        f"{settings.DB_PASSWORD}@"
        f"{settings.DB_HOST}:"
        f"{settings.DB_PORT}/"
        f"{settings.DB_NAME}"
    )


DATABASE_URL = get_database_url()


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)


def execute_query(query: str) -> None:
    """
    Execute SQL query (CREATE, INSERT, UPDATE, DELETE).
    """

    with engine.begin() as conn:
        conn.execute(text(query))


def read_table(query: str) -> pd.DataFrame:
    """
    Read data from PostgreSQL into a Pandas DataFrame.

    Parameters
    ----------
    query : str
        SQL SELECT query.

    Returns
    -------
    pd.DataFrame
    """

    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)

    return df