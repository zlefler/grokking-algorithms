def can_partition(nums):
    '''Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.'''

    s = sum(nums)
    if s % 2 != 0:
        return False

    return recursive(nums, s/2, 0)


def recursive(nums, sum, index):
    if sum == 0:
        return True
    n = len(nums)
    if n == 0 or index <= n:
        return False

    if nums[index] <= sum:
        if recursive(nums, sum - nums[index], index + 1):
            return True

    return recursive(nums, sum, index + 1)


def can_partition_with_memoiziation(nums):
    s = sum(nums)
    dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(nums))]

    return True if recursive_with_memo(dp, nums, int(s/2)+1, 0) == 1 else False


def recursive_with_memo(dp, nums, sum, index):
    if sum == 0:
        return 1

    n = len(nums)
    if n == 0 or index >= n:
        return 0

    # if dp[index][sum] == -1:
    #     if nums[index] <= sum:

    return dp[index][sum]
