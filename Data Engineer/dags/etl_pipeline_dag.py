"""
Airflow DAG for ETL Pipeline.
"""

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from scripts.airflow_tasks import (
    task_extract_load_raw,
    task_validate,
    task_analytics_pipeline,
)

default_args = {
    "owner": "ForecastLab",
    "depends_on_past": False,
    "retries": 1,
}

with DAG(
    dag_id="etl_pipeline",
    description="Daily ETL Pipeline for FMCG Sales Forecasting",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["forecastlab", "etl"],
) as dag:

    extract_load_raw = PythonOperator(
        task_id="extract_load_raw",
        python_callable=task_extract_load_raw,
    )

    validate = PythonOperator(
        task_id="validate",
        python_callable=task_validate,
    )

    analytics_pipeline = PythonOperator(
        task_id="analytics_pipeline",
        python_callable=task_analytics_pipeline,
    )

    extract_load_raw >> validate >> analytics_pipeline