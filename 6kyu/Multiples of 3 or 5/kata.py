# def solution(number):
#     ans = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             ans += i
#     return ans


def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
