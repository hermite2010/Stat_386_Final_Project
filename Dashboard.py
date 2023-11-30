import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import seaborn as sns

st.title('Sexual Crimes in the Big Twelve')
df = pd.read_csv('SexOffensePlotData.csv')

df['Year'] = df['Year'].astype(str)

# Create a sidebar for user input
x_axis = st.sidebar.selectbox('Select X axis', df.columns)

df.sort_values(by=x_axis, inplace=True, ascending=True)

# Allow the user to select the schools to display
schools = st.sidebar.multiselect('Select schools to display', df['School'].unique())
df = df[df['School'].isin(schools)]

# Plot the data using the selected X axis on a bar plot
fig = px.bar(df, x=x_axis, y='School', color='Year')
st.plotly_chart(fig)


