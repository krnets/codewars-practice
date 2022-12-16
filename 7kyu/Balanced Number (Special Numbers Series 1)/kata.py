# def balanced_num(number):
#     digits = [*map(int, str(number))]
#     n = len(digits)
#     mid = n // 2 if n % 2 else (n + 1) // 2
#     left_sum = sum(digits[: (mid if n % 2 else mid - 1)])
#     right_sum = sum(digits[mid + 1 :])

#     return "%sBalanced" % ("Not " if left_sum != right_sum else "")


def balanced_num(number):
    digits = [*map(int, str(number))]
    mid = (len(digits) - 1) // 2
    balance_sum = sum(digits[i] - digits[-i-1] for i in range(mid))

    return "%sBalanced" % ("Not " if balance_sum else "")


q = balanced_num(7)  # "Balanced"
q
q = balanced_num(959)  # "Balanced"
q
q = balanced_num(13)  # "Balanced"
q
q = balanced_num(432)  # "Not Balanced"
q
q = balanced_num(424)  # "Balanced"
q

q = balanced_num(1024)  # "Not Balanced"
q
q = balanced_num(66545)  # "Not Balanced"
q
q = balanced_num(295591)  # "Not Balanced"
q
q = balanced_num(1230987)  # "Not Balanced"
q
q = balanced_num(56239814)  # "Balanced"
q
