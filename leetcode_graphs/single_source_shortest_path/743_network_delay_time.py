# 743. Network Delay Time
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times
# as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it
# takes for a signal to travel from source to target.
#
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def dijkstra_algorithm(self, graph, n: int, k: int):
        distances = [float('infinity')] * (n + 1)
        visited = [False] * (n + 1)
        pq = []

        distances[k] = 0
        heapq.heappush(pq, (0, k))

        while pq:
            node_distance, node = heapq.heappop(pq)
            if visited[node]:
                continue
            visited[node] = True

            for [neighbor, weight] in graph[node]:
                current_distance = node_distance + weight
                if current_distance < distances[neighbor]:
                    distances[neighbor] = current_distance
                    heapq.heappush(pq, (current_distance, neighbor))

        return distances

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for weighted_edge in times:
            source, destination, time = weighted_edge
            graph[source].append([destination, time])

        distances = self.dijkstra_algorithm(graph, n, k)
        result = 0
        for i in range(1, n + 1):
            if distances[i] == float('infinity'):
                return -1
            result = max(result, distances[i])

        return result


if __name__ == "__main__":
    solution = Solution()
    # times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    # n = 4
    # k = 2

    # times = [[1, 2, 1]]
    # n = 2
    # k = 1

    times = [[1, 2, 1]]
    n = 2
    k = 2

    print(solution.networkDelayTime(times, n, k))
