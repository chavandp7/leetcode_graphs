# 547. Number of Provinces
#
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
# and city b is connected directly with city c, then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city
# are directly connected, and isConnected[i][j] = 0 otherwise.
#
# Return the total number of provinces.

from typing import List


class Solution:
    root = None
    rank = None

    def initialize(self, n: int):
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.initialize(n)

        for i in range(n):
            for j in range(i + 1, n):
                if i == 5 and j == 12:
                    print()
                if isConnected[i][j] == 1:
                    self.union(i, j)

        provinces = set()
        for i in range(n):
            root = self.find(i)
            if root not in provinces:
                provinces.add(root)

        return len(provinces)

    def print_parent_and_rank(self):
        print("elements -> parent node")
        for i in range(len(self.root)):
            print(f" {self.root[i]}", end=' ')

        print()
        for i in range(len(self.root)):
            print(f" {i}", end=' ')

        # print("node --> rank")
        # for i in range(len(self.root)):
        #     print(f"{i} --> {self.rank[i]}")


if __name__ == "__main__":
    is_connected = [
        # 0. 1. 2. 3. 4. 5. 6. 7  8. 9.10 11 12 13.14
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 4
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 5
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],  # 6
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],  # 7
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],  # 10
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],  # 11
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # 12
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 13
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]]  # 14

    solution = Solution()
    print(solution.findCircleNum(is_connected))
    solution.print_parent_and_rank()
