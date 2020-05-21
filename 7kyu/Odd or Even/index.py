# 7kyu - Odd or Even?

""" Given a list of numbers, determine whether the sum of its elements is odd or even.
Give your answer as a string matching "odd" or "even".
If the input array is empty consider it as: [0] (array with a zero).

odd_or_even([0])          ==  "even"
odd_or_even([0, 1, 4])    ==  "odd"
odd_or_even([0, -1, -5])  ==  "even" """


# def odd_or_even(arr):
#     return 'odd' if sum(arr) % 2 else 'even'

# def odd_or_even(arr):
#     return 'even' if sum(arr) % 2 == 0 else 'odd'

def odd_or_even(arr):
    return ['even', 'odd'][sum(arr) % 2]


q = odd_or_even([0, 1, 2])  # "odd"
q
q = odd_or_even([0, 1, 3])  # "even"
q
q = odd_or_even([1023, 1, 2])  # "even"
q
