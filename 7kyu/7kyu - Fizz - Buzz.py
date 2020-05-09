# 7kyu - Fizz / Buzz

""" Write a function that takes an integer and returns an array [A, B, C], where 
A is the number of multiples of 3 (but not 5) below the given integer, 
B is the number of multiples of 5 (but not 3) below the given integer and 
C is the number of multiples of 3 and 5 below the given integer.

For example, solution(20) should return [5, 2, 1] """


# def solution(number):
#     arr = range(1, number)
#     A = [x for x in arr if x % 3 == 0 and x % 5 != 0]
#     B = [x for x in arr if x % 3 != 0 and x % 5 == 0]
#     C = [x for x in arr if x % 3 == 0 and x % 5 == 0]
#     return [len(A), len(B), len(C)]

# def solution(number):
#     A = (number-1) // 3
#     B = (number-1) // 5
#     C = (number-1) // (3 * 5)
#     return [A-C, B-C, C]

def solution(number):
    number = number - 1
    C = number // (3 * 5)
    B = number // 5 - C
    A = number // 3 - C
    return [A, B, C]


q = solution(20), [5, 2, 1]
q
q = solution(2), [0, 0, 0]
q
q = solution(14), [4, 2, 0]
q
q = solution(30), [8, 4, 1]
q
q = solution(141), [37, 19, 9]
q
