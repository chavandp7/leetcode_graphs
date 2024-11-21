# 1557. Minimum Number of Vertices to Reach All Nodes
# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where
# edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.
#
# Find the smallest set of vertices from which all nodes in the graph are reachable.
# It's guaranteed that a unique solution exists.
#
# Notice that you can return the vertices in any order.
from collections import defaultdict
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [False] * n

        for [source, destination] in edges:
            indegree[destination] = True

        result = []

        for node in range(n):
            if not indegree[node]:
                result.append(node)

        return result


if __name__ == "__main__":
    # n, edges = 6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    # n, edges = 5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
    n, edges = 3, [[1, 2], [1, 0], [0, 2]]
    solution = Solution()
    print(f"minimum set - {solution.findSmallestSetOfVertices(n, edges)}")
