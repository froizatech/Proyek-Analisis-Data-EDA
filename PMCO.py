import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import datetime
from babel.numbers import format_currency

df = pd.read_csv("dingling_data.csv")

df.columns = df.columns.str.strip()

st.header('Pengukuran Parameter Udara PM10 dan CO pada Kota Dingling dalam rentang Maret 2013- Februari 2017')
st.write("Data yang tersedia hanya dari 1 Maret 2013 - 28 Februari 2017")

df.columns = df.columns.str.strip()


df['date'] = pd.to_datetime(df['date'], errors='coerce')

# === Sidebar Filter ===
st.header("🔍 Filter Data")

# Pilih rentang tanggal
min_date = df['date'].min()
max_date = df['date'].max()

date_range = st.date_input(
    "Pilih rentang tanggal:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)
search_clicked = st.button("Cari", type="primary")

if search_clicked:

    # === Filter Berdasarkan Rentang Tanggal ===
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = df[(df['date'] >= pd.to_datetime(start_date)) &
                         (df['date'] <= pd.to_datetime(end_date))]
    else:
        filtered_df = df.copy()

    st.write(f"📅 Menampilkan data dari **{start_date}** hingga **{end_date}**")

    if filtered_df.empty:
        st.warning("⚠️ Tidak ada data dalam rentang tanggal tersebut.")
    else:
        st.write("Grafik PM10")
        st.line_chart(filtered_df, x="date", y=["PM10"])

        st.write("Grafik CO")
        st.line_chart(filtered_df, x="date", y=["CO"])

