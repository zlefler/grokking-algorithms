# figuring out where to worry about dupes is the hard part.
# if you just make sure the dupe only loops over the arrays
# you've already done with the previous number, it will only give
# discrete solutions.

def find_subsets(nums: list[int]) -> list[list[int]]:
    '''Given a set of numbers that might contain duplicates, find all of its distinct subsets.'''
    nums.sort()
    subsets = []
    subsets.append([])
    start, end = 0, 0
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            start = end
        end = len(subsets)
        for j in range(start, end):
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)
    return subsets


print(find_subsets([1, 3, 3]))
print(find_subsets([1, 5, 3, 3]))
