def longestConsecutive(nums: list[int]) -> int:
    nums.sort()
    best = 0
    current = 1
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1] + 1:
            current += 1
        else:
            best = max(best, current)
            current = 1
    return best


l1 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

print(longestConsecutive(l1))
