# 2368. Reachable Nodes With Restrictions
# There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
#
# You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge
# between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.
#
# Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.
#
# Note that node 0 will not be a restricted node.
from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = {node for node in restricted}
        graph = defaultdict(list)
        visited = set()

        for [source, destination] in edges:
            graph[source].append(destination)
            graph[destination].append(source)

        def dfs(node):
            if node in visited:
                return 0

            if node in restricted:
                return 0

            count = 1
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    count += dfs(neighbor)

            return count

        return dfs(0)


if __name__ == "__main__":
    # n = 7
    # edges = [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]]
    # restricted = [4, 5]

    n = 7
    edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
    restricted = [4, 2, 1]

    solution = Solution()
    print(f"reachable nodes - {solution.reachableNodes(n, edges, restricted)}")
