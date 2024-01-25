# Importing necessary libraries
import networkx as nx
import random
import matplotlib.pyplot as plt
import operator

# Generating a directed random graph with 10 nodes and edge probability of 0.5
G = nx.gnp_random_graph(10, 0.5, directed=True)

# Drawing the graph with node labels
nx.draw(G, with_labels=True)
plt.show()

# Selecting a random starting node
x = random.choice([i for i in range(G.number_of_nodes())])

# Initializing a dictionary to count the number of visits to each node
dict_counter = {}

# Initializing the counter for each node to 0
for i in range(G.number_of_nodes()):
    dict_counter[i] = 0

# Incrementing the count for the initially chosen node
dict_counter[x] += 1

# Random Walk on the graph for 1000000 steps
for i in range(1000000):
    list_n = list(G.neighbors(x))
    
    # If the current node has no neighbors (sink), choose a random node
    if len(list_n) == 0:
        x = random.choice([i for i in range(G.number_of_nodes())])
    else:
        # Choose a random neighbor and update the counter
        x = random.choice(list_n)
        dict_counter[x] += 1

# Computing PageRank for each node
p = nx.pagerank(G)

# Sorting the PageRank dictionary by values
sorted_p = sorted(p.items(), key=operator.itemgetter(1))

# Sorting the Random Walk counter dictionary by keys
sorted_rw = sorted(dict_counter.items(), key=operator.itemgetter(0))

# Printing the PageRank, Random Walk counter, and sorted versions of both
print("PageRank:", p)
print("Random Walk Counter:", dict_counter)
print("Sorted PageRank:", sorted_p)
print("Sorted Random Walk Counter:", sorted_rw)
