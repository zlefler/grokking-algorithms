class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_frequency = {}
        current_window = {}
        r = 0
        for i in range(len(s1)):
            char_frequency[s1[i]] = char_frequency.get(s1[i], 0) + 1
            current_window[s2[i]] = current_window.get(s2[i], 0) + 1
            r += 1

        if current_window == char_frequency:
            return True

        l = 0
        while r < len(s2):
            current_window[s2[r]] = current_window.get(s2[r], 0) + 1
            if current_window[s2[l]] == 1:
                del current_window[s2[l]]
            else:
                current_window[s2[l]] -= 1
            if current_window == char_frequency:
                return True
            l += 1
            r += 1

        return False


s1 = "ab"
s2 = "eidbaooo"

sol = Solution()
print(sol.checkInclusion(s1, s2))
