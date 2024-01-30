from math import ceil, floor


# def find_squares(num):
#     m = (num - 1) // 2
#     return f"{(m+1)**2}-{m**2}"


def find_squares(num):
    return "%d-%d" % (ceil(num / 2) ** 2, floor(num / 2) ** 2)
