class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        best = 0
        seen = set()
        while r <= len(s):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            else:
                best = max((r - l) + 1, best)
            seen.add(s[r])
            r += 1
        return best


s1 = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s1))
