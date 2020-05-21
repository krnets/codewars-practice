# 8kyu - Exclamation marks series #2: Remove all exclamation marks from the end of sentence


# def remove(s):
#     res = list(reversed(s))
#     for x in res:
#         if x == '!':
#             res = res[1:]
#         else: break
#     return ''.join(reversed(res))

# def remove(s):
#     while s and s[-1] == '!':
#         s = s[:-1]
#     return s

def remove(s):
    return s.rstrip('!')

# def remove(s):
#     if not s.endswith('!'):
#         return s
#     else:
#         return remove(s[:-1])


q = remove("Hi!")     # "Hi"
q
q = remove("Hi!!!")   # "Hi"
q
q = remove("!Hi")     # "!Hi"
q
q = remove("!Hi!")    # "!Hi"
q
q = remove("Hi! Hi!")  # "Hi! Hi"
q
q = remove("Hi")      # "Hi"
q
