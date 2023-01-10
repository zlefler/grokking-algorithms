import math


class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_infinite_array(reader: ArrayReader, key: int) -> int:
    '''Given an infinite sorted array (or an array with unknown size), find if a given number ‘key’ is present in the array. Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.
Since it is not possible to define an array with infinite (unknown) size, you will be provided with an interface ArrayReader to read elements of the array. ArrayReader.get(index) will return the number at index; if the array’s size is smaller than the index, it will return Integer.MAX_VALUE.'''
    start = 0
    end = 1

    while reader.get(end) < key:
        newStart = end + 1
        end += (end - start + 1) * 2
        start = newStart

    return binary_search(reader, key, start, end)


def binary_search(reader, key, start, end):
    l = start
    r = end - 1

    while l <= r:
        mid = l + (r - l) // 2
        if reader.get(mid) == key:
            return mid
        elif reader.get(mid) < key:
            l = mid + 1
        else:
            r = mid - 1
    return -1


reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

print(search_infinite_array(reader, 16))
