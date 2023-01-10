def separate_dupes(array) -> int:
    '''Given an array of sorted numbers, remove all duplicate number instances from it in-place, 
    such that each element appears only once. The relative order of the elements should be kept the same 
    and you should not use any extra space so that that the solution have a space complexity of O(1).

Move all the unique elements at the beginning of the array and after moving 
return the length of the subarray that has no duplicate in it.'''
    count = 1
    while count < len(array):
        if array[count] == array[count - 1]:
            array = array[:count] + array[count + 1:]
        else:
            count += 1
    return len(array)


print(separate_dupes([2, 3, 3, 3, 6, 9, 9]))
