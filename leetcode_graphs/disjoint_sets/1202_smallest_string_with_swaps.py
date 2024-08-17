from collections import defaultdict
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

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        self.initialize(n)

        for i in range(len(pairs)):
            a, b = pairs[i]
            self.union(a, b)

        for i in range(n):
            self.find(i)

        substrings = defaultdict(list)

        # iterate on string index
        for i in range(n):
            root = self.find(i)
            substrings[root].append(s[i])

        for i in range(len(substrings)):
            substrings[i].sort()

        result = ''
        # iterate on string index
        for i in range(n):
            root = self.find(i)
            result += substrings[root].pop(0)

        return result


if __name__ == "__main__":
    # s = "dcab"
    # pairs = [[0, 3], [1, 2]]

    s = "dcab"
    pairs = [[0, 3], [1, 2], [0, 2]]

    solution = Solution()
    print(solution.smallestStringWithSwaps(s, pairs))
