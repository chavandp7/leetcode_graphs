# 200. Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
# return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            cell_num = r * cols + c
            if cell_num in seen:
                return

            seen.add(cell_num)

            # up
            if r > 0 and grid[r - 1][c] == "1":
                dfs(r - 1, c)

            # down
            if r < rows - 1 and grid[r + 1][c] == "1":
                dfs(r + 1, c)

            # left
            if c > 0 and grid[r][c - 1] == "1":
                dfs(r, c - 1)

            # right
            if c < cols - 1 and grid[r][c + 1] == "1":
                dfs(r, c + 1)

        seen = set()
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                cell_num = row * cols + col
                if grid[row][col] == "1" and cell_num not in seen:
                    islands += 1
                    dfs(row, col)

        return islands


if __name__ == "__main__":
    grid = [
        ["1", "0", "1", "1", "1"],
        ["1", "0", "1", "0", "1"],
        ["1", "1", "1", "0", "1"]
    ]
    solution = Solution()
    print(f"num of islands - {solution.numIslands(grid)}")
