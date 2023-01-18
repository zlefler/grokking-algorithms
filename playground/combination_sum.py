def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def dfs(start, target, current):
        if target == 0:
            res.append(list(current))
        for i in range(start, len(candidates)):
            new_target = target - candidates[i]
            if new_target < 0:
                return
            current.append(candidates[i])
            dfs(i, new_target, current)
            current.pop()

    dfs(0, target, [])
    return res


print(combinationSum([2, 3, 6, 7], 7))


def comboSum(target, candidates):
    result = []

    def helper(start, sum_so_far, subset):
        if sum_so_far == target:
            result.append(subset[::])
            return
        if sum_so_far > target:
            return

        for i in range(start, len(candidates)):
            num = candidates[i]
            subset.append(num)
            sum_so_far += num
            helper(i, sum_so_far, subset)
            sum_so_far -= num
            subset.pop()

    helper(0, 0, [])
    return result


print(comboSum(7, [2, 3, 6, 7]))
