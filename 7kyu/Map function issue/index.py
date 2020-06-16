""" 7kyu - Map function issue

In computer science, a programming language is said to have first-class functions 
if it treats functions as first-class citizens. Specifically, this means the language 
supports passing functions as arguments to other functions, returning them as the values 
from other functions, and assigning them to variables or storing them in data structures.

First-class functions are a necessity for the functional programming style, in which the use 
of higher-order functions is a standard practice. A simple example of a higher-ordered function 
is the map function, which takes, as its arguments, a function and a list, and returns the list 
formed by applying the function to each member of the list. For a language to support map, 
it must support passing a function as an argument. See more on https://en.wikipedia.org/wiki/First-class_function

Your task is to rewrite your own map function which takes :

    an array
    a predicate function func which returns true (boolean) with even arguments

For example :

map([1,2,3,4],func)

produces

[ false, true, false, true ]  

The code also has to perform input validation, return :

    'given argument is not a function' if func is not a function
    'array should contain only numbers' if any elements are not numbers """


def func(n):
    return n % 2 == 0


# def map(arr, somefunction):
#     if not callable(somefunction):
#         return 'given argument is not a function'
#     try:
#         arr = [int(x) for x in arr if str(x).isdigit]
#     except:
#         return 'array should contain only numbers'

#     return [somefunction(x) for x in arr]

def map(arr, somefunction):
    try:
        return [somefunction(int(x)) for x in arr]
    except ValueError:
        return 'array should contain only numbers'
    except TypeError:
        return 'given argument is not a function'


q = map([1, 2, 3, '8'], func), [False, True, False, True]
q
q = map([77, 84, 18, 43, 16, 70, 53], func), [
    False, True, True, False, True, True, False]
q
q = map([1, 96, 37, 60, 7], 'test'), 'given argument is not a function'
q
q = map([72, 12, 30, 'q'], func), 'array should contain only numbers'
q
q = map([9, 53], func), [False, False]
q
