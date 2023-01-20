from functools import lru_cache
from math import factorial


@lru_cache
def steps_to(stair):
    if stair == 1:
        return 1
    if stair == 2:
        return 2
    if stair == 3:
        return 4
    else:
        return (steps_to(stair - 3) + steps_to(stair-2) + steps_to(stair-1))


print(steps_to(5))
print(factorial(10))
