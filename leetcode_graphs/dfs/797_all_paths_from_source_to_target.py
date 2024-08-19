# 797. All Paths From Source to Target
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths
# from node 0 to node n - 1 and return them in any order.
#
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
# (i.e., there is a directed edge from node i to node graph[i][j]).
from typing import List


class Solution:
    def dfs(self, graph: List[List[int]], n: int, seen: set, source: int, current_path: List[int]):
        if source == n - 1:
            path = list(current_path)
            self.result.append(path)
            return

        for neighbor in graph[source]:
            if neighbor not in seen:
                seen.add(neighbor)
                current_path.append(neighbor)
                self.dfs(graph, n, seen, neighbor, current_path)
                seen.remove(neighbor)
                current_path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        seen = {0}
        current_path = [0]
        self.result = []
        n = len(graph)
        self.dfs(graph, n, seen, 0, current_path)
        return self.result


if __name__ == "__main__":
    graph = [[1, 2], [3], [3], []]
    solution = Solution()
    print(solution.allPathsSourceTarget(graph))

    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    print(solution.allPathsSourceTarget(graph))
