# Breadth First Search (BFS) Graph Traversal in Python

```python
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    # Function to perform BFS traversal
    def bfs(self, root):
        visited = [False] * self.V
        distance = [float('inf')] * self.V
        parent = [None] * self.V

        # Create a queue and enqueue the root node
        queue = deque([root])
        visited[root] = True
        distance[root] = 0

        while queue:
            node = queue.popleft()

            # Traverse all adjacent nodes
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    # Update the distance and parent nodes
                    distance[neighbor] = distance[node] + 1
                    parent[neighbor] = node
                    # Enqueue the neighbor node
                    queue.append(neighbor)
                    visited[neighbor] = True

        # Print the BFS traversal
        print("BFS Traversal:")
        for i in range(self.V):
            if distance[i] != float('inf'):
                print(f"Node {i} is reachable at distance {distance[i]}")
            else:
                print(f"Node {i} is not reachable")

        # Print the parent nodes
        print("\nParent Nodes:")
        for i in range(self.V):
            print(f"Node {i} is parent of node {parent[i]}")

# Create a graph with 5 vertices
g = Graph(5)

# Add edges to the graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

# Perform BFS traversal from node 0
g.bfs(0)