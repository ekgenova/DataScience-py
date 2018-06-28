
# coding: utf-8

# In[32]:


import pandas
df = pandas.read_csv("C:\\Users\\Admin\\Downloads\\Wine_Data_Unclean.csv")


# In[41]:


df['variety'] = df.variety_and_region.str.split('/').str.get(0)


# In[42]:


df['region1'] = df.variety_and_region.str.split('/').str.get(1)


# In[43]:


df['region2'] = df.variety_and_region.str.split('/').str.get(2)


# In[44]:


df = df.drop(columns=['variety_and_region','Unnamed: 0'])


# In[45]:


df.to_csv('C:\\Users\\Admin\\Downloads\\Wine_Data_Clean.csv', index='false', header='false')


# In[46]:


df

