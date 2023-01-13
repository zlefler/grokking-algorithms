def fibonacci(num):  # fibonacci(40) takes 45s
    if num == 0:
        return 0
    if num == 1:
        return 1
    return (fibonacci(num - 1) + fibonacci(num - 2))


def fib(num):  # 40 takes .055s, 400 takes .055s
    cache = {0: 0, 1: 1}
    return _fib(num, cache)


def _fib(n, cache):
    if n in cache and cache[n] >= 0:
        return cache[n]
    cache[n] = _fib(n-1, cache) + _fib(n-2, cache)
    return cache[n]


# print(fib(400))


def fib_bottom_up(num):  # fib_bottom_up(40) takes .053s, 400 takes .049s
    if num == 0:
        return 0
    cache = {0: 0, 1: 1}
    for i in range(2, num + 1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[num]


print(fib_bottom_up(400000))


def fib_bu_optimized(num):  # fib_bu_optimized(40) takes .052s
    if num < 2:
        return num
    n1, n2 = 1, 0
    for i in range(2, num):
        n0 = n1 + n2
        n2 = n1
        n1 = n0
    return n1 + n2


# print(fib_bu_optimized(4000000))
