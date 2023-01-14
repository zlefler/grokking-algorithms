def flood_fill(matrix, i, j, color):
    old = matrix[i][j]
    dfs(matrix, i, j, old, color)
    return matrix


def dfs(matrix, i, j, old, new):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return
    if matrix[i][j] != old:
        return
    matrix[i][j] = new
    dfs(matrix, i-1, j, old, new)
    dfs(matrix, i+1, j, old, new)
    dfs(matrix, i, j+1, old, new)
    dfs(matrix, i, j-1, old, new)


def main():
    print(flood_fill([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]], 1, 3, 2))
    print(flood_fill([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
          0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]], 3, 2, 5))


main()
