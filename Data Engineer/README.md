# 📊 ForecastLab - Data Engineering Pipeline

> ETL Pipeline for FMCG Sales Forecasting

This repository contains the **Data Engineering** component of the ForecastLab Final Project. The pipeline automates the extraction, validation, cleaning, transformation, loading, and exporting of FMCG sales data using **Apache Airflow**, **Docker**, and **Supabase PostgreSQL**.

---

# 🚀 Project Overview

The goal of this project is to build a robust ETL pipeline that prepares historical FMCG sales data for downstream analytics and forecasting.

The processed dataset will be consumed by:

- 📈 Data Analyst
- 🤖 Data Scientist

---

# 🏗️ Architecture

```text
                    FMCG_2022_2024.csv
                             │
                             ▼
                     Extract Module
                             │
                             ▼
                  raw.sales (Supabase)
                             │
                             ▼
                    Validation Module
                             │
                             ▼
                      Cleaning Module
                             │
                             ▼
                Feature Engineering Module
                             │
                             ▼
               analytics.sales (Supabase)
                     │                 │
                     ▼                 ▼
      forecasting_dataset.csv     Airflow DAG
```

---

# ⚙️ ETL Workflow

The pipeline consists of three Airflow tasks.

## 1️⃣ Extract + Load Raw

- Read raw CSV dataset
- Load into `raw.sales`

---

## 2️⃣ Validate

Perform data quality checks:

- Missing values
- Duplicate rows
- Promotion flag validation
- Negative values
- Delivery days validation

---

## 3️⃣ Analytics Pipeline

Process raw data into analytics-ready data.

Includes:

- Data Cleaning
- Data Transformation
- Feature Engineering
- Load into `analytics.sales`
- Export CSV

---

# 📂 Project Structure

```text
Data Engineer
│
├── config/
│   ├── config.py
│   ├── database.py
│   └── logger.py
│
├── dags/
│   └── etl_pipeline_dag.py
│
├── data/
│   └── FMCG_2022_2024.csv
│
├── logs/
│
├── output/
│   └── forecasting_dataset.csv
│
├── scripts/
│   ├── airflow_tasks.py
│   ├── clean.py
│   ├── export.py
│   ├── extract.py
│   ├── load.py
│   ├── transform.py
│   ├── validate.py
│   └── etl_pipeline.py
│
├── sql/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

# 🛠️ Technologies

- Python 3.12
- Pandas
- SQLAlchemy
- PostgreSQL
- Supabase
- Apache Airflow
- Docker
- Loguru

---

# 🗄️ Database Architecture

```
Supabase PostgreSQL

├── raw
│      └── sales
│
└── analytics
       └── sales
```

---

# 📦 Pipeline Output

The pipeline produces:

### Database

```
raw.sales
analytics.sales
```

### CSV

```
output/
└── forecasting_dataset.csv
```

---

# 📋 Data Validation

Validation performed during the ETL process:

- Missing values
- Duplicate records
- Promotion flag validation
- Negative stock validation
- Negative delivered quantity validation
- Negative units sold validation
- Delivery days validation

---

# 🧹 Data Cleaning

Cleaning steps include:

- Convert date column to datetime
- Trim whitespace from string columns
- Handle negative values
- Standardize text columns

---

# ⚡ Feature Engineering

Several additional features are generated to support forecasting and analytics.

Examples include:

- Revenue calculation
- Time-based features
- Sales performance indicators

---

# 🐳 Running with Docker

Build image

```bash
docker compose build
```

Start services

```bash
docker compose up -d
```

Stop services

```bash
docker compose down
```

---

# 🌬️ Apache Airflow

Open Airflow

```
http://localhost:8080
```

Default credentials

```
Username : admin
Password : admin
```

Pipeline schedule

```
@daily
```

---

# ▶️ Run Pipeline Manually

Trigger the DAG from the Airflow UI.

Or execute locally

```bash
python main.py
```

---

# 📊 ETL Flow

```text
Extract
    │
    ▼
Load Raw
    │
    ▼
Validate
    │
    ▼
Clean
    │
    ▼
Transform
    │
    ▼
Load Analytics
    │
    ▼
Export Dataset
```

---

# 👥 Team

ForecastLab

Final Project — Data Science & AI

Hacktiv8 FTDS Batch 041

---

# 📄 License

This project was developed for educational purposes as part of the Hacktiv8 Final Project.