# 7kyu - STRONGN Strong Number (Special Numbers Series #2)

""" Definition

Strong number is the number that the sum of the factorial of its digits is equal to number itself.
For example: 145, since

1! + 4! + 5! = 1 + 24 + 120 = 145

So, 145 is a Strong number.

Given a number, Find if it is Strong or not.

Notes

    Number passed is always Positive.
    Return the result as String

strong_num(1) ==> return "STRONG!!!!"
Since , the sum of its digits' factorial of (1) is equal to number itself (1) , Then its a Strong .

strong_num(123) ==> return "Not Strong !!"
Since the sum of its digits' factorial of 1! + 2! + 3! = 9 is not equal to number itself (123) , Then it's Not Strong .

strong_num(2)  ==>  return "STRONG!!!!"
Since the sum of its digits' factorial of 2! = 2 is equal to number itself (2) , Then its a Strong .

strong_num(150) ==> return "Not Strong !!"
Since the sum of its digits' factorial of 1! + 5! + 0! = 122 is not equal to number itself (150), Then it's Not Strong .  """

# from math import factorial as fct


# def strong_num(number):
#     return 'STRONG!!!!' if sum(fct(int(c)) for c in str(number)) == number else "Not Strong !!"

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

def strong_num(number):
    return ("Not Strong !!", "STRONG!!!!")[sum(factorial(int(c)) for c in str(number)) == number]


q = strong_num(1)  # "STRONG!!!!"
q
q = strong_num(2)  # "STRONG!!!!"
q
q = strong_num(145)  # "STRONG!!!!"
q
q = strong_num(7)  # "Not Strong !!"
q
q = strong_num(93)  # "Not Strong !!"
q
q = strong_num(185)  # "Not Strong !!"
q
