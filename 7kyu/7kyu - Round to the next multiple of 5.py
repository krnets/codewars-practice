# 7kyu - Round to the next multiple of 5

""" Given an integer as input, can you round it to the next (meaning, "higher") 5?

input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.

Input may be any positive or negative integer (including 0).

You can assume that all inputs are valid integers. """

# from math import ceil

# def round_to_next5(n):
#     return ceil(n / 5) * 5


def round_to_next5(n):
    return -n % 5 + n


q = round_to_next5(0)  # 0
q
q = round_to_next5(1)  # 5
q
q = round_to_next5(-1)  # 0
q
q = round_to_next5(5)  # 5
q
q = round_to_next5(7)  # 10
q
q = round_to_next5(20)  # 20
q
q = round_to_next5(39)  # 40
q
