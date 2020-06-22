""" 7kyu - Nth power rules them all!

You are provided with array of positive non-zero ints and int n representing n-th power (n >= 2).

For the given array, calculate the sum of each value to the n-th power. Then subtract the sum of the original array.

Example 1: Input: {1, 2, 3}, 3 --> (1 ^ 3 + 2 ^ 3 + 3 ^ 3 ) - (1 + 2 + 3) --> 36 - 6 --> Output: 30
Example 2: Input: {1, 2}, 5 --> (1 ^ 5 + 2 ^ 5) - (1 + 2) --> 33 - 3 --> Output: 30 """


# def modified_sum(a, n):
#     return sum(x**n for x in a) - sum(a)

def modified_sum(a, n):
    return sum(x**n - x for x in a)


q = modified_sum([1, 2, 3], 3), 30
q
q = modified_sum([1, 2], 5), 30
q
