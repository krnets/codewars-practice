# 7kyu - Collatz Conjecture Length

""" The Collatz Conjecture states that for any natural number n, if n is even, divide it by 2. 
If n is odd, multiply it by 3 and add 1. If you repeat the process continously for n, n will eventually reach 1.

For example, if n = 20, the resulting sequence will be:

[20, 10, 5, 16, 8, 4, 2, 1]

Write a program that will output the length of the Collatz Conjecture for any given n. In the example above, the output would be 8.

For more reading see: http://en.wikipedia.org/wiki/Collatz_conjecture """


# def collatz(n):
#     count = 1
#     while n != 1:
#         n = (n // 2 if n % 2 == 0 else n * 3 + 1)
#         count += 1
#     return count

def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatz(n // 2)
    else:
        return 1 + collatz(n * 3 + 1)


q = collatz(20)  # 8
q
q = collatz(15)  # 18
q
