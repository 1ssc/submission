import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st

# Load data
data_df = pd.read_csv("https://raw.githubusercontent.com/1ssc/submission/main/dashboard/main_data.csv")
data_df['dateday'] = pd.to_datetime(data_df['dateday'])

sns.set(style='dark')

st.set_page_config(page_title="Dashboard Data Sewa Sepeda",
                   page_icon=":bar_chart:",
                   layout="wide")

# Define Function
def pengguna_bulanan_df(df):
    pengguna_bulanan_df = df.resample(rule='M', on='dateday').agg({
        "count": "sum",
        'registered': "sum",
        'casual': "sum"
    })
    pengguna_bulanan_df.index = pengguna_bulanan_df.index.strftime('%b-%y')
    pengguna_bulanan_df = pengguna_bulanan_df.reset_index()
    pengguna_bulanan_df.rename(columns={
        "dateday": "Bulan-Tahun",
        "count": "Jumlah Sewa",
        "registered": "Registered",
        "casual": "Casual"
    }, inplace=True)

    return pengguna_bulanan_df

def pengguna_musiman_df(df):
    pengguna_musiman_df = df.groupby('season').agg({
        "count": "sum"
    })

    pengguna_musiman_df = pengguna_musiman_df.reset_index()
    pengguna_musiman_df.rename(columns={
        "season": "Musim",
        "count": "Jumlah Sewa"
    }, inplace=True)

    pengguna_musiman_df = pd.melt(pengguna_musiman_df, id_vars=['Musim'], value_vars=['Jumlah Sewa'])

    pengguna_musiman_df['Musim'] = pd.Categorical(pengguna_musiman_df['Musim'], categories=['Spring', 'Summer', 'Fall', 'Winter'])

    pengguna_musiman_df = pengguna_musiman_df.sort_values(by=['Musim'])

    return pengguna_musiman_df

def pengguna_harian_df(df):
    pengguna_harian_df = df.groupby('day_of_week').agg({
        'count': 'sum'
    })

    pengguna_harian_df = pengguna_harian_df.reset_index()

    pengguna_harian_df.rename(columns={
        'count': 'Jumlah Sewa',
        'day_of_week': 'Hari',
    }, inplace=True)

    pengguna_harian_df = pd.melt(pengguna_harian_df, id_vars=['Hari'], value_vars=['Jumlah Sewa'])

    pengguna_harian_df['hari'] = pd.Categorical(pengguna_harian_df['Hari'], categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    pengguna_harian_df = pengguna_harian_df.sort_values(by=['Hari'])

    return pengguna_harian_df

def musim_hari_df(df):
    musim_hari_df = df.groupby(['season', 'weather_condition']).agg({
        'count': 'sum'
    })

    musim_hari_df = musim_hari_df.reset_index()

    musim_hari_df.rename(columns={
        'count': 'Jumlah Sewa',
    }, inplace=True)

    return musim_hari_df


# Sidebar
min_date = data_df["dateday"].min()
max_date = data_df["dateday"].max()

with st.sidebar:
    st.image('https://raw.githubusercontent.com/1ssc/submission/main/dashboard/bike-rental.png')

    st.sidebar.header("Filter Data")

    start_date, end_date = st.date_input(label="Rentang Tanggal", min_value=min_date,  max_value=max_date, value=[min_date, max_date])

main_df = data_df[
    (data_df["dateday"] >= str(start_date)) &
    (data_df["dateday"] <= str(end_date))
]

pengguna_bulanan_df = pengguna_bulanan_df(main_df)
pengguna_musiman_df = pengguna_musiman_df(main_df)
pengguna_harian_df = pengguna_harian_df(main_df)

# Main
st.title(":bar_chart: Dashboard Data Sewa Sepeda")
st.markdown('##')

kolom1, kolom2, kolom3 = st.columns((2,2,2))

with kolom1:
    total_keseluruhan_penyewa = main_df['count'].sum()
    st.metric(label='Total Keseluruhan Penyewa', value="{:,.0f}".format(total_keseluruhan_penyewa))
with kolom2:
    total_penyewa_kasual = main_df['casual'].sum()
    st.metric(label='Total Penyewa Kasual', value="{:,.0f}".format(total_penyewa_kasual))
with kolom3:
    total_penyewa_teregistrasi = main_df['registered'].sum()
    st.metric(label='Total Penyewa Teregistrasi', value="{:,.0f}".format(total_penyewa_teregistrasi))


fig = px.line(pengguna_bulanan_df, x='Bulan-Tahun', y=['Jumlah Sewa', 'Registered', 'Casual'], title='Jumlah Sewa Sepeda per Bulan', template='plotly_dark', markers=True, line_shape='spline')
st.plotly_chart(fig, use_container_width=True)

st.markdown('---')

col1, col2 = st.columns((2, 2))

with col1:
    st.subheader('Jumlah Sewa Sepeda Berdasarkan Kondisi Cuaca di Berbagai Musim')
    fig = px.bar(musim_hari_df(main_df), x='season', y='Jumlah Sewa', color='weather_condition', barmode='group', height=400)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader('Jumlah Sewa Sepeda per Musim')
    fig = px.bar(pengguna_musiman_df, x='Musim', y='value', color='value', height=400)
    st.plotly_chart(fig, use_container_width=True)

st.header('Jumlah Sewa Sepeda per Hari')
fig = px.bar(pengguna_harian_df, x='Hari', y='value', color='value', height=400)
st.plotly_chart(fig, use_container_width=True)


# Add RFM to the dashboard
def calculate_rfm(df, analysis_date):
    # Assume each unique user is identified by 'registered' or 'casual'
    # Filter out rows where users are 0 (assumption that it means no user)
    rfm_df = df[
        df["registered"] > 0
    ]  # This is for registered users, modify based on your dataset
    rfm_df = (
        rfm_df.groupby("registered")
        .agg(
            {
                "dateday": lambda x: (analysis_date - x.max()).days,  # Recency
                "count": "count",  # Frequency
                "count": "sum",  # Monetary, can modify as per actual monetary value if available
            }
        )
        .reset_index()
    )

    rfm_df.columns = ["registered", "Recency", "Frequency", "Monetary"]

    # Assign RFM scores
    rfm_df["R_Score"] = pd.qcut(rfm_df["Recency"], 4, labels=[4, 3, 2, 1])
    rfm_df["F_Score"] = pd.qcut(rfm_df["Frequency"], 4, labels=[1, 2, 3, 4])
    rfm_df["M_Score"] = pd.qcut(rfm_df["Monetary"], 4, labels=[1, 2, 3, 4])

    rfm_df["RFM_Score"] = (
        rfm_df["R_Score"].astype(str)
        + rfm_df["F_Score"].astype(str)
        + rfm_df["M_Score"].astype(str)
    )

    return rfm_df


# Date for Recency calculation
analysis_date = max_date

# Filtered main_df for RFM calculation
rfm_result = calculate_rfm(main_df, analysis_date)

# Add RFM to the dashboard
st.header("Analisis RFM (Recency, Frequency, Monetary)")
st.dataframe(rfm_result)

# Display RFM segmentation in charts
fig_rfm = px.scatter(
    rfm_result,
    x="Recency",
    y="Monetary",
    size="Frequency",
    color="RFM_Score",
    hover_name="registered",
    title="Distribusi Pelanggan Berdasarkan Skor RFM",
)
st.plotly_chart(fig_rfm, use_container_width=True)


st.caption('Copyright (c), created by Moh. Wahyu Abrory')

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
