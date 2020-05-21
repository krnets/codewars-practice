# 7kyu - Geometric Progression Sequence

""" In your class, you have started lessons about geometric progression. 
Since you are also a programmer, you have decided to write a function that will 
print first n elements of the sequence with the given constant r and first element a.

Result should be separated by comma and space.

geometric_sequence_elements(2, 3, 5) == '2, 6, 18, 54, 162' """


def geometric_sequence_elements(a, r, n):
    return ', '.join(str(a * r ** i) for i in range(n))


q = geometric_sequence_elements(2, 3, 5)  # '2, 6, 18, 54, 162'
q
# '2, 4, 8, 16, 32, 64, 128, 256, 512, 1024'
q = geometric_sequence_elements(2, 2, 10)
q
# '1, -2, 4, -8, 16, -32, 64, -128, 256, -512'
q = geometric_sequence_elements(1, -2, 10)
q
