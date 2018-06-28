
# coding: utf-8

# In[1]:


import sklearn
import pandas
import math
rawBCD = pandas.read_csv("C:\\Users\\Admin\\Downloads\\BreastCancerData.csv")


# In[2]:


BCD_noID = rawBCD.drop(columns='842302')


# In[6]:


BCD_noResults = BCD_noID.drop(columns='M')


# In[3]:


FeatureScaling = lambda x: ((x- min(x))/(max(x)-min(x)))


# In[7]:


BCD_Normalised = BCD_noResults.apply(FeatureScaling)


# In[13]:


BCD_Training = BCD_Normalised[0:450]


# In[75]:


BCD_TrainingNormal = BCD_Training.apply(FeatureScaling)


# In[18]:


from sklearn.neighbors import KNeighborsClassifier
K_value = math.floor(math.sqrt(len(BCD_Training.index)))
knn = KNeighborsClassifier(n_neighbors=K_value)


# In[44]:


from sklearn.model_selection import train_test_split
X = BCD_Normalised.iloc[:, 0:].values
y = BCD_noID.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.33)
X


# In[33]:


BCD_Prediction = knn.fit(X_train,y_train)


# In[35]:


predict = knn.predict(X_test)


# In[36]:


from sklearn.metrics import classification_report, confusion_matrix


# In[37]:


print(confusion_matrix(y_test, predict))


# In[38]:


print(classification_report(y_test, predict))

