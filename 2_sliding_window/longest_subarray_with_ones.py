def longest(array, k: int) -> int:
    '''Given an array containing 0s and 1s, 
    if you are allowed to replace no more than ‘k’ 
    0s with 1s, find the length of the longest contiguous 
    subarray having all 1s.'''
    left, longest = 0, 0
    seen = {}

    for right in range(len(array)):
        if array[right] not in seen:
            seen[array[right]] = 0
        seen[array[right]] += 1
        if seen.get(0, 0) >= k:
            seen[array[left]] -= 1
            left += 1
        longest = max(longest, right - left + seen.get(0, 0) + 1)
    return longest

    # left, longest = 0, 0
    # seen = {}
    # for right in range(len(array)):
    #     if not in seen, add it
    #     if it is, increment it
    #     if seen[0] <= k: continue and add to longest if longer
    #     if not, move left pointer up and decrement as needed


print(longest([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(longest([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
print(longest([1, 1, 1, 1, 1, 1], 3))
