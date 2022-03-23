## Network-Science-Facebook-Social-Networks
### Table of Contents
- [Project Overview](#project-overview)
- [Graph Representations](#graph-representations)
- [Conclusion](#conclusion)
### Project Overview

- The project focuses on Facebook connections
- To complete the project, we used existing data "**Facebook Large Page-Page Network Data Set**" from **Kaggle** Database
- The dataset has two columns and 171002 rows
- Nodes represent Official Facebook Pages while the Links/Edges are mutual likes between sites
- Facebook ids with similar likes in Column1 are matched with Facebook ids with similar likes in column 2
- See dataset used on **[Kaggle](https://www.kaggle.com/ishandutta/facebook-large-pagepage-network-data-set)**

### PART 1: Getting Our Project Data Ready
- Our dataset is a comma separated value (csv) file of two columns of facebook ids and connections
- To use the data, we used pandas to read the data as shown below

```py

import pandas as pd
mydata = pd.read_csv(r"D:\KCA\Network Science\Facebook_Network_Edges.csv")
# Overview of the Data Frame
mydata.head

```
<img width="400" height="250" src="https://user-images.githubusercontent.com/77758884/159596832-3c7486bb-b02b-4907-b029-15c3d8a14f43.png" >


### Graph Representations
```py

# First, we created the World into which the Graph will exist
# Here, we needed the NetworkX Python Package, as shown below
# The name of our graph is "GG"
​
import networkx as nx
GG = nx.Graph()

# We can check the Graph for nodes as below
GG.nodes()       # Gives empty since we have not added any Nodes yet
NodeView(())

# We can also check the Graph for edges as below
GG.edges()      # Gives empty since we have not added any edges yet
EdgeView([])
```
- Our dataset is in columns and rows. Next, adding the edges using pandas to created Graph 'GG'
```py
GG = nx.from_pandas_edgelist(mydata1, 'Facebook_id_1', 'Facebook_id_2')

# Next, checking the NEW outlook of the Graph based on Nodes
GG.nodes()

# Next, we can also check the Graph outlook based on Edges
GG.nodes()
```
### Visualizing Graph GG
```py
# Now, we need to visualize the Graph 'GG'
# Here, matplotlib.pyplot Python library was used to make this possible

from matplotlib.pyplot import figure
figure(figsize=(200, 200))                                    # Specifying the figure size
nx.draw_shell(GG,  with_labels=True, node_color='red')
```
- **Below is the Original Dataset's Graph**

### Conclusion
- The network representation is based on past data **[Facebook Large Page-Page Network Data Set](https://www.kaggle.com/ishandutta/facebook-large-pagepage-network-data-set)** uploaded by **Ishan Dutta**
