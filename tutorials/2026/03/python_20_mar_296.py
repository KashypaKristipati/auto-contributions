# Dijkstra's Shortest Path Algorithm
=====================================

This Python script implements Dijkstra's algorithm to find the shortest path between two nodes in a weighted graph.

```python
import sys
import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, node):
        """Add a new node to the graph."""
        self.nodes.add(node)
        if node not in self.edges:
            self.edges[node] = {}

    def add_edge(self, from_node, to_node, weight):
        """Add an edge between two nodes with a given weight."""
        self.edges[from_node][to_node] = weight
        self.edges[to_node].setdefault(from_node, weight)  # Add reverse edge

    def dijkstra(self, start_node):
        """Find the shortest path from the start node to all other nodes."""
        distances = {node: sys.maxsize for node in self.nodes}
        distances[start_node] = 0
        previous_nodes = {node: None for node in self.nodes}

        priority_queue = [(0, start_node)]
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Nodes can get added to the priority queue multiple times. We only
            # process a node the first time we remove it from the priority queue.
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.edges[current_node].items():
                distance = current_distance + weight

                # Only consider this new path better than any existing one to the same
                # destination: update our way of reaching that place with a shorter
                # total path length.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, previous_nodes

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")

    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 1)

    start_node = "A"
    distances, previous_nodes = graph.dijkstra(start_node)

    print(f"Shortest path from {start_node}:")
    current_node = start_node
    while current_node is not None:
        print(current_node)
        current_node = previous_nodes[current_node]

    print("\nDistances:")
    for node, distance in distances.items():
        print(node, ":", distance)