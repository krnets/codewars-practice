# 6kyu - memoize

""" Implement the "memoize" decorator, which adds memoization capabilities to a function in order to make it more efficient. 
In short, memoization means storing computed values instead of recomputing every time. 
In the example below, this means that you only calculate fib(n) once for every n.

The decorated function must return the same values as before for the same inputs. 
Your decorator must be well-behaved, i.e. the returned function must have the same name and docstring as the original.

Your decorator will only be tested on functions that have a single argument.

Example :

@count_calls
def fib(n):
    # Computes the nth number in the Fibonacci sequence.
    return fib(n - 2) + fib(n - 1) if n > 1 else [0, 1][n]

fib(10)
fib.call_count == 177 # True
fib(10)
fib.call_count == 344 # True

fib = count_calls(memoize(fib))
fib(10)
fib.call_count == 19 # True
fib(10)
fib.call_count == 20 # True

The count_calls decorator is preloaded for you if you wish to use it. 
Do not rebind count_calls, as this could cause the tests to fail.

Note: you are not allowed to use the lru_cache decorator from the functools module for this task. """


# from functools import wraps

# def memoize(func):
#     cache = {}
#     @wraps(func)
#     def decorator(arg):
#         if not arg in cache:
#             cache[arg] = func(arg)
#         return cache[arg]
#     return decorator

import functools

def memoize(func):
    cache = {}

    @functools.wraps(func)
    def decorator(*args):
        if args in cache:
            return cache[args]
        return cache.setdefault(args, func(*args))

    return decorator
