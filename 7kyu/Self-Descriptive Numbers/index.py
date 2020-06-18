""" 7kyu - Self-Descriptive Numbers

A number is self-descriptive when the n'th digit describes the amount n appears in the number.

E.g. 21200:

There are two 0's in the number, so the first digit is 2.
There is one 1 in the number, so the second digit is 1.
There are two 2's in the number, so the third digit is 2.
There are no 3's in the number, so the fourth digit is 0.
There are no 4's in the number, so the fifth digit is 0

Numbers can be of any length up to 9 digits and are only full integers.
For a given number derive a function selfDescriptive(num) that returns;
true if the number is self-descriptive or false if the number is not. """

from collections import Counter

# def self_descriptive(num):
#     str_n = str(num)
#     res = []
#     c = Counter(str_n)
#     str_n = str_n.split('0')[0]
#     for i in range(len(str_n)):
#         count = c.get(str(i), 0)
#         res.append(count == int(str_n[i]))
#     return all(res)


# def self_descriptive(num):
#     str_n = str(num)
#     count = Counter(str_n)
#     str_n = str_n.split('0')[0]
#     for i in range(len(str_n)):
#         if count[str(i)] != int(str_n[i]):
#             return False
#     return True

def self_descriptive(num):
    split = list(map(int, str(num)))
    count = Counter(split)
    return all(count[i] == x for i, x in enumerate(split))

q = self_descriptive(21200), True
q
q = self_descriptive(3211000), True
q
q = self_descriptive(42101000), True
q
q = self_descriptive(21230), False
q
q = self_descriptive(11200), False
q
q = self_descriptive(1210), True
q
q = self_descriptive(51120111), False
q
q = self_descriptive(2020), True
q
q = self_descriptive(11201), False
q
q = self_descriptive(6210001000), True
q
