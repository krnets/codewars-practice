# 7kyu - Lazily executing a function

""" Deferring a function execution can sometimes save a lot of execution time in our programs 
by postponing the execution to the latest possible instant of time, when we're sure that 
the time spent while executing it is worth it.

Write a method make_lazy that takes in a function (symbol for Ruby) and the arguments to 
the function and returns another function (lambda for Ruby) which when invoked, 
returns the result of the original function invoked with the supplied arguments.

For example:

Given a function add

function add (a, b) {
  return a + b;
}

One could make it lazy as:

var lazy_value = make_lazy(add, 2, 3);

The expression does not get evaluated at the moment, but only when you invoke lazy_value as:

lazy_value() => 5

The above invokation then performs the sum.

Please note: The functions that are passed to make_lazy may take one or more arguments 
and the number of arguments is not fixed. """

from random import randint


# def make_lazy(f, *args):
#     return lambda: f(*args)

def make_lazy(f, *args, **kwargs):
    return lambda: f(*args, **kwargs)

# from functools import partial as make_lazy

def modding(a, b):
    return a % b


lazy_mod = make_lazy(modding, 4, 4)
q = lazy_mod() == 0
q
rand_num = randint(0, 10)
rand_num2 = randint(0, 10)
lazy_rand = make_lazy(modding, rand_num, rand_num2)
q = lazy_rand() == modding(rand_num, rand_num2)
q
