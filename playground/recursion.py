# linear

EPSILON = 1e-15  # define EPSILON value


def my_sqrt(x, a):
    difference = a*x - x
    if difference < 0.0:
        difference = -difference
    if difference < EPSILON:
        return a
    else:
        return my_sqrt(x, (a + x/a)/2.0)

# tail


def gcd(m, n):
    r = 0  # initialize variable r
    if m < n:
        return gcd(n, m)
    r = m % n
    if r == 0:
        return n
    else:
        return gcd(n, r)


# binary

def choose(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return choose(n-1, k) + choose(n-1, k-1)


# exponential

def print_array(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


def print_permutations(arr, n, i):
    print_array(arr, n)
    for j in range(i+1, n):
        arr[i], arr[j] = arr[j], arr[i]
        print_permutations(arr, n, i+1)
        arr[i], arr[j] = arr[j], arr[i]

# nested


def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


# mutual

def is_even(n):
    if n == 0:
        return 1
    else:
        return is_odd(n-1)


def is_odd(n):
    return not is_even(n)
