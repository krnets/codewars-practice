# def div_con(x):
#     a = sum(num for num in x if not isinstance(num, str))
#     b = sum(int(s) for s in x if isinstance(s, str))
#     return a - b


def div_con(x):
    return sum(-int(d) if isinstance(d, str) else d for d in x)


q = div_con([9, 3, "7", "3"])  # 2
q
q = div_con(["5", "0", 9, 3, 2, 1, "9", 6, 7])  # 14
q
q = div_con(["3", 6, 6, 0, "5", 8, 5, "6", 2, "0"])  # 13
q
q = div_con(["1", "5", "8", 8, 9, 9, 2, "3"])  # 11
q
q = div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7])  # 61
q
