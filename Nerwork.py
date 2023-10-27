import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
'''
G.add_node(1)               # add one node
G.add_node(2)
G.add_node(3)

G.add_edge(1,2)             # add one edge
G.add_edge(3,2)
G.add_edge(1,3)
'''

l = [1,2,3]

G.add_nodes_from(l)          # add nodes from a list,tuple or any ds

G = nx.complete_graph(10)   # all nodes are connected to each other

G = nx.gnp_random_graph(20,0.2)     # random graph (no. of nodes, degree of connections)

G = nx.barabasi_albert_graph(50,2)
print(G.nodes())
print(G.edges())

nx.draw(G)
plt.show()

nx.write_gexf(G,"test.gexf")
# index(ele,beg,end)  retuens the 1st index of ele after beg and before end

# Gephi - software to view gexf
