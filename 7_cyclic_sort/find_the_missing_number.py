def find_it(arr):
    '''We are given an array containing n distinct numbers taken from the range 0 to n. Since the array has only n numbers out of the total n+1 numbers, find the missing number.'''

    i, n = 0, len(arr)
    while i < n:
        j = arr[i]
        if arr[i] < n and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]  # swap
        else:
            i += 1

  # find the first number missing from its index, that will be our required number
    for i in range(n):
        if arr[i] != i:
            return i

    return n

    # i = 0
    # while i < len(arr):
    #     if arr[i] != i:
    #         if arr[i] == len(arr):
    #             arr[i], arr[-1] = arr[-1], arr[i]
    #         try:
    #             x = arr.index(i)
    #         except ValueError:
    #             return i
    #         else:
    #             arr[i], arr[x] = arr[x], arr[i]
    #     else:
    #         i += 1
    # return len(arr)


one = [0, 4, 2, 3]
two = [1, 4, 2, 3]
three = [0, 1, 3, 2]


print(find_it(one))
print(find_it(two))
print(find_it(three))
