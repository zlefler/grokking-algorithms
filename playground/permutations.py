from collections import deque


def permutations(nums):
    res = []
    permutations = deque()
    permutations.append([])
    for num in nums:
        n = len(permutations)
        for _ in range(n):
            old_perm = permutations.popleft()
            for j in range(len(old_perm)+1):
                new_perm = list(old_perm)
                new_perm.insert(j, num)
                if len(new_perm) == len(nums):
                    res.append(new_perm)
                else:
                    permutations.append(new_perm)
    return res


a1 = [1, 3, 5]

print(permutations(a1))
