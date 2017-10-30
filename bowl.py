
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as  plt
import math 


# In[3]:


df1=pd.read_csv('./cricket/india-bowling.csv')
df2=pd.read_csv('./cricket/australia-bowling.csv')


# In[4]:


df1=df1[df1['Overs'].str.contains('DNB')==False]
df2=df2[df2['Overs'].str.contains('DNB')==False]


# In[5]:


df1[['Maidens','Overs','Runs','Wickets']]=df1[['Maidens','Overs','Runs','Wickets']].astype(float)
df2[['Maidens','Overs','Runs','Wickets']]=df2[['Maidens','Overs','Runs','Wickets']].astype(float)
del df1['Inns']
del df2['Inns']


# In[6]:


grouped1=df1.groupby('Player')
df1=grouped1.agg(sum)
grouped2=df2.groupby('Player')
df2=grouped2.agg(sum)


# In[7]:


def ovr(x):
    dec,int_=math.modf(x)
    if(dec>=0.6):
        dec=dec-0.6
        num=int_+1+dec
    else:
        num=int_+dec
    return num


# In[14]:


df1['Overs']=df1['Overs'].apply(ovr)
df2['Overs']=df2['Overs'].apply(ovr)


# In[9]:


df1['rpo']=df1['Runs']/df1['Overs']
df2['rpo']=df2['Runs']/df2['Overs']
df1['rpw']=df1['Runs']/df1['Wickets']
df2['rpw']=df2['Runs']/df2['Wickets']

dfr1=df1.sort_values('rpo')
dfw1=df1.sort_values('rpw')
dfr2=df2.sort_values('rpo')
dfw2=df2.sort_values('rpw')


# In[10]:


del df1['rpw']
del df2['rpw']
df2


# In[11]:


df1.to_csv('indbow')
df2.to_csv('ausbow')


# In[12]:


dfr1=dfr1.head(1)
dfr2=dfr2.head(1)
dfr=pd.concat([dfr1,dfr2])
dfw1=dfw1.head(1)
dfw2=dfw2.head(1)
dfw=pd.concat([dfw1,dfw2])
get_ipython().magic('matplotlib inline')
dfr


# In[13]:


fig, axes = plt.subplots(nrows=1, ncols=2)
dfr=dfr.T.plot(title='BEST BOWLERS MEASURED RUNS PER OVER',ax=axes[0],kind='bar',figsize=(15,5),rot=20)
dfr.set(xlabel='Bowlers Attribute',ylabel='Values')
dfw=dfw.T.plot(title='BEST BOWLERS MEASURED RUNS PER WICKET',ax=axes[1],kind='bar',figsize=(15,5),rot=20)
dfw.set(xlabel='Bowlers Attribute',ylabel='Values')

