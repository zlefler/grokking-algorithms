from collections import deque


def subarrays(arr, k):
    left = 0  # 0
    right = 0  # 1
    subarrays = []  # [[2]]
    while left < len(arr) and right < len(arr):  # 4
        if left == right:
            if arr[left] < k:
                subarrays.append([arr[left]])
                right += 1
        else:
            product = 1
            sub = []
            for num in range(left, right + 1):
                sub.append(arr[num])
                product *= arr[num]
            if product < 30:
                subarrays.append(sub)
                right += 1
            else:
                left += 1
                right = left
    return subarrays


def find_subarrays(arr, k):
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while product >= k and left < len(arr):
            product /= arr[left]
            left += 1
        temp_list = deque()
        for i in range(right, left-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
    return result


arr1 = [2, 5, 3, 10]
arr2 = [8, 2, 6, 5]

# print(subarrays(arr1, 30))
# print(subarrays(arr2, 50))

opcl = dict(('()', '[]', '{}'))

print(opcl)
