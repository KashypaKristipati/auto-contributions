import sys
import heapq

def dijkstra(graph, start):
    # Create a dictionary to store the distance to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Create a dictionary to store the shortest path to each node
    shortest_path = {node: None for node in graph}

    # Create a priority queue to store the nodes to be processed
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the stored distance, skip this node
        if current_distance > distances[current_node]:
            continue

        # For each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found, update the distance and shortest path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, shortest_path

def print_shortest_path(graph, start, end):
    # Print the shortest path from the start node to the end node
    path = []
    current_node = end

    while current_node is not None:
        path.append(current_node)
        current_node = shortest_path[current_node]

    path.reverse()
    print(' -> '.join(path))

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
end_node = 'D'

distances, shortest_path = dijkstra(graph, start_node)
print(f'Shortest distance from {start_node} to {end_node}: {distances[end_node]}')
print_shortest_path(graph, start_node, end_node)