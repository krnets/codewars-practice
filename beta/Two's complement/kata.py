# def get_two_complement_int(n):
#     return int(f"{n:b}".translate(str.maketrans("01", "10")), 2) + 1


# def get_two_complement_int(n: int):
#     return 2 ** n.bit_length() - n


def get_two_complement_int(n: int):
    return 1 + (n ^ (1 << n.bit_length()) - 1)
