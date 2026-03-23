# Bfs Graph Traversal in Python
=====================================

```python
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    # function to add an edge between vertex x and y
    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    # function to implement BFS traversal of graph
    def bfs_traversal(self, root):
        visited = [False] * (self.V + 1)  
        queue = deque() 
        queue.append(root)
        visited[root] = True

        while queue:
            temp = queue.popleft()
            print(temp, end=" ")

            for neighbour in self.graph[temp]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True

# Example usage
g = Graph(6)  
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("BFS Traversal of graph starting from vertex 0 is:")
g.bfs_traversal(0)