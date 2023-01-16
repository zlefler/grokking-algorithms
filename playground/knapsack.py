def knapsack(weights, profits, capacity):
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    print(dp)
    return _knapsack(dp, weights, profits, capacity, 0)


def _knapsack(dp, weights, profits, capacity, index):

    if capacity <= 0 or index >= len(weights):
        return 0

    if dp[index][capacity] != -1:
        return dp[index][capacity]

    profit1 = 0
    if weights[index] <= capacity:
        profit1 += profits[index]
        profit1 += _knapsack(dp, weights, profits, capacity -
                             weights[index], index+1)

    profit2 = _knapsack(dp, weights, profits, capacity, index+1)
    dp[index][capacity] = max(profit1, profit2)
    return dp[index][capacity]


w1 = [2, 3, 1, 4]
p1 = [4, 5, 3, 7]

print(knapsack(w1, p1, 5))
