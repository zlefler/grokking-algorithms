from heapq import *

# essentially the inverse of top_k_numbers. Just need more practice with heaps, maxHeaps in particular.


def kth_smallest(nums, k):
    '''Given an unsorted array of numbers, find Kth smallest number in it.
Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.'''

    maxHeap = []

    for i in range(k):
        heappush(maxHeap, -nums[i])

    for i in range(k, len(nums)):
        if -nums[i] > maxHeap[0]:
            heappop(maxHeap)
            heappush(maxHeap, -nums[i])

    return -maxHeap[0]


# works but slow. Not as slow as a regular sort MAYBE but slow.
#     minHeap = []

#     for num in nums:
#         heappush(minHeap, num)

#     for _ in range(k - 1):
#         heappop(minHeap)

#     return heappop(minHeap)


array = [1, 4, 10, 8, 3, 6, 5, 23]

print(kth_smallest(array, 3))
