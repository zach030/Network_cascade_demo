import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()  # or DiGraph, MultiGraph, MultiDiGraph, etc
G.add_node(1)
G.add_node(2)
nx.draw_networkx(G)
#nx.draw_networkx_nodes(G, pos=nx.circular_layout(G))
plt.show()
G.add_edge(1, 2)
# G.add_edges_from([1, 2])
# nx.draw_networkx_edges(G, pos=nx.circular_layout(G))
nx.draw_networkx(G)
#nx.draw_networkx_nodes(G, pos=nx.circular_layout(G))
plt.show()
