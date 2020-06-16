""" 7kyu - Zip it!

Write lstzip that merges the corresponding elements of two sequences using a specified selector function fn

For example:

a = [1, 2, 3, 4, 5]
b = ['a', 'b']
lstzip(a,b, lambda a,b: str(a)+str(b))

a = [1, 2, 3, 4, 5]
b = ['a','b','c','d','e']
lstzip(a,b, lambda a, b: a * ord(b[0]))

if arrays have different lengths, go up to the minimum length and then stop. """


# def lstzip(a, b, fn):
#     if len(a) > len(b):
#         a = a[:len(b)]
#     return [fn(a[i], b[i]) for i in range(len(a))]

def lstzip(a, b, fn):
    return list(map(fn, *(a, b)))


a = [1, 2, 3, 4, 5, 6, 7]
b = ['a', 'b', 'c', 'd', 'e']
q = lstzip(a, b, lambda a, b: str(a) + str(b))
q
#      ["1a", "2b", "3c", "4d", "5e"]
q = lstzip(b, a, lambda a, b: str(a) + str(b))
q
#      ["a1", "b2", "c3", "d4", "e5"]
q = lstzip(b, lstzip(a, b, lambda a, b: a * ord(b[0])),
           lambda a, b: str(a) + str(b))
q
#      ["a97", "b196", "c297", "d400", "e505"]
