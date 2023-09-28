import streamlit as st
import plotly.express as px
import pandas as pd
data = pd.read_csv("toy_dataset.csv")
df = pd.DataFrame(data)
result = df.head(25)
st.write(result)
x=list(df.iloc[:, 1])
y=list(df.iloc[:, 4])
fig = px.bar(x, y, width=0.4)
fig.update_xaxes(tickangle=45, tickvals=x, ticktext=x)
px.title("SALARY BASED ON LOCATION")
px.xlabel("CITY")
px.ylabel("INCOME")
fig.show() 
