class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


n1 = [10, 5, 2, 6]
k1 = 100
sol = Solution()
print(sol.numSubarrayProductLessThanK(n1, k1))
