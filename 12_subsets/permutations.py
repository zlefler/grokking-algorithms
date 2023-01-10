from collections import deque

# This is a complicated one. You use a deque so you can populate the
# right number of arrays with each number, then when you move onto
# the next number, you can just sub in the number you actually want
# at each index.


def find_permutations(nums):
    '''Given a set of distinct numbers, find all of its permutations.
Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:'''
    nums_length = len(nums)
    res = []
    perms = deque()
    perms.append([])
    for current_num in nums:
        n = len(perms)
        for _ in range(n):
            old_perm = perms.popleft()
            for j in range(len(old_perm)+1):
                new_perm = list(old_perm)
                new_perm.insert(j, current_num)
                if len(new_perm) == nums_length:
                    res.append(new_perm)
                else:
                    perms.append(new_perm)

    return res


print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
