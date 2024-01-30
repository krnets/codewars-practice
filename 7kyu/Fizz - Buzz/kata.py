# def solution(number):
#     a = sum((i % 3 == 0 and i % 5 != 0) for i in range(1, number))
#     b = sum((i % 3 != 0 and i % 5 == 0) for i in range(1, number))
#     c = sum((i % 3 == 0 and i % 5 == 0) for i in range(1, number))
#     return [a, b, c]


# def solution(number):
#     a, b, c = 0, 0, 0
#     for i in range(1, number):
#         if i % 3 == 0:
#             if i % 5 == 0:
#                 c += 1
#             else:
#                 a += 1
#         elif i % 5 == 0:
#             b += 1
#     return [a, b, c]


def solution(number):
    n = number - 1
    m = n // 15
    return [n // 3 - m, n // 5 - m, m]
