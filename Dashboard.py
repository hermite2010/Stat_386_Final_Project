import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import seaborn as sns

st.title('Sexual Crimes in the Big Twelve')
df = pd.read_csv('SexOffensePlotData.csv')

df['Year'] = df['Year'].astype(str)

# Create a dropdown for user input
x_axis = st.selectbox('Select X axis', df.columns)

df.sort_values(by=x_axis, inplace=True, ascending=True)

# Allow the user to select the schools to display
schools = st.multiselect('Select schools to display', df['School'].unique(), default=list(df['School'].unique())) 
df = df[df['School'].isin(schools)]

# Plot the data using the selected X axis on a bar plot
fig = px.bar(df, x=x_axis, y='School', color='Year')
st.plotly_chart(fig)

# Plot a line graph for a single school over the years
selected_school = st.selectbox('Select a school', schools)
y_axis = st.selectbox('Select Y axis', df.columns)
df_single_school = df[df['School'] == selected_school]
fig_line = px.line(df_single_school, x='Year', y=y_axis)
st.plotly_chart(fig_line)





