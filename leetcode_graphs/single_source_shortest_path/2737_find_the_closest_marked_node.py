# 2737 find the closest marked node
# You are given a positive integer n which is the number of nodes of a 0-indexed directed weighted graph and a 0-indexed
# 2D array edges where edges[i] = [ui, vi, wi] indicates that there is an edge from node ui to node vi with weight wi.
#
# You are also given a node s and a node array marked; your task is to find the minimum distance from s
# to any of the nodes in marked.
#
# Return an integer denoting the minimum distance from s to any node in marked or -1 if there are no paths
# from s to any of the marked nodes.
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def found_all_marked(self, visited, marked):
        for node in marked:
            if not visited[node]:
                return False
        return True

    def dijekstra(self, graph, n, source, marked):
        visited = [False] * n
        pq = []
        distances = [float('infinity')] * n

        heapq.heappush(pq, (0, source))

        while pq:
            node_distance, node = heapq.heappop(pq)
            visited[node] = True

            if self.found_all_marked(visited, marked):
                return distances

            for [neighbor, weight] in graph[node]:
                current_distance = weight + node_distance
                if not visited[neighbor] and current_distance < distances[neighbor]:
                    distances[neighbor] = current_distance
                    heapq.heappush(pq, (current_distance, neighbor))

        return distances

    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        graph = defaultdict(list)

        # populate graph
        for edge in edges:
            source, destination, weight = edge
            graph[source].append([destination, weight])

        distances = self.dijekstra(graph, n, s, marked)
        minimum = float('infinity')
        for node in marked:
            minimum = min(minimum, distances[node])

        if minimum == float('infinity'):
            return -1

        return minimum


if __name__ == "__main__":
    n = 4
    edges = [[0, 1, 1], [1, 2, 3], [2, 3, 2], [0, 3, 4]]
    s = 0
    marked = [2, 3]

    solution = Solution()
    print(solution.minimumDistance(n, edges, s, marked))
