# making a copy of each set (including an empty one) makes sure that you
# iterate over each possibility when creating subsets.
# using force typing makes sure you don't just alias the list.

def find_subsets(nums: list[int]) -> list[list[int]]:
    '''Given a set with distinct elements, find all of its distinct subsets.'''
    subsets = []
    subsets.append([])
    for num in nums:
        n = len(subsets)
        for i in range(n):
            set1 = list(subsets[i])
            set1.append(num)
            subsets.append(set1)

    return subsets


print("Here is the list of subsets: " + str(find_subsets([1, 3])))
print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))
