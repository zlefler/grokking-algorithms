from heapq import *


def find_closest_elements(nums, k, x):
    '''Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.'''
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < x:
            l = mid + 1
        elif nums[mid] > x:
            r = mid - 1
        else:
            break

    minHeap = [nums[mid]]
    i = 1
    while len(minHeap) < k:
        heappush(minHeap, nums[mid-i])
        heappush(minHeap, nums[mid+i])
    if len(minHeap) > k:
        heappop(minHeap)
    return minHeap


print("'K' closest numbers to 'X' are: " +
      str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
print("'K' closest numbers to 'X' are: " +
      str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
print("'K' closest numbers to 'X' are: " +
      str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))
