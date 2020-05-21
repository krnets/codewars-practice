# 8kyu - Beginner - Lost Without a Map

""" Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]

For the beginner, try to use the map method - it comes in very handy quite a lot so is a good one to know. """


# def maps(a):
#     return list(map(lambda x: x * 2, a))

# def maps(a):
#     return [x * 2 for x in a]


q = maps([1, 2, 3])  # [2, 4, 6]
q
q = maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
q
q = maps([])  # []
q
