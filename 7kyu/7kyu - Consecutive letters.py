# 7kyu - Consecutive letters

""" In this Kata, we will check if a string contains consecutive letters as they appear in the English alphabet 
and if each letter occurs only once.

For example: 
solve("abc") = True, because it contains a,b,c
solve("abd") = False, because a, b, d are not consecutive.
solve("dabc") = True, because it contains a, b, c, d
solve("abbc") = False, because b does not occur once.
solve("v") = True

All inputs will be lowercase letters. """


# def solve(st):
#     res = ''
#     for i in range(len(st)):
#         res += chr(i + ord(min(st)))
#     return set(res) == set(st)

def solve(st):
    return ord(max(st)) - ord(min(st)) + 1 == len(set(st)) == len(st)

# import string

# def solve(st):
#     return ''.join(sorted(st)) in string.ascii_letters


q = solve("abc")  # True
q
q = solve("abd")  # False
q
q = solve("dabc")  # True
q
q = solve("abbc")  # False
q
q = solve("trr")  # False
q
