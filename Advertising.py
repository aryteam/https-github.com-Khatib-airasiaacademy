import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Advertising.csv')

st.write("""
# Number of Sales Prediction App
This app predicts the *Number of Sales*!
""")

st.write("Below are the data:")

st.write(df)

st.sidebar.header('User Input Parameters')

def user_input_features():
    tv_value = st.sidebar.slider('TV Value', 0, 150, 300)
    radio_value = st.sidebar.slider('Radio Value', 0, 25, 50)
    newspaper_value = st.sidebar.slider('Newspaper Value', 0, 75, 150)
    data = {'TV': tv_value,
            'Radio': radio_value,
            'Newspaper': newspaper_value}
    features = pd.DataFrame(data, index=[0])
    return features

uif = user_input_features()

st.subheader('User Input parameters')
st.write(uif)

data = pd.read_csv('Advertising.csv')
data = data.drop(data.columns[0], axis=1)

x = data[['TV', 'Radio', 'Newspaper']]
y = data[ 'Sales' ]

regr = LinearRegression()
regr.fit(x,y)

prediction = regr.predict(uif)

st.subheader('Prediction')
st.write(prediction[0])
