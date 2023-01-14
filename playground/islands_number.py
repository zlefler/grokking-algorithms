def countIslandsDFS(arr):
    rows = len(arr)
    cols = len(arr[0])
    islands = 0
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 1:
                islands += 1
                dfs(arr, i, j)

    return islands


def dfs(arr, i, j):
    if i < 0 or i >= len(arr):
        return
    if j < 0 or j >= len(arr[0]):
        return
    if arr[i][j] == 0:
        return

    arr[i][j] = 0
    dfs(arr, i-1, j)
    dfs(arr, i+1, j)
    dfs(arr, i, j-1)
    dfs(arr, i, j+1)


def main():
    print(countIslandsDFS([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))
    print(countIslandsDFS([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))


main()
