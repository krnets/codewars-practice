# 6kyu - Nested List Depth

""" A nested list (or array in JavaScript) is a list that apears as a value inside another list,

[item, item, [item, item], item]

in the above list, [item, item] is a nested list.

Your goal is to write a function that determines the depth of the deepest nested list within a given list.
return 1 if there are no nested lists. The list passed to your function can contain any data types.

A few examples:

list_depth([True])
return 1

list_depth([])
return 1

list_depth([2, "yes", [True, False]])
return 2

list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1])
return 6

list_depth([2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]])
return 2 """


# def list_depth(l, depth=1):
#     max_depth = depth
#     for e in l:
#         if isinstance(e, list):
#             max_depth = max(max_depth, list_depth(e, depth+1))
#     return max_depth

# def list_depth(l):
#     depths = [1]
#     for x in l:
#         if isinstance(x, list):
#             depths.append(list_depth(x)+1)
#     return max(depths)

# def list_depth(l):
#     result = [list_depth(x) for x in l if isinstance(x, list)]
#     return 1 + max(result) if result else 1

def list_depth(l):
    return max((1 + list_depth(x) for x in l if isinstance(x, list)), default=1)


q = list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1]), 6
q
q = list_depth([True]), 1
q
q = list_depth([]), 1
q
q = list_depth([2, "yes", [True, False]]), 2
q
q = list_depth([2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]]), 2
q
