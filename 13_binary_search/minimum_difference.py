# This should be basically memorized, as it's basically as important as basic binary search.

def minimum_difference(arr: list[int], key: int) -> int:
    '''Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.'''

    if key < arr[0]:
        return arr[0]
    n = len(arr)
    if key > arr[n - 1]:
        return arr[n-1]

    start, end = 0, n - 1

    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return arr[mid]

    if arr[start] - key < key - arr[end]:
        return arr[start]
    return arr[end]

    # works, I think:
    # if arr[0] > key:
    #     return arr[0]
    # if arr[-1] < key:
    #     return arr[-1]

    # l, r = 0, len(arr) - 1
    # while l <= r:
    #     mid = l + (r - l) // 2
    #     if arr[mid] == key:
    #         return arr[mid]
    #     elif arr[mid] < key:
    #         l = mid + 1
    #     else:
    #         r = mid - 1

    # if min(abs(key - l), abs(l - key)) > min(abs(key - r), abs(r - key)):
    #     return arr[l]
    # else:
    #     return arr[r]


print(minimum_difference([4, 6, 10], 7))
print(minimum_difference([4, 6, 10], 4))
print(minimum_difference([1, 3, 8, 10, 15], 12))
print(minimum_difference([4, 6, 10], 17))
