from collections import deque


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        start_color = image[sr][sc]

        queue = deque()
        queue.append((sr, sc))
        while queue:
            (x, y) = queue.popleft()
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
                continue
            if image[x][y] != start_color:
                continue
            image[x][y] = color
            queue.append((x-1, y))
            queue.append((x+1, y))
            queue.append((x, y-1))
            queue.append((x, y+1))
        return image

    def floodFillRecursive(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        start_color = image[sr][sc]

        self.dfs(image, sr, sc, start_color, color)
        return image

    def dfs(self, image, x, y, start_color, end_color):
        if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
            return
        if image[x][y] != start_color:
            return
        image[x][y] = end_color

        self.dfs(image, x-1, y, start_color, end_color)
        self.dfs(image, x+1, y, start_color, end_color)
        self.dfs(image, x, y-1, start_color, end_color)
        self.dfs(image, x, y+1, start_color, end_color)


sol = Solution()
i1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(sol.floodFill(i1, 1, 1, 2))
