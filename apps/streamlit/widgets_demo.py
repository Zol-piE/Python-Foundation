import streamlit as st
import pandas as pd
st.title('Stream Test input')
name = st.text_input('Enter your Name')
age = st.slider("Select Your Age :",0,100,25)
st.write(f"{name} Your Age is {age}")
options = ['C++','Java','Python','PHP']
choice = st.selectbox("Chose Your Favorite Lang",options)
st.write(f"You chose {choice}")
if name:
  st.write(f"Hello {name}")

uploadFile = st.file_uploader("Upload a CSV file",type='csv')
if uploadFile is not None:
  df = pd.DataFrame(uploadFile)
  st.write(df.head())