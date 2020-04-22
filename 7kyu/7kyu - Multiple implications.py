# 7kyu - Multiple implications

""" In logic, an implication (or material conditional) states that If p is true, q should be true too.

We can express the result of any implication of two statements as an logical table:

p\q T F      
T   T F
F   T T

In this kata, we will take that further. 
Given an array (return false if the array is empty), assume that from first to last item in the array, 
each implies the next (for example, in an array of three items, p, q, and r: (p->q)->r. 
Return the boolean answer.

Assume that there will be no more than 8 variables in the array, and the array will contain only boolean values. """

from functools import reduce

# def mult_implication(lst):
#     return reduce(lambda p, q: not p or q, lst, True) if lst else None

def mult_implication(lst):
    return reduce(lambda p, q: not p or q, lst) if lst else None


q = mult_implication([False, False]), True
q
q = mult_implication([False, True]), True
q
q = mult_implication([True, False]), False
q
q = mult_implication([True, True]), True
q
q = mult_implication([False]), False
q
q = mult_implication([True]), True
q
q = mult_implication([]), None
q
q = mult_implication(
    [False, False, False, False, False, True, True, False]), False
q
q = mult_implication(
    [False, False, True, True, True, True, True, False]), False
q
q = mult_implication(
    [True, False, True, False, False, True, False, False]), True
q
