# Dijkstra's Shortest Path Algorithm in Python

# Import the heapq module for priority queue operations
import heapq

def dijkstra(graph, start_node):
    # Initialize a dictionary to store the distance to each node
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0  # The distance to the start node is 0

    # Create a priority queue to store nodes to be processed
    priority_queue = [(0, start_node)]  # The priority is the distance to the node

    while priority_queue:
        # Extract the node with the minimum distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the already known distance, skip this node
        if current_distance > distances[current_node]:
            continue

        # Iterate over the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found, update the distance and push it to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def print_distances(distances):
    for node, distance in distances.items():
        print(f"Node {node}: {distance}")

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print_distances(distances)