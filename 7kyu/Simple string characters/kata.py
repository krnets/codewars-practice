# def solve(s):
#     uppercase_count, lowercase_count, numbers_count, special_char_count = 0, 0, 0, 0

#     for c in s:
#         if c.isupper(): uppercase_count += 1
#         elif c.islower(): lowercase_count += 1
#         elif c.isdigit(): numbers_count += 1
#         else: special_char_count += 1

#     return [uppercase_count, lowercase_count, numbers_count, special_char_count]


def solve(s):
    res = [0, 0, 0, 0]
    for c in s:
        i = 0 if c.isupper() else 1 if c.islower() else 2 if c.isdigit() else 3
        res[i] += 1
    return res
