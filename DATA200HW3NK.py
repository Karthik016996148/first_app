import plotly.express as ps
import streamlit as st
import pandas as pd
df = pd.read_csv(Fish.csv)
fig = px.bar(df, x='Species',y='Weight')
st.pyplot(fig)
