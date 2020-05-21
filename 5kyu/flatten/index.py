# 5kyu - flatten()

""" For this exercise you will create a global flatten method. 
The method takes in any number of arguments and flattens them into a single array. 
If any of the arguments passed in are an array then the individual objects within 
the array will be flattened so that they exist at the same level as the other arguments. 
Any nested arrays, no matter how deep, should be flattened into the single array result.

The following are examples of how this function would be used and what the expected results would be:

flatten(1, [2, 3], 4, 5, [6, [7]]) # returns [1, 2, 3, 4, 5, 6, 7]
flatten('a', ['b', 2], 3, None, [[4], ['c']]) # returns ['a', 'b', 2, 3, None, 4, 'c'] """


# def deepflatten(iterable, depth=None, types=None, ignore=None):
#     if depth is None:
#         depth = float('inf')
#     if depth == -1:
#         yield iterable
#     else:
#         for x in iterable:
#             if ignore is not None and isinstance(x, ignore):
#                 yield x
#             if types is None:
#                 try:
#                     iter(x)
#                 except TypeError:
#                     yield x
#                 else:
#                     yield from deepflatten(x, depth - 1, types, ignore)
#             elif not isinstance(x, types):
#                 yield x
#             else:
#                 yield from deepflatten(x, depth - 1, types, ignore)

# def flatten(*args):
#     return list(deepflatten(args, types=list))

# def flatten(*lst):
#     result = []
#     for value in lst:
#         if not isinstance(value, list):
#             result.append(value)
#         else:
#             result.extend(flatten(*value))
#     return result

# def flatten(*lst):
#     result = []
#     for value in lst:
#         if isinstance(value, list):
#             result.extend(flatten(*value))
#         else:
#             result.append(value)
#     return result

# def flatten(*t):
#     def trav(t):
#         if isinstance(t, (list, tuple)):
#             for n in t:
#                 yield from trav(n)
#         else:
#             yield t
#     return list(trav(t))

def flatten(*args):
    return [x for a in args for x in (flatten(*a) if isinstance(a, list) else [a])]


q = flatten()  # []
q
q = flatten(1, 2, 3)  # [1,2,3]
q
q = flatten([1, 2], [3, 4, 5], [6, [7], [[8]]])  # [1,2,3,4,5,6,7,8]
q
q = flatten(1, 2, ['9', [], []], None)  # [1,2,'9',None]
q
q = flatten(['hello', 2, ['text', [4, 5]]], [[]], '[list]')
q
#      ['hello',2,'text',4,5,'[list]']
