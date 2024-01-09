# def solve(a, b):
#     common_chars = set(a) & set(b)
#     return "".join(filter(lambda c: c not in common_chars, a + b))


def solve(a, b):
    common_chars = set(a) & set(b)
    return "".join(c for c in a + b if c not in common_chars)
