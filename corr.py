import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import datetime
from babel.numbers import format_currency

df = pd.read_csv("dingling_data.csv")

st.header('Pengukuran Parameter Udara PM10 dan CO pada Kota Dingling dalam rentang Maret 2013- Februari 2017')
st.write("Korelasi antara PM10 dan CO terhadap parameter suhu, tekanan, dan hujan")




df.columns = df.columns.str.strip()


df['date'] = pd.to_datetime(df['date'], errors='coerce')

# === Sidebar Filter ===
st.sidebar.header("🔍 Filter Data")

# Pilih rentang tanggal
min_date = df['date'].min()
max_date = df['date'].max()

date_range = st.sidebar.date_input(
    "Pilih rentang tanggal:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Pilih parameter
all_params = ["PM10", "CO", "TEMP", "PRES", "RAIN"]
selected_cols = st.sidebar.multiselect(
    "Pilih parameter yang ingin dikorelasikan:",
    options=all_params,
    default=all_params
)

# === Filter Berdasarkan Rentang Tanggal ===
if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = df[(df['date'] >= pd.to_datetime("2013-03-01")) & 
                     (df['date'] <= pd.to_datetime("2017-02-28"))]
else:
    filtered_df = df.copy()

st.write(f"📅 Menampilkan data dari **{start_date}** hingga **{end_date}**")

# === Pastikan minimal dua parameter terpilih ===
if len(selected_cols) < 2:
    st.warning("⚠️ Pilih minimal dua parameter untuk menghitung korelasi.")
else:
    # === Pembersihan data seperti di kode kamu ===
    df_selected = filtered_df[selected_cols].copy()
    for col in selected_cols:
        df_selected[col] = (
            df_selected[col].astype(str)
            .str.replace(",", ".", regex=False)
            .str.extract(r"(\d+\.?\d*)")[0]
        )
        df_selected[col] = pd.to_numeric(df_selected[col], errors="coerce")

    # === Hitung Korelasi ===
    corr = df_selected.corr()

    # === Tampilkan Heatmap ===
    st.subheader("🔥 Peta Korelasi antar Variabel Terpilih")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, fmt=".2f", linewidths=0.5)
    ax.set_title("Heatmap Korelasi (PM10, CO, TEMP, PRES, RAIN)")
    st.pyplot(fig)

    # === Tampilkan Tabel Korelasi ===
    st.subheader("📊 Tabel Korelasi")
    st.dataframe(corr.style.background_gradient(cmap="coolwarm").format("{:.2f}"))

