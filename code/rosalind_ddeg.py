# ^_^ coding:utf-8 ^_^

"""
Double-Degree Array
url: http://rosalind.info/problems/ddeg/

Given: A simple graph with n≤103 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the sum of the degrees of i's neighbors.
"""

# the input
# ==============================
data = "../data/rosalind_ddeg.txt"

# the solution
# ==============================
with open(data, "r") as f:
    n, edges = f.readline().strip().split(" ")
    edges_list = [line.strip().split(" ") for line in f]
# print(n, edges)
# print(edges_list)

nodes_neighbours = {}
for i in range(int(n)):
    nodes_neighbours[str(i+1)] = [t for l in edges_list for t in l if str(i+1) in l and str(i+1) != t]

for i in range(int(n)):
    print(sum([len(nodes_neighbours[k]) for k in nodes_neighbours[str(i+1)]]), end=" ")
