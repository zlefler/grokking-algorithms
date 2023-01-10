from heapq import *

# Put K numbers into the heap, then go through the rest, adding one if it's big enough
# and pulling the smallest out.


def find_k_largest_numbers(nums, k):
    '''Given an unsorted array of numbers, find the ‘K’ largest numbers in it.'''

    minHeap = []

    for i in range(k):
        heappush(minHeap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    return minHeap


array = [1, 4, 10, 8, 3, 6, 5, 23]

print(find_k_largest_numbers(array, 5))
