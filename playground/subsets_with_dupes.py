def subsets(nums):
    nums.sort()
    res = [[]]
    start_idx = 0
    for i in range(len(nums)):
        if i > 0 and nums[i] != nums[i-1]:
            start_idx = 0
        end_idx = len(res)
        for j in range(start_idx, end_idx):
            new_set = list(res[j])
            new_set.append(nums[i])
            res.append(new_set)
            start_idx += 1
    return res


a1 = [1, 3, 3]

print(subsets(a1))
