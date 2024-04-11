# def solve(s):
#     if s == s[::-1]:
#         return "OK"
#     for i in range(len(s)):
#         candidate = s[:i] + s[i + 1 :]
#         if candidate == candidate[::-1]:
#             return "remove one"
#     return "not possible"


def solve(s):
    is_pali = lambda x: x == x[::-1]
    return "OK" if is_pali(s) else "remove one" if any(is_pali(s[:i] + s[i+1:]) for i in range(len(s))) else "not possible"