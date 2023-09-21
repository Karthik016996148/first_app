import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
data = pd.read_csv(r"C:\Users\Karthik\Desktop\SEM 1\DATA 200\ASsignments\toy_dataset.csv")
df = pd.DataFrame(data)
x=list(df.iloc[:, 1])
y=list(df.iloc[:, 4])
plt.bar(x, y, width=0.4)
plt.xticks(rotation=45, ha='right')
plt.title("SALARY BASED ON LOCATION")
plt.xlabel("CITY")
plt.ylabel("INCOME")
fig=plt.show()
st.plotly_chart(fig)
