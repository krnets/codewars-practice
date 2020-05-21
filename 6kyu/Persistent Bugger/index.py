# 6kyu - Persistent Bugger

""" Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.

 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number """

# from functools import reduce

# def persistence(n):
#     if len(str(n)) == 1:
#         return 0
#     return 1 + persistence(reduce(lambda x, y: int(x) * int(y), list(str(n))))

# from operator import mul

# def persistence(n):
#     count = 0
#     while n >= 10:
#         n = reduce(mul, [int(x) for x in str(n)], 1)
#         count += 1
#     return count

# def persistence(n):
#     nums = [int(x) for x in str(n)]
#     count = 0
#     while len(nums) > 1:
#         res = reduce(lambda x, y: x * y, nums)
#         nums = [int(x) for x in str(res)]
#         count += 1
#     return count

def persistence(n):
    if n < 10:
        return 0
    mult = 1
    while n > 0:
        mult = n % 10 * mult
        n = n // 10
    return 1 + persistence(mult)

q = persistence(39)  # 3
q
q = persistence(4)  # 0
q
q = persistence(25)  # 2
q
q = persistence(999)  # 4
q
