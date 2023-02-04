class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        best = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    best = max(best, self.dfs(grid, i, j))
        return best

    def dfs(self, grid, x, y, area=0):
        if grid[x][y] == 0:
            return area

        area += 1

        if x < len(grid) - 1:
            self.dfs(grid, x+1, y, area)
        if x > 0:
            self.dfs(grid, x-1, y, area)
        if y < len(grid[0]) - 1:
            self.dfs(grid, x, y+1, area)
        if y > 0:
            self.dfs(grid, x, y-1, area)

        return area


sol = Solution()
g1 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(sol.maxAreaOfIsland(g1))
