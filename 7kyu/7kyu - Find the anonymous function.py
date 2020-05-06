# 7kyu - Find the anonymous function

""" Your input. First Parameter will be an array with an anonymous function somewhere in the lot, 

The second Parameter will be an array which you will filter using the anonymous function you find.

Your output. Output a filtered version of the second parameter using the function found in the first parameter.  """


# def find_function(func, arr):
#     return list(filter(list(filter(callable, func))[0], arr))

# def find_function(func, arr):
#     fn = [x for x in func if not isinstance(x, (int, str))][0]
#     return list(filter(fn, arr))

# def find_function(func, arr):
#     pred = next(x for x in func if callable(x))
#     return [x for x in arr if pred(x)]

def find_function(func, arr):
    for x in func:
        if hasattr(x, '__call__'):
            return list(filter(x, arr))


q = find_function([lambda a: a % 2 == 0, 9, 3, 1, 0], [1, 2, 3, 4]), [2, 4]
q
q = find_function([9, 3, lambda a: a % 2, 1, 0], [1, 2, 3, 4]), [1, 3]
q
q = find_function([9, 3, lambda a: a % 13 == 0, 1, 0], [1, 2, 3, 4]), []
q
q = find_function([9, 3, lambda a: a % 13 != 0, 1, 0],
                  [1, 2, 3, 4]), [1, 2, 3, 4]
q
q = find_function([5, 'a', lambda a: a*4 != 0, 1, 0],
                  [0, 1, 2, 3, 4]), [1, 2, 3, 4]
q
