# 5kyu - Moving Zeros To The End

""" Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"])
#   returns[false,1,1,2,1,3,"a",0,0] """

# def move_zeros(array):
#     orig = array[:]
#     xs_moved = 0
#     for i, x in enumerate(orig):
#         if x == 0 and not (x is False):
#             val = array.pop(i - xs_moved)
#             array.append(val)
#             xs_moved += 1
#     return array

# def move_zeros(array):
#     return sorted(array, key=lambda x: x == 0 and type(x) != bool)

def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)

# def move_zeros(array):
#     return [x for x in array if x != 0 or x is False] + [x for x in array if x == 0 and not(x is False)]

q = move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
q
#      [ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ]
q = move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
q
#      [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
q = move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
q
#      ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
q = move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, { }, 0, 0, 9])
q
#      ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]
q = move_zeros([0, 1, None, 2, False, 1, 0])
q
#      [1,None,2,False,1,0,0]
q = move_zeros(["a", "b"])  # ["a","b"]
q
q = move_zeros(["a"])  # ["a"]
q
q = move_zeros([0, 0])  # [0,0]
q
q = move_zeros([0])  # [0]
q
q = move_zeros([False])  # [False]
q
q = move_zeros([])  # []
q
