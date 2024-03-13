# def one_two_three(n):
#     if n == 0:
#         return [0, 0]
#     r = 0
#     m = n
#     while m > 0:
#         r = 10 * r + (m, 9)[m >= 9]
#         m -= 9
#     return [r, int("1" * n)]


def one_two_three(n):
    if n == 0:
        return [0, 0]
    q, r = divmod(n, 9)
    return [int("9" * q + (str(r) if r else "")), int("1" * n)]
