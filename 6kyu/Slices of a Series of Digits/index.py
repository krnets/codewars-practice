""" 6kyu - Slices of a Series of Digits

Write a program that will take a string of digits and give you all the possible consecutive slices of length n in that string.

Raise an error if n is larger than the length of the string.

For example, the string "01234" has the following 2-digit slices:

[0, 1], [1, 2], [2, 3], [3, 4]

The same string has the following 4-digit slices:

[0, 1, 2, 3], [1, 2, 3, 4] """


def series_slices(digits, n):
    if n > len(digits):
        raise ValueError('n is larger than the length of digits')
    return [list(map(int, digits[i:i+n])) for i in range(len(digits)-n+1)]


q = series_slices("01234", 2)
#  [[0, 1], [1, 2], [2, 3], [3, 4]]
q
q = series_slices("01234", 4)
#  [[0, 1, 2, 3], [1, 2, 3, 4]]
q
