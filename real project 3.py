#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pl=pd.read_csv("3. Police Data.csv")


# In[3]:


pl.head()


# In[5]:


pl.describe()


# In[10]:


pl.info()


# # NULL COLUMNS

# In[9]:


pl.isnull().sum()


# In[11]:


pl.shape


# In[13]:


pl.drop(labels=['country_name','search_type'],axis=1,inplace = True)


# In[14]:


pl.head(2)


# # For speeding , were men or women stopped more often

# In[16]:


pl.head(2)


# In[19]:


pl[pl['violation']=='Speeding'].driver_gender.value_counts()


# # Does gender effect who gets searched during a stop

# In[21]:


pl.head(2)


# In[27]:


pl.groupby('driver_gender').search_conducted.sum()


# # Mapping 

# In[28]:


pl['stop_duration'].value_counts()


# In[29]:


pl['stop_duration']= pl['stop_duration'].map({'0-15 Min':7.5,'16-30 Min':24,'30+ Min':45})


# In[32]:


pl['stop_duration'].mean()


# In[34]:


pl.head(2)


# In[35]:


pl['driver_age'].mean()


# In[37]:


pl['driver_age'].describe()


# In[49]:





# In[ ]:




