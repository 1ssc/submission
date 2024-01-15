# 🚲 Bike-Sharing: Analysis and Dashboard

## 📝 Comprehensive Analysis and Visualization
⚡ Explore the detailed analysis and visualizations in the [ipynb](https://github.com/1ssc/submission/blob/main/Proyek_Analisis_Data.ipynb) file

### 🤔Defining Questions
1. Bagaimana perkembangan peminjaman sepeda selama satu tahun terakhir? Apakah terdapat tren kenaikan atau penurunan yang signifikan?
2. Pada musim apa terjadi jumlah peminjaman sepeda paling sedikit? Dan pada musim apa terjadi jumlah peminjaman sepeda paling banyak?
3. Bagaimana variabel-variabel seperti workday, day_of_week, dan holiday mempengaruhi pola peminjaman sepeda? Apakah ada perbedaan yang signifikan pada hari kerja, hari dalam seminggu, atau hari libur?
4. Bagaimana cuaca dan musim mempengaruhi tingkat peminjaman sepeda? Apakah terdapat preferensi tertentu terkait kondisi cuaca atau musim tertentu?
5. Apakah terdapat korelasi antara kecepatan suhu (*temperature*) dengan total peminjaman sepeda?

### ℹ️Insight and Findings
1. Total penyewaan sepeda di tahun 2012 melebihi jumlah penyewaan sepeda di tahun 2011📈. Tren yang jelas dari peningkatan penyewaan sepeda terlihat dari awal hingga pertengahan tahun, diikuti dengan penurunan menjelang akhir tahun.
2. Selama musim dingin, penyewaan sepeda berada pada titik terendah, sementara musim panas mengalami angka tertinggi. Ada peningkatan yang signifikan di setiap musim, kecuali penurunan 📉 selama musim dingin karena cuaca bersepeda yang tidak mendukung.
3. Penyewaan sepeda 🚴🏻 pada hari kerja lebih banyak daripada hari libur. Hari Jumat merupakan hari dengan jumlah penyewaan sepeda tertinggi, sedangkan hari Senin merupakan hari dengan jumlah penyewaan sepeda terendah. Pada hari kerja, orang cenderung menyewa sepeda pada hari yang bukan hari kerja, seperti Sabtu atau Minggu, sebagaimana dibuktikan oleh penyewaan sepeda yang berimbang pada hari kerja di tahun 2011, dibandingkan dengan akhir pekan yang hanya terbatas pada hari Sabtu dan Minggu. Hal ini mengindikasikan adanya preferensi untuk penyewaan sepeda, terutama pada akhir pekan.
4. Penyewaan sepeda cenderung meningkat saat cuaca cerah☀️😎, terlepas dari musimnya. Meskipun dalam kondisi bersalju, jika cuaca cerah, ada minat yang berkelanjutan terhadap penyewaan sepeda. Hal yang sebaliknya juga berlaku.
5. Pada suhu dingin🥶, penyewaan sepeda umumnya lebih rendah, tetapi akan meningkat seiring dengan meningkatnya suhu, terutama di musim gugur. Ada *sweet-spot* dalam suhu selama musim semi dan musim panas🥵 ketika penyewaan sepeda mencapai puncaknya. Oleh karena itu, dapat disimpulkan bahwa selama musim-musim ini, penyewaan sepeda cenderung tinggi.

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
