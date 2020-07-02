""" 6kyu - Mutual Recursion

Mutual Recursion allows us to take the fun of regular recursion (where a function calls itself 
until a terminating condition) and apply it to multiple functions calling each other!

Let's use the Hofstadter Female and Male sequences to demonstrate this technique. 
You'll want to create two functions F and M such that the following equations are true:

F(0) = 1
M(0) = 0
F(n) = n - M(F(n - 1))
M(n) = n - F(M(n - 1))

Don't worry about negative numbers, n will always be greater than or equal to zero.

Hofstadter Wikipedia Reference http://en.wikipedia.org/wiki/Hofstadter_sequence#Hofstadter_Female_and_Male_sequences """


# def f(n):
#     if n == 0:
#         return 1
#     return n - m(f(n-1))

# def m(n):
#     if n == 0:
#         return 0
#     return n - f(m(n-1))

# def f(n):
#     return 1 if n == 0 else n - m(f(n-1))

# def m(n):
#     return 0 if n == 0 else n - f(m(n-1))

def f(n):
    return n - m(f(n-1)) if n else 1

def m(n):
    return n - f(m(n-1)) if n else 0


q = f(0), 1
q
q = f(5), 3
q
q = f(10), 6
q
q = m(0), 0
q
q = m(5), 3
q
q = m(10), 6
q
