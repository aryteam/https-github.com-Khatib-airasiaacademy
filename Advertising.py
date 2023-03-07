import streamlit as st
import numpy as np
import pandas as pd

pd.read_csv('Advertising.csv')
st.header("My first Streamlit App")
st.write(pd.DataFrame(pd))
