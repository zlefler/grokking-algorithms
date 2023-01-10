def solve_knapsack_recursive(profits, weights, capacity):
    '''Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a capacity ‘C.’ The goal is to get the maximum profit out of the knapsack items. Each item can only be selected once, as we don’t have multiple quantities of any item.'''
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_recursive(dp, profits, weights, capacity, 0)


def knapsack_recursive(dp, profits, weights, capacity, index):
    if capacity <= 0 or index >= len(profits):
        return 0

    if dp[index][capacity] != -1:
        return dp[index][capacity]

    profit1 = 0
    if weights[index] <= capacity:
        profit1 = profits[index] + knapsack_recursive(
            dp, profits, weights, capacity - weights[index], index + 1)

    profit2 = knapsack_recursive(dp, profits, weights, capacity, index + 1)

    dp[index][capacity] = max(profit1, profit2)
    return dp[index][capacity]


def solve_knapsack(profits, weights, capacity):

    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = 0

    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0

            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]
            profit2 = dp[i-1][c]

            dp[i][c] = max(profit1, profit2)
    return dp[n-1][capacity]


def solve_knapsack_with_items(profits, weights, capacity):

    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = 0

    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, n):
        for c in range(0, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            profit2 = dp[i-1][c]

            dp[i][c] = max(profit1, profit2)

    print_selected_elements(dp, weights, profits, capacity)
    return dp[n-1][capacity]


def print_selected_elements(dp, weights, profits, capacity):
    print('selected weights are: ')
    n = len(weights)
    total_profit = dp[n-1][capacity]
    for i in range(n-1, 0, -1):
        if total_profit != dp[i-1][capacity]:
            print(f'{weights[i]} ')
            capacity -= weights[i]
            total_profit -= profits[i]
    if total_profit != 0:
        print(f'{weights[0]} ')


def main():
    print(solve_knapsack_with_items([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_with_items([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
