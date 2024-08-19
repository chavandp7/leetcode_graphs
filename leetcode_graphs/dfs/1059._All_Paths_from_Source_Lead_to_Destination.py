# Given the edges of a directed graph where edges[i] = [ai, bi] indicates there is an edge between nodes ai and bi,
# and two nodes source and destination of this graph, determine whether or not all paths starting from source eventually,
# end at destination, that is:
#
# At least one path exists from the source node to the destination node
# If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
# The number of possible paths from source to destination is a finite number.
# Return true if and only if all roads from source lead to destination.
from collections import defaultdict
from typing import List


class Solution:
    def build_graph(self, edges: List[List[int]]):
        self.graph = defaultdict(list)

        # build adjacency list
        for edge in edges:
            source, destination = edge
            self.graph[source].append(destination)

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.build_graph(edges)
        seen = {set}
        return self.dfs(source, destination, seen)

    def dfs(self, source, destination, seen):
        if source == destination:
            return True

        seen.add(source)
        size = len(self.graph[source])
        if size == 0:
            return False

        for neighbor in self.graph[source]:
            if source == neighbor and source != destination:
                return False

            if source == neighbor:
                continue

            if neighbor != destination and neighbor in seen:
                return False

            if neighbor not in seen:
                result = self.dfs(neighbor, destination, seen)
                if not result:
                    return False
        return True


if __name__ == "__main__":
    n = 4
    source = 0
    edges = [[0, 1], [1, 1]]
    destination = 3
    print(Solution().leadsToDestination(n, edges, source, destination))
