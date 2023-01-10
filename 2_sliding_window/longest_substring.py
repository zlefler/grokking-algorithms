def longest(string, k):
    '''Given a string, find the length of the longest substring in it with 
    no more than K distinct characters.
You can assume that K is less than or equal to the length of the given string.'''

    if k == 0:
        return -1

    left, longest = 0, 0
    seen = {}

    for right in range(len(string)):
        if string[right] in seen:
            seen[string[right]] += 1
            while seen[string[right]] > k:
                if seen[string[left]] == 1:
                    del seen[string[left]]
                else:
                    seen[string[left]] -= 1
                left += 1
            longest = max(longest, (right - left) + 1)
        else:
            seen[string[right]] = 1
    return longest


print(longest('araaci', 2))
print(longest('araaci', 1))
print(longest('cbbebi', 3))
