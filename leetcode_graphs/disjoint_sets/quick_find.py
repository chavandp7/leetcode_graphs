class QuickFind:
    root = None

    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x: int):
        return self.root[x]

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        # update all values for which root is root of Y
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
