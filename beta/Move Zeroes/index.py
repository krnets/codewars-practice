# Beta - Move Zeroes

""" Given the numerical series as argument. 
Write a function to move all zeros to the end non-zero elements will be sorted into their natural order (from smaller to bigger).

For instance: 
Given numbers (0, 3, 0, 1, 9, 6). 
Your function should return an array of numbers: [1, 3, 6, 9, 0, 0].

Note: You must do this in-place without making a copy of the array. 
Don't use .sort & .sort! methods. Main idea of this kata is realisation algo without a built-in methods. """


# def move_zeroes(*args):
#     arr = sorted(args)
#     index = 0
#     for i, x in enumerate(arr):
#         if x:
#             arr[index] = x
#             index += 1
#     for i in range(index, len(arr)):
#         arr[i] = 0
#     return arr

from heapq import heappush, heappop

def move_zeroes(*args):
    zeroes = []
    non_zeroes = []
    for x in args:
        if x == 0:
            zeroes.append(x)
        else:
            heappush(non_zeroes, x)
    return [heappop(non_zeroes) for i in range(len(non_zeroes))] + zeroes

q = move_zeroes(0, 3, 0, 1, 9, 6), [1, 3, 6, 9, 0, 0]
q
q = move_zeroes(6, 0, 9, 15), [6, 9, 15, 0]
q
q = move_zeroes(34, 12, 2, 0, 4, 8, 78), [2, 4, 8, 12, 34, 78, 0]
q
q = move_zeroes(0, 0, 4, 12, 17, 99, 34, 101, 0, 1, 1), [1, 1, 4, 12, 17, 34, 99, 101, 0, 0, 0]
q
q = move_zeroes(0, 0, 1), [1, 0, 0]
q
q = move_zeroes(0, 0, 1, 1), [1, 1, 0, 0]
q
q = move_zeroes(0, 1, 0, 1), [1, 1, 0, 0]
q
q = move_zeroes(0, 0, 0, 1), [1, 0, 0, 0]
q
q = move_zeroes(0, 0, 0, 0), [0, 0, 0, 0]
q
q = move_zeroes(), []
q
