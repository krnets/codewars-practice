# Beta - Rotated string

""" Write to function that takes as argument two strings and returns True
if one string is a rotation of the other or else it returns False.

# ohell is left rotation of hello
is_rotation('hello','ohell') => True

# elloh is right rotation of hello 
is_rotation('hello','elloh') => True """


# def is_rotation(s1, s2):
#     for i in range(len(s2)):
#         if s2[i:] + s2[:i] == s1:
#             return True
#     return s1 == s2

def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 * 2)


q = is_rotation('hello', 'ohell'), True
q
q = is_rotation('hello', 'lloeh'), False
q
