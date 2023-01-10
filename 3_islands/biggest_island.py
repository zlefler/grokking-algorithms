def biggest_island(matrix):
    '''Given a 2D array (i.e., a matrix) containing
    only 1s (land) and 0s (water), find the biggest
    island in it. Write a function to return the area of the biggest island.
An island is a connected set of 1s (land) and is surrounded by either an edge
 or 0s (water). Each cell is considered connected to other cells horizontally
 or vertically (not diagonally).'''

    rows = len(matrix)
    cols = len(matrix[0])
    biggest = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                biggest = max(biggest, dfs(matrix, i, j))
    return biggest


def dfs(matrix, x, y):
    if x < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[0]):
        return 0
    if matrix[x][y] == 0:
        return 0
    matrix[x][y] = 0

    area = 1

    area += dfs(matrix, x - 1, y)
    area += dfs(matrix, x + 1, y)
    area += dfs(matrix, x, y - 1)
    area += dfs(matrix, x, y + 1)
    return area


example = [[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
    0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]
print(biggest_island(example))

# print(dfs(example, 0, 0))
