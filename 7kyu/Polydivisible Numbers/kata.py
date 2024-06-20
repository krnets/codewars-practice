# def polydivisible(x):
#     digits = [*map(int, str(x))]
#     n = digits[0]

#     for i in range(1, len(digits)):
#         n = n * 10 + digits[i]
#         if n % (i + 1) != 0:
#             return False
#     return True


# def polydivisible(x):
#     digits = str(x)

#     for i in range(1, len(digits) + 1):
#         if int(digits[:i]) % i != 0:
#             return False
#     return True


def polydivisible(x):
    digits = str(x)
    return all(int(digits[:i]) % i == 0 for i in range(1, len(digits) + 1))
