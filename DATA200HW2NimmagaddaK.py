import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.sidebar.header('Interactive Controls')
selected_variable = st.sidebar.selectbox('Select a variable:', ('first column', 'second column'))
slider_value = st.sidebar.slider('Select a range:', min_value=0, max_value=100, value=(0, 100))
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
