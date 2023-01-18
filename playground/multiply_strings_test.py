def multiply(num1: str, num2: str) -> str:
    num_dict = {'1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
    string_dict = {1: '1', 2: '2', 3: '3', 4: '4',
                   5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 0: '0'}

    def string_to_int(string):
        int1 = 0
        for char in string:
            int1 *= 10
            int1 += num_dict[char]
        return int1

    int1 = string_to_int(num1)
    int2 = string_to_int(num2)

    product = int1 * int2


def int_to_string(int):
    string = ''
    while int > 0:
        pass


def test_int1():
    assert multiply('100', '5') == (100, 5)
