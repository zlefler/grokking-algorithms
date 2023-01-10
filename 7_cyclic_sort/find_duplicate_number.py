from ast import AugAssign
from turtle import onclick


def find_dupe(arr: list[int]) -> int:
    '''We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.'''
    nums = arr
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1
    return -1

 # Doesn't work:
    # for i in range(len(arr)):
    #     if arr[i] != i + 1:
    #         if arr[i] == len(arr):
    #             arr[i], arr[-1] = arr[x], arr[-1]
    #         else:
    #             try:
    #                 x = arr[i:].index(i+1)
    #             except ValueError:
    #                 continue
    #             else:
    #                 arr[i], arr[x] = arr[x], arr[i]
    # for i in range(len(arr)):
    #     if arr[i] != i + 1:
    #         return arr.index(arr[i])
    # for i in range(len(arr)):
    #     if arr[i] != i + 1:
    #         find index of i + 1
    #         if not there:
    #             move on
    #         if it is:
    #             swap places
    # iterate through again
    # return what's out of place
arr1 = [5, 4, 3, 1, 1]
arr2 = [2, 4, 3, 3, 5]
arr3 = [2, 1, 4, 3, 3]

print(find_dupe(arr1))
print(find_dupe(arr2))
print(find_dupe(arr3))
