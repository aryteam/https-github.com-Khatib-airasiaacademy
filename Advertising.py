import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv('Advertising.csv')
st.header("My first Streamlit App")
st.write(df)

option = st.sidebar.selectbox(
    'Select a mini project',
     ['line chart','map','T n C','Long Process'])

if option=='line chart':
    chart_data = pd.DataFrame(
    df)

    st.line_chart(chart_data)

elif option=='map':
    map_data = pd.DataFrame(df,
    columns=['Sales', 'TV'])

    st.map(map_data)



