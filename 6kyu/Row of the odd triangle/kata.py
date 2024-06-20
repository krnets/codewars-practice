# def odd_row(n):
#     start = n * (n - 1) + 1
#     return [*range(start, start + 2 * n, 2)]


def odd_row(n):
    return [*range(s := n * (n - 1) + 1, s + 2 * n, 2)]
