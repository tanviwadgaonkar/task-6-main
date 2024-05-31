#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv(r"C:\Users\Tanvi\Downloads\disney_plus_titles.csv")
df


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.isna().sum()


# In[6]:


df.hist(bins=25,grid=True,figsize=(20,25))


# In[7]:


df.info()


# In[8]:


df.describe()


# In[11]:


#1.How to count the occurrences of each year in the release_year column? 
df.release_year.value_counts()


# In[18]:


df.release_year.value_counts().plot(kind='bar',color=('Khaki'))
plt.title('release in a year')
plt.xlabel('release')
plt.ylabel('year')
plt.show()


# In[21]:


df.release_year.value_counts().plot(kind='pie')
plt.title('release per year')
plt.legend('release','year')
plt.show()


# In[22]:


#2.no of movies and tv shows?
df.type.value_counts()


# In[25]:


df.type.value_counts().plot(kind='bar', color=('orange','lightblue'))
plt.title('Movie vs tv shows')
plt.xlabel('movie')
plt.ylabel('tv shows')
plt.show()


# In[26]:


#3.movies and tv shows release per year
pd.crosstab(df.type,df.release_year)


# In[58]:


plt.figure(figsize=(25, 20))
sns.countplot(data=df, x='release_year', hue='type')
plt.title('Movies and TV Shows Released per Year')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.show()


# In[33]:


#4 what is the duration 
df.duration.value_counts()


# In[56]:


plt.figure(figsize=(25, 20))
sns.displot(x='duration',data=df,bins=25,kde=True)


# In[42]:


#what is per duration of movies and tv shows
pd.crosstab(df.type,df.duration)


# In[55]:


plt.figure(figsize=(25, 20))
sns.countplot(data=df, x='duration', hue='type', palette='viridis')
plt.title('Movies and TV Shows total duration')
plt.xlabel('duration')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
plt.show()


# In[ ]:




