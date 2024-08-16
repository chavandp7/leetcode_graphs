# 1091. Shortest Path in Binary Matrix
# Given an n x n binary matrix grid, return the length of the shortest clear path
# in the matrix. If there is no clear path, return -1.
#
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
# to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
#
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected
# (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def valid(x, y):
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                return True
            return False

        if grid[0][0] == 1:
            return -1
            # right  left.    top      down
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1),
                      # up-left down-left up-right down-right
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        queue = deque([(0, 0, 1)])
        seen = {(0, 0)}
        n = len(grid)

        while queue:
            row, col, steps = queue.popleft()
            if row == n - 1 and col == n - 1:
                return steps

            for x, y in directions:
                dx = row + x
                dy = col + y

                if valid(dx, dy) and (dx, dy) not in seen:
                    seen.add((dx, dy))
                    queue.append((dx, dy, steps + 1))
                    if (dx, dy) == (n - 1, n - 1):
                        return steps + 1

        return -1


if __name__ == "__main__":
    # grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    # grid = [[1,0,0],[1,1,0],[1,1,0]]
    grid = [[0, 1], [1, 0]]
    result = Solution().shortestPathBinaryMatrix(grid)
    print(f"Number of shortest steps = {result}")
