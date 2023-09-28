import plotly.express as px
import streamlit as st
import pandas as pd
df = pd.read_csv("Fish.csv")
fig = px.bar(df, x='Species',y='Weight', title='WEIGHTS OF DIFFERENT TYPES OF FISH')
st.plotly_chart(fig)
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))