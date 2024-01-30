from collections import Counter


# def solve(st, k):
#     if k < 1:
#         return st
#     for c, v in sorted(Counter(st).items()):
#         for _ in range(v):
#             st = st.replace(c, "", 1)
#             k -= 1
#             if k == 0:
#                 return st
#     return st


# def solve(st, k):
#     for c in sorted(st)[:k]:
#         st = st.replace(c, "", 1)
#     return st

from string import ascii_lowercase

def solve(st, k):
    abc_iter = iter(ascii_lowercase)
    while k and st:
        prev_len = len(st)
        st = st.replace(next(abc_iter), "", k)
        k = k - (prev_len - len(st))
    return st
