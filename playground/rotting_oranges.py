class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        minutes = 0

        while minutes < len(grid) * len(grid[0]):
            minutes += 1
            seen = set()
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    dirs = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
                    if grid[i][j] == 2 and (i, j) not in seen:
                        for (x, y) in dirs:
                            self.rotOrange(i+x, j+y, grid, seen)
            if self.allRotten(grid):
                return minutes
        return -1

    def rotOrange(self, x, y, grid, seen):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        if (x, y) in seen:
            return
        if grid[x][y] != 2:
            seen.add((x, y))
        if grid[x][y] == 1:
            grid[x][y] = 2

    def allRotten(self, grid):
        for row in grid:
            for num in row:
                if num == 1:
                    return False
        return True


sol = Solution()
g1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(sol.orangesRotting(g1))
