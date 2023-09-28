import streamlit as st
import plotly.express as px
import pandas as pd
data = pd.read_csv("toy_dataset.csv")
df = pd.DataFrame(data)
result = df.head(25)
st.write(result)
x=list(df.iloc[:, 1])
y=list(df.iloc[:, 4])
px.xticks(rotation=45, ha='right')
px.title("SALARY BASED ON LOCATION")
px.xlabel("CITY")
px.ylabel("INCOME")
st.plotly_chart(x, y, width=0.4)
