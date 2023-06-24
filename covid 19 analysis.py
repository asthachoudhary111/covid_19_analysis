#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[4]:


covid_df=pd.read_csv("C:/Users/ACER/Downloads/covid-india/covid_19_india.csv")


# In[5]:


covid_df


# In[4]:


covid_df.info()


# In[5]:


covid_df.describe()


# In[6]:


vaccine_df= pd.read_csv("C:/Users/ACER/Downloads/covid_statewise/covid_vaccine_statewise.csv")


# In[7]:


vaccine_df.head(7)


# # data cleaning

# In[8]:


covid_df.drop(["Sno", "Time" , "ConfirmedIndianNational" , "ConfirmedForeignNational"], inplace = True , axis = 1)


# In[9]:


covid_df.head()


# In[10]:


# covid_df['Date'] = pd.to_datetime(covid_df['Date'],format = '%d/%m/%Y')


# In[11]:


#active cases

covid_df['Active_Cases']= covid_df['Confirmed']-(covid_df['Cured']+covid_df['Deaths'])
covid_df.tail()


# In[12]:


statewise = pd.pivot_table(covid_df,values=["Confirmed","Deaths","Cured"],index="State/UnionTerritory",aggfunc = max)


# In[13]:


statewise["Recovery Rate"] = statewise["Cured"]*100/statewise["Confirmed"]


# In[14]:


statewise["Mortality Rate"] = statewise["Deaths"]*100/statewise["Confirmed"]


# In[15]:


statewise= statewise.sort_values(by= "Confirmed",ascending = False)


# In[16]:


statewise.style.background_gradient(cmap="cubehelix")


# In[17]:


#top 10 active cases states

top_10_active_cases =covid_df.groupby(by= 'State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by= ['Active_Cases'],ascending = False).reset_index()


# In[18]:


fig=plt.figure(figsize=(16,9))


# In[19]:


plt.title("Top 10 states with most active cases in India",size = 25)


# In[20]:


ax =sns.barplot(data = top_10_active_cases.iloc[:10],y="Active_Cases",x="State/UnionTerritory",linewidth=2,edgecolor='red')


# In[21]:


top_10_active_cases =covid_df.groupby(by= 'State/UnionTerritory').max()[['Active_Cases','Date']].sort_values(by= ['Active_Cases'],ascending = False).reset_index()
fig= plt.figure(figsize=(20,5))
plt.title("Top 10 states with most active cases in India",size = 25)
ax =sns.barplot(data = top_10_active_cases.iloc[:11],y="Active_Cases",x="State/UnionTerritory",linewidth=2,edgecolor='red')
plt.xlabel("States")
plt.ylabel("Total Active Cases")
plt.show()


# In[22]:


#top states with highest deaths

top_10_deaths = covid_df.groupby(by= 'State/UnionTerritory').max()[['Deaths','Date']].sort_values(by=['Deaths'],ascending = False).reset_index()
fig=plt.figure(figsize=(18,5))
plt.title("Top 10 states with most Deaths",size = 25)
ax = sns.barplot(data=top_10_deaths.iloc[:10],y="Deaths",x="State/UnionTerritory",linewidth = 2 ,edgecolor="black")
plt.xlabel("States")
plt.ylabel("Total Death Cases")
plt.show()
                
    


# In[23]:


#growth trend

# fig = plt.figure(figsize =(12,6))

# ax=sns.lineplot(data=covid_df[covid_df['State/UnionTerritory'].isin(['Maharastra'],['Delhi'],['Tamil Nadu'],['Gujarat'],['Uttar Pradesh']),x='Date', y = 'Active_Cases',hue = 'State/UnionTerritory'])


# ax.set_title("Top 5 affected states in India",size = 16)


# In[24]:


vaccine_df.head()


# In[25]:


vaccine_df.rename(columns={'Updated On': 'Vaccine_Date'},inplace = True)


# In[26]:


vaccine_df.head(10)


# In[27]:


vaccine_df.info()


# In[28]:


vaccine_df.isnull().sum()


# In[ ]:





# In[30]:


vaccination = vaccine_df.drop(columns= ['Sputnik V (Doses Administered)','AEFI','18-44 Years (Doses Administered)','45-60 Years (Doses Administered)','60+ Years (Doses Administered)'],axis =1)


# In[31]:


vaccination.head()


# In[34]:


#male vs female vaccination

male = vaccination["Male(Individuals Vaccinated)"].sum()
female = vaccination["Female(Individuals Vaccinated)"].sum()
px.pie(names=["Male", "Female"],values =[male, female],title = "Male and Female Vaccination")


# In[35]:


#REMOVE ROWS WHERE STATE = INDIA
   
vaccine= vaccine_df[vaccine_df.State!='India']
vaccine


# In[41]:


vaccine.rename(columns = {"Total Individuals Vaccinated": "Total"},inplace = True)
vaccine.head()


# In[45]:


#most vaccinated state

max_vac= vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac= max_vac.sort_values('Total', ascending = False)[:5]
max_vac


# In[47]:


fig = plt.figure(figsize = (10,5))
plt.title("Top 5 Vaccinated States in India",size =20)
x = sns.barplot(data= max_vac.iloc[:10],y = max_vac.Total, x=max_vac.index,linewidth=2,edgecolor='black')
plt.xlabel("States")
plt.ylabel("Vaccination")
plt.show()


# In[ ]:




