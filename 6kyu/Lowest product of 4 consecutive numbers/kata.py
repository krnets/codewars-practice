from math import prod


def lowest_product(num):
    if len(num) < 4:
        return "Number is too small"
    arr = list(map(int, num))
    return min(prod(arr[i : i + 4]) for i in range(len(arr) - 3))
