import math


def isPowerOfTwo(n: int) -> bool:
    for num in range(int(math.sqrt(n))+2):
        if n == 0:
            return False
        return n and (-n) == n


print(isPowerOfTwo(8))
