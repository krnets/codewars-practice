# Beta - Generating Permutations

""" Write a generator function named permutations that returns all permutations of the supplied list.

This function cannot modify the list that is passed in, or modify the lists that it returns inbetween iterations.

In Python a generator function is a function that uses the yield keyword instead of return to return an iterable set of results.

example output:

for p in permutations([1, 2, 3]):
  print p

[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 2, 1]
[3, 1, 2]

Note 1: itertools.permutations has been disabled for this kata.

Note 2: The function must be a real generator function, not just an iterator. 
All generators are iterators, but not all iterators are generators. """

# def permutations(lst, start=0):
#     if start == 0:
#         lst = lst[:]
#     if start == len(lst)-1:
#         yield lst[:]
#     for i in range(start, len(lst)):
#         lst[start], lst[i] = lst[i], lst[start]
#         for p in permutations(lst, start+1):
#             yield p
#         lst[start], lst[i] = lst[i], lst[start]


def permutations(lst):
    if len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            for perm in permutations(lst[:i] + lst[i+1:]):
                yield [lst[i]] + perm

# p = permutations = lambda a: ([x] + y for i, x in enumerate(a) for y in p(a[:i] + a[i+1:])) if len(a) - 1 else [a]


q = set([tuple(p) for p in permutations([1, 2, 3])])
q

q = set([(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 2, 1), (3, 1, 2)])
q
