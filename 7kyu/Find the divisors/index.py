# 7kyu - Find the divisors!

""" Create a function named divisors that takes an integer n > 1 and returns an array with all of the integer's 
divisors (except for 1 and the number itself), from smallest to largest. 
If the number is prime return the string '(integer) is prime' """


# def divisors(integer):
#     divs = []
#     for i in range(2, integer//2+1):
#         if integer % i == 0:
#             divs.append(i)
#     return divs if divs else f'{integer} is prime'


# def divisors(integer):
#     return [i for i in range(2, integer//2+1) if integer % i == 0] or f'{integer} is prime'

# def divisors(n):
#     d = set()
#     for k in range(2, int(n ** 0.5) + 1):
#         if n % k == 0:
#             d.add(k)
#             d.add(n // k)
#     return sorted(d) if d else f"{n} is prime"

# def divisors(integer):
#     nums = []

#     for i in range(2, integer // 2 + 1):
#         if integer % i == 0:
#             nums.append(i)

#     return nums if nums else f'{integer} is prime'


def divisors(integer):
    nums = [x for x in range(2, integer // 2 + 1) if integer % x == 0]

    return nums if nums else f"{integer} is prime"


q = divisors(15)  # [3, 5]
q
q = divisors(12)  # [2, 3, 4, 6]
q
q = divisors(13)  # "13 is prime"
q
q = divisors(25)  # [5]
q
