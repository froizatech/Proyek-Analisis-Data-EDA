import pandas as pd
import streamlit as st

st.header("About This Project")

st.markdown("""
This website is an personal website built using **Streamlit** to explore an student placement result dataset.  
Users can search the placement results based on Student ID, also student visualization from gender and degree.
""")


st.subheader("Dataset")

st.markdown("Source: Kaggle Student Placement Dataset (https://www.kaggle.com/datasets/sonalshinde123/student-placement-dataset/data)")


st.subheader("Features")

st.markdown("""
- 🔎 Placement result search by Student ID  
- 📊 Interactive data visualizations  
- 🎛 Filtering by genre and degree  
- 📈 Distribution charts for age, branch, CGPA, and placement status  
""")


st.subheader("Technologies Used")

st.markdown("""
- **Python**
- **Pandas** – data processing
- **Matplotlib** – data visualization
- **Streamlit** – web dashboard
""")


st.subheader("Author")

st.markdown("""
Created by **F5**

This project was developed as part of a data visualization and dashboard portfolio using Python.
""")
