"""Given a string str, reverse it and omit all non-alphabetic characters"""

# from collections import deque

# def reverse_letter(string):
#     queue = deque()

#     for _, c in enumerate(string):
#         if c.isalpha():
#             queue.appendleft(c)

#     return "".join(queue)


def reverse_letter(string):
    return "".join(filter(str.isalpha, string))[::-1]


q = reverse_letter("krishan")  # "nahsirk"
q
q = reverse_letter("ultr53o?n")  # "nortlu"
q
q = reverse_letter("ab23c")  # "cba"
q
q = reverse_letter("krish21an")  # "nahsirk"
q
