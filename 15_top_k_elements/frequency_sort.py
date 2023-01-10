from heapq import *


# make a frequency map, add the pair to a maxHeap as a tuple, then pop them off and append according
# to the frequency.

def sort_by_frequency(str):
    '''Given a string, sort it based on the decreasing frequency of its characters.'''
    freq_map = {}
    for char in str:
        freq_map[char] = freq_map.get(char, 0) + 1

    maxHeap = []

    for char, freq in freq_map.items():
        heappush(maxHeap, (-freq, char))

    sorted_string = []

    while maxHeap:
        freq, char = heappop(maxHeap)
        for _ in range(-freq):
            sorted_string.append(char)

    return ''.join(sorted_string)


# def frequency_sort(string):
#     freq_map = {}
#     for char in string:
#         freq_map[char] = freq_map.get(char, 0) + 1
#     maxHeap = []
#     for char, freq in freq_map.items():
#         heappush(maxHeap, (-freq, char))
#     res = ''
#     for i in range(len(maxHeap)):
#         for j in range(-maxHeap[i][0]):
#             res += maxHeap[i][1]
#     return res


# print(frequency_sort('Here is the given string after sorting characters by frequency'))
print(sort_by_frequency(
    'Here is the given string after sorting characters by frequency'))
