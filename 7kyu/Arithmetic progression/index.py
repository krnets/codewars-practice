# 7kyu - Arithmetic progression

""" In your class, you have started lessons about arithmetic progression. 
Since you are also a programmer, you have decided to write a function 
that will return the first n elements of the sequence with the given 
common difference d and first element a. 
Note that the difference may be zero!

The result should be a string of numbers, separated by comma and space.

# first element: 1, difference: 2, how many: 5
arithmetic_sequence_elements(1, 2, 5) == "1, 3, 5, 7, 9" """


def arithmetic_sequence_elements(a, r, n):
    return ', '.join(str(a + r * x) for x in range(n))


q = arithmetic_sequence_elements(1, 2, 5)  # '1, 3, 5, 7, 9'
q
q = arithmetic_sequence_elements(1, 0, 5)  # '1, 1, 1, 1, 1'
q
q = arithmetic_sequence_elements(1, -3, 10)
q
#     '1, -2, -5, -8, -11, -14, -17, -20, -23, -26'
