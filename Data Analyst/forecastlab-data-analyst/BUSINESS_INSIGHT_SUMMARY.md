# FMCG Supply Chain — Business Insight Summary
**Project: ForecastLab · Disusun oleh: Tim Data Analyst**

---

Analisis terhadap 190.757 transaksi penjualan FMCG sepanjang 2022–2024 (total revenue $19,95 juta)
mengonfirmasi dua masalah inventory yang terjadi secara bersamaan namun pada produk yang berbeda:
**stockout**, dengan tingkat 2,03% dari seluruh hari transaksi dan estimasi kehilangan revenue
sebesar $414 ribu; serta **overstock**, dengan rata-rata $128 ribu per hari tertahan sebagai stok
idle yang tidak terjual. Kedua risiko ini tidak tersebar merata — keduanya terkonsentrasi pada
kategori **Juice** serta pada 35 dari 270 kombinasi SKU × channel × region (11 berstatus *Critical*,
24 *High*) yang teridentifikasi melalui metode Days of Stock Remaining. Promosi juga terbukti
mendongkrak penjualan secara konsisten sebesar 94–96% di semua channel, sehingga tanpa perencanaan
buffer stok yang tepat, momen promosi justru berisiko memicu stockout baru.

Karena overstock dan stockout terjadi pada SKU yang berbeda di waktu yang sama, kebijakan stok yang
seragam untuk seluruh produk tidak akan efektif menyelesaikan kedua masalah sekaligus — solusi
perlu bekerja di level kombinasi SKU, channel, dan region secara spesifik. Berdasarkan temuan ini,
tim merekomendasikan tindakan restock segera untuk 11 kombinasi *Critical* dalam 1–3 hari ke depan,
peninjauan kebijakan pemesanan pada kombinasi dengan waste tertinggi (terutama Juice), serta
penyelarasan buffer stok dengan kalender promosi. Jika diterapkan, langkah-langkah ini berpotensi
menurunkan idle stock menjadi $64 ribu per hari (‑50%, sesuai target bisnis) dan memulihkan
$124 ribu–$249 ribu revenue yang selama ini hilang akibat stockout.

---

<p align="center"><i>ForecastLab · FMCG Supply Chain Analysis · Tim Data Analyst</i></p>
