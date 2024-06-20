import re


def i_or_f(arr):
    pattern = r"[+-]?\d*\.?\d*([Ee][+-]?)?\d*"
    return bool(re.fullmatch(pattern, arr))


# def i_or_f(arr):
#     try:
#         float(arr)
#     except ValueError:
#         return False
#     return True


# def i_or_f(arr):
#     try:
#         float(arr)
#         return True
#     except ValueError:
#         return False
