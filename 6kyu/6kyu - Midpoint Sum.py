# 6kyu - Midpoint Sum

""" For a given list of integers, return the index of the element where the sums of the integers 
to the left and right of the current element are equal.

Ex:

ints = [4, 1, 7, 9, 3, 9]
# Since 4 + 1 + 7 = 12 and 3 + 9 = 12, the returned index would be 3

ints = [1, 0, -1]
# Returns None/nil/undefined/etc (depending on the language) as there
# are no indices where the left and right sums are equal

Here are the 2 important rules:

    The element at the index to be returned is not included in either of the sum calculations!
    Both the first and last index cannot be considered as a "midpoint" (So None for [X] and [X, X]) """

# def midpoint_sum(ints):
#     if len(ints) > 2 and sum(ints) > 1:
#         for i in range(len(ints)):
#             if sum(ints[:i]) == sum(ints[i+1:]):
#                 return i


def midpoint_sum(ints):
    for i in range(1, len(ints)-1):
        if sum(ints[:i]) == sum(ints[i+1:]):
            return i


q = midpoint_sum([4, 1, 7, 9, 3, 9]), 3
q
q = midpoint_sum([1, 0, 1]), 1
q
q = midpoint_sum([9, 0, 1, 2, 3, 4]), 2
q
q = midpoint_sum([0, 0, 4, 0]), 2
q
q = midpoint_sum([-10, 3, 7, 8, -6, -13, 21]), 4
q
q = midpoint_sum([1, 1, 1, 1, -5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 52
q
