#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd

# Loading the dataset
df = pd.read_csv('brain_tumor_dataset.csv')

#Displaying the first few rows of the dataset
df.head()


# In[18]:


# Displaying basic information about the dataset
df.info()

# Checking for missing values
df.isnull().sum()


# In[19]:


# Descriptive statistics for numerical columns
df.describe()


# In[20]:


import plotly.express as px

# Interactive Tumor Type Distribution
fig = px.histogram(df, x='Tumor Type', color='Tumor Type', title='Distribution of Tumor Types', nbins=10)
fig.update_layout(
    xaxis_title='Tumor Type',
    yaxis_title='Count',
    font=dict(size=14),
    width=400,
    height=500
)
fig.show()


# In[5]:


# Interactive Patient Age Distribution
fig = px.histogram(df, x='Patient Age', nbins=30, color='Gender', title='Distribution of Patient Ages')
fig.update_layout(
    xaxis_title='Patient Age',
    yaxis_title='Count',
    font=dict(size=12),
    width=800,
    height=600
)
fig.show()


# In[21]:


# Interactive Boxplot of Size (cm) by Tumor Type
fig = px.box(df, x='Tumor Type', y='Size (cm)', color='Tumor Type', title='Tumor Size by Tumor Type')
fig.update_layout(
    xaxis_title='Tumor Type',
    yaxis_title='Size (cm)',
    font=dict(size=14),
    width=800,
    height=600
)
fig.show()


# In[22]:


# Interactive Boxplot of Size (cm) by Location
fig = px.box(df, x='Location', y='Size (cm)', color='Location', title='Tumor Size by Location')
fig.update_layout(
    xaxis_title='Location',
    yaxis_title='Size (cm)',
    font=dict(size=14),
    width=800,
    height=600
)
fig.show()


# In[23]:


# Interactive Boxplot of Patient Age by Gender
fig = px.box(df, x='Gender', y='Patient Age', color='Gender', title='Patient Age by Gender')
fig.update_layout(
    xaxis_title='Gender',
    yaxis_title='Patient Age',
    font=dict(size=14),
    width=800,
    height=600
)
fig.show()


# In[26]:


import numpy as np
np.random.seed(0)
time_series_data = pd.DataFrame({
    'Time': np.arange(1, 101),
    'Tumor Type': np.random.choice(df['Tumor Type'].unique(), size=100),
    'Count': np.random.randint(1, 10, size=100)
})
time_series_data = time_series_data.groupby(['Time', 'Tumor Type']).sum().reset_index()

# Create an animated bar chart
fig_animated_bar = px.bar(time_series_data, x='Tumor Type', y='Count', animation_frame='Time', 
                          color='Tumor Type', range_y=[0, 50], 
                          title='Animated Distribution of Tumor Types Over Time',
                          labels={'Tumor Type': 'Tumor Type', 'Count': 'Count', 'Time': 'Time'})

fig_animated_bar.update_layout(
    xaxis_title='Tumor Type',
    yaxis_title='Count',
    font=dict(size=14),
    width=800,
    height=600
)


# In[ ]:




