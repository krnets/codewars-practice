# from functools import reduce

# def title_to_number(title):
#     return reduce(lambda acc, c: 26 * acc + ord(c) - 64, title, 0)


# def title_to_number(title):
#     res = 0
#     for c in title:
#         res = 26 * res + ord(c) - 64
#     return res


def title_to_number(title):
    return sum((ord(c) - 64) * 26**i for i, c in enumerate(reversed(title)))
