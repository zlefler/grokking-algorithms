def pattern_matches(window: dict, pattern: dict) -> bool:
    for key in window:
        if window[key] != pattern.get(key, 0):
            return False
    return True


def build_window(string: str, length: int) -> dict:
    window = {}
    i = 0
    while i < length:
        window[string[i]] = window.get(
            string[i], 0) + 1
        i += 1
    return window


def find_permutations(string: str, pattern: str) -> bool:
    '''Given a string and a pattern, find out if the string contains any permutation of the pattern.

    Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

    abc
    acb
    bac
    bca
    cab
    cba
    If a string has ‘n’ distinct characters, it will have n!n! permutations.'''

    chars_in_pattern = {}

    for char in pattern:
        chars_in_pattern[char] = chars_in_pattern.get(char, 0) + 1

    chars_in_window = build_window(string, len(pattern))

    if pattern_matches(chars_in_window, chars_in_pattern):
        return True

    left = 0
    right = len(pattern)

    while right < len(string):
        chars_in_window[string[right]] = chars_in_window.get(
            string[right], 0) + 1
        right += 1
        chars_in_window[string[left]] -= 1
        if chars_in_window[string[left]] == 0:
            del chars_in_window[string[left]]
        left += 1
        if pattern_matches(chars_in_window, chars_in_pattern):
            return True

    return False


def find_permutation(str1, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # our goal is to match all the characters from the 'char_frequency' with the current
    # window try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False

# map = {}
# len(pattern) times, add char to map
# if len(map) == len(pattern):
# see if map matches pattern
# if yes, return true
# if not, increment right pointer and add to map
# increment left pointer and subtract from map
# if never matches, return false


s1 = "asdcbaf"
p1 = "abc"

s2 = "asdcba"

s3 = "cbgasec"


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
