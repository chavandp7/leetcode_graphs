# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between
# two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads
# in one direction because they are too narrow.
#
# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
#
# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
#
# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum
# number of edges changed.
#
# It's guaranteed that each city can reach city 0 after reorder.
from collections import defaultdict
from typing import List


class Solution:
    result = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(source, destination) for source, destination in connections}
        neighbors = defaultdict(list)
        visited = set()
        self.result = 0

        # build neighbors
        for source, destination in connections:
            neighbors[source].append(destination)
            neighbors[destination].append(source)

        def dfs(city):
            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue

                if (neighbor, city) not in edges:
                    self.result += 1

                visited.add(neighbor)
                dfs(neighbor)

        visited.add(0)
        dfs(0)
        return self.result


if __name__ == "__main__":
    # n, connections = 6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    n, connections = 5, [[1, 0], [1, 2], [3, 2], [3, 4]]
    solution = Solution()
    print(f"min reorder - {solution.minReorder(n, connections)} ")
