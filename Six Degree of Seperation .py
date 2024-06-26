import networkx as nx
import numpy

G = nx.read_edgelist("facebook_content.txt")
N = list(G.nodes())

spll = []

for u in N:
    for v in N:
        if u != v:
            l = nx.shortest_path_length(G, u,v)
            print("The shortest path b/w ",u," and ",v," is ",l)
            
            spll.append(l)
            
min_spl = min(spll)
max_spl = max(spll)
avg_spl = numpy.average(spll)

print("Minimum shortest path length is ",min_spl)
print("Maximum shortest path length is ",max_spl)
print("Average shortest path length is ",avg_spl)

