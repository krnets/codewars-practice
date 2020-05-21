# 7kyu - Sum of integers in string

""" Your task in this kata is to implement a function that calculates the sum of the integers inside a string. 

For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", 
the sum of the integers is 3635.

Note: only positive integers will be tested. """

import re

# def sum_of_integers_in_string(s):
#     return sum(int(x) for x in re.sub(r'\D+', ' ', s).split())

def sum_of_integers_in_string(s):
    return sum(int(x) for x in re.findall('\d+', s))

q = sum_of_integers_in_string("12.4")  # 16
q
q = sum_of_integers_in_string("h3ll0w0rld")  # 3
q
q = sum_of_integers_in_string("2 + 3 = ")  # 5
q
q = sum_of_integers_in_string("Our company made approximately 1 million in gross revenue last quarter.")  # 1
q
q = sum_of_integers_in_string("The Great Depression lasted from 1929 to 1939.")  # 3868
q
q = sum_of_integers_in_string("Dogs are our best friends.")  # 0
q
q = sum_of_integers_in_string("C4t5 are 4m4z1ng.")  # 18
q
q = sum_of_integers_in_string("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog")  # 3635
q
