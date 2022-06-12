#%% import
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
# %%
# Create an empty graph
G = nx.DiGraph()
# Add nodes to the graph
G.add_nodes_from([1], layer=0)
G.add_nodes_from([2,3,4,5], layer=1)
G.add_nodes_from([6,7,8,9], layer=2)
G.add_nodes_from([10], layer=3)
# Add edges to the graph
G.add_weighted_edges_from([
[1,2,10],
[1,3,5],
[1,4,10],
[1,5,5],
[2,6,5],
[2,7,5],
[3,7,3],
[3,8,1],
[4,7,3],
[4,8,2],
[4,9,5],
[5,8,4],
[5,9,4],
[6,10,10],
[7,10,2],
[8,10,10],
[9,10,5]
])
weights = nx.get_edge_attributes(G,'weight')
pos=nx.multipartite_layout(G, subset_key="layer")
nx.draw(G, pos, with_labels=True, edge_color='red', node_color='yellow')
_=nx.draw_networkx_edge_labels(G,pos,edge_labels=weights, label_pos=0.3)
# %%
max_flow, capacity = nx.maximum_flow(G, 1, 10, capacity="weight")
print(max_flow)
# %%
capacity
# %%
cut_value, min_cut = nx.minimum_cut(G, 1, 10, capacity="weight")
print(min_cut)
# %%
