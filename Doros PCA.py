#!/usr/bin/env python
# coding: utf-8

# In[2]:



from sklearn.decomposition import PCA as sklearnPCA

from sklearn import datasets
from sklearn import linear_model, svm, tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from scipy.cluster.hierarchy import dendrogram, linkage 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


data = pd.read_csv("Datasets/dorothea_smaller.csv")


# In[4]:


#print(data.describe)


# In[5]:


doros_x=pd.DataFrame(data[data],columns=data.feature_names) #these will be x in our model
doros_y=data.target # these will be y in our model


# In[ ]:


#from sklearn.model_selection import train_test_split
# = train_test_split(doros, test_size=0.30, random_state=5)
#print(X_train.shape, X_test.shape)


# In[1]:


#def pca(doros, k):
    #pca = sklearnPCA(n_components = k)
    #PCA_projected_doros = pca.fit_transform(doros)
    #return PCA_projected_doros


# In[ ]:





# In[ ]:




