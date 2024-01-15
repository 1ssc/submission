# 🚲 Bike-Sharing: Analysis and Dashboard

## 📝 Analyze the Datasets
‼️ See the details of this analysis and visualization on the [ipynb](https://github.com/1ssc/submission/blob/main/Proyek_Analisis_Data.ipynb) file

### 🤔Defining Question
1. Bagaimana perkembangan peminjaman sepeda selama satu tahun terakhir? Apakah terdapat tren kenaikan atau penurunan yang signifikan?
2. Pada musim apa terjadi jumlah peminjaman sepeda paling sedikit? Dan pada musim apa terjadi jumlah peminjaman sepeda paling banyak?
3. Bagaimana variabel-variabel seperti workday, day_of_week, dan holiday mempengaruhi pola peminjaman sepeda? Apakah ada perbedaan yang signifikan pada hari kerja, hari dalam seminggu, atau hari libur?
4. Bagaimana cuaca dan musim mempengaruhi tingkat peminjaman sepeda? Apakah terdapat preferensi tertentu terkait kondisi cuaca atau musim tertentu?
5. Apakah terdapat korelasi antara kecepatan suhu (*temperature*) dengan total peminjaman sepeda?

### ℹ️Insight and Findings
1. Total peminjaman tertingga sepeda pada tahun 2012 lebih besar dibandingkan dengan tahun 2011. Terlihat pola tren peningkatan jumlah peminjaman sepeda dari awal tahun hingga pertengahan tahun dan menurun pada akhir tahun.
2. Pada musim dingin/ `Winter` peminjaman sepeda paling sedikit. Pada musim `Summer` peminjaman sepeda paling banyak. Terjadi kenaikan yang signifikan di tiap tiap musim, namun terjadi penurunuran pada musim salju `Winter`. Hal ini bisa jadi karena cuaca yang tidak mendukung untuk bersepeda.
3. Total peminjaman sepeda pada hari kerja lebih banyak dibandingkan hari libur. Pada hari kerja, peminjaman sepeda paling banyak terjadi pada hari `Jumat`. Sedangkan peminjaman sepeda paling sedikit terjadi pada hari `Senin`. Pada hari kerja, orang cenderung meminjam sepeda pada hari-hari `non-kerja`, seperti `Sabtu` atau `Minggu`. Hal ini dapat terlihat dari grafik yang menunjukkan total peminjaman sepeda pada tahun 2011 seimbang antara hari kerja, sementara pada akhir pekan hanya terjadi pada `Sabtu` dan `Minggu`. Hasil ini mengindikasikan preferensi orang untuk meminjam sepeda terutama pada `akhir pekan`.
4. Peminjaman sepeda cenderung meningkat saat grafik sedang cerah, tidak peduli pada musim apa pun. Hal ini dapat diamati dari informasi yang tertera di atas, bahwa meskipun saat musim salju, namun ketika grafik cerah, minat masyarakat untuk meminjam sepeda tetap tinggi. Begitupun sebaliknya.
5. Ketika suhu rendah total peminjaman sepeda cenderung sedikit, sebaliknya jika suhu meningkat maka total peminjaman juga meningkat hal ini terjadi pada musim gugur. Dari sini terdapat `sweet-spot` dari suhu, ketika total peminjaman sepeda berada dipuncak. Kita bisa melihatnya ketika musim gugur dan musim panas. Dapat disimpulkan bahwa ketika pada saat itu, maka total peminjaman sepeda akan cenderung tinggi.

## 📊Dashboard w/ [Streamlit](https://dashboard-penyewaan-sepeda.streamlit.app/)
### Streanlit Cloud
🔗 Visit my streamlit dashboard directly through this link: https://dashboard-penyewaan-sepeda.streamlit.app/ 🔗

The dashboard shows the count of total bike-sharing across the year and season. It shows the difference count of total bike-sharing based on weather condition and season. It also shows count of total bike-sharing per day

<p align="center">
  <img src="https://github.com/1ssc/submission/blob/main/screenshots_dashboard.jpeg"/>

## ⏩Run this project locally
### Install Dependencies
To install all the required libraries, open your terminal/command prompt/conda prompt, navigate to this project folder, and run the following command:
```bash
pip install -r requirements.txt
```

### Run the Dashboard
```bash
cd dashboard
streamlit run dashboard.py
```
