class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = r = 0
        sub_arrays = 0
        while l < len(nums):
            r = l
            while r < len(nums):
                product = 1
                for num in nums[l:r+1]:
                    product *= num
                if product < k:
                    sub_arrays += 1
                    r += 1
                else:
                    l += 1
                    break
            l += 1
        return sub_arrays
