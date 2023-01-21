from collections import deque
import math


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        total_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    total_islands += 1
                    self.bfs(grid, i, j)
        return total_islands

    def bfs(self, grid, x, y):
        queue = deque([[x, y]])
        while queue:
            curr = queue.popleft()
            row = curr[0]
            col = curr[1]
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue

            if grid[row][col] == '0':
                continue
            grid[row][col] = '0'
            queue.append([row-1, col])
            queue.append([row+1, col])
            queue.append([row, col-1])
            queue.append([row, col+1])


sol = Solution()
grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(math.sqrt(50000))
