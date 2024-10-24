import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(page_icon="Welcome")

im = Image.open('maybank.png')
st.image(im, width=600)

st.header("**Welcome to our page**")
st.subheader("*We are exploring the banking.csv data using streamlit!*")

st.sidebar.write('banking')

st.write("Take a look at our data...")
df = pd.read_csv('banking.csv')
st.dataframe(df)