import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import datetime
from babel.numbers import format_currency

df = pd.read_csv("dingling_data.csv")

st.header('Pengukuran Parameter Udara PM10 dan CO pada Kota Dingling dalam rentang Maret 2013- Februari 2017')

st.write("Silahkan menuju ke tab PM10 dan CO jika ingin mengetahui perkembangan PM10 dan CO, atau melihat korelasinya dengan parameter suhu, tekanan, dan curah hujan pada tab Korelasi")

