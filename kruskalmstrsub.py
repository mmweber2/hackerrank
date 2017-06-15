# Problem located at: https://www.hackerrank.com/challenges/kruskalmstrsub
# Solution modified to read input from a file rather than the command line.
from collections import defaultdict
# Set scope on edge list and number of nodes
all_edges = []
n = 0
with open("edges.txt", "r") as raw_file:
    # First line contains number of nodes and edges, but Python doesn't
    #   need to know the number of edges.
    n = int(raw_file.readline().split()[0])
    all_edges = [map(int, x.split()) for x in raw_file.readlines()]
# For each node, track the adjacent nodes in a dictionary and list.
# Use a list because multi-edges are possible.
graph = {x: defaultdict(list) for x in xrange(1, n + 1)}
for start, end, weight in all_edges:
    graph[start][end].append(weight)
    graph[end][start].append(weight)
# Sort edges first by weight, then by sum of node indices for tie breaks
all_edges = sorted(all_edges, key=lambda x: (x[2], x[0] + x[1]))
# No need to keep track of edges, since we only need total weight
subtree_weight = 0
# Each forest initially contains only one node
forests = {x: set((x,)) for x in xrange(1, n + 1)}
for start, end, weight in all_edges:
    if end in forests[start]:
        # Adding this edge would create a cycle, so skip it
        continue
    new_forest = set.union(forests[start], forests[end])
    # Don't just update the two nodes being joined, but their entire
    #  forests
    for other_tree in new_forest:
        forests[other_tree] = new_forest
    subtree_weight += weight
    if len(forests[start]) == n:
        # MST is complete, no more edges need to be considered
        break
print subtree_weight
