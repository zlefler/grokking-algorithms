def longest(string, k: int) -> int:
    '''Given a string with lowercase letters only, if you are allowed to 
    replace no more than ‘k’ letters with any letter, find the length of
     the longest substring having the same letters after replacement.'''

    left, max_length, max_repeated = 0, 0, 0
    seen = {}

    for right in range(len(string)):
        if string[right] in seen:
            seen[string[right]] += 1
        else:
            seen[string[right]] = 1
        max_repeated = max(max_repeated, seen[string[right]])
        if (right - left + 1 - max_repeated) > k:
            seen[string[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length


print(longest("aabccbb", 2))
