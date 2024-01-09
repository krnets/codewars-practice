# def remove(s):
#     i = len(s)-1
#     while i >= 0:
#         if s[i] != '!':
#             break
#         i -= 1
#     return s[:i+1]

# def remove(s):
#     i = len(s)-1

#     while s[i] == '!':
#         i -= 1

#     return s[:i+1]

def remove(s):
    return s.rstrip('!')
