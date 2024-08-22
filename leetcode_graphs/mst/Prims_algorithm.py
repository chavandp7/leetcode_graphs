# 1584. Min Cost to Connect All Points
# You are given an array points representing integer coordinates of some points on a 2D-plane,
# where points[i] = [xi, yi].
#
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|,
# where |val| denotes the absolute value of val.
#
# Return the minimum cost to make all points connected. All points are connected if there is
# exactly one simple path between any two points.
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) <= 1:
            return 0

        size = len(points)
        visited = [False] * size
        unvisited = {i for i in range(size)}
        edges = []
        result = 0

        # process first vertice
        x, y = points[0]
        for i in range(1, size):
            newX, newY = points[i]
            cost = abs(newX - x) + abs(newY - y)
            edge = Edge(0, i, cost)
            edges.append(edge)

        visited[0] = True
        unvisited.remove(0)

        vertices = size - 1
        heapq.heapify(edges)  # O(E log E)

        # process remaining vertices
        while edges and vertices > 0:  # O(E)
            edge = heapq.heappop(edges)  # O(log E)
            point1, point2, cost = edge.point1, edge.point2, edge.cost
            if not visited[point2]:
                visited[point2] = True
                unvisited.remove(point2)
                result += cost

                for j in unvisited:  # O(V)
                    x, y = points[point2]
                    newX, newY = points[j]

                    cost = abs(newX - x) + abs(newY - y)
                    heapq.heappush(edges, Edge(point2, j, cost))  # O (log E)
                vertices -= 1

        return result


class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


if __name__ == "__main__":
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    solution = Solution()
    print(f"points = {points}")
    print(f"Minimum Cost to Connect Points = {solution.minCostConnectPoints(points)}")
