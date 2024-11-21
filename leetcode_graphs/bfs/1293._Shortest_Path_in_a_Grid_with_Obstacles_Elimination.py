# 1293. Shortest Path in a Grid with Obstacles Elimination
# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
# You can move up, down, left, or right from and to an empty cell in one step.
#
# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1)
# given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        queue = deque([])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # row, col, steps, obstacles
        queue.append((0, 0, 0, 0))
        if grid[0][0] == 1 and k == 0:
            return -1

        while queue:
            row, col, steps, obstacles = queue.popleft()
            visited.add((row, col))

            if row == m - 1 and col == n - 1:
                return steps

            for x, y in directions:
                dx = row + x
                dy = col + y

                if 0 <= dx < m and 0 <= dy < n:
                    pass
