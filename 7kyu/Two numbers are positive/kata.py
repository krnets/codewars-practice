# def two_are_positive(a, b, c):
#     if a <= 0 and (b > 0 and c > 0):
#         return True
#     if b <= 0 and (a > 0 and c > 0):
#         return True
#     if c <= 0 and (a > 0 and b > 0):
#         return True
#     return False


# def two_are_positive(a, b, c):
#     return (
#         (a <= 0 and (b > 0 and c > 0))
#         or (b <= 0 and (a > 0 and c > 0))
#         or (c <= 0 and (a > 0 and b > 0))
#     )


def two_are_positive(a, b, c):
    return sum([a > 0, b > 0, c > 0]) == 2
