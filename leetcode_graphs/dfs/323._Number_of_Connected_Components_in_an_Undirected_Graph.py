# 323. Number of Connected Components in an Undirected Graph
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that
# there is an edge between ai and bi in the graph.
#
# Return the number of connected components in the graph.
from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for [source, destination] in edges:
            graph[source].append(destination)
            graph[destination].append(source)

        visited = set()
        self.result = 0

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for i in range(n):
            if i not in visited:
                self.result += 1
                dfs(i)

        return self.result


if __name__ == "__main__":
    # n, edges = 5, [[0, 1], [1, 2], [3, 4]]
    n, edges = 5, [[0, 1], [1, 2], [2, 3], [3, 4]]
    solution = Solution()
    print(f"count components - {solution.countComponents(n, edges)}")
