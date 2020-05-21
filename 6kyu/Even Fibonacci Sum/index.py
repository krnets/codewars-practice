# 6kyu - Even Fibonacci Sum

""" Give the summation of all even numbers in a Fibonacci sequence up to, 
but not including, the maximum value.

The Fibonacci sequence is a series of numbers where the next value 
is the addition of the previous two values. The series starts with 0 and 1:

0 1 1 2 3 5 8 13 21...

For example:

eve_fib(0)==0
eve_fib(33)==10
eve_fib(25997544)==19544084 """


def even_fib(m):
    a, b, total = 1, 1, 0
    while a < m:
        if a % 2 == 0:
            total += a
        a, b = b, a+b
    return total


q = even_fib(8), 2
q
q = even_fib(1), 0
q
q = even_fib(10), 10
q
q = even_fib(5), 2
q
