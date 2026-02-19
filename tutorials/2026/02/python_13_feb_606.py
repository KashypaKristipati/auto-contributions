# Graph BFS Traversal in Python
=====================================

This script teaches how to perform Breadth-First Search (BFS) traversal on a graph using Python.

```python
from collections import deque

class Graph:
    def __init__(self):
        # Initialize an empty dictionary to represent the graph's adjacency list.
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # Add a new vertex to the graph if it doesn't exist already.
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Connect two vertices with an edge.
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def bfs_traversal(self, start_vertex):
        """
        Performs a Breadth-First Search traversal on the graph starting from the given vertex.

        Args:
        start_vertex: The vertex to begin the traversal from.
        """

        # Create a set to keep track of visited vertices.
        visited = set()

        # Create a queue for BFS, enqueue the starting vertex and mark it as visited.
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            # Dequeue the next unvisited vertex from the front of the queue.
            current_vertex = queue.popleft()

            # Print the current vertex's value.
            print(current_vertex, end=" ")

            # Iterate over all adjacent vertices that have not been visited yet.
            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    # Mark the neighbor as visited and enqueue it to explore further.
                    queue.append(neighbor)
                    visited.add(neighbor)

# Example usage:
if __name__ == "__main__":
    graph = Graph()

    # Create vertices and add them to the graph.
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    # Connect vertices with edges.
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("A", "D")
    graph.add_edge("C", "D")

    print("Performing BFS traversal starting from vertex 'A':")
    graph.bfs_traversal("A")