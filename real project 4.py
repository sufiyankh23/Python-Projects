#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[4]:


df=pd.read_csv("4. covid_19_data.csv")


# In[5]:


df.head()


# In[6]:


df.describe()


# In[7]:


df.info()


# In[8]:


df.shape


# In[10]:


df.isnull().sum()


# In[11]:


import seaborn as sns 


# In[12]:


import matplotlib.pyplot as plt


# In[14]:


sns.heatmap(df.isnull())
plt.show


# # Number of confirmed,deaths and recovered cases in each region

# In[16]:


df.head(2)


# In[29]:


df.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(15)


# In[26]:


df.groupby('Region').sum()


# In[32]:


df.groupby('Region')['Confirmed','Recovered'].sum().head(20)


# # remove all the records having confirmed cases less than 10

# In[33]:


import pandas as pd


# In[35]:


df.head(2)


# In[41]:


df=df[~(df.Confirmed < 10)]


# # Region with max number of deaths

# In[51]:


df.groupby('Region')['Deaths'].sum().sort_values(ascending=False)


# # Sorting by column

# In[53]:


df.sort_values(by = 'Confirmed',ascending = True).head(30)


# In[ ]:




