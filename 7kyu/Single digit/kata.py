def single_digit(n):
    while n > 9:
        n = n.bit_count()
    return n