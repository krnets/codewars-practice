# 7kyu - Multiple remainder of the division

""" Your task it to return true if the fractional part (rounded to 1 digit) of the result (a / b) exists, 
more than 0 and is multiple of n. Otherwise return false. (For Python return True or False)

All arguments are positive digital numbers.

Rounding works like toFixed() method. (if more than...5 rounds up)

isMultiple(5, 2, 3) -> false // 2.5 -> 5 is not multiple of 3
isMultiple(5, 3, 4) -> false // 1.7 -> 7 is not multiple of 4
isMultiple(5, 4, 3) -> true // 1.3 -> 3 is multiple of 3
isMultiple(666, 665, 2) -> false // 1.0 -> return false """


# def isMultiple(a, b, n):
#     if a % b == 0:
#         return False
#     add, num = 0, 0
#     number = str(a / b).split('.')[-1]
#     for i in reversed(number):
#         num = int(i) + add
#         add = num >= 5
#     num = num % 10
#     return num % n == 0 and num != 0

def isMultiple(a, b, n):
    remainder = int((a / b + 0.05) * 10) % 10
    return remainder > 0 and remainder % n == 0


q = isMultiple(5, 2, 3)  # False
q
q = isMultiple(5, 3, 4)  # False
q
q = isMultiple(5, 4, 3)  # True
q
q = isMultiple(666, 665, 2)  # False
q
q = isMultiple(3691401, 1892272, 5)  # False
q
q = isMultiple(5702391, 6121205, 1)  # False
q
