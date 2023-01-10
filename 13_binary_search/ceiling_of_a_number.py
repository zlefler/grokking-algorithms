# Not complicated, just need to read it carefully and make sure you understand the question.

def call(arr: list[int], key: int) -> int:
    '''Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.'''
    l = 0
    r = len(arr) - 1
    smallest_valid_num = float('inf')
    smallest_valid_index = float('inf')

    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] < key:
            l = mid + 1
        elif arr[mid] == key:
            return mid
        else:
            if arr[mid] < smallest_valid_num:
                smallest_valid_num = arr[mid]
                smallest_valid_index = mid
            r = mid - 1
    if smallest_valid_num != float('inf'):
        return smallest_valid_index
    return -1


print(call([4, 6, 10], 6))
print(call([1, 3, 8, 10, 15], 12))
print(call([4, 6, 10], 17))
