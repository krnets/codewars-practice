# Beta - Flattening Lists

""" Create a function that takes a list of lists as an input and returns a flattened list.

Note that if there are more lists inside these lists, they should not be flattened. """

# def flatten(l):
#     return [x for xs in l for x in (xs if isinstance(xs, list) else [xs])]

def flatten(l):
    return [x for xs in l for x in xs]

q = flatten([[1,2],[3,4]]) # [1,2,3,4]
q
q = flatten([[1],[2],[3],[4]]) # [1,2,3,4]
q
