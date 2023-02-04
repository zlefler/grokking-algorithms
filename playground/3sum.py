class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        for i in range(len(nums)):
            target = -nums[i]
            triplets = self.twoSum(nums[i+1:], target)
            if triplets:
                res.extend(triplets)
        return res

    def twoSum(self, nums, target):
        triplets = []
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                triplets.append([-target, nums[i], complement])
            hashmap[complement] = True
        return triplets


n1 = [-1, 0, 1, 2, -1, -4]
sol = Solution()
# print(sol.threeSum(n1))


def my_func(x, y=[]):
    y.append(x)
    return y
