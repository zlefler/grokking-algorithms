def island_permiter(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    seen = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(0)
        seen.append(row)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                return dfs(matrix, i, j, seen)


def dfs(matrix, i, j, seen):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return 1

    if matrix[i][j] == 0:
        return 1

    if seen[i][j] == 1:
        return 0
    seen[i][j] = 1

    p = 0
    p += dfs(matrix, i+1, j, seen)
    p += dfs(matrix, i-1, j, seen)
    p += dfs(matrix, i, j+1, seen)
    p += dfs(matrix, i, j-1, seen)

    return p


def main():
    print(island_permiter([[1, 1, 0, 0, 0],
                           [0, 1, 0, 0, 0],
                           [0, 1, 0, 0, 0],
                           [0, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0]]))

    print(island_permiter([[0, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 1, 0, 0],
                           [0, 1, 1, 0],
                           [0, 1, 0, 0]]))


main()
