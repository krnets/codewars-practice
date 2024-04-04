from collections import deque

# def shift_left(a, b):
#     a, b = deque(a), deque(b)
#     counter = 0

#     while a != b:
#         max(a, b, key=len).popleft()
#         counter += 1

#     return counter

# def shift_left(a, b):
#     while a[-1:] == b[-1:] and a:
#         a = a[:-1]
#         b = b[:-1]
#     return len(a) + len(b)


def shift_left(a, b):
    res = 0
    while a != b:
        if len(a) > len(b):
            a = a[1:]
        else:
            b = b[1:]
        res += 1
    return res
