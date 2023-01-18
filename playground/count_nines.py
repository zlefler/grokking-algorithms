def count_nines(n):
    num = 0
    l = len(str(n))
    i = l
    while i > 0:
        k = 10**i
        m = 10**(i-1)
        num += n//k * (i*m)
        n = n % k
        if n >= k-m:
            num += n % m + 1
        i -= 1
    return int(num)


# def count_nines(n):

#     def _parse_last_two_digits(adder, n, total):
#         last_two = n % 100
#         while last_two > 0:
#             if last_two < 9:
#                 last_two -= 1
#                 total += adder
#             if last_two == 99:
#                 last_two -= 1
#                 total += 2 + adder
#             if last_two > 89:
#                 last_two -= 1
#                 total += 1 + adder
#             if last_two < 89 and last_two > 8:
#                 last_two -= 10
#                 total += 1 + adder
#         n = n * 100 + last_two
#         if last_two < 0:
#             n -= 100
#         return (n, total)
#     total = 0
#     adder = 0
#     while n > 99:
#         if n == 900:
#             n -= 1
#             total += 1
#         if n > 900 and n < 1000:
#             n, total = _parse_last_two_digits(
#                 1, n, total)[0], _parse_last_two_digits(1, n, total)[1]
#         adder = 0
#         for digit in str(n)[:-2]:
#             if digit == '9':
#                 adder += 1
#         n -= 100
#         total += 100 * adder + 20
#     return _parse_last_two_digits(adder, n, total)[1]


class TestCountNines():
    def test_one(self):
        assert count_nines(9) == 1

    def test_two(self):
        assert count_nines(80) == 8

    def test_three(self):
        assert count_nines(100) == 20

    def test_four(self):
        assert count_nines(899) == 180

    def test_five(self):
        assert count_nines(900) == 181

    def test_six(self):
        assert count_nines(901) == 182


test = TestCountNines()
# test.test_one()
# test.test_two()
test.test_four()
