""" Beta - Number of ones in binary

Write a function which takes a positive integer and returns the number of ones that appear in its binary representation.  """


def ones(n):
    return f'{n:b}'.count('1')


q = ones(1)  # 1
q
q = ones(4)  # 1
q
q = ones(7)  # 3
q
