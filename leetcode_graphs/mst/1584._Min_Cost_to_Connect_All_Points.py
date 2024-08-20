# 1584. Min Cost to Connect All Points
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
#
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|,
# where |val| denotes the absolute value of val.
#
# Return the minimum cost to make all points connected. All points are connected
# if there is exactly one simple path between any two points.
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) <= 1:
            return 0

        edges = []
        size = len(points)
        uf = UnionFind(size)

        for i in range(size):
            xi, yi = points[i]
            for j in range(i + 1, size):
                xj, yj = points[j]
                cost = abs(xj - xi) + abs(yj - yi)
                edge = Edge(i, j, cost)
                edges.append(edge)

        heapq.heapify(edges)
        count = size - 1
        result = 0

        # Kruskal's algorithm
        while edges and count > 0:
            edge = heapq.heappop(edges)
            if not uf.connected(edge.point1, edge.point2):
                uf.union(edge.point1, edge.point2)
                result += edge.cost
                count -= 1

        return result


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


if __name__ == "__main__":
    # points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    points = [[3, 12], [-2, 5], [-4, 1]]
    solution = Solution()
    result = solution.minCostConnectPoints(points)
    print(result)
