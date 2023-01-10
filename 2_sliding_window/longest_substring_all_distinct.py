def longest(string) -> int:
    '''Given a string, find the length of the longest substring, which has all distinct characters.'''

    longest, current, left = 0, 0, 0
    seen = {}

    for right in range(len(string)):
        while string[right] in seen:
            del seen[string[left]]
            left += 1
            current -= 1
        seen[string[right]] = True
        current += 1
        longest = max(longest, current)

    return longest

    # for char in string:
    #     while char in seen:
    #         del seen[left]
    #         move left up one
    #     seen[char] = True
    #     current += 1
    #     update longest
    # return


print(longest("aabccbb"))
print(longest("abbbb"))
print(longest("abccde"))
