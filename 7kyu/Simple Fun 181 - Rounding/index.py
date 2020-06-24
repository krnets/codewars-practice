""" 7kyu - Simple Fun #181: Rounding

Round the given number n to the nearest multiple of m.

If n is exactly in the middle of 2 multiples of m, return n instead.

For n = 20, m = 3, the output should be 21.
For n = 19, m = 3, the output should be 18.
For n = 50, m = 100, the output should be 50.

    [input] integer n
    1 ≤ n < 10^9.

    [input] integer m
    3 ≤ m < 109.

    [output] an integer """


# def rounding(n, m):
#     if n == 1:
#         return 0
#     elif m % n == 0:
#         return n
#     else:
#         return (n + (m // 2)) // m * m

def rounding(n, m):
    return n if n % m == m / 2 else round(n / m) * m


q = rounding(1495,  29),  1508
q
q = rounding(1227,  15),  1230
q
q = rounding(20, 3), 21
q
q = rounding(19, 3), 18
q
q = rounding(1, 10), 0
q
q = rounding(50, 100), 50
q
q = rounding(123, 456), 0
q
