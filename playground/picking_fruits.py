class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        curr = {}
        l = 0
        r = 0
        total = 0

        while len(curr.keys()) < 1:
            total += fruits[r]
            r += 1

        while l < len(fruits):
            if len(curr.keys()) <= 2:
                total = max(total, sum(fruits[l:r+1]))
                curr[r] = curr.get(r, 0) + 1
                r += 1
            else:
                curr[l] -= 1
                if curr[l] == 0:
                    del curr[l]
                l += 1
        return total


f1 = [1, 2, 1]
sol = Solution()
# print(sol.totalFruit(f1))

bs = ((b'\x10'))
print(bin(int(bs.hex(), 16)))
