import plotly.express as px
import streamlit as st
import pandas as pd
df = pd.read_csv("Fish.csv")
fig = px.bar(df, x='Species',y='Weight', title='Fish')
st.plotly_chart(fig)
