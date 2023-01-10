def square_it(arr: list) -> list:
    '''Given a sorted array, create a new array containing squares of all the numbers 
    of the input array in the sorted order.'''

    n = len(arr)
    squares = [0 for _ in range(n)]
    highest_index = n - 1
    left = 0
    right = n - 1

    while left < right:
        leftSquare = arr[left] ** 2
        rightSquare = arr[right] ** 2
        if leftSquare > rightSquare:
            squares[highest_index] = leftSquare
            left += 1
        else:
            squares[highest_index] = rightSquare
            right -= 1
        highest_index -= 1

    return squares


    # n = len(arr)
    # squares = [0 for _ in range(n)]
    # highest_index = n - 1
    # left, right = 0, n - 1
    # while left <= right:
    #     leftSquare = arr[left] ** 2
    #     rightSquare = arr[right] ** 2
    #     if leftSquare > rightSquare:
    #         squares[highest_index] = leftSquare
    #         left += 1
    #     else:
    #         squares[highest_index] = rightSquare
    #         right -= 1
    #     highest_index -= 1
    # return squares
one = [-2, -1, 0, 2, 3]
two = [-3, -1, 0, 1, 2]

print(square_it(one))
print(square_it(two))
