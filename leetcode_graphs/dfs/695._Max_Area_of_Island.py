# 695. Max Area of Island
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
# (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return 0.
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows:
                return 0

            if c < 0 or c >= cols:
                return 0

            if (r, c) in visited:
                return 0

            if grid[r][c] != 1:
                return 0

            count = 1
            visited.add((r, c))

            count += dfs(r - 1, c)
            count += dfs(r + 1, c)
            count += dfs(r, c - 1)
            count += dfs(r, c + 1)

            return count

        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ans = dfs(r, c)
                    result = max(result, ans)
        return result


if __name__ == "__main__":
    # grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    solution = Solution()
    print(f"max island area - {solution.maxAreaOfIsland(grid)}")
