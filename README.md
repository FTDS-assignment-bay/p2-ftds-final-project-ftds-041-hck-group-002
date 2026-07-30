# 📦 ForecastLab — FMCG Inventory Forecasting & Analytics

> **End-to-end Data Engineering, Data Analytics, and Machine Learning project for FMCG inventory planning**

ForecastLab adalah project **Data Science & AI** yang bertujuan membantu perusahaan **Fast-Moving Consumer Goods (FMCG)** mengoptimalkan inventory dengan memanfaatkan data historis penjualan, inventory, promosi, harga, dan karakteristik order.

Project ini mengintegrasikan tiga komponen utama:

- **Data Engineering** — membangun pipeline ETL yang reliable dan otomatis untuk menyiapkan data.
- **Data Analytics** — memahami kondisi bisnis, menemukan pola inventory, serta mengidentifikasi risiko overstock dan stockout.
- **Data Science** — membangun dan mengevaluasi model forecasting untuk mendukung demand, revenue, dan weekly aggregate demand planning.

Tujuan akhirnya adalah menghasilkan **data yang siap digunakan, insight bisnis yang actionable, serta model forecasting yang dapat mendukung keputusan supply chain dan inventory planning.**

---

## 🎯 Business Problem

Perusahaan FMCG menghadapi dua permasalahan inventory yang saling berlawanan:

### 1. Overstock / Inventory Waste
Stok terlalu tinggi dapat menyebabkan:

- modal kerja tertahan,
- biaya penyimpanan meningkat,
- inventory menjadi idle,
- risiko waste meningkat.

### 2. Stockout
Stok terlalu rendah dapat menyebabkan:

- kehilangan peluang penjualan,
- revenue yang hilang,
- customer demand tidak terpenuhi,
- kebutuhan restock yang bersifat mendadak.

ForecastLab dibangun untuk membantu perusahaan melakukan **perencanaan inventory yang lebih proaktif**, dengan memanfaatkan data historis untuk memahami demand dan menentukan kebutuhan restock.

### 🎯 Business Target

> **Menurunkan inventory waste sebesar 50%.**

---

# 🏗️ End-to-End Project Architecture

Secara keseluruhan, project berjalan melalui alur berikut:

```text
                       FMCG_2022_2024.csv
                                │
                                ▼
                    ┌─────────────────────┐
                    │   DATA ENGINEERING  │
                    │                     │
                    │ Extract & Load Raw  │
                    │ Validation          │
                    │ Cleaning            │
                    │ Transformation      │
                    │ Feature Engineering │
                    └──────────┬──────────┘
                               │
                               ▼
                     Supabase PostgreSQL
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
              raw.sales             analytics.sales
                                          │
                                          ▼
                               forecasting_dataset.csv
                                          │
                         ┌────────────────┴────────────────┐
                         │                                 │
                         ▼                                 ▼
                 DATA ANALYTICS                     DATA SCIENCE
                         │                                 │
                 EDA & Business                  Target Evaluation
                    Analysis                     Feature Engineering
                         │                        Model Training
                         ▼                        Model Evaluation
                Inventory Insights                       │
                Stockout Analysis                         ▼
                Restock Risk Analysis              Forecasting Models
                         │                                 │
                         └────────────────┬────────────────┘
                                          │
                                          ▼
                                BUSINESS DECISION
                                          │
                                          ▼
                            Inventory & Supply Planning
```

---

# 📊 Dataset

Dataset yang digunakan adalah **FMCG Daily Sales Data 2022–2024**.

| Information | Detail |
|---|---|
| Dataset | `FMCG_2022_2024.csv` / `forecasting_dataset.csv` |
| Records | 190,757 rows |
| Columns | 21 columns |
| Period | January 2022 – December 2024 |
| SKU | 30 SKU |
| Category | 5 categories |
| Channel | 3 channels |
| Region | 3 regions |
| Granularity | SKU × Channel × Region × Pack Type |

### Product Categories

- Milk
- Yogurt
- Juice
- ReadyMeal
- SnackBar

### Sales Channels

- Retail
- Discount
- E-commerce

### Regions

- PL-Central
- PL-North
- PL-South

Data yang digunakan untuk analytics dan forecasting memiliki beberapa field penting seperti:

```text
price_unit
promotion_flag
delivery_days
stock_available
delivered_qty
units_sold
revenue
month
quarter
week_of_year
day_of_week
weekend_flag
```

---

# ⚙️ Data Engineering

Data Engineering bertanggung jawab menyediakan data yang **clean, validated, transformed, dan siap digunakan** oleh Data Analyst dan Data Scientist.

## ETL Pipeline

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

### 1. Extract & Load

Raw FMCG CSV dibaca dan dimasukkan ke database:

```text
Supabase PostgreSQL
│
├── raw
│    └── sales
│
└── analytics
     └── sales
```

### 2. Validation

Pipeline melakukan validasi terhadap:

- Missing values
- Duplicate records
- Promotion flag
- Negative stock
- Negative delivered quantity
- Negative units sold
- Delivery days

### 3. Cleaning

Data kemudian dibersihkan melalui:

- konversi date menjadi datetime,
- trimming whitespace pada string,
- penanganan nilai negatif,
- standardisasi text columns.

### 4. Transformation & Feature Engineering

Pipeline menghasilkan data yang lebih siap digunakan untuk analytics dan forecasting, termasuk:

- revenue calculation,
- time-based features,
- sales performance indicators.

### 5. Output

Pipeline menghasilkan:

```text
raw.sales
analytics.sales
output/
└── forecasting_dataset.csv
```

---

# 🔎 Data Analytics

Data Analyst bertugas menerjemahkan data menjadi **business insight** yang dapat digunakan untuk pengambilan keputusan inventory.

## Business Analysis

Analisis berfokus pada dua risiko utama:

```text
                 INVENTORY
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       Overstock             Stockout
          │                     │
          ▼                     ▼
    Inventory Waste        Lost Revenue
```

## Key Metrics

| Metric | Result |
|---|---:|
| Total Revenue (2022–2024) | $19.95 million |
| Stockout Rate | 2.03% |
| Estimated Lost Revenue | ~$414K |
| Average Idle Stock / Day | $128K |
| Critical Restock Combinations | 11 |
| High-Risk Restock Combinations | 24 |
| Total SKU × Channel × Region combinations | 270 |

## Restock Risk Analysis

Salah satu pendekatan utama adalah **Days of Stock Remaining (DSR)**:

```text
DSR = Available Stock / Average Daily Sales (last 30 days)
```

DSR digunakan untuk mengidentifikasi kombinasi SKU × Channel × Region yang memiliki risiko restock.

Hasil analisis kemudian digunakan untuk memberikan insight mengenai:

- inventory yang berisiko habis,
- inventory yang berpotensi idle,
- prioritas restock,
- potensi kehilangan revenue,
- pola penjualan dan inventory.

---

# 🤖 Data Science & Forecasting

Data Scientist membangun model forecasting berdasarkan dataset hasil preprocessing.

Sebelum membangun model final, beberapa kandidat target diuji secara **data-driven** untuk menentukan target yang memiliki sinyal prediktif yang cukup.

## Target Evaluation

| Target | Result | Decision |
|---|---:|---|
| `units_sold` per order | R² = 0.34 | ✅ Model 1 |
| `revenue` per order | R² = 0.54 | ✅ Model 2 |
| Weekly total demand per category | R² = 0.95 | ✅ Model 3 |
| `delivery_days` | R² ≈ 0.00 | ❌ Rejected |
| Stockout classification | ROC-AUC ≈ 0.49 | ❌ Rejected |

Target `delivery_days` dan stockout classification tidak dilanjutkan karena fitur yang tersedia tidak memberikan sinyal prediktif yang memadai.

---

# 📈 Forecasting Models

ForecastLab menghasilkan tiga model forecasting utama.

| Model | Target | Best Algorithm | R² | MAE | Primary User |
|---|---|---|---:|---:|---|
| Model 1 | `units_sold` order-level | Gradient Boosting | 0.339 | ≈ 6.0 units | Supply Chain / Warehouse |
| Model 2 | `revenue` order-level | Gradient Boosting | 0.544 | ≈ 31.5 | Finance / Commercial |
| Model 3 | Weekly demand per category | Gradient Boosting | 0.946 | ≈ 6.6% of average | Category / Supply Planning |

Ketiga model dibandingkan dengan baseline:

- Linear Regression
- Random Forest
- Gradient Boosting

Gradient Boosting dipilih sebagai model final berdasarkan hasil evaluasi.

---

# 🧠 Forecasting Methodology

## Time-Based Train/Test Split

Karena data merupakan time series, pembagian data dilakukan berdasarkan waktu:

```text
Historical Data
│
├────────────── 80% ──────────────┤── 20% ──┤
│             TRAIN               │  TEST   │
│                                 │         │
└──────────── Past ───────────────┴─ Future ┘
```

Pendekatan ini digunakan agar data masa depan tidak digunakan untuk melatih model.

## Lag & Rolling Features

Historical features dibuat menggunakan pola:

```python
.shift(1)
```

sebelum:

```python
.rolling()
```

Hal ini dilakukan untuk mencegah **data leakage**, sehingga informasi pada periode saat ini tidak secara tidak sengaja digunakan untuk memprediksi periode yang sama.

## Revenue Forecasting & Leakage

Model Revenue Forecasting tidak menggunakan `units_sold` sebagai feature.

Alasannya:

```text
revenue = price_unit × units_sold
```

Jika `units_sold` digunakan sebagai feature untuk memprediksi revenue, model akan memperoleh informasi target secara langsung dan menyebabkan **data leakage**.

---

# 📦 Business Application

Output forecasting dapat digunakan sebagai dasar untuk mendukung:

- demand planning,
- inventory planning,
- procurement planning,
- supply chain planning,
- revenue planning,
- safety stock calculation,
- reorder point calculation.

Notebook forecasting juga menghasilkan perhitungan:

```text
Safety Stock
       +
Reorder Point
       │
       ▼
Inventory Planning
```

Dengan demikian, forecasting tidak hanya berhenti pada prediksi, tetapi dapat diterjemahkan menjadi **business decision support**.

---

# 📁 Project Outputs

Data Engineering menghasilkan:

```text
raw.sales
analytics.sales
forecasting_dataset.csv
```

Data Science menghasilkan:

```text
model1_demand_forecasting.pkl
model1_feature_columns.pkl

model2_revenue_forecasting.pkl
model2_feature_columns.pkl

model3_weekly_demand_forecasting.pkl
model3_feature_columns.pkl

safety_stock_reorder_point.csv
model_comparison_summary.csv
```

Data Analytics menghasilkan:

```text
BUSINESS_INSIGHT_SUMMARY.md
EDA notebooks
EDA metadata
Visualizations
Stakeholder presentation
Tableau dashboard
```

---

# 🗂️ Project Structure

Secara keseluruhan, project terdiri dari tiga area utama:

```text
ForecastLab
│
├── Data Engineering
│   ├── config/
│   ├── dags/
│   ├── data/
│   ├── scripts/
│   ├── sql/
│   ├── tests/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── requirements.txt
│
├── Data Analytics
│   ├── notebooks/
│   ├── reports/
│   ├── visuals/
│   ├── presentation/
│   ├── dashboard/
│   └── BUSINESS_INSIGHT_SUMMARY.md
│
└── Data Science
    ├── FMCG_3_Best_Forecasting_Models.ipynb
    ├── forecasting_dataset.csv
    ├── model*.pkl
    ├── safety_stock_reorder_point.csv
    └── model_comparison_summary.csv
```

---

# 🛠️ Technology Stack

## Data Engineering

- Python 3.12
- Pandas
- SQLAlchemy
- PostgreSQL
- Supabase
- Apache Airflow
- Docker
- Loguru

## Data Analytics

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Tableau Public

## Data Science

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Jupyter Notebook

---

# 🚀 How to Run

## 1. Data Engineering

Build Docker image:

```bash
docker compose build
```

Start services:

```bash
docker compose up -d
```

Stop services:

```bash
docker compose down
```

Open Airflow:

```text
http://localhost:8080
```

Pipeline schedule:

```text
@daily
```

Trigger the DAG through the Airflow UI or execute the pipeline locally:

```bash
python main.py
```

---

## 2. Data Science

Install required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib jupyter
```

Run the forecasting notebook:

```bash
jupyter notebook FMCG_3_Best_Forecasting_Models.ipynb
```

Then execute the notebook from the first cell to the last cell.

Make sure:

```text
forecasting_dataset.csv
```

is available in the same directory as the notebook.

---

# 📊 Dashboard & Presentation

Business insights are presented through:

- EDA visualizations
- Stakeholder presentation
- Tableau dashboard

The Tableau dashboard provides an interactive view of the business analysis and inventory-related insights.

---

# ⚠️ Limitations

### Model 1 — Order-Level Demand

R² of approximately 0.34 is relatively low because order-level data is highly noisy.

For business decisions, **MAE (≈6 units)** can be more interpretable than R² alone.

### Delivery Days

`delivery_days` was not successfully predicted because the available features did not contain sufficient predictive signal.

Additional data that may improve this analysis includes:

- courier/supplier ID,
- warehouse distance,
- weather,
- traffic,
- logistics information.

### Stockout Classification

Stockout classification achieved ROC-AUC of approximately 0.49, which is close to random classification. Therefore, the target was not used as a final machine learning model.

### Safety Stock Assumption

The safety stock calculation assumes demand and lead time follow a normal distribution. This is a standard assumption, but should be periodically validated as more operational data becomes available.

---

# 🔄 End-to-End Value Chain

ForecastLab connects the three data roles into one complete workflow:

```text
                 DATA ENGINEERING
                        │
                        ▼
             Reliable & Clean Dataset
                        │
                        ▼
                  DATA ANALYTICS
                        │
                        ▼
              Business Understanding
              & Inventory Insights
                        │
                        ▼
                   DATA SCIENCE
                        │
                        ▼
                 Forecasting Models
                        │
                        ▼
               Business Applications
                        │
                        ▼
          Inventory & Supply Planning
                        │
                        ▼
             Better Inventory Decisions
```

The project therefore demonstrates how **Data Engineering, Data Analytics, and Data Science work together**, rather than operating as separate deliverables.

---

# 👥 Team

**ForecastLab — Hacktiv8 FTDS Batch 041**

- Khalfani Novian Habibi
- Rendy Azly
- Dennis Wirawan

---

# 📄 Project Purpose

ForecastLab was developed as an educational **Final Project — Data Science & AI** for Hacktiv8 FTDS Batch 041.

The project demonstrates an end-to-end workflow covering:

> **Data → ETL → Data Quality → Analytics → Business Insight → Forecasting → Inventory Planning**

