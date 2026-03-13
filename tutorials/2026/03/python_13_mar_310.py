# Topological Sort in Python
=====================================

A topological sort is an ordering of the vertices in a directed acyclic graph (DAG) such that for every directed edge u -> v, vertex u comes before v in the ordering.

Here's a simple implementation of a topological sort using DFS and a dictionary to keep track of visited nodes:

```python
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # graph using adjacency list representation
        self.graph = defaultdict(list)
    
    def addEdge(self, v, w):
        self.graph[v].append(w)

    def topologicalSortUtil(self, v, visited, stack):
        # Mark the current node as visited.
        visited[v] = True
        
        # Recur for all vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        
        # Push the current vertex to stack after visiting
        # all its adjacent vertices
        stack.insert(0, v)

    def topologicalSort(self):
        # Create a stack to store the sorted nodes
        stack = []
        
        # Step 1: Initialize an array to keep track of visited nodes
        visited = [False] * (self.V + 1)
        
        # Step 2: Perform DFS for every unvisited node
        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
                
        return stack

# Test the code
g = Graph(6);
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print("Topological Sort is:")
sorted_nodes = g.topologicalSort()
for node in sorted_nodes:
    print(node)