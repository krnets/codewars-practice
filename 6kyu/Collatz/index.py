# 6kyu - Collatz

""" A collatz sequence, starting with a positive integern, is found by 
repeatedly applying the following function to n until n == 1 :

collatz sequence

 n = { n / 2 for even n ;
      3n + 1 for odd n }

=======

Create a function collatz that returns a collatz sequence string starting with the positive integer argument 
passed into the function, in the following form:

"X0->X1->...->XN"

Where Xi is each iteration of the sequence and N is the length of the sequence.

Sample Input

collatz(4) # should return "4->2->1"
collatz(3) # should return "3->10->5->16->8->4->2->1"

Don't worry about invalid input. Arguments passed into the function are guaranteed to be valid integers >= 1. """


# def collatz(n):
#     seq = [n]
#     while n > 1:
#         n = (n // 2 if n % 2 == 0 else n * 3 + 1)
#         seq.append(n)
#     return '->'.join(str(x) for x in seq)

# def collatz(n):
#     seq = [str(n)]
#     while n > 1:
#         n = (n // 2 if n % 2 == 0 else n * 3 + 1)
#         seq.append(str(n))
#     return '->'.join(seq)

def collatz(n):
    return str(n) + '->' + collatz(n // 2 if n % 2 == 0 else n * 3 + 1) if n != 1 else '1'


q = collatz(3)  # "3->10->5->16->8->4->2->1"
q
