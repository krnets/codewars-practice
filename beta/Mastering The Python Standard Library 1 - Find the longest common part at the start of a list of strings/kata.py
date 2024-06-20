# def sol(lst):
#     k = 0
#     m = len(min(lst, key=len)) + 1
#     found_end = False

#     for i in range(1, m):
#         sub = lst[0][:i]

#         for word in lst:
#             if not word.startswith(sub):
#                 found_end = True
#                 break
#         if found_end:
#             break
#         k = i

#     return lst[0][:k]


def sol(lst):
    longest = 0
    for i in range(1, len(min(lst, key=len)) + 1):
        sub = lst[0][:i]
        for word in lst:
            if not word.startswith(sub):
                return lst[0][:longest]
        longest = i
    return lst[0][:longest]
