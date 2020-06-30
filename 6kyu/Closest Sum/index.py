""" 6kyu - Closest Sum

Given an array (ints) of n integers, find three integers in arr such that the sum is closest to a given number (num), target.

Return the sum of the three integers. You may assume that each input would have exactly one solution.

closest_sum([-1, 2, 1, -4], 1) # 2 (-1 + 2 + 1 = 2)

Note: your solution should not modify the input array. """

from itertools import combinations


def closest_sum(ints, num):
    return sum(min(combinations(ints, 3), key=lambda x: abs(num - sum(x))))


q = closest_sum([-1, 2, 1, -4], 1), 2
q
q = closest_sum([5, 4, 0, 3], 3), 7
q
q = closest_sum([1, 2, 3, 4], 4), 6
q
q = closest_sum([-2, 2, -3, 1], 3), 1
q
