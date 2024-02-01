# def diamond(n):
#     if n < 1 or n % 2 == 0:
#         return None
#     res = ""
#     for i in range(n):
#         offset = abs(n // 2 - i)
#         res += "{a}{b}{c}".format(a=" " * offset, b="*" * (n - 2 * offset), c="\n")
#     return res


#   *\n
#  ***\n
# *****\n
#  ***\n
#   *\n


def diamond(n):
    return  "".join("{}{}{}".format(
            " " * (k := abs(n // 2 - i)), "*" * (n - 2 * k), "\n")
            for i in range(n)) if n > 0 and n & 1 else None
