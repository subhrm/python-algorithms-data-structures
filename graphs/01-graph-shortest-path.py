#%% imports 
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
# %%
# Create an empty graph
G = nx.Graph()  
# Add nodes to the graph
G.add_nodes_from([1,2,3,4,5,6,7,8])
# Add edges to the graph
G.add_weighted_edges_from([
[1,2,5],
[1,5,2],
[1,7,5],
[2,3,6],
[2,5,2],
[3,4,7],
[3,5,3],
[4,6,5],
[4,8,2],
[5,6,1],
[5,7,2],
[6,7,2],
[6,8,1],
[7,8,2]])
# %%
# extract weights from the graph
weights = nx.get_edge_attributes(G,'weight')
pos=nx.spring_layout(G)
# pos=nx.spectral_layout(G)
nx.draw(G, pos, with_labels=True, edge_color='red', node_color='yellow')
_=nx.draw_networkx_edge_labels(G,pos,edge_labels=weights)
# %%
path = nx.shortest_path(G,1,4, weight='weight')
print(path)
path_length = nx.shortest_path_length(G,1,4, weight='weight')
print(path_length)
# %%
