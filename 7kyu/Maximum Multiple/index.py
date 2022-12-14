# 7kyu - Maximum Multiple

""" Given a Divisor and a Bound , Find the largest integer N , Such That ,

    N is divisible by divisor
    N is less than or equal to bound
    N is greater than 0.

    The parameters (divisor, bound) passed to the function are only positve values .
    It's guaranteed that a divisor is Found .

maxMultiple (2,7) ==> return (6)
(6) is divisible by (2) , (6) is less than or equal to bound (7) , and (6) is > 0 .

maxMultiple (10,50)  ==> return (50)
(50) is divisible by (10) , (50) is less than or equal to bound (50) , and (50) is > 0 .*

maxMultiple (37,200) ==> return (185)
(185) is divisible by (37) , (185) is less than or equal to bound (200) , and (185) is > 0 . """


# def max_multiple(divisor, bound):
#     for x in range(bound+1)[-1::-1]:
#         if x % divisor == 0:
#             return x

# def max_multiple(divisor, bound):
#     return bound - (bound % divisor)


def max_multiple(divisor, bound):
    for i in reversed(range(bound + 1)):
        if i % divisor == 0:
            return i


q = max_multiple(2, 7)  # 6
q
q = max_multiple(3, 10)  # 9
q
q = max_multiple(7, 17)  # 14
q
q = max_multiple(10, 50)  # 50
q
q = max_multiple(37, 200)  # 185
q
q = max_multiple(7, 100)  # 98
q
