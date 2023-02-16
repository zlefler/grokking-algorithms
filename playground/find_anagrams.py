class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_map = {}
        for char in p:
            p_map[char] = p_map.get(p, 0) + 1

        l = r = 0
        indices = []
        s_map = {}
        while r < len(p):
            s_map[s[r]] = s_map.get(s[r], 0) + 1
            r += 1

        while r < len(s):
            if s_map == p_map:
                indices.append(l)
            s_map[s[r]] = s_map.get(s[r], 0) + 1
            s_map[s[l]] -= 1
            if s_map[s[l]] == 0:
                del s_map[s[l]]
            r += 1
            l += 1

        if s_map == p_map:
            indices.append(l)
        return indices
