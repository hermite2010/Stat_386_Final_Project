import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import seaborn as sns

st.title('Sexual Crimes in the Big Twelve')
df = pd.read_csv('SexOffensePlotData.csv')

# Add a markdown section for the description of the project
st.markdown('''
This is an interactive dashboard using crime data on the schools in the big 12 conference (as of 2023). 
I provide links at the bottom to find the data, github repositories, and the blog posts that go more into the why of this project.  
''')

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
df_barplot = df[df['School'].isin(schools)]
# Allow the user to select the years to display
#years = st.multiselect('Select years to display', df['Year'].unique(), default=list(df['Year'].unique()))

# Plot the data using the selected X axis on a bar plot
fig = px.bar(df_barplot, x=x_axis, y='School', color='Year', orientation='h', barmode='group')
st.plotly_chart(fig)
st.markdown('''
This is the main graph for comparing schools against one another. I included the three years as this is the only years all the schools reported the crimes. Add or take away any schools that you want. ''')

# Plot a line graph for a single school over the years
st.title('One School over the years')
selected_school = st.selectbox('Select a school', schools)
y_axis = st.selectbox('Select Y axis', crimes)
df_single_school = df[df['School'] == selected_school]
fig_line = px.line(df_single_school, x='Year', y=y_axis)
# Edit the x-axis tick marks
fig_line.update_xaxes(tickvals=[2020, 2021, 2022])
st.plotly_chart(fig_line)
st.markdown('''
This is a line graph for the selected school over the years.  The x-axis is the year and the y-axis is the selected variable.
''')

# Box plot comparing religious and non-religious schools based on the selected variable
st.title('Religious vs. Non-Religious Schools')
selected_variable = st.selectbox('Select a variable', crimes)
df_religious = df[df['Religious'] == 'Yes']
df_non_religious = df[df['Religious'] == 'No']
fig_box = px.box(df, x='Religious', y=selected_variable)
st.plotly_chart(fig_box)
st.markdown('''
This is a box-plot for comparing the three religious schools (Brigham Young University, Baylor University, and Texas Christian University) against the remaining 11 non-religious universities.  
''')

# Add a section for links
st.title('Links')
st.markdown('''
* [GitHub repository for Code](https://github.com/hermite2010/Stat_386_Final_Project)
* [Data Gathering Blog Post](https://hermite2010.github.io/2023/11/30/Gathering_The_Data.html)
* [EDA Blog Post](https://hermite2010.github.io/2023/12/01/Final_Report.html)
''')



