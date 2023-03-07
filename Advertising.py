import streamlit as st
import numpy as np
import pandas as pd

dp = pd.read_csv('Advertising.csv')
st.header("My first Streamlit App")
st.write(dp)

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sales', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('TV', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Radio', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Newspaper', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(dp, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)


X = dp
Y = dp['Sales']

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(clf)

st.subheader('Prediction')
st.write(clf[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)



