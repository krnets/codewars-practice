"""Unpack a list of elements that contains unpackable objects.

    # >>> unpack([None, [1, ({2, 3}, {'foo': 'bar'})]])
    [None, 1, 2, 3, 'foo', 'bar']
"""

def unpack(l):
    res = []

    def inner(elems):
        if isinstance(elems, (list, tuple, set)):
            for x in elems:
                inner(x)
        elif isinstance(elems, dict):
            for k, v in elems.items():
                inner(k)
                inner(v)
        else:
            res.append(elems)

    inner(l)
    return res


# def unpack(l):
#     res = []
#     for elems in l:
#         if isinstance(elems, (list, tuple, set)):
#             elems = unpack(elems)
#         elif isinstance(elems, dict):
#             elems = unpack(elems.items())
#         else:
#             elems = [elems]
#         res.extend(elems)
#     return res
