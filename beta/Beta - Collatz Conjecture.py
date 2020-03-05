# Beta - Collatz Conjecture

""" The conjecture can be summarized as follows.

Take any positive integer n. 
If n is even, divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. 
Repeat the process indefinitely.

The conjecture is that no matter what number you start with, you will always eventually reach 1.

Write code to perform the Collatz conjecture and print the number of steps to reach 1.

For instance, starting with n = 12, one gets the sequence 12,6, 3, 10, 5, 16, 8, 4, 2, 1. This takes 9 steps. """


def collatz(n):
    count = 0
    while n > 1:
        n = (n / 2 if n % 2 == 0 else n * 3 + 1)
        count += 1
    return count


q = collatz(12)  # 9
q
q = collatz(19)  # 20
q
q = collatz(27)  # 111
q
