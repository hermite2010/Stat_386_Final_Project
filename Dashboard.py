import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

st.title('Sexual Crimes in the Big Twelve')
df = pd.read_csv('SexOffensePlotData.csv')

# Create a sidebar for user input
x_axis = st.sidebar.selectbox('Select X axis', df.columns)

# Plot the data using the selected X axis on a bar plot
fig = px.bar(df, x=x_axis, y='School', color='Year')
st.plotly_chart(fig)


