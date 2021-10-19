from typing import Collection


import collections
'''
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
'''
myfruits = ("apple","banana","cherry")
# print(type(myfruits))
# print(myfruits[1])

#A set is a collection which is both unordered and unindexed.
thisset = {"apple", "banana", "cherry"}
# print(thisset)

'''
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
Dictionaries cannot have two items with the same key:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict)
# print(thisdict["brand"])

'''
Depth-first search (DFS), is an algorithm 
for tree traversal on graph or tree data structures. 
It can be implemented easily using recursion and 
data structures like dictionaries and sets.

The Algorithm
Pick any node. If it is unvisited, mark it as visited 
and recur on all its adjacent nodes.
Repeat until all the nodes are visited, or the node to be searched is found.

Since all the nodes and vertices are visited, 
the average time complexity for DFS on a graph is O(V + E)
where V is the number of vertices and EE is the number of edges. 
In case of DFS on a tree, the time complexity is O(V), 
where V is the number of nodes.

Use cases:
Count connected components 
Determine connectivity
Find bridges  
'''
# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : [],
    'G' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
#dfs(visited, graph, 'A')
#print(visited)
dfs(visited, graph, 'B')
print(visited)
