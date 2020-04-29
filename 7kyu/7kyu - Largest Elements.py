# 7kyu - Largest Elements

""" Write a program that outputs the top n elements from a list. """

from heapq import nlargest

# def largest(n, xs):
#     return sorted(xs)[-n:]

def largest(n, xs):
    return list(reversed(nlargest(n, xs)))

# def largest(n, xs):
#     return sorted(nlargest(n, xs))

q = largest(2, [7,6,5,4,3,2,1]), [6,7]
q
q = largest(2,[10,9,8,7,6,5,4,3,2,1]),[9,10]
q
q = largest(3,[5,1,5,2,3,1,2,3,5]),[5,5,5]
q
q = largest(7,[9,1,50,22,3,13,2,63,5]),[3, 5, 9, 13, 22, 50, 63]
q