# 7kyu - Penultimate

""" Find the second-to-last element of a list."""


def penultimate(a):
    try:
        return a[-2]
    except IndexError:
        pass


q = penultimate([1, 2, 3, 4])  # => 3
q
