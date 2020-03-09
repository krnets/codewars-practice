# 7kyu - Array Array Array

""" You are given an initial 2-value array (x). You will use this to calculate a score.

If both values in (x) are numbers, the score is the sum of the two. 
If only one is a number, the score is that number. 
If neither is a number, return 'Void!'.

Once you have your score, you must return an array of arrays. 
Each sub array will be the same as (x) and the number of sub arrays should be equal to the score.

For example:

if (x) == ['a', 3] you should return [['a', 3], ['a', 3], ['a', 3]]. """


# def explode(arr):
#     if isinstance(arr[0], int) and isinstance(arr[1], int):
#         return sum(arr) * [arr]
#     elif isinstance(arr[0], int):
#         return arr[0] * [arr]
#     elif isinstance(arr[1], int):
#         return arr[1] * [arr]
#     else:
#         return 'Void!'

def explode(arr):
    return [arr] * sum(x for x in arr if isinstance(x, int)) or 'Void!'

# def explode(arr):
#     return [arr] * sum(x for x in arr if type(x) == int) or 'Void!'


# [[9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3]]
q = explode([9, 3])
q
q = explode(['a', 3])  # [['a', 3], ['a', 3], ['a', 3]] )
q
# [[6, 'c'], [6, 'c'], [6, 'c'], [6, 'c'], [6, 'c'], [6, 'c']])
q = explode([6, 'c'])
q
q = explode(['a', 'b'])  # 'Void!')
q
q = explode([1, 0])  # [[1,0]]
q
