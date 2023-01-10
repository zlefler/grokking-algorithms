from collections import deque


def find_subarrays(arr: int, target: int) -> list:
    '''Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.'''

    res = []
    product = 1
    left = 0

    for right in range(len(arr)):
        product *= arr[right]
        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1
        temp_list = deque()
        for i in range(right, left - 1, -1):
            temp_list.appendleft(arr[i])
            res.append(list(temp_list))
    return res


    # arr.sort()
    # left, right = 0, 0
    # subarrays = []
    # for left in range(len(arr) - 1):
    #     count = 0
    #     if count == 0:
    #         if arr[left] < target:
    #             subarrays.append([arr[left]])
    #     else:
    #         product = arr[left]
    #         for i in range(1, count):
    #             product *= arr[left + count]
    #         if product < target:
    #             subarray = []
    #             for i in range(count):
    #                 subarray.append(arr[left + count])
    #             subarrays.append(subarray)
    # return subarrays
    # sort array
    # left is zero
    # right is zero
    # while right >= left
    # if and left < target:
    #     append subarray
    #     add left
    #     increment right
    # else:
    #     left += 1
    # return subarrays
arr1 = [2, 5, 3, 10]
targ1 = 30
arr2 = [8, 2, 6, 5]
targ2 = 50

print(find_subarrays(arr1, targ1))
