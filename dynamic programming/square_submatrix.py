def largest_square(arr):
    max_size = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]:
                max_size = max(max_size, _largest_square(arr, i, j))
    return max_size


def _largest_square(arr, i, j):
    if i == len(arr) or j == len(arr[0]):
        return 0
    if not arr[i][j]:
        return 0
    return 1 + min(min(_largest_square(arr, i + 1, j), _largest_square(arr, i, j+1)), _largest_square(arr, i+1, j+1))


arr1 = [[False, True, False, False], [
    True, True, True, True], [False, True, True, False]]

print(largest_square(arr1))
