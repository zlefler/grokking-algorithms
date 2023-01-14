def biggest_island(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    biggest = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                biggest = max(biggest, dfs(matrix, 0, i, j))
    return biggest


def dfs(matrix, size, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return 0
    if matrix[i][j] == 0:
        return 0
    if matrix[i][j] == 1:
        size = 1
        matrix[i][j] = 0
        size += dfs(matrix, size, i+1, j)
        size += dfs(matrix, size, i-1, j)
        size += dfs(matrix, size, i, j+1)
        size += dfs(matrix, size, i, j-1)
    return size


def main():
    print(biggest_island([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]))


main()
