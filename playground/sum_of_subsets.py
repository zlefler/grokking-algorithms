def sum_of_subsets(weights: list[int], target: int) -> list[list[int]]:
    '''given a list of weights `weights` and a target `target`, return all subsets of weights that add up exactly to target. '''

    res = []

    def backtrack(i, array, total):
        if i == len(weights):
            return
        if total < 0:
            return
        if total == 0:
            res.append(list(array))
        array.append(weights[i])
        backtrack(i+1, array, total - weights[i])
        array.pop()
        backtrack(i+1, array, total)

    backtrack(0, [], target)

    return res


w1 = [5, 10, 12, 13, 15, 18]
t1 = 30
print(sum_of_subsets(w1, t1))
