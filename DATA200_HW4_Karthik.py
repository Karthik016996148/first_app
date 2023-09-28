import streamlit as st
import plotly.express as plt
import pandas as pd
data = pd.read_csv("toy_dataset.csv")
df = pd.DataFrame(data)
result = df.head(25)
st.write(result)
x=list(df.iloc[:, 1])
y=list(df.iloc[:, 4])
plt.bar(x, y, width=0.4)
plt.xticks(rotation=45, ha='right')
plt.title("SALARY BASED ON LOCATION")
plt.xlabel("CITY")
plt.ylabel("INCOME")
st.pyplot(plt.gcf())
