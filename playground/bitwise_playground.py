[ord(character) for character in "€uro"]

(42).bit_length()


def get_bit(value, bit_index):
    return value & (1 << bit_index)


def bit(value):
    print(value)
    print(value & 1 << 5)


# print(get_bit(0b10000000, bit_index=5))
bit(0b10111111)
