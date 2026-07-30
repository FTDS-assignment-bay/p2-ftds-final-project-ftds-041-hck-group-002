# 📊 FMCG Forecasting — Notebook Pembuatan Model

Notebook analisis & training model untuk 3 model forecasting FMCG terbaik. Ini adalah **notebook
sumber** — tempat data dianalisis, kandidat target diuji, model dilatih, dievaluasi, dan disimpan
sebagai file `.pkl`. (Aplikasi deployment/Streamlit didokumentasikan terpisah, tidak dibahas di sini.)

## 📁 File

| File | Keterangan |
|---|---|
| `FMCG_3_Best_Forecasting_Models.ipynb` | Notebook utama — jalankan dari atas ke bawah |
| `forecasting_dataset.csv` | Dataset sumber, wajib ada di folder yang sama sebelum menjalankan notebook |

## 🎯 Tujuan

Dari beberapa kandidat target yang mungkin diprediksi, notebook ini **menguji kelayakan tiap
kandidat secara data-driven** sebelum membangun model penuh — hanya target dengan
sinyal prediktif nyata yang dilanjutkan.

| Target diuji | Hasil uji | Status |
|---|---|---|
| `units_sold` per order | R² = 0,34 | ✅ Dibangun → **Model 1** |
| `revenue` per order | R² = 0,54 | ✅ Dibangun → **Model 2** |
| Total demand mingguan per kategori | R² = 0,95 | ✅ Dibangun → **Model 3** |
| `delivery_days` | R² ≈ 0,00 | ❌ Ditolak (tidak ada sinyal) |
| Klasifikasi stockout | ROC-AUC ≈ 0,49 | ❌ Ditolak (setara tebak acak) |

## 📦 Dataset

- **File**: `forecasting_dataset.csv` (190.757 baris × 21 kolom)
- **Periode**: Januari 2022 – Desember 2024
- **Cakupan**: 30 SKU, 5 kategori (Milk, Yogurt, Juice, ReadyMeal, SnackBar), 3 channel (Retail,
  Discount, E-commerce), 3 wilayah (PL-Central, PL-North, PL-South)
- **Granularitas**: satu baris = satu event order/pengiriman untuk kombinasi
  `sku × channel × region × pack_type` pada tanggal tertentu
- **Kolom kunci**: `price_unit`, `promotion_flag`, `delivery_days`, `stock_available`,
  `delivered_qty`, `units_sold`, `revenue`, plus fitur tanggal siap pakai (`month`, `quarter`,
  `week_of_year`, `day_of_week`, `weekend_flag`)
- Sudah bersih (tanpa missing value, duplikat, atau anomali nilai negatif) — diverifikasi ulang di
  Bagian 2 notebook.

## 🧭 Struktur Notebook

1. **Business Understanding** — kenapa 3 model dgn granularitas berbeda dibutuhkan
2. **Data Understanding & Quality Check** — verifikasi kualitas data + formula kolom `revenue`
3. **Exploratory Data Analysis** — efek promosi, pola musiman, hubungan harga-penjualan
4. **Verifikasi Data-Driven** — uji cepat `delivery_days` & stockout classification, dgn bukti kode
5. **Model 1 — Demand Forecasting** — feature engineering, split waktu, training, evaluasi
6. **Model 2 — Revenue Forecasting** — sama seperti Model 1, dgn catatan anti-leakage
7. **Model 3 — Weekly Aggregate Demand Forecasting** — agregasi mingguan per kategori
8. **Ringkasan Perbandingan 3 Model**
9. **Aplikasi Bisnis** — safety stock & reorder point per kategori
10. **Kesimpulan & Rekomendasi Bisnis**

## 🤖 Hasil Model

| Model | Target | Algoritma terbaik | R² | MAE | Untuk siapa |
|---|---|---|---|---|---|
| 1. Demand Forecasting | `units_sold` (order-level) | Gradient Boosting | 0,339 | ≈ 6,0 unit | Supply Chain / Gudang |
| 2. Revenue Forecasting | `revenue` (order-level) | Gradient Boosting | 0,544 | ≈ 31,5 | Finance / Commercial |
| 3. Weekly Aggregate Demand | total unit/minggu per kategori | Gradient Boosting | 0,946 | ≈ 6,6% dari rata-rata | Category / Supply Planning |

Ketiga model dibandingkan terhadap 2 baseline (Linear Regression, Random Forest) sebelum Gradient
Boosting dipilih sbg model final — perbandingan lengkap ada di tabel `results_m*_df` pada masing-masing
bagian model di notebook.

**Metodologi:**
- Split train/test **berbasis waktu** (80% data awal = train, 20% terakhir = test), bukan acak
- Fitur historis (`demand_lag1`, `demand_roll3`, `demand_roll7`, dst) dihitung pakai `.shift(1)`
  sebelum `.rolling()` untuk mencegah data leakage
- Model 2 sengaja **tidak** memakai `units_sold` sbg fitur (karena `revenue = price_unit × units_sold`
  secara eksak — memakainya = leakage)

## 💾 Output yang Dihasilkan

Menjalankan notebook sampai selesai akan membuat file-file berikut di folder yang sama:

```
model1_demand_forecasting.pkl        # model terlatih Model 1
model1_feature_columns.pkl           # urutan kolom fitur Model 1
model2_revenue_forecasting.pkl       # model terlatih Model 2
model2_feature_columns.pkl           # urutan kolom fitur Model 2
model3_weekly_demand_forecasting.pkl # model terlatih Model 3
model3_feature_columns.pkl           # urutan kolom fitur Model 3
safety_stock_reorder_point.csv       # tabel safety stock & reorder point per kategori
model_comparison_summary.csv         # tabel ringkasan perbandingan 3 model
```

## 🚀 Cara Menjalankan

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib jupyter
jupyter notebook FMCG_3_Best_Forecasting_Models.ipynb
```
Lalu **Run All** dari cell paling atas. Pastikan `forecasting_dataset.csv` ada di folder yang sama
dengan notebook.

**Versi library** (untuk hasil yang konsisten):
`pandas 3.0.2`, `numpy 2.4.4`, `scikit-learn 1.8.0`, `matplotlib 3.10.8`, `seaborn 0.13.2`.

## ⚠️ Keterbatasan

- R² Model 1 (0,34) relatif rendah karena granularitas order-level sangat noisy — MAE (≈6 unit)
  lebih relevan dipakai untuk keputusan bisnis dibanding R² itu sendiri.
- `delivery_days` dan status stockout **sengaja tidak dimodelkan** — datanya terbukti tidak
  menyimpan sinyal prediktif dari fitur yang tersedia. Rekomendasi: kumpulkan data tambahan (ID
  kurir/supplier, jarak gudang, cuaca/lalu lintas) sebelum mencoba lagi di masa depan.
- Formula safety stock (Bagian 9) mengasumsikan demand & lead time berdistribusi normal — asumsi
  standar industri, sebaiknya divalidasi ulang berkala seiring bertambahnya data.
