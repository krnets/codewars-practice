# 7kyu - Pair Zeros

""" For a given array whose element values are randomly picked from single-digit integers 0 to 9, 
return an array with the same digit order but all 0's paired. 
Paring two 0's generates one 0 at the location of the first.

pair_zeros([0, 1, 0, 2])
# paired: ^-----^ cull second zero
       == [0, 1, 2];
#   kept: ^

pair_zeros([0, 1, 0, 0])
# paired: ^-----^
       == [0, 1,    0];
#   kept: ^

pair_zeros([1, 0, 7, 0, 1])
# paired:    ^-----^
       == [1, 0, 7,    1];
#   kept:    ^

pair_zeros([0, 1, 7, 0, 2, 2, 0, 0, 1, 0])
# paired: ^--------^ 
#        [0, 1, 7,    2, 2, 0, 0, 1, 0]
#   kept: ^         paired: ^--^
       == [0, 1, 7,    2, 2, 0,    1, 0];
#   kept:                   ^

Here are the 2 important rules:

    Pairing happens from left to right in the array. 
    However, for each pairing, the "second" 0 will always be paired towards the first (right to left)
    0's generated by pairing can NOT be paired again """


# def pair_zeros(arr):
#     res = []
#     flag = False
#     for x in arr:
#         if x == 0:
#             if flag is False:
#                 res.append(x)
#             flag = not flag
#         else:
#             res.append(x)
#     return res

from itertools import cycle

def pair_zeros(arr):
    toggle = cycle([True, False])
    return [x for x in arr if x or next(toggle)]


# _empty array
q = pair_zeros([]), []
q
# Without zeros [1] -> [1]
q = pair_zeros([1]), [1]
q
# Without zeros [1,2,3] -> [1,2,3]
q = pair_zeros([1, 2, 3]), [1, 2, 3]
q
# [0] -> [0]
q = pair_zeros([0]), [0]
q
# [0,0] -> [0]
q = pair_zeros([0, 0]), [0]
q
# [1,0,1,0,2,0,0] -> [1,0,1,2,0]
q = pair_zeros([1, 0, 1, 0, 2, 0, 0]), [1, 0, 1, 2, 0]
q
# [0,0,0] -> [0,0]
q = pair_zeros([0, 0, 0]), [0, 0]
q
# [1,0,1,0,2,0,0,3,0] -> [1,0,1,2,0,3,0]
q = pair_zeros([1, 0, 1, 0, 2, 0, 0, 3, 0]), [1, 0, 1, 2, 0, 3, 0]
q
# handles large arrays
q = pair_zeros([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0]
q
q = pair_zeros([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0, 0]
q