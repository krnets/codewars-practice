# 4kyu - Permutations

""" In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

The order of the permutations doesn't matter. """


# def permutations(s):
#     if len(s) == 0:
#         return []
#     elif len(s) == 1:
#         return [s]
#     else:
#         return set(s[i]+p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))

# def permutations(s):
#     if not s:
#         return []
#     elif len(s) == 1:
#         return [s]
#     else:
#         return set(s[i] + p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))


# def permutations(s):
#     if not s:
#         return ['']
#     else:
#         return set(s[i] + p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))

# def permutations(s):
#     return set(s[i] + p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:])) if s else ['']

# from itertools import permutations as perm

# def permutations(s):
#     return [''.join(p) for p in set(perm(s))]

# def permutations(s):
#     return set(''.join(x) for x in perm(s))

def permutations(s):
    if len(s) == 1:
        return s
    head = s[0]
    tail = permutations(s[1:])
    result = set()
    for i in range(len(s)):
        for t in tail:
            result.add(t[:i] + head + t[i:])
    return result

# def permutations(s):
#     result = set()
#     if len(s) == 1:
#         return s
#     else:
#         for i in range(len(s)):
#             for perm in permutations(s[:i] + s[i+1:]):
#                 result.add(s[i] + perm)
#     return result


q = permutations('aabb')  # , ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
q
q = sorted(permutations('a')), ['a']
q
q = sorted(permutations('ab')), ['ab', 'ba']
q
q = sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
q
