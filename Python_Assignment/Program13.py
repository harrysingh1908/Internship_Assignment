import heapq

def dijkstra(graph, start):
    
    # Initialize distances with infinity and set the distance to the start node to 0
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    previous_nodes = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the current distance is greater than the recorded shortest distance, skip
        if current_distance > distances[current_vertex]:
            continue

        # Check neighbors of the current vertex
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def shortest_path(previous_nodes, start, end):
    
    path = []
    current_vertex = end

    while current_vertex != start:
        if current_vertex is None:
            return []
        path.append(current_vertex)
        current_vertex = previous_nodes[current_vertex]

    path.append(start)
    path.reverse()
    return path

# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_vertex = 'A'
end_vertex = 'D'

distances, previous_nodes = dijkstra(graph, start_vertex)
path = shortest_path(previous_nodes, start_vertex, end_vertex)

print(f"Shortest distances: {distances}")
print(f"Shortest path from {start_vertex} to {end_vertex}: {path}")
