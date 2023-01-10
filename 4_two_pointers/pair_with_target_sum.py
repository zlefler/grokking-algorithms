def pair_with_target_sum(array, target: int) -> list:
    '''Given an array of sorted numbers and a target sum, find a pair in the array whose 
    sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.'''
    left = 0
    right = len(array) - 1

    while right > left:
        if array[left] + array[right] > target:
            right -= 1
        elif array[left] + array[right] < target:
            left += 1
        elif array[left] + array[right] == target:
            return [left, right]
    return [-1, -1]


input = [1, 2, 3, 4, 6]
targ = 6
print(pair_with_target_sum(input, targ))
