# 7kyu - Difference between two collections

""" Find the difference between two collections. 
The difference means that either the character is present in one collection or it is present in other, but not in both. 
Return a sorted set with difference.

The collections can contain any character and can contain duplicates.

For instance:

A = [a,a,t,e,f,i,j]
B = [t,g,g,i,k,f]
difference = [a,e,g,j,k] """

# def diff(a, b):
#     return sorted(x for x in set(a + b) if x in a and x not in b or x in b and x not in a)

# def diff(a, b):
#     return sorted(x for x in set(a + b) if (x in a and x not in b) or (x in b and x not in a))

def diff(a, b):
    return sorted(set(a) ^ set(b))

# def diff(a, b):
#     return sorted(set(a).symmetric_difference(set(b)))


# Test.it("should return empty for the same content")
q = diff(['a', 'b'], ['a', 'b'])  # []
q

# Test.it("should return A if B is empty")
a = ['a', 'b']
b = []
q = diff(a, b)  # a
q

# Test.it("should return B if A is empty")
a = []
b = ['a', 'b']
q = diff(a, b)  # b
q

# Test.it("should return empty for the empty content")
q = diff([], [])  # []
q

# Test.it("should return the last character")
a = ['a', 'b', 'z']
b = ['a', 'b']
q = diff(a, b)  # ['z']
q

# Test.it("should return the sorted characteres")
a = ['a', 'b', 'z', 'd', 'e', 'd']
b = ['a', 'b', 'j', 'j']
q = diff(a, b)  # ['d','e','j','z']
q
