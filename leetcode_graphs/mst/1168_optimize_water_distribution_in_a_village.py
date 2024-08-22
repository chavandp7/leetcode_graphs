# 1168 optimize water distribution in a village
# There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.
#
# For each house i, we can either build a well inside it directly with cost wells[i - 1]
# (note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to lay pipes
# between houses are given by the array pipes where each pipes[j] = [house1j, house2j, costj] represents the cost
# to connect house1j and house2j together using a pipe. Connections are bidirectional, and there could be
# multiple valid connections between the same two houses with different costs.
#
# Return the minimum total cost to supply water to all houses.
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        edges = []
        for i in wells:
            edges.append([i - 1, i - 1, wells[i]])

        for pipe in pipes:
            source, destination, cost = pipe
            edges.append([source, destination, cost])

        heapq.heapify(edges)
        visited = [False] * n
        count = n
        result = 0

        while edges and count > 0:
            pipe = heapq.heappop(edges)
            source, destination, cost = pipe

            # 1 - Self loop
            if source == destination and not visited[source]:
                visited[source] = True
                result += cost

            # 2 - pipe
            if visited[source] and not visited[destination]:
                visited[destination] = True
                result += cost
