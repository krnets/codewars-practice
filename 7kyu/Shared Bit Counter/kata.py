# def shared_bits(a, b):
#     counter = 0
#     while a and b:
#         if a & 1 and b & 1:
#             counter += 1
#         a >>= 1
#         b >>= 1
#     return counter >= 2


def shared_bits(a, b):
    return (a & b).bit_count() >= 2
