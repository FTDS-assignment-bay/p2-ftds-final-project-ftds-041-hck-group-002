"""
Export module.

Responsible for exporting analytics data into CSV.
"""

from pathlib import Path

from config.database import read_table
from config.logger import logger


def export_dataset(
    output_path: str = "output/forecasting_dataset.csv",
) -> None:
    """
    Export analytics.sales into CSV.

    Parameters
    ----------
    output_path : str
        Destination CSV file.
    """

    logger.info("Exporting analytics dataset...")

    query = """
        SELECT *
        FROM analytics.sales
        ORDER BY date, sku;
    """

    df = read_table(query)

    output_file = Path(output_path)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_file, index=False)

    logger.success(f"{len(df)} rows exported.")

    logger.success(f"Dataset saved to {output_file}")