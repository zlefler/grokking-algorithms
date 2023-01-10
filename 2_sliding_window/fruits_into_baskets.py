def fruits_into_baskets(fruit: list) -> int:
    '''You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.
You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:
Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.'''
    left, max_num, current = 0, 0, 0
    seen = {}
    for right in range(len(fruit)):
        if fruit[right] in seen:
            seen[fruit[right]] += 1
        else:
            seen[fruit[right]] = 1
        current += 1
        while len(seen) > 2:
            current -= 1
            seen[fruit[left]] -= 1
            if seen[fruit[left]] == 0:
                del seen[fruit[left]]
            left += 1
        max_num = max(max_num, current)

    return max_num


print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
