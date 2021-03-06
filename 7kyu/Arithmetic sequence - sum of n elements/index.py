# 7kyu - Arithmetic sequence - sum of n elements

""" In your class, you have started lessons about "arithmetic progression". 
Because you are also a programmer, you have decided to write a function.

This function, arithmetic_sequence_sum(a, r, n), should return the sum of the 
first (n) elements of a sequence in which each element is the sum of the given integer (a), 
and a number of occurences of the given integer (r), based on the element's position within the sequence.

For example:

arithmetic_sequence_sum(2, 3, 5) should return 40:

1     2        3          4            5
a + (a+r) + (a+r+r) + (a+r+r+r) + (a+r+r+r+r) 
2 + (2+3) + (2+3+3) + (2+3+3+3) + (2+3+3+3+3) = 40    """

# def arithmetic_sequence_sum(a, r, n):
#     res = []
#     for i in range(n):
#         temp = r * i + a
#         res.append(temp)
#     return sum(res)

# def arithmetic_sequence_sum(a, r, n):
#     res = []
#     for i in range(n):
#         res.append(r * i + a)
#     return sum(res)

# def arithmetic_sequence_sum(a, r, n):
#     res = 0
#     for i in range(n):
#         res += r * i + a
#     return res

# def arithmetic_sequence_sum(a, r, n):
#     return n * (a + a + (n - 1) * r) // 2


# def arithmetic_sequence_sum(a, r, n):
#     return n * (a * 2 + r * (n - 1)) // 2

def arithmetic_sequence_sum(a, r, n):
    return a * n + r * n * (n - 1) // 2


q = arithmetic_sequence_sum(3, 2, 20)  # 440
q
q = arithmetic_sequence_sum(2, 2, 10)  # 110
q
q = arithmetic_sequence_sum(1, -2, 10)  # -80
q
