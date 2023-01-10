import random


def cyclic_sort(arr: list) -> list:
    '''We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based on their creation sequence. This means that the object with sequence number 3 was created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without using any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.'''

    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    return arr[-1]

    # for i in range(1, len(arr)):
    #     if arr[i] != i:
    #         new_index = arr.index(i)
    #         arr[new_index] = arr[i]
    #         arr[i] = i
    # return arr


array = []
for i in range(999999):
    array.append(random.randint(1, 999999))


print(cyclic_sort(array))
