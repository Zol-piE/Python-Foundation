import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
 
st.title("Hello Streamlit")
#displat a simple Text
st.write("Hey this Simple Text")
df = pd.DataFrame(
  {
    'row1' : [1,2,3,4,5],
    'row2' : [10,20,30,40,50]
  }
)
st.write('This is a Dataframe')
st.write(df)
#create a line chart
df = pd.DataFrame(
  np.random.randn(50,3),columns=['a','b','c']
)
st.line_chart(df)
 