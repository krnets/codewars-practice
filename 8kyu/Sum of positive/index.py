# 8kyu - Sum of positive

""" You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0. """


# def positive_sum(arr):
#     sum = 0
#     for x in arr:
#         if x > 0:
#             sum += x
#     return sum

# def positive_sum(arr):
#     return sum(filter(lambda x: x > 0, arr))

def positive_sum(arr):
    return sum(x for x in arr if x > 0)


# Test.it("works for some examples")
q = positive_sum([1, 2, 3, 4, 5])  # 15
q
q = positive_sum([1, -2, 3, 4, 5])  # 13
q
q = positive_sum([-1, 2, 3, 4, -5])  # 9
q

# Test.it("returns 0 when array is empty")
q = positive_sum([])  # 0
q

# Test.it("returns 0 when all elements are negative")
q = positive_sum([-1, -2, -3, -4, -5])  # 0
q
