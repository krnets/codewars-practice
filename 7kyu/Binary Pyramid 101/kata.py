# def binary_pyramid(m, n):
#     ans = 0
#     for i in range(m, n + 1):
#         ans += int(f"{i:b}")
#     return f"{ans:b}"


def binary_pyramid(m, n):
    return f"{sum(int(f'{i:b}') for i in range(m, n + 1)):b}"
