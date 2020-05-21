# 7kyu - Flatten

""" Write a function that flattens an Array of Array objects into a flat Array. 
Your function must only do one level of flattening."""


# def flatten(lst):
#     return [x for y in lst for x in y] if any(x for x in lst if isinstance(x, list)) else lst

# def flatten(lst):
#     return [x for xs in lst for x in (xs if isinstance(xs, list) else [xs])]

def flatten(lst):
    res = []
    for x in lst:
        if isinstance(x, list):
            res.extend(x)
        else:
            res.append(x)
    return res

# from itertools import chain

# def flatten(lst):
#     try:
#         return list(chain.from_iterable(lst))
#     except:
#         return lst

# def flatten(lst):
#     try:
#         return list(chain(*lst))
#     except:
#         return lst



q = flatten([])  # []
q
q = flatten([1, 2, 3])  # [1,2,3]
q
q = flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3]])
q
#      [1,2,3,"a","b","c",1,2,3]
q = flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3], "a"])
q
#      [1,2,3,"a","b","c",1,2,3,"a"]
q = flatten([[3, 4, 5], [[9, 9, 9]], ["a,b,c"]])
q
#      [3,4,5,[9,9,9],"a,b,c"]
q = flatten([[[3], [4], [5]], [9], [9], [8], [[1, 2, 3]]])
q
#      [[3],[4],[5],9,9,8,[1,2,3]]
