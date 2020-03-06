# 7kyu - Boolean logic from scratch

""" You need to implement two functions, xor and or, that replicate the behaviour of their respective operators:

    xor = Takes 2 values and returns true if, and only if, one of them is truthy.
    or = Takes 2 values and returns true if either one of them is truthy.

When doing so, you cannot use the or operator:
||
.
Input

    Not all input will be booleans - there will be truthy and falsey values 
    [the latter including also empty strings and empty arrays]
    There will always be 2 values provided

Examples

    xor(true, true) should return false
    xor(false, true) should return true
    or(true, false) should return true
    or(false, false) should return false """


# def func_or(a, b):
#     if bool(a) == True and bool(b) == True:
#         return True
#     if bool(a) == True and bool(b) == False:
#         return True
#     if bool(a) == False and bool(b) == True:
#         return True
#     if bool(a) == False and bool(b) == False:
#         return False


# def func_xor(a, b):
#     if bool(a) == True and bool(b) == True:
#         return False
#     if bool(a) == True and bool(b) == False:
#         return True
#     if bool(a) == False and bool(b) == True:
#         return True
#     if bool(a) == False and bool(b) == False:
#         return False

# def func_or(a, b):
#     return not bool(a) == bool(b) == False

# def func_xor(a, b):
#     return not bool(a) == bool(b)

# def func_or(a, b):
#     return bool(a) + bool(b) > 0

# def func_xor(a, b):
#     return bool(a) + bool(b) == 1

def func_or(a, b):
    return bool(a) | bool(b) 

def func_xor(a, b):
    return bool(a) ^ bool(b) 

q = func_or(0, 11)  # True
q
q = func_or(None, [])  # False
q
q = func_xor(True, True)  # False
q
q = func_xor(True, False)  # True
q
q = func_xor(False, False)  # False
q
q = func_xor(0, 11)  # True
q
q = func_xor(None, [])  # False
q
