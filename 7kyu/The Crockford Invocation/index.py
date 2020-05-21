# 7kyu - The Crockford Invocation

""" Write three functions add, subtract, and multiply such that each require two invocations.

add(3)(4)      # 7
subtract(3)(4) # -1
multiply(3)(4) # 12

Once you have done this. Write a function apply that takes one of these functions as an argument and invokes it.

apply(add)(3)(4)      # 7
apply(subtract)(3)(4) # -1
apply(multiply)(3)(4) # 12 """


def add(a):
    return lambda b: a + b

def subtract(a):
    return lambda b: a - b

def multiply(a):
    return lambda b: a * b

# def apply(a):
#     return lambda b: a(b)

def apply(op):
    return op

q = add(3)(4)  # 7
q
q = subtract(3)(4)  # -1
q
q = multiply(3)(4)  # 12
q
q = apply(add)(3)(4)  # 7
q
q = apply(subtract)(3)(4)  # -1
q
q = apply(multiply)(3)(4)  # 12
q
