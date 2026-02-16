# Dijkstra's Shortest Path Algorithm Implementation in Python

def dijkstra(graph, start_node):
    """
    This function implements Dijkstra's algorithm to find the shortest path from a given start node to all other nodes in a graph.

    Args:
        graph (dict): A dictionary representing the graph where each key is a node and its corresponding value is another dictionary with neighboring nodes as keys and edge weights as values.
        start_node (str): The node from which to start the search.

    Returns:
        dict: A dictionary containing the shortest distance from the start node to all other nodes in the graph.
    """

    # Initialize distances dictionary with infinite values for all nodes except the start node, which is set to 0
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0

    # Create a set of unvisited nodes and add the start node
    unvisited_nodes = set(graph.keys())

    # While there are still unvisited nodes
    while unvisited_nodes:
        # Find the unvisited node with the smallest distance value
        current_node = min(unvisited_nodes, key=lambda node: distances[node])

        # If no shorter path is found, stop the algorithm
        if distances[current_node] == float('infinity'):
            break

        # Mark the current node as visited
        unvisited_nodes.remove(current_node)

        # For each neighbor of the current node that has not been visited yet
        for neighbor, weight in graph[current_node].items():
            # Calculate the tentative distance from the start node to the neighbor through the current node
            distance = distances[current_node] + weight

            # If this path is shorter than any previously found path to the neighbor
            if distance < distances[neighbor]:
                # Update the shortest distance value for the neighbor
                distances[neighbor] = distance

    return distances


# Example usage:

# Define a weighted graph
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 4},
    'C': {'A': 3, 'F': 5},
    'D': {'B': 4, 'E': 1},
    'E': {'D': 1, 'F': 7},
    'F': {'C': 5, 'E': 7}
}

# Find the shortest distances from node A
distances = dijkstra(graph, 'A')

# Print the shortest distances
for node, distance in distances.items():
    print(f"Shortest distance from node A to {node}: {distance}")