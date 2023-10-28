import networkx as nx


G = nx.barbell_graph(4,2)  
# two communities connected by a sequence of nodes
# barbell_graph(no. of nodes in one community,no. of nodes b/w them)        
nx.draw(G)

G = nx.complete_graph(4)        # no. of nodes
nx.draw(G)

G = nx.cycle_graph(6)        # no. of nodes
nx.draw(G)

G = nx.ladder_graph(4)        # no. of nodes in parallel edges
nx.draw(G)

G = nx.path_graph(4)        # no. of nodes
nx.draw(G)

G = nx.star_graph(5)        # no. of nodes on corners except middle
nx.draw(G)

G = nx.wheel_graph(8)        # no. of nodes including middle
nx.draw(G)

G = nx.gnp_random_graph(5,0.5)        # no. of nodes including middle
nx.draw(G)

