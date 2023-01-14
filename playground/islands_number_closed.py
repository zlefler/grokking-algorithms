def closed_islands(matrix: list[list]) -> int:
    num_islands = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == 1:
                if dfs(matrix, i, j):
                    num_islands += 1
    return num_islands


def dfs(matrix, i, j):
    if i < 1 or i > len(matrix) - 1 or j < 1 or j > len(matrix) - 1:
        if matrix[i][j] == 1:
            return False
    if matrix[i][j] == 0:
        return True
    matrix[i][j] = 0
    return dfs(matrix, i+1, j) and dfs(matrix, i-1, j) and dfs(matrix, i, j-1) and dfs(matrix, i, j+1)


# iterate through matrix minus all edge pieces
# do dfs - if adjacent to edge, return false


def main():
    print(closed_islands([[1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [
          0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))

    print(closed_islands([[0, 0, 0, 0], [0, 1, 0, 0], [
          0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))


main()
