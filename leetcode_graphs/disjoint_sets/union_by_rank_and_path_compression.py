class OptimizedDisjointSet:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x

        y = self.find(self.root[x])
        self.root[x] = y
        return y

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

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    od = OptimizedDisjointSet(10)
    od.union(1, 2)
    od.union(2, 5)
    od.union(5, 6)
    od.union(6, 7)
    od.union(3, 8)
    od.union(8, 9)
    print(od.connected(1, 5))  # true
    print(od.connected(5, 7))  # true
    print(od.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    od.union(9, 4)
    print(od.connected(4, 9))  # true
