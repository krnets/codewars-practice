# def asterisc_it(n):
#     if isinstance(n, list):
#         n = "".join(map(str, n))
#     arr = [*map(int, str(n))]
#     res = str(arr[0])

#     for i, x in enumerate(arr[1:], 1):
#         if x % 2 == 0 and arr[i - 1] % 2 == 0:
#             res += "*"
#         res += str(x)
#     return res


import re

def asterisc_it(n):
    s = n
    if   isinstance(n, int):  s = str(n)
    elif isinstance(s, list): s = "".join(map(str, n))
    return re.sub(r"(?<=[02468])(?=[02468])", "*", s)
