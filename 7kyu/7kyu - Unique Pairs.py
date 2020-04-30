# 7kyu - Unique Pairs

""" Mrs. Frizzle is beginning to plan lessons for her science class next semester, and wants to encourage friendship 
amongst her students. To accomplish her goal, Mrs. Frizzle will ensure each student has a chance to partner with 
every other student in the class in a series of science projects.

Mrs. Frizzle does not know who will be in her class next semester, but she does know she will have n students total in her class.

Create the function projectPartners with the parameter n representing the number of students in Mrs. Frizzle's class. 
The function should return the total number of unique pairs she can make with n students.

projectPartners(2) --> returns 1
projectPartners(4) --> returns 6

    your solution should not contain any arrays or objects that are used similar to an array. 
    your function will only recieve a single number that is greater than or equal to 2 
    you do not need to worry about input validation. """

# from itertools import combinations

# def projectPartners(n):
#     return len(list(combinations(range(n), 2)))

def projectPartners(n):
    return n * (n - 1) // 2

# def projectPartners(n):
#     return sum(range(n))

q = projectPartners(2), 1
q
q = projectPartners(3), 3
q
q = projectPartners(4), 6
q
q = projectPartners(5), 10
q
