# def check_exam(arr1, arr2):
#     ans = 0

#     for x, y in zip(arr1, arr2):
#         if x == y:
#             ans += 4
#         elif y != "":
#             ans -= 1

#     return 0 if ans < 0 else ans

def check_exam(arr1, arr2):
    return max(0, sum(4 if x == y else -1 for x, y in zip(arr1, arr2) if y))


q = check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"])  # 6
q
q = check_exam(["a", "a", "c", "b"], ["a", "a", "b", ""])  # 7
q
q = check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"])  # 16
q
q = check_exam(["b", "c", "b", "a"], ["", "a", "a", "c"])  # 0
q
