class UnionByRank:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def find(self, x: int) -> int:
        while x != self.root[x]:
            x = self.root[x]
        return x

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

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)

    def print_parent_and_rank(self):
        print("elements -> parent node")
        for i in range(len(self.root)):
            print(f"{i} --> {self.root[i]}")

        print("node --> rank")
        for i in range(len(self.root)):
            print(f"{i} --> {self.rank[i]}")


if __name__ == "__main__":
    ubr = UnionByRank(10)
    ubr.union(1, 2)
    ubr.print_parent_and_rank()

    ubr.union(2, 5)
    ubr.print_parent_and_rank()

    ubr.union(5, 6)
    ubr.print_parent_and_rank()

    ubr.union(6, 7)
    ubr.print_parent_and_rank()

    ubr.union(3, 8)
    ubr.print_parent_and_rank()

    ubr.union(8, 9)
    ubr.print_parent_and_rank()

    print(ubr.connected(1, 5))
    print(ubr.connected(5, 7))
    print(ubr.connected(4, 9))

    ubr.union(9, 4)
    ubr.print_parent_and_rank()
    print(ubr.connected(4, 9))
