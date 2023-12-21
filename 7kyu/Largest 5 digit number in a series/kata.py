# def solution(digits):
#     ans = ""

#     for i in range(len(digits) - 4):
#         slice = digits[i : i + 5]
#         if slice > ans:
#             ans = slice

#     return int(ans)


def solution(digits):
    return int(max(digits[i : i + 5] for i in range(len(digits) - 4)))
