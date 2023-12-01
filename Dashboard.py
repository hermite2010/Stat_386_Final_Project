import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import seaborn as sns

st.title('Sexual Crimes in the Big Twelve')
df = pd.read_csv('SexOffensePlotData.csv')

df['Year'] = df['Year'].astype(str)

crimes = list(df.columns)
crimes.remove('School')
crimes.remove('Year')
crimes.remove('Enrollment')
crimes.remove('Religious')


# Create a dropdown for user input
x_axis = st.selectbox('Select X axis', crimes)

df.sort_values(by=['Year',x_axis], inplace=True, ascending=True)

# Allow the user to select the schools to display
schools = st.multiselect('Select schools to display', df['School'].unique(), default=list(df['School'].unique())) 
df = df[df['School'].isin(schools)]
# Allow the user to select the years to display
years = st.multiselect('Select years to display', df['Year'].unique(), default=list(df['Year'].unique()))

# Plot the data using the selected X axis on a bar plot
fig = px.bar(df, x=x_axis, y='School', color=years, orientation='h', barmode='group')
st.plotly_chart(fig)

# Plot a line graph for a single school over the years
st.title('One School over the years')
selected_school = st.selectbox('Select a school', schools)
y_axis = st.selectbox('Select Y axis', crimes)
df_single_school = df[df['School'] == selected_school]
fig_line = px.line(df_single_school, x='Year', y=y_axis)
st.plotly_chart(fig_line)





