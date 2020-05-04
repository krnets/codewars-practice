# 7kyu - SequenceSum

""" Sum of 'n' Numbers

A sequence or a series, in mathematics, is a string of objects, like numbers, 
that follow a particular pattern. The individual elements in a sequence are called terms.

For example, some simple patterns include: 3, 6, 9, 12, 15, 18, 21, ...
Pattern: "add 3 to the previous number to get the next number"

0, 12, 24, 36, 48, 60, 72, ...

Pattern: "add 12 to the previous number to get the next number"

How about generating a more complicated pattern?
0, 1, 3, 6, 10, 15, 21, 28, ...
0(0)_
,1
(0+1)
,3
(0+1+2)
,6
(0+1+2+3)_...

Pattern: "thenth term is the sum of numbers(from 0 ton, inclusive)"

sum_of_n takes an integer n and returns a List of length abs(n) + 1. 

The List contains the numbers in the arithmetic series produced by taking the sum of 
the consecutive integer numbers from 0 to n inclusive.

    n can also be 0 or a negative value.

5 -> [0, 1, 3, 6, 10, 15]
-5 -> [0, -1, -3, -6, -10, -15]
7 -> [0, 1, 3, 6, 10, 15, 21, 28] """


# def sum_of_n(n):
#     res = []
#     x = 0
#     sign = -1 if n < 0 else 1
#     for i in range(abs(n)+1):
#         x += i
#         res.append(x * sign)
#     return res

def sum_of_n(n):
    sign = -1 if n < 0 else 1
    return [(i * (i+1) // 2) * sign for i in range(abs(n)+1)]

# def sum_of_n(n):
#     sign = -1 if n < 0 else 1
#     return [i * (i+1) // 2 * sign for i in range(abs(n)+1)]


q = sum_of_n(3), [0, 1, 3, 6]
q
q = sum_of_n(1), [0, 1]
q
q = sum_of_n(0), [0]
q
q = sum_of_n(-4), [0, -1, -3, -6, -10]
q
