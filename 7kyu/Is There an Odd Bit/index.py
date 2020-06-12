""" 7kyu - Is There an Odd Bit?

Return 1 when ANY odd bit of x equals 1; 0 otherwise.

x is unsigned.
(Assume "0 index", aka the least significant bit is considered position 0)
Assume x is 32 bits.

Example:

any_odd(2) will return 1 because at least one odd bit is 1 (0010).
any_odd(170) will return 1 because all of the odd bits are 1 (10101010).
any_odd(5) will return 0 because none of the odd bits are 1 (0101). """


def any_odd(x):
    return 1 if '1' in bin(x)[-2::-2] else 0


q = any_odd(5), 0
q
q = any_odd(170), 1
q
q = any_odd(2), 1
q
