# def convert_bits(a, b):
#     return sum(abs(int(x) - int(y)) for x, y in zip(f"{a:032b}", f"{b:032b}"))


def convert_bits(a, b):
    return (a ^ b).bit_count()
