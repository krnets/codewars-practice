# 7kyu - Enumerable Magic #5- True for Just One?

""" Create a function called one that accepts two params:

    a sequence
    a function

and returns true only if the function in the params returns true for exactly one item in the sequence.

one([1, 3, 5, 6, 99, 1, 3], bigger_than_ten) -> true
one([1, 3, 5, 6, 99, 88, 3], bigger_than_ten) -> false
one([1, 3, 5, 6, 5, 1, 3], bigger_than_ten) -> false """


# def one(sq, fun):
#     return len(list(filter(fun, sq))) == 1

def one(sq, fun):
    return sum(map(fun, sq)) == 1


def equals_9(x): return x == 9


def less_than_9(x): return x < 9


def greater_than_9(x): return x > 9


arr = (6, 7, 8, 9, 10, 11)


q = one(arr, equals_9), True
q
q = one(arr, less_than_9), False
q
q = one(arr, greater_than_9), False
q
