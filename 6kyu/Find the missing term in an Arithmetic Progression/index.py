# 6kyu - Find the missing term in an Arithmetic Progression

""" An Arithmetic Progression is defined as one in which there is a constant difference 
between the consecutive terms of a given series of numbers. 

You are provided with consecutive elements of an Arithmetic Progression. 
There is however one hitch: exactly one term from the original series is missing 
from the set of numbers which have been given to you.

The rest of the given series is the same as the original AP. 
Find the missing term.

You have to write a function that receives a list, list size will always be at least 3 numbers. 
The missing term will never be the first or last one.

find_missing([1, 3, 5, 9, 11]) == 7 """


def find_missing(sequence):
    return (len(sequence)+1) * (sequence[0] + sequence[len(sequence)-1]) // 2 - sum(sequence)


q = find_missing([1, 2, 3, 4, 6, 7, 8, 9])  # 5
q
q = find_missing([1, 3, 4, 5, 6, 7, 8, 9])  # 2
q
