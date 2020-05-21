# 7kyu - Exclamation marks series #3: Remove all exclamation marks from sentence except at the end


# def remove(s):
#     excl_count = 0
#     i = len(s) - 1
#     while s[i] == '!':
#         excl_count += 1
#         i -= 1
#     return s.replace('!', '') + '!' * excl_count

def remove(s):
    return s.replace('!', '') + '!' * (len(s) - len(s.rstrip('!')))


q = remove("Hi!")     # "Hi!"
q
q = remove("Hi!!!")   # "Hi!!!"
q
q = remove("!Hi")     # "Hi"
q
q = remove("!Hi!")    # "Hi!"
q
q = remove("Hi! Hi!")  # "Hi Hi!"
q
q = remove("Hi")      # "Hi"
q
