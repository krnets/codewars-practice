# 7kyu - Sheffer stroke

""" Traditionally, all programming languages implement the 3 most common boolean operations: and, or, not. 
These three form the complete boolean algebra, i.e. every possible boolean function from N arguments can be 
decomposed into combination of arguments and and, or, not.

In the school we have learned, that only 2 operations (not and 1 of remaining) is enough to form a complete algebra, 
and the last one can be expressed as a combination of the former. 
A great kata to test that: https://www.codewars.com/kata/boolean-logic-from-scratch/python

Several other operations may form a complete boolean algebra, i.e. xor, 1 and and. 
However, we are interested in an operation, which forms boolean algebra all by itself: 
Sheffer stroke (another operation with such a property is Peirce's arrow).

Sheffer stroke is defined as follows:

sheffer(False, False) = True
sheffer(False, True) = True
sheffer(True, False) = True
sheffer(True, True) = False

The task:

Implement functions and, not and or by only using the preloaded sheffer function. 
Using built-in boolean primitives is disallowed.

Note: for reasons of banning strange solutions, using anonymous functions is also disallowed. """


def sheffer(a, b):
    return False if bool(a) == True and bool(b) == True else True


# def NOT(a):
#     return sheffer(a, a)

# def OR(a, b):
#     return NOT(AND(sheffer(a, a), sheffer(b, b)))

# def AND(a, b):
#     return NOT(sheffer(a, b))


def NOT(a):
    return sheffer(a, a)

def OR(a, b):
    return sheffer(NOT(a), NOT(b))

def AND(a, b):
    return NOT(sheffer(a, b))


# def NOT(a):
#     return sheffer(a, a)

# def OR(a, b):
#     return sheffer(sheffer(a, a), sheffer(b, b))

# def AND(a, b):
#     return NOT(sheffer(a, b))


# @test.describe("Test not")
q = NOT(False)  # True
q
q = NOT(True)  # False
q


# @test.describe("Test or")
q = OR(False, False)  # False
q
q = OR(False, True)  # True
q
q = OR(True, False)  # True
q
q = OR(True, True)  # True
q

# @test.describe("Test and")
q = AND(False, False)  # False
q
q = AND(False, True)  # False
q
q = AND(True, False)  # False
q
q = AND(True, True)  # True
q
