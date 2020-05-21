# 7kyu - No oddities here

""" Write a small function that returns the values of an array that are not odd.
All values in the array will be integers. Return the good values in the order they are given."""


def no_odds(values):
    return [x for x in values if x % 2 == 0]


q = no_odds([0, 1])  # [0], 'Zero through one'
q
q = no_odds([0, 1, 2, 3])  # [0, 2], 'Zero through three'
q
q = no_odds([1, 3, 5, 7, 9])  # [], 'Odds through ten'
q
q = no_odds([0, 2, 4, 6, 8, 10])  # [0, 2, 4, 6, 8, 10], 'Evens through ten'
q
q = no_odds([-1, -3, -5, -7, -9])  # [], 'Negative odds'
q
q = no_odds([2, 4, 8, 6, 0])  # [2, 4, 8, 6, 0], 'Out of order'
q
q = no_odds([])  # [], 'Empty list'
q
