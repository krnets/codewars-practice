# 7kyu - Product Of Maximums Of Array (Array Series #2)

""" Given an array/list [] of integers, Find the product of the k maximal numbers.
    Array/list size is at least 3.
    Array/list's numbers Will be mixture of positives, negatives and zeros
    Repetition of numbers in the array/list could occur.

Input >> Output Examples

maxProduct ({4, 3, 5}, 2) ==>  return (20)
    Since the size (k) equal 2 , then the subsequence of size 2 whose gives product of maxima is 5 * 4 = 20 .

maxProduct ({8, 10 , 9, 7}, 3) ==>  return (720)
    Since the size (k) equal 3 , then the subsequence of size 2 whose gives product of maxima is 8 * 9 * 10 = 720 .

maxProduct ({10, 8, 3, 2, 1, 4, 10}, 5) ==> return (9600)
    Since the size (k) equal 5 , then the subsequence of size 2 whose gives product of maxima is 10 * 10 * 8 * 4 * 3 = 9600 .

maxProduct ({-4, -27, -15, -6, -1}, 2) ==> return (4)
    Since the size (k) equal 2 , then the subsequence of size 2 whose gives product of maxima is -4 * -1 = 4 .

maxProduct ({10, 3, -1, -27} , 3)  return (-30)
    Since the size (k) equal 3 , then the subsequence of size 2 whose gives product of maxima is 10 * 3 * -1 = -30  """

# from numpy import prod

# def max_product(lst, n_largest_elements):
#         return prod(sorted(lst)[-n_largest_elements:])

from functools import reduce
from operator import mul

def max_product(lst, n):
    return reduce(mul, sorted(lst)[-n:])

# def max_product(lst, n_largest_elements):
#     if isinstance(n_largest_elements, int):
#         return reduce(mul, sorted(lst)[-n_largest_elements:])
#     else:
#         return 0

# from functools import reduce
# from operator import mul
# from heapq import nlargest

# def max_product(lst, n):
#     return reduce(mul, nlargest(n, lst))


# Test.it("Basic Tests")
q = max_product([0]*10, 5)  # 0
q
q = max_product([4, 3, 5], 2)  # 20
q
q = max_product([10, 8, 7, 9], 3)  # 720
q
q = max_product([8, 6, 4, 6], 3)  # 288
q

# Test.it("Larger arrays")
q = max_product(list(range(10, -1, -1)), 5)  # 10*9*8*7*6
q
q = max_product([10, 2, 3, 8, 1, 10, 4], 5)  # 9600
q
q = max_product([13, 12, -27, -302, 25, 37, 133, 155, -1], 5)  # 247895375
q

# Test.it("Arrays with negative values")
q = max_product([-4, -27, -15, -6, -1], 2)  # 4
q
q = max_product([-17, -8, -102, -309], 2)  # 136
q

# Test.it("Arrays with positive and negative values")
q = max_product([10, 3, -27, -1], 3)  # -30
q
q = max_product([14, 29, -28, 39, -16, -48], 4)  # -253344
q
