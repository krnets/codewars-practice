# 7kyu - Round to nearest 0 or 5

""" Given an array of numbers, return an array, with each member of input array rounded to a nearest number, divisible by 5.

For example:

roundToFive([34.5, 56.2, 11, 13]);

should return

[35, 55, 10, 15]

Roundings have to be done like "in real life": 22.5 -> 25 """


def round_to_five(numbers):
    base = 5
    return [base * int(x / base + base / 10) for x in numbers]


q = round_to_five([1, 5, 87, 45, 8, 8])  # [0, 5, 85, 45, 10, 10]
q
q = round_to_five([3, 56.2, 11, 13])  # [5, 55, 10, 15]
q
q = round_to_five([22.5, 544.9, 77.5])  # [25, 545, 80]
q
