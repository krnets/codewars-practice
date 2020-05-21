# 7kyu - The dropWhile Function

""" Yet another staple for the functional programmer. 
You have a sequence of values and some predicate for those values. 
You want to remove the longest prefix of elements such that the predicate is true for each element. 
We'll call this the dropWhile function. It accepts two arguments. 
The first is the sequence of values, and the second is the predicate function. 
The function does not change the value of the original sequence.

def isEven(num):
  return num % 2 == 0

arr = [2,4,6,8,1,2,5,4,3,2]

dropWhile(arr, isEven) == [1,2,5,4,3,2] # True

Your task is to implement the dropWhile function. 
If you've got a span function lying around, this is a one-liner! 
Alternatively, if you have a takeWhile function on your hands, then combined with the dropWhile function, 
you can implement the span function in one line. This is the beauty of functional programming: 
there are a whole host of useful functions, many of which can be implemented in terms of each other. """

# from itertools import dropwhile

# def drop_while(arr, pred):
#     return list(dropwhile(pred, arr))


def drop_while(arr, pred):
    for i, x in enumerate(arr):
        if not pred(x):
            return arr[i:]
    return []


def is_even(n): return not n % 2


def is_odd(n): return n % 2


q = drop_while([2, 6, 4, 10, 1, 5, 4, 3], is_even), [1, 5, 4, 3]
q
q = drop_while([2, 100, 1000, 10000, 10000, 5, 3, 4, 6], is_even), [5, 3, 4, 6]
q
q = drop_while([998, 996, 12, -1000, 200, 0, 1, 1, 1], is_even), [1, 1, 1]
q
q = drop_while([1, 4, 2, 3, 5, 4, 5, 6, 7], is_even), [
    1, 4, 2, 3, 5, 4, 5, 6, 7]
q
q = drop_while([2, 4, 10, 100, 64, 78, 92], is_even), []
q
q = drop_while([1, 2, 3, 4, 5], is_odd), [2, 3, 4, 5]
q
q = drop_while([1, 5, 111, 1111, 1111, 2, 4, 6, 4, 5], is_odd), [2, 4, 6, 4, 5]
q
q = drop_while([-1, -5, 127, 86, 902, 2, 1], is_odd), [86, 902, 2, 1]
q
q = drop_while([2, 1, 2, 4, 3, 5, 4, 6, 7, 8, 9, 0], is_odd), [
    2, 1, 2, 4, 3, 5, 4, 6, 7, 8, 9, 0]
q
q = drop_while([1, 3, 5, 7, 9, 111], is_odd), []
q
