from collections import defaultdict
import re


# def sort_twisted37(arr):
#     d = defaultdict(int)

#     for x in arr:
#         d[x] = int(re.sub(r"3|7", lambda m: ("7", "3")[m.group() == "7"], str(x)))

#     return sorted(arr, key=lambda x: d.get(x, x))


def sort_twisted37(arr):
    swap37 = lambda x: int(str(x).translate(str.maketrans("37", "73")))
    return sorted(arr, key=swap37)
