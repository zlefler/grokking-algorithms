import random


def find_all_duplicates(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    duplicateNumbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicateNumbers.append(nums[i])

    return duplicateNumbers


# works but slow af:
def find_all_dupes(nums: list[int]) -> list[int]:
    '''We are given an unsorted array containing n numbers taken from the range 1 to n. The array has some numbers appearing twice, find all these duplicate numbers using constant space.'''
    i = 0
    res = []
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] == nums[j]:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            res.append(nums[i])
    return res


arr1 = []
for i in range(1000):
    arr1.append(random.randrange(1, 1000))


def find_dupes_fast(nums):
    seen = {}
    for num in nums:
        if seen.get(num, False):
            seen[num] += 1
        else:
            seen[num] = 1
    res = []
    for key in seen.keys():
        if seen[key] > 1:
            res.append(key)
    return res


print(find_all_dupes(arr1))
