import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import datetime
from babel.numbers import format_currency


# Define your pages
home = st.Page("home.py", title="Home")
pm_co = st.Page("PMCO.py", title="PM10 dan CO")
corr = st.Page("corr.py", title="Korelasi")

# Create the navigation bar at the top
pg = st.navigation([home, pm_co, corr], position="top")
pg.run()