def searchInsert(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            if mid == len(nums) - 1:
                return mid + 1
            plus_one = nums[mid+1]
            if plus_one < target:
                l = mid + 1
            else:
                return mid + 1
        elif nums[mid] > target:
            if mid == 0:
                return 0
            minus_one = nums[mid-1]
            if minus_one > target:
                r = mid - 1
            else:
                return mid
        else:
            return mid
    return -1


l1 = [1, 3, 5]
print(searchInsert(l1, 1))
