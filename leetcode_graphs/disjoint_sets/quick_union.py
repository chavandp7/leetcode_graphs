class QuickUnion:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x: int) -> int:
        while x != self.root[x]:
            x = self.root[x]

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
