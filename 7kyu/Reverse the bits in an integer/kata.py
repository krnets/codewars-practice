# def reverse_bits(n):
#     return int(bin(n)[2:][::-1], 2)


# def reverse_bits(n):
#     return int(f"{n:b}"[::-1], 2)


def reverse_bits(n):
    return int(bin(n)[:1:-1], 2)
