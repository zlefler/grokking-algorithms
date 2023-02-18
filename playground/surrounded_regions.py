class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def dfs(board, x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return False
            if board[x][y] == 'O' and (x < 1 or x >= rows-1 or y < 1 or y >= cols-1):
                return False
            if board[x][y] == 'X':
                return True

            board[x][y] = 'X'

            if not (dfs(board, x-1, y) and dfs(board, x+1, y) and dfs(board, x, y-1) and dfs(board, x, y+1)):
                board[x][y] = 'O'
                return False
            return True

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    dfs(board, i, j)


sol = Solution()
b1 = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
b2 = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
      ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
b3 = [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"], [
    "X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"], ["X", "X", "O", "X", "O"]]
sol.solve(b3)
print(b3)
