# 7kyu - Find Factors Down to Limit

""" In this Kata you have to find the factors of integer down to the limit including the limiting number. 
There will be no negative numbers. Return the result as an array of numbers in ascending order.

If the limit is more than the integer, return an empty list

As a challenge, see if you can do it in one line """


def factors(integer, limit):
    return [num for num in range(limit, integer+1) if integer % num == 0]


q = factors(5, 1), [1, 5]
q
q = factors(30, 2), [2, 3, 5, 6, 10, 15, 30]
q
q = factors(100, 75), [100]
q
q = factors(40, 5), [5, 8, 10, 20, 40]
q
q = factors(1, 5), []
q
