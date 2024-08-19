# 1971. Find if Path Exists in Graph
# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
# The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional
# edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
#
# You want to determine if there is a valid path that exists from vertex source to vertex destination.
#
# Given edges and the integers n, source, and destination, return true if there is a valid path
# from source to destination, or false otherwise.
from collections import defaultdict
from typing import List


class Solution:
    def build_graph(self, edges: List[List[int]]):
        graph = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            graph[a].append(b)
            graph[b].append(a)

        return graph

    def dfs(self, graph, seen: set, source: int, destination: int):
        if source == destination:
            return True

        seen.add(source)
        for i in graph[source]:
            if i not in seen:
                connected = self.dfs(graph, seen, i, destination)
                if connected:
                    return True
        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.build_graph(edges)
        seen = {set}

        return self.dfs(graph, seen, source, destination)


if __name__ == "__main__":
    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 5

    solution = Solution()
    print(solution.validPath(n, edges, source, destination))
