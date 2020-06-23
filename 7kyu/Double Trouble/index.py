""" 7kyu - Double Trouble

Given an array of integers (x), and a target (t), find out if any two consecutive numbers in the array sum to t. 
If so, remove the second number.

x = [1, 2, 3, 4, 5]
t = 3

1+2 = t, so remove 2. 
No other pairs = t, so rest of array remains:

[1, 3, 4, 5]

Work through the array from left to right.
Return the resulting array. """


# def trouble(x, t):
#     for i in range(len(x)-1):
#         if x[i] + x[i+1] == t:
#             return trouble(x[:i+1] + x[i+2:], t)
#     return x

def trouble(x, t):
    res = [x[0]]
    for el in x[1:]:
        if t - el != res[-1]:
            res.append(el)
    return res


q = trouble([1, 3, 5, 6, 7, 4, 3], 7), [1, 3, 5, 6, 7, 4]
q
q = trouble([4, 1, 1, 1, 4], 2), [4, 1, 4]
q
q = trouble([2, 6, 2], 8), [2, 2]
q
q = trouble([2, 2, 2, 2, 2, 2], 4), [2]
q
