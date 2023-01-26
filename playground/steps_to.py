from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        # self.cache = {}
        # return self.recurse(n)

        if n <= 2:
            return n

        a, b, c = 0, 1, 2

        while (n > 2):
            a, b = b, c
            c = a + b
            n = n - 1

        return c

    @lru_cache
    def recurse(self, n):
        if n == 1:
            return 1
        elif n == 0:
            return 1

        # if n in self.cache:
        #     return self.cache[n]

        ans = self.climbStairs(n-1) + self.climbStairs(n-2)

        # self.cache[n] = ans

        return ans


sol = Solution()

print(sol.climbStairs(35))
