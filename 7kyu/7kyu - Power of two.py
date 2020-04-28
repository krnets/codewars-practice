# 7kyu - Power of two

""" Complete the function power_of_two that determines if a given non-negative integer is a power of two. 
From the corresponding Wikipedia entry:

    a power of two is a number of the form 2n where n is an integer, i.e. the result of exponentiation 
    with number two as the base and integer n as the exponent.

You may assume the input is always valid.

power_of_two(1024) ==> True
power_of_two(4096) ==> True
power_of_two(333)  ==> False

Beware of certain edge cases - for example, 1 is a power of 2 since 2^0 = 1 and 0 is not a power of 2. """


# def power_of_two(x):
#     return x > 0 and not bool(x & (x - 1))

# def power_of_two(x):
#     return x and not bool(x & (x-1))

def power_of_two(x):
    return bin(x).count('1') == 1


q = power_of_two(147573952589676412923), False
q
q = power_of_two(1152921504606846977), False
q
q = power_of_two(0), False
q
q = power_of_two(1), True
q
q = power_of_two(2), True
q
q = power_of_two(5), False
q
q = power_of_two(6), False
q
q = power_of_two(4096), True
q
q = power_of_two(1024), True
q
q = power_of_two(333), False
q
