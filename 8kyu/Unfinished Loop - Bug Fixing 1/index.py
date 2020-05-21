# 8kyu - Unfinished Loop - Bug Fixing #1

""" Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished For Loop! """


def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1
    return res

# def create_array(n):
#     res = []
#     for i in range(1, n + 1):
#         res += [i]
#     return res

# def create_array(n):
#     return list(range(1, n + 1))


q = create_array(1)  # [1]
q
q = create_array(2)  # [1,2]
q
q = create_array(3)  # [1,2,3]
q
q = create_array(4)  # [1,2,3,4]
q
q = create_array(5)  # [1,2,3,4,5]
q
