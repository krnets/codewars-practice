# def manipulate(n):
#     s = str(n)
#     mid = len(s) // 2
#     return int(s[:mid] + "0" * (mid + (len(s) & 1)))

# return int(s[:half] + "0" * (half + 1)) if len(s) & 1 else int(s[:half] + "0" * (half))


# def manipulate(n):
#     s = str(n)
#     mid = len(s) // 2
#     return int(s[:mid] + "0" * len(s[mid:]))

from math import log10


def manipulate(n):
    pow_10_digits = 10 ** (1 + log10(n or 1) // 2)
    return n // pow_10_digits * pow_10_digits
