# 7kyu - SevenAte9

""" Write a function that removes every lone 9 that is inbetween 7s.

seven_ate9('79712312') => '7712312'
seven_ate9('79797') => '777'

Input: String Output: String """

import re

def seven_ate9(str):
    return re.sub('79(?=7)', '7', str)

# def seven_ate9(str):
#     return re.sub(r'79(?=7)', r'7', str)

q = seven_ate9('165561786121789797')  # '16556178612178977'
q
q = seven_ate9('797')  # '77'
q
q = seven_ate9('7979797')  # '7777'
q
