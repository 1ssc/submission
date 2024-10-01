import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

# Konfigurasi halaman yang lebih profesional
st.set_page_config(
    page_title="Analisis Sewa Sepeda",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Fungsi untuk memuat dan memproses data
@st.cache_data
def load_data():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/1ssc/submission/main/dashboard/main_data.csv"
    )
    df["dateday"] = pd.to_datetime(df["dateday"])
    return df


# Fungsi untuk styling yang ditingkatkan
def apply_custom_style():
    st.markdown(
        """
        <style>
        .main {
            padding: 2rem;
        }
        div[data-testid="stMetricValue"] {
            font-size: 24px;
            color: #0066cc;
        }
        div[data-testid="stMetricLabel"] {
            font-size: 16px;
            color: #333333;
        }
        div[data-testid="metric-container"] {
            background-color: #ffffff;
            border: 1px solid #ddd;
            padding: 1rem;
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .metric-row {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 2rem;
        }
        h1, h2, h3 {
            color: #1f77b4;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )


# Fungsi untuk membuat visualisasi yang lebih efektif
def create_monthly_trend(df):
    monthly_data = (
        df.resample("M", on="dateday")
        .agg({"count": "sum", "registered": "sum", "casual": "sum"})
        .reset_index()
    )

    fig = go.Figure()

    # Menambahkan garis untuk setiap kategori
    categories = {"Total": "count", "Registered": "registered", "Casual": "casual"}

    colors = {"Total": "#1f77b4", "Registered": "#2ca02c", "Casual": "#ff7f0e"}

    for name, col in categories.items():
        fig.add_trace(
            go.Scatter(
                x=monthly_data["dateday"],
                y=monthly_data[col],
                name=name,
                line=dict(color=colors[name], width=3),
                mode="lines+markers",
            )
        )

    fig.update_layout(
        title="Tren Penyewaan Sepeda Bulanan",
        xaxis_title="Tanggal",
        yaxis_title="Jumlah Penyewaan",
        hovermode="x unified",
        template="plotly_white",
    )

    return fig


def create_seasonal_comparison(df):
    seasonal_data = (
        df.groupby("season")
        .agg({"count": "sum", "registered": "sum", "casual": "sum"})
        .reset_index()
    )

    season_order = ["Spring", "Summer", "Fall", "Winter"]
    seasonal_data["season"] = pd.Categorical(
        seasonal_data["season"], categories=season_order
    )
    seasonal_data = seasonal_data.sort_values("season")

    # Skema warna modern dan vibrant
    modern_colors = {
        "total": "#FF6B6B",  # Coral merah muda
        "registered": "#4ECDC4",  # Turquoise
        "casual": "#45B7D1",  # Biru cerah
        "background": "#2A2A72",  # Biru gelap untuk aksen
    }

    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=(
            "<b>Total Penyewaan per Musim</b>",
            "<b>Perbandingan Tipe Pengguna per Musim</b>",
        ),
        horizontal_spacing=0.1,
    )

    # Bar chart untuk total penyewaan dengan styling yang ditingkatkan
    fig.add_trace(
        go.Bar(
            x=seasonal_data["season"],
            y=seasonal_data["count"],
            name="Total",
            marker=dict(
                color=modern_colors["total"],
                line=dict(color=modern_colors["background"], width=1),
            ),
            hovertemplate="<b>%{x}</b><br>Total: %{y:,.0f}<extra></extra>",
        ),
        row=1,
        col=1,
    )

    # Stacked bar untuk perbandingan tipe pengguna
    fig.add_trace(
        go.Bar(
            x=seasonal_data["season"],
            y=seasonal_data["registered"],
            name="Registered",
            marker=dict(color=modern_colors["registered"]),
            hovertemplate="<b>%{x}</b><br>Registered: %{y:,.0f}<extra></extra>",
        ),
        row=1,
        col=2,
    )
    fig.add_trace(
        go.Bar(
            x=seasonal_data["season"],
            y=seasonal_data["casual"],
            name="Casual",
            marker=dict(color=modern_colors["casual"]),
            hovertemplate="<b>%{x}</b><br>Casual: %{y:,.0f}<extra></extra>",
        ),
        row=1,
        col=2,
    )

    # Update layout dengan styling yang lebih modern
    fig.update_layout(
        height=500,
        showlegend=True,
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        barmode="stack",
        font=dict(family="Roboto, sans-serif", size=12, color="#ffffff"),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            bordercolor="rgba(0,0,0,0)",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        margin=dict(l=40, r=40, t=80, b=40),
    )

    # Update axes untuk styling yang konsisten
    fig.update_xaxes(
        showgrid=False,
        showline=True,
        linecolor="rgba(255,255,255,0.2)",
        tickfont=dict(size=10),
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(255,255,255,0.1)",
        showline=True,
        linecolor="rgba(255,255,255,0.2)",
        tickfont=dict(size=10),
    )

    return fig


# Main app
def main():
    apply_custom_style()

    st.title("🚲 Analisis Sewa Sepeda")

    # Load data
    data_df = load_data()

    # Sidebar untuk filter
    with st.sidebar:
        st.image(
            "https://raw.githubusercontent.com/1ssc/submission/main/dashboard/bike-rental.png"
        )
        st.header("Filter Data")

        date_range = st.date_input(
            "Pilih Rentang Tanggal",
            value=[data_df["dateday"].min(), data_df["dateday"].max()],
            min_value=data_df["dateday"].min(),
            max_value=data_df["dateday"].max(),
        )

    # Filter data berdasarkan tanggal
    mask = (data_df["dateday"].dt.date >= date_range[0]) & (
        data_df["dateday"].dt.date <= date_range[1]
    )
    filtered_df = data_df.loc[mask]

    # Metrics dalam container
    with st.container():
        col1, col2, col3 = st.columns(3)

        metrics = {
            "📊 Total Penyewaan": filtered_df["count"].sum(),
            "👥 Pengguna Terdaftar": filtered_df["registered"].sum(),
            "🚴 Pengguna Kasual": filtered_df["casual"].sum(),
        }

        for col, (label, value) in zip([col1, col2, col3], metrics.items()):
            with col:
                st.metric(label, f"{value:,.0f}")

    # Visualisasi tren bulanan
    st.plotly_chart(create_monthly_trend(filtered_df), use_container_width=True)

    # Visualisasi perbandingan musiman
    st.plotly_chart(create_seasonal_comparison(filtered_df), use_container_width=True)

    # Informasi tambahan
    with st.expander("ℹ️ Informasi Dashboard"):
        st.markdown(
            """
        Dashboard ini menampilkan analisis data sewa sepeda dengan mempertimbangkan:
        - Tren penyewaan sepeda dari waktu ke waktu
        - Perbandingan antara pengguna terdaftar dan kasual
        - Pola penyewaan berdasarkan musim
        """
        )

    st.caption("© 2024 Moh. Wahyu Abrory - Data Visualization Project")


if __name__ == "__main__":
    main()
