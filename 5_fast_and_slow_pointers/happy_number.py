def happy_number(num: int) -> bool:
    '''Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.'''
    p1, p2 = num, sum_squares(num)

    while p1 != p2:
        p1 = sum_squares(p1)
        p2 = sum_squares(sum_squares(p2))
        if p1 == 1:
            return True
    return False


def sum_squares(num):
    old_string = str(num)
    arr = [int(num) for num in old_string]
    total = 0
    for num in arr:
        total += num ** 2
    return total


print(happy_number(23))
print(happy_number(12))
