from itertools import zip_longest
import numpy as np

# def transpose_two_strings(arr):
#     m, n = map(len, arr)
#     if m < n: arr[0] = arr[0].ljust(n)
#     if m > n: arr[1] = arr[1].ljust(m)
#     df = np.array([*map(list, arr)]).transpose()
#     return "\n".join(" ".join(sub) for sub in df)


# def transpose_two_strings(arr):
#     return "\n".join(" ".join(pair) for pair in zip_longest(*arr, fillvalue=" "))


def transpose_two_strings(arr):
    return "\n".join(map(" ".join, zip_longest(*arr, fillvalue=" ")))


#  ['Hello','World']
# should return

# H W
# e o
# l r
# l l
# o d
