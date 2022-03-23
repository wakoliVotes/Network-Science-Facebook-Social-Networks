#!/usr/bin/env python
# coding: utf-8

# #                             Final Report Presentation

# 
# ###          GROUP 5 MEMBERS:
# 
# ###            20/04694 Votes Wakoli
# ###            18/06864 Kisang Alex
# ###            19/05533 Nicasio Mugendi
# ###           19/02533 Nelson Mandelas
# 
# 
# ###         Date: 23rd March 2022

# ### Project Overview
# 
# - The project focuses on Facebook connections
# - To complete the project, we used existing data "Facebook Large Page-Page Network Data Set" from Kaggle online database
# - The dataset has two columns and 171002 rows
# - Nodes represent Official Facebook Pages while the Links/Edges are mutual likes between sites
# - Facebook ids with similar likes in Column1 are matched with Facebook ids with similar likes in column 2
# 
# 
# Link to dataset https://www.kaggle.com/ishandutta/facebook-large-pagepage-network-data-set

# ### PART 1: Getting Our Project Data Ready

# In[2]:


# Our dataset is a comma separated value (csv) file of two columns of facebook ids and connections
# To use the data, we used pandas to read the data as shown below
import pandas as pd
mydata = pd.read_csv(r"D:\KCA\Network Science\Facebook_Network_Edges.csv")


# #### Scenario 1 with All Data Items

# In[3]:


# Overview of the Data Frame
mydata.head(n=20)


# In[8]:


# We are interested to show connections between the FaceBook pages and other Pages
# Hence, we need to trim the dataframe into needed columns and store in new dataframe for manipulation
# In this case, from our dataframe above, we have, 'facebook_id_1', 'facebook_id_2'
# We created a new dataframe, so that in case of any changes, the original remains intact

mydata1 = mydata[['Facebook_id_1', 'Facebook_id_2']]


# In[9]:


# Getting an overview of the New Dataframe that we will manipulate
mydata1.head


# ### Part 2: Graphing Networks

# In[10]:


# First, we created the World into which the Graph will exist
# Here, we needed the NetworkX Python Package, as shown below
# The name of our graph is "GG"

import networkx as nx
GG = nx.Graph()


# In[11]:


# We can check the Graph for nodes and edges as below
GG.nodes()       # Gives empty since we have not added any Nodes yet


# In[12]:


GG.edges()      # Gives empty since we have not added any edges yet


# In[14]:


# Our dataset is in columns and rows
# Adding the edges using pandas to created Graph 'GG'
GG = nx.from_pandas_edgelist(mydata1, 'Facebook_id_1', 'Facebook_id_2')


# In[15]:


# Checking the NEW outlook of the Graph based on Nodes
GG.nodes()


# In[16]:


# Checking the outlook of the Graph based on Edges
GG.edges()


# In[17]:


# Now, we need to visualize the Graph 'GG'
# Here, matplotlib.pyplot Python library was used to make this possible

from matplotlib.pyplot import figure
figure(figsize=(200, 200))                                    # Specifying the figure size
nx.draw_shell(GG,  with_labels=True, node_color='red')


# ### PART 3: Making Adjustments

# ####    As shown above, the created graph using all the collected data is challenging to explain
# ####   To make this simple, we selected only the first 200 items from the total 171002 in the original data

# In[3]:


import pandas as pd
datafile = pd.read_csv(r"C:\Users\User\Documents\Machine Learning\Network Science\new_data_500_items.csv")


# In[5]:


datafile.head(20)


# In[13]:


data500 = datafile.head(200)


# In[14]:


data500.head(20)


# In[15]:


# Creating new graph GS that will form the world for the connections

import networkx as nx
GS = nx.Graph()


# In[16]:


GS = nx.from_pandas_edgelist(data500, "Facebook_id_1", "Facebook_id_2")


# In[17]:


GS.nodes()


# In[18]:


# Now, we need to visualize the Graph 'Gs', using matplotlib.pyplot library

from matplotlib.pyplot import figure
figure(figsize=(100, 100))                                    # Specifying the figure size
nx.draw_shell(GS,  with_labels=True, node_color='red')


# In[37]:


from matplotlib.pyplot import figure
figure(figsize=(100, 100))                                    # Specifying the figure size
nx.draw_planar(GS,  with_labels=True, node_color='red')


# In[39]:


from matplotlib.pyplot import figure
figure(figsize=(50, 50))                                    # Specifying the figure size
nx.draw_networkx(GS,  with_labels=True, node_color='red')


# ## PART 4: Connection Degree

# ### Next, we also created another dataframe that shows the nodes and their number of connections.

# In[35]:


# Using online resources, the following scripts helped depict the nodes and number of connections on each

connectionsBoard = {}
for x in GS.nodes:
    connectionsBoard[x] = len(GS[x])
s = pd.Series(connectionsBoard, name='Connections')
connectionDataframe = s.to_frame().sort_values('Connections', ascending = False)


# In[36]:


connectionDataframe.head(50)


# In[ ]:


# From the information above, person 14 (node 14) has the largest connections[links], and hence highest degree
# This is also evident as shown in the network connection representation/graph above


# ###  Group Members Discussion Meetup Day Logs
# Day                  Present         Absent and Reason
# 8  Feb 2022          All 4 members    None
# 11 Feb 2022          All 4 members    None
# 18 Feb 2022          All 4 Members    None
# 25 Feb 2022          3 Members        1 - Internal Exams
# 4  March 2022        All 4 Members    None
# 11 March 2022        All 4 Members    None
# 15 March 2022        All 4 Members    None
# 22 March 2022        All 4 Members    None

# ### GitHub Link
# 
# https://github.com/danny-votez/Network-Science-Facebook-Social-Networks/blob/main/README.md
