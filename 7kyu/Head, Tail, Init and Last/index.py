# 7kyu - Head, Tail, Init and Last

""" Haskell has some useful functions for dealing with lists:

λ head [1,2,3,4,5]  #  1
λ tail [1,2,3,4,5]  #  [2,3,4,5]
λ init [1,2,3,4,5]  #  [1,2,3,4]
λ last [1,2,3,4,5]  #  5

Your job is to implement these functions in your given language. 
Make sure it doesn't edit the array; that would cause problems! Here's a cheat sheet:

| HEAD | <----------- TAIL ------------> |
[  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
| <----------- INIT ------------> | LAST |

head [x] = x
tail [x] = []
init [x] = []
last [x] = x

Here's how I expect the functions to be called in your language:

head([1,2,3,4,5]) => 1
tail([1,2,3,4,5]) => [2,3,4,5]

Most tests consist of 100 randomly generated arrays, each with four tests, one for each operation. 
There are 400 tests overall. No empty arrays will be given. Haskell has QuickCheck tests """

# head = lambda array: array[0]
# tail = lambda array: array[1:]
# init = lambda array: array[1:-1]
# last = lambda array: array[-1]

def head(arr):
    return arr[0]

def tail(arr):
    return arr[1:]

def init(arr):
    return arr[:-1]

def last(arr):
    return arr[-1]

q = head([5, 1])  # 5
q
q = tail([1])  # []
q
q = init([1, 5, 7, 9])  # [1,5,7]
q
q = last([7, 2])  # 2
q
