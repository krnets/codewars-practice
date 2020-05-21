# 6kyu - @count_calls

""" Implement the "count" decorator, which adds an attribute "call_count" to a function passed in to it, and increments it every time the function is called.

The behavior of the decorated function must be the same as before. Your decorator must be well-behaved, i.e. the returned function must have the same name and docstring as the original, and must be able to handle the same arguments.

Here's an example :

@count_calls
def multiply(a, b=1):
  # Calculates the product of a and b.
  return a * b

multiply.call_count == 0 # True

for _ in range(3):
  multiply(1)

multiply.call_count == 3 # True """

# import functools

# def count_calls(func):
#     @functools.wraps(func)
#     def decorator(*args, **kwargs):
#         decorator.call_count += 1
#         return func(*args, **kwargs)
#     decorator.call_count = 0
#     return decorator

from functools import wraps


def count_calls(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper


@count_calls
def multiply(a, b=1):
    """Calculates the product of a and b."""
    return a * b


# Decorated function should have call_count attribute equal to zero
q = multiply.call_count, 0
q

# Decorated function should have call_count attribute equal to three after three calls have been made
[multiply(1) for _ in range(3)]
q = multiply.call_count, 3
q

# Decorated function has same behavior as before
q = multiply(1, b=2), 2
q

# Decorated function has the same name as before
q = multiply.__name__, "multiply"
q

# Decorated function has the same docstring as before
q = multiply.__doc__, "Calculates the product of a and b."
q
