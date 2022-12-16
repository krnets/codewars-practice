"""
Take 2 strings s1 and s2 including only letters from a to z. 
Return a new sorted string, the longest possible, 
containing distinct letters - 
each taken only once - 
coming from s1 or s2.

"""

# def longest(a1, a2):
#     return ''.join(sorted(set(a1).union(a2)))


# def longest(a1, a2):
#     return "".join(sorted(set(a1 + a2)))


def longest(a1, a2):
    return "".join(sorted(set(a1) | set(a2)))


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
q = longest(a, b)  # "abcdefklmopqwxy"
q

a = "abcdefghijklmnopqrstuvwxyz"
q = longest(a, a)  # "abcdefghijklmnopqrstuvwxyz"
q

a = "aretheyhere"
b = "yestheyarehere"
q = longest(a, b)  # "aehrsty"
q

q = "loopingisfunbutdangerous"
b = "lessdangerousthancoding"
q = longest(a, b)  # "abcdefghilnoprstu"
q

a = "inmanylanguages"
b = "theresapairoffunctions"
q = longest(a, b)  # "acefghilmnoprstuy"
q
