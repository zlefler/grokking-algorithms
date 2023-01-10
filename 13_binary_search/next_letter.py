# circular lists are dumb and I've never seen a problem that uses them, but this solution
# is a very clever way to deal with it, so it might be worth remembering. The last line
# is the only one that changes anything from basic binary search.

def next_letter(arr: list[str], key: str) -> str:
    '''Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.
Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter. This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.
Write a function to return the next letter of the given ‘key’.'''
    if key > arr[-1]:
        return arr[0]
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if key < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return arr[l % len(arr)]


#  I think it works:
    # while l <= r:
    #     mid = l + (r - l) // 2
    #     if arr[mid] == key:
    #         if mid < len(arr) - 1:
    #             return arr[mid + 1]
    #         else:
    #             return arr[0]
    #     elif arr[mid] < key:
    #         l = mid + 1
    #     else:
    #         r = mid - 1
    # return arr[l]
print(next_letter(['a', 'c', 'f', 'h'], 'f'))
print(next_letter(['a', 'c', 'f', 'h'], 'b'))
print(next_letter(['a', 'c', 'f', 'h'], 'm'))
print(next_letter(['a', 'c', 'f', 'h'], 'h'))
