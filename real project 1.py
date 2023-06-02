#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[5]:


data= pd.read_csv("1. Weather Data.csv")


# In[6]:


data 


# In[7]:


data.head() 


# In[9]:


data.shape


# In[10]:


data.index


# In[11]:


data.columns


# In[12]:


data.dtypes


# In[17]:


data['Weather'].unique()


# In[18]:


data.nunique()


# In[19]:


data['Weather'].value_counts()


# In[20]:


data.info()


# # All unique wind speeds values in data

# In[24]:


data['Wind Speed_km/h'].unique()


# #  Number of times when weather is all cloudy

# In[31]:


#data.head(2)
data[data.Weather=='Cloudy']


# # Number of times when the wind speed is exactly 7 km/h

# In[38]:


#data.head(2)
data[data['Wind Speed_km/h']==7]


# # All null values

# In[39]:


data.isnull().sum()


# # Rename 'Weather' column to 'Weather condition'

# In[42]:


data.rename(columns = {'Weather':'Weather condition'}, inplace=True)


# In[43]:


data.head()


# In[47]:


#data.head(2)
data['Visibility_km'].mean()


# # Standard deviation of press

# In[49]:


data['Press_kPa'].std()


# # All instances when snow was recorded

# In[55]:


#data.head(2)
data[data['Weather condition']=='Snow']


# In[56]:


data['Weather condition'].value_counts()


# In[58]:


data[data['Weather condition'].str.contains('Snow')]


# # Instances when wind speed is greater than 20 and visibility is 25

# In[64]:


#data.head(2)
data[(data['Wind Speed_km/h']>20) & (data['Visibility_km']==25)]


# # Mean against Weather condition

# In[67]:


#data.head(2)
data.groupby('Weather condition').mean()


# # Min and max value against Weather condition

# In[68]:


data.groupby('Weather condition').min()


# In[69]:


data.groupby('Weather condition').max()


#  # All the instances when weather is 'clear' or visibility is above '30'

# In[77]:


#data.head(2)
data[(data['Weather condition']=='Clear') | (data['Visibility_km']>30)]


# In[ ]:




