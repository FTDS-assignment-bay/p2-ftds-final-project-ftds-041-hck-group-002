# 📊 Interactive Dashboard — Tableau Public

Dashboard interaktif ini melengkapi analisis statis pada notebook (`/notebooks`) dengan tampilan
yang bisa di-filter langsung oleh pengguna (per kategori, region, dan channel).

🔗 **Live Dashboard:** [ForecastLab — Supply Chain Dashboard (Tableau Public)](https://public.tableau.com/app/profile/rendy.azly/viz/Book1_17853856825220/Dashboard1?publish=yes)

## Cakupan Dashboard
- Ringkasan revenue per kategori, region, dan channel
- Stockout rate dan inventory waste dengan filter interaktif
- Restock priority (Days of Stock Remaining) per SKU

## Catatan
Dashboard ini merupakan snapshot dari dataset yang sama dengan yang digunakan pada
`notebooks/FMCG_Supply_Chain_Predictor_Analysis_v2.ipynb` dan `reports/eda_metadata.json`.
Jika dataset sumber diperbarui, workbook Tableau perlu di-refresh dan dipublish ulang secara manual
(saat ini bukan live-connected, melainkan extract).
