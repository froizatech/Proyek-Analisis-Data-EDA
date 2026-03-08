import pandas as pd
import streamlit as st

st.header("About This Project")

st.markdown("""
This website is an personal website for Dicoding Data Science Boothcamp assignment. Built using **Streamlit** to explore an student placement result dataset.  
Users can search the placement results based on start and end date, also heatmap visualization from each parameter.
""")


st.subheader("Dataset")

st.markdown("Source: Air quality Github (https://github.com/marceloreis/HTI/tree/master)")


st.subheader("Features")

st.markdown("""
- 🔎 air quality measurement result
- 📊 Interactive data visualizations  
- 🎛 Filtering by date range  
- 📈 Line graph and heatmap visualization  
""")


st.subheader("Technologies Used")

st.markdown("""
- **Python**
- **Pandas** – data processing
- **Matplotlib** – data visualization
- **Streamlit** – web dashboard
- **Seaborn** – data visualization
- **Numpy** – data processing
- **datetime** – date data
""")

st.subheader("Author")

st.markdown("""
Created by **Fardhan Roiza (F5)**

This project was developed as part of a data visualization and dashboard portfolio using Python.
""")


