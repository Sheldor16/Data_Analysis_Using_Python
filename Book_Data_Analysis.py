#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/vaibh/Downloads/books/books.csv')
df.head(5)


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


# CLEANING THE DATASETS

# Dropping the null values

df.dropna(inplace=True)
df.isnull().sum()


# In[6]:


# Dropping the unncessary variables

df.drop(columns=['cover','isbn','link','image','paper'],
       inplace = True)
df.columns


# In[7]:


df.head(5)


# In[10]:


# Removing Duplicated Values

df = df.drop_duplicates(subset = ['title'])
df.drop(df[df['reviews'] == 0].index, inplace = True)
df.drop(df[df['rating'] == 0].index, inplace = True)
df.head(5)


# In[19]:


# RESHAPING AND EDA

df['discount_rate_num'] = df['discount_rate'].str.slice(1,).astype(int)
df['new_date'] = df['date'].str.slice(0,4)
df.drop(df[df['new_date']=='unkn'].index, inplace=True)
df['new_date'] = df['new_date'].astype(int)

# Converting column-price datatype from object to float type

df['price'] = df['price'].str.slice(0,3).astype(float)
df.info()




# In[23]:


# VISUALIZING NUMERICAL VARIABLES

df.hist( bins = 10, figsize=(28,20))
plt.show()


# In[24]:


# HEATMAP

plt.figure(figsize=(10,8))
sns.set_context('paper', font_scale=1.4)

df_corr = df.corr()
sns.heatmap(df_corr, annot = True, cmap = 'Oranges')


# In[27]:


sns.displot(df, x='new_date', y = 'price', bins = 20)
plt.xlabel('YEARS')
plt.ylabel('PRICES')
plt.title('BOOK PRICES VS YEARS')
plt.show()


# In[30]:


# BEST 5 AUTORS ( ACCORDING TO BEST RATINGS )

df[df['rating'] == 5]['author'].value_counts().head(5)


# In[32]:


plt.figure(figsize=(10,15))
values = [894,876,103,88,82]
labels = ['unknown','Kolektif','Mustafa Orakçı','Birsen Ekim Özen',
         'Stefan Zweig']
plt.title(' BEST FIVE AUTHORS - ACCORDING TO RATINGS', fontsize = 30)
colors = sns.color_palette('pastel')
plt.pie(values, labels = labels, colors = colors, autopct = '%0.0f%%')
plt.show()


# In[37]:


top_five_reviews = df.sort_values(
    by =['reviews'], ascending = False)['reviews'].head(5)

top_five_title = df.sort_values(
    by =['reviews'], ascending = False)['title'].head(5)

top_five_authors = df.sort_values(
    by =['reviews'], ascending = False)['author'].head(5)

y = []
m = []

for j in top_five_reviews:
    y.append(j)
    
for k in top_five_title:
    m.append(k)
    
    
plt.figure(figsize = (15,7))
sns.barplot(x=m, y=y, data=df, palette = 'Blues_d')
plt.xlabel(' TITLES OF THE BOOKS')
plt.ylabel('NUMBER OF REVIEWS')
plt.title('TOP 5 BOOKS WITH THE HIGHEST REVIEWS', fontsize = 15)
plt.show()


# In[ ]:




