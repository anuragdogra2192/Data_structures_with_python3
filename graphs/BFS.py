'''
Breadth First Search (BFS)
Time complexity of O(V+E)
Use cases:
Shortest path on unweighted graphs.

A BFS starts at some arbitrary node of a graph and 
explores the neighbour nodes first,
before moving to the next level neighbours.

The BSF algorithm uses a queue dat structure to track which node to visit next.

Breadth-first search (BFS) is an algorithm used for tree traversal on graphs or tree data structures. BFS can be easily implemented using recursion and data structures like dictionaries and lists.

The Algorithm
Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it, and insert it in a queue.
If there are no remaining adjacent vertices left, remove the first vertex from the queue.
Repeat step 1 and step 2 until the queue is empty or the desired node is found.

Since all of ​the nodes and vertices are visited, 
the time complexity for BFS on a graph is O(V + E);
where V is the number of vertices and EE is the number of edges.
'''
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

adj = graph['E']
print(adj)

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print (s, end = " ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')