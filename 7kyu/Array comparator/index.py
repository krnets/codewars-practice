# 7kyu -Array comparator

""" You have two arrays in this kata, every array contain only unique elements. 
Your task is to calculate number of elements in first array which also are in second array. """

# def match_arrays(v, r):
#     count = 0
#     for x in v:
#         if x in r:
#             count += 1
#     return count

# def match_arrays(v, r):
#     return sum(1 for x in v if x in r)

# def match_arrays(v, r):
#     return sum(x in r for x in v)

# from collections import Hashable

# def setify(s):
#     return {elt if isinstance(elt, Hashable) else tuple(elt) for elt in s}

# def match_arrays(v, r):
#     return len(setify(v) & setify(r))

# def match_arrays(v, r):
#   v = ['mangling is bad!' + str(i) if isinstance(i, list) else i for i in v]
#   r = ['mangling is bad!' + str(i) if isinstance(i, list) else i for i in r]

#   return len(set(v) & set(r))

# verbose = False # set to True to diplay arrays being tested in the random tests

# def hashable(v):
#     return set(tuple(a) if isinstance(a, list) else a for a in v)

# def match_arrays(v, r):
#     return len(hashable(v).intersection(hashable(r)))

def hashable(v):
    return {tuple(a) if isinstance(a, list) else a for a in v}

def match_arrays(v, r):
    return len(hashable(v) & (hashable(r)))

q = match_arrays(['Perl', 'Closure', 'JavaScript'], ['Go', 'C++', 'Erlang'])  # 0
q
q = match_arrays(['Erlang', 'JavaScript'], ['Go', 'C++', 'Python'])  # 0
q
q = match_arrays([True, 3, 9, 11, 15], [True, 3, 11])  # 3
q
