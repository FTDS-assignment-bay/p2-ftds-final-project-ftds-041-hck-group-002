# 📦 ForecastLab — Supply Chain Predictor
### Data Analyst Report: Prediksi Risiko Stockout & Inventory Waste pada FMCG

Repositori ini berisi kontribusi **Data Analyst** pada final project tim *ForecastLab* — studi kasus
prediksi ketersediaan inventory untuk perusahaan FMCG. Project dikerjakan oleh tim lintas peran
(Data Analyst, Data Scientist, Data Engineer); repositori ini fokus pada proses EDA, business
understanding, dan insight generation yang menjadi fondasi bagi model forecasting (Data Scientist)
dan data pipeline (Data Engineer).

## Latar Belakang & Tujuan Bisnis

FMCG menghadapi dua pain point yang sama-sama merugikan: **overstock** (modal tertahan, biaya
gudang naik) dan **stockout** (kehilangan penjualan). ForecastLab dibangun untuk memprediksi
ketersediaan inventory sehingga tim procurement bisa merestock lebih awal, dengan target:

> **Menurunkan inventory waste sebesar 50%.**

Ringkasan bisnis lengkap ada di [`BUSINESS_INSIGHT_SUMMARY.md`](BUSINESS_INSIGHT_SUMMARY.md).

## Dataset

FMCG Daily Sales Data (2022–2024) — 190.757 baris x 21 kolom, granularitas SKU x Channel x Region x
Pack Type. Sumber: [Kaggle](https://www.kaggle.com/code/mishashikhov/fmcg-sales-forecasting-ml-case-study)
(CC0).

## Struktur Repositori

```
forecastlab-data-analyst/
├── README.md
├── BUSINESS_INSIGHT_SUMMARY.md     # ringkasan bisnis untuk stakeholder
├── requirements.txt
├── notebooks/                      # notebook EDA & business analysis lengkap
├── reports/eda_metadata.json       # angka kunci, insight, tabel restock
├── visuals/                        # 6 chart hasil EDA (PNG)
├── presentation/                   # slide deck stakeholder (.pptx)
└── dashboard/                      # tautan dashboard Tableau
```

## Hasil Kunci

| Metrik | Nilai |
|---|---|
| Total Revenue (2022–2024) | $19,95 juta |
| Stockout Rate | 2,03% (~$414K revenue hilang) |
| Rata-rata Idle Stock / hari | $128K |
| Kombinasi Restock Berisiko | 11 Critical, 24 High dari 270 |

Metodologi utama: **Days of Stock Remaining (DSR)** = stok tersedia ÷ rata-rata penjualan harian
30 hari terakhir, untuk mengklasifikasikan risiko restock per kombinasi SKU x Channel x Region.
Detail visualisasi, insight, dan rekomendasi lengkap ada di notebook dan
`BUSINESS_INSIGHT_SUMMARY.md`.

## Dashboard & Presentasi

- 🔗 [Dashboard Tableau](https://public.tableau.com/app/profile/rendy.azly/viz/Book1_17853856825220/Dashboard1?publish=yes)

## Tools

Python (Pandas, NumPy), Matplotlib/Seaborn, Jupyter Notebook, Tableau Public.

## Tim ForecastLab (FTDS-041-HCK)

Khalfani Novian Habibi · Rendy Azly · Dennis Wirawan
