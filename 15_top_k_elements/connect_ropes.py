from heapq import *


def connect_ropes(ropes):
    '''Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. The cost of connecting two ropes is equal to the sum of their lengths.'''

    minHeap = []

    for rope in ropes:
        heappush(minHeap, rope)

    cost = 0

    while len(minHeap) > 1:
        sum = heappop(minHeap) + heappop(minHeap)
        cost += sum
        heappush(minHeap, sum)

    return cost


print(connect_ropes([1, 3, 11, 5]))
