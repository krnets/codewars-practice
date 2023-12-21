import itertools


def smallest_integer(matrix):
    s = set(itertools.chain.from_iterable(matrix))

    for i in range(0, max(s)):
        if i not in s:
            return i

    return max(s) + 1
