import heapq


def dijkstra(graph, source):
    min_distances = [float('infinity') for node in graph]
    visited = [False for node in graph]
    pq = []
    iterations = 0

    min_distances[source] = 0
    heapq.heappush(pq, (0, source))

    while pq:
        current_distance, node = heapq.heappop(pq)
        if visited[node]:
            continue

        visited[node] = True

        for neighbor, weight in graph[node]:
            iterations += 1
            if visited[neighbor]:
                continue

            neighbor_distance = current_distance + weight
            if neighbor_distance < min_distances[neighbor]:
                min_distances[neighbor] = neighbor_distance
                heapq.heappush(pq, (neighbor_distance, neighbor))

    print(f"iterations - {iterations}")
    return min_distances


if __name__ == "__main__":
    graph = [
        [[1, 1], [2, 4]], # 0
        [[0, 1], [2, 2], [3, 5]], # 1
        [[0, 4], [1, 2], [3, 1]],
        [[1, 5], [2, 1]]
    ]
    source = 0
    distances = dijkstra(graph, source)
    print(distances)
