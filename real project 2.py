#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


car=pd.read_csv("2. Cars Data1.csv")


# In[18]:


car.head(31)


# In[5]:


car.info()


# In[6]:


car.describe()


# In[8]:


car.shape


# In[11]:


car.isnull().sum()


# In[20]:


car.drop(labels=[30,39,161,173] , inplace=True)


# In[21]:


car.isnull().sum()


# In[22]:


car['Cylinders'].fillna(car['Cylinders'].mean(),inplace =True)


# In[23]:


car.isnull().sum()


# # different types of Make in our datasets

# In[25]:


car['Make'].unique()


# In[27]:


car['Make'].value_counts()


# # filtering

# In[28]:


car['Origin'].unique()


# > show all records where Origin is asia and usa

# In[32]:


car[car['Origin'].isin(['Asia','USA'])]


# > remove all the data for weight > 4200

# In[33]:


car.head(2)


# In[36]:


car[~(car['Weight']>4200)]


# # using a function

# show all the records after increasing MPG_city value by 4

# In[37]:


car['MPG_City']=car['MPG_City'].apply(lambda x:x+3)


# In[38]:


car


# In[ ]:




