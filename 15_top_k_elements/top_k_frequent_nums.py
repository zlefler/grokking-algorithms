from heapq import *


def most_frequent(nums, k):

    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    minHeap = []

    for num, frequency in frequency_map.items():
        heappush(minHeap, (frequency, num))
        if len(minHeap) > k:
            heappop(minHeap)

    top_numbers = []

    while minHeap:
        top_numbers.append(heappop(minHeap)[1])

    return top_numbers


# doesn't work
    # maxHeap = []
    # seen = {}
    # for num in nums:
    #     if num in seen:
    #         seen[num] += 1
    #     else:
    #         seen[num] = 1
    # seen_values = list(seen.values())
    # for i in range(k):
    #     heappush(maxHeap, -seen_values[i])
    # for i in range(k, len(nums)):
    #     if -seen_values[i] > maxHeap[0]:
    #         heappop(maxHeap)
    #         heappush(-seen_values[i])
    # return maxHeap()
array = [1, 3, 5, 12, 11, 12, 11]

print(most_frequent(array, 2))
