def search(arr, key):
    '''Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.
Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.'''
    is_ascending = arr[0] < arr[-1]

    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == key:
            return mid
        if is_ascending:
            if arr[mid] > key:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if arr[mid] < key:
                r = mid - 1
            else:
                l = mid + 1

    return -1


print(search([4, 6, 10], key=10))
print(search([1, 2, 3, 4, 5, 6, 7], key=5))
print(search([10, 6, 4], key=10))
