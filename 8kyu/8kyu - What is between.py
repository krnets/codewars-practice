# 8kyu - What is between?

""" Complete the function that takes two integers (a, b, where a < b) and 
return an array of all integers between the input parameters, including them.

For example:

a = 1
b = 4
--> [1, 2, 3, 4] """

def between(a, b):
    return list(range(a, b+1))

q = between(1, 4)  # [1, 2, 3, 4]
q
q = between(-2, 2)  # [-2, -1, 0, 1, 2]
q
