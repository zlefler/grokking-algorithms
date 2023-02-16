class Solution:
    def search(self, nums: list[int], target: int):

        def find_pivot():
            l = 0
            r = len(nums)-1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] < nums[mid+1]:
                    if nums[mid] < nums[0]:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] < nums[mid-1]:
                    return mid
                else:
                    return mid + 1

        def bin_search(array):
            l = 0
            r = len(array)-1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return target
            return -1

        if nums[0] < nums[-1]:
            return bin_search(nums)
        pivot = find_pivot()
        left_side = bin_search(nums[:pivot])
        if left_side > -1:
            return left_side
        return bin_search(nums[pivot:])


n1 = [4, 5, 6, 7, 0, 1, 2]
t1 = 0
sol = Solution()
print(sol.search(n1, t1))
