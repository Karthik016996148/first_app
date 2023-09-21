import plotly.express as px
import streamlit as st
import pandas as pd
df = pd.read_csv(r"C:\Users\Karthik\Desktop\SEM 1\DATA 200\ASsignments\Fish.csv")
fig = px.bar(df, x='Species', y='Weight')
st.plotly_chart(fig)
