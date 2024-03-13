# from collections import deque

# def arrange(s):    # works but times out on large tests
#     q = deque(s)
#     t = []
#     while q:
#         t.append(q.popleft())
#         if q:
#             t.append(q.pop())
#         r = deque()
#         while q:
#             r.append(q.pop())
#         q = r
#     return t


# def arrange(s):
#     if len(s) < 2:
#         return s
#     l, r = 0, len(s) - 1
#     t = []
#     flag = False

#     while l < r:
#         if flag:
#             t.append(s[r])
#             t.append(s[l])
#         else:
#             t.append(s[l])
#             t.append(s[r])
#         l += 1
#         r -= 1
#         flag = not flag

#     if len(s) & 1:
#         t.append(s[l])

#     return t

from itertools import count, cycle

def arrange(s):
    inc, dec = count(), count(-1, -1)
    c_iter = cycle([inc, dec, dec, inc])
    return [s[next(next(c_iter))] for _ in range(len(s))]
