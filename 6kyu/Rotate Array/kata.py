# def rotate(arr, n):
#     if n < 0:
#         m = len(arr) + n
#         return arr[-m:] + arr[:-m]
#     m = len(arr) - n
#     return arr[m:] + arr[:m]


# def rotate(arr, n):
#     m = len(arr)
#     idx = (m - (n % m)) % m
#     return arr[idx:] + arr[:idx]


def rotate(arr, n):
    n %= len(arr)
    return arr[-n:] + arr[:-n]
