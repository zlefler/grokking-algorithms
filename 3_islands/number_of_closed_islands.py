def count_closed_islands(matrix: list) -> int:
    '''You are given a 2D matrix containing only 1s (land) and 0s (water).

An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

A closed island is an island that is totally surrounded by 0s (i.e., water). This means all horizontally and vertically connected cells of a closed island are water. This also means that, by definition, a closed island can't touch an edge (as then the edge cells are not connected to any water cell). 

Write a function to find the number of closed islands in the given matrix.'''

    rows = len(matrix)
    cols = len(matrix[0])
    seen = [[False for i in range(cols)] for j in range(rows)]
    closed_islands = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not seen[i][j]:
                if dfs(seen, matrix, i, j):
                    closed_islands += 1

    return closed_islands


def dfs(seen, matrix, x, y):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return False
    if matrix[x][y] == 0 or seen[x][y]:
        return True
    seen[x][y] = True

    isClosed = True

    isClosed &= dfs(seen, matrix, x - 1, y)
    isClosed &= dfs(seen, matrix, x + 1, y)
    isClosed &= dfs(seen, matrix, x, y - 1)
    isClosed &= dfs(seen, matrix, x, y + 1)

    return isClosed


first = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [
    0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]

print(count_closed_islands(first))
