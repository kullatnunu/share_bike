#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


get_ipython().run_line_magic('time', 'df = pd.read_csv("./status.csv")')


# In[4]:


df.head()


# In[40]:


datime = df["time"]
datime = datime.astype(str)
datime = datime.str.split(" ",expand=True)


# In[41]:


date=datime.loc[:,0].str.split("/",expand=True)
time=datime.loc[:,1].str.split(":",expand=True)
datetime = pd.concat([date,time],axis=1)
datime_concat = pd.concat([df,datetime],axis=1)
datime_concat.columns=(['station_id','bikes_available','docks_available','time','year','month','day','hour','min','sec'])
datime_concat.head(10)


# In[43]:


len(datime_concat)


# In[42]:


datime_concat['dock'] = datime_concat['bikes_available']+datime_concat['docks_available']
datime_concat['dock_shift'] = datime_concat['docks_available'].shift()
datime_concat['retu_borr'] = datime_concat['docks_available']-datime_concat['dock_shift']
datime_concat.loc[datime_concat['retu_borr']>0,'retu']=1
datime_concat['retu']=datime_concat['retu'].fillna(0)
datime_concat.loc[datime_concat['retu_borr']<0,'borr']=1
datime_concat['borr']=datime_concat['borr'].fillna(0)

datime_concat['min']=datime_concat['min'].astype('int32')
datime_concat.loc[datime_concat['min']<=30,'to_half']=1
datime_concat['to_half']=datime_concat['to_half'].fillna(0)

# datime_concat.loc[datime_concat['min']>30,'to_one']=1
# datime_concat['to_one']=datime_concat['to_one'].fillna(0)

datime_concat_value = datime_concat.groupby(['station_id','year','month','day','hour','to_half'])['borr'].sum().reset_index()


# In[44]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('seaborn-white')
plt.hist(datime_concat_value)


# In[ ]:




