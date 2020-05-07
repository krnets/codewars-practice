# 7kyu - Digits Average

""" Given an integer, take the (mean) average of each pair of consecutive digits.
Repeat this process until you have a single integer, then return that integer. e.g.

Note: if the average of two digits is not an integer, round the result up (e.g. the average of 8 and 9 will be 9)

digitsAverage(246)  ==>  4

original: 2   4   6
           \ / \ /
1st iter:   3   5
             \ /
2nd iter:     4


digitsAverage(89)  ==>  9

original: 8   9
           \ /
1st iter:   9 """

from math import ceil

# def digits_average(input):
#     while len(str(input)) > 1:
#         input = ''.join(str(ceil((int(x) + int(y)) / 2))
#                         for x, y in zip(str(input), str(input)[1:]))
#     return int(input)

# def digits_average(input):
#     while len(str(input)) > 1:
#         averages = []
#         for x, y in zip(str(input), str(input)[1:]):
#             averages.append(str(ceil((int(x) + int(y)) / 2)))
#         input = ''.join(averages)
#     return int(input)


def digits_average(input):
    digits = list(map(int, str(input)))
    while len(digits) > 1:
        digits = [(x + y + 1) // 2 for x, y in zip(digits, digits[1:])]
    return digits[0]


q = digits_average(246), 4
q
q = digits_average(89), 9
q
q = digits_average(2), 2
q
q = digits_average(245), 4
q
q = digits_average(345), 5
q
q = digits_average(346), 5
q
