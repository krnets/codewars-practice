# 6kyu - Calculate the function f(x) for a simple linear sequence (Easy)

""" For any given linear sequence, calculate the function [f(x)] and return it as a string.

For example:

get_function([0, 1, 2, 3, 4]) => "f(x) = x"
get_function([0, 3, 6, 9, 12]) => "f(x) = 3x"
get_function([1, 4, 7, 10, 13]) => "f(x) = 3x + 1"

Assumptions for this kata are:

    the sequence argument will always contain 5 values equal to f(0) - f(4).
    the function will always be in the format "nx +/- m", 'x +/- m', 'nx', 'x' or 'm'
    if a non-linear sequence simply return 'Non-linear sequence' or Nothing in Haskell. """

def get_function(seq):
    m = seq[0]
    n = seq[1] - m
    if any(s != n*x+m for x, s in enumerate(seq)):
        return "Non-linear sequence"
    return "f(x) = {}{}{}{}{}{}".format(
        "-"         * (n < 0),
        str(abs(n)) * (abs(n) > 1),
        "x"         * (n != 0),
        " + "       * (m > 0 and n != 0),
        " - "       * (m < 0),
        str(abs(m)) * (m != 0 or n == 0)
    )


q = get_function([0, 1, 2, 3, 4])  # "f(x) = x"
q
q = get_function([0, 3, 6, 9, 12])  # "f(x) = 3x"
q
q = get_function([1, 4, 7, 10, 13])  # "f(x) = 3x + 1"
q
q = get_function([1, 4, 7, 10, 12])  # "Non-linear sequence"
q
