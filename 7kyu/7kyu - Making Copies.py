# 7kyu - Making Copies

""" Note that you may have troubles if you do not return an actual copy, item by item, 
just a pointer or an alias for an existing list or array.

If not a list or array is given as a parameter in interpreted languages, the function should raise an error. """

# def copy_list(l):
#     return l[::]

def copy_list(l):
    return list(l)

t = [1, 2, 3, 4]
t_copy = copy_list(t)
t_copy

t[1] += 5
t = [1, 7, 3, 4]
t_copy = [1, 2, 3, 4]
t_copy
