# 7kyu - Sub-array elements sum

""" Given an list of lists of integers, return the sum of a specific set of numbers, 
starting with elements whose position is equal to the main array length and going down by one at each step.

Say for example the parent array (etc, etc) has 3 sub-arrays inside: 
you should consider the third element of the first sub-array, 
the second of the second array and the first element in the third one: 

[[3, 2, 1, 0], [4, 6, 5, 3, 2], [9, 8, 7, 4]] 
    would have you considering
        1 for [3, 2, 1, 0], 
        6 for [4, 6, 5, 3, 2] and 
        9 for [9, 8, 7, 4], which sums up to 16.

One small note is that not always each sub-array will have enough elements, 
in which case you should then use a default value (if provided) or 0 (if not provided), as shown in the test cases. """


def elements_sum(arr, d=0):
    return sum(lst[i] if i < len(lst) else d for i, lst in enumerate(reversed(arr)))

# def elements_sum(arr, d=0):
#     return sum(a[i] if i < len(a) else d for i, a in enumerate(arr[::-1]))

# def elements_sum(arr, d=0):
#     return sum(a[len(arr)-1-i] if len(arr)-1-i < len(a) else d for i, a in enumerate(arr))


q = elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], [9, 8, 7, 4]])  # 16
q
q = elements_sum([[3], [4, 6, 5, 3, 2], [9, 8, 7, 4]])  # 15
q
q = elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], []])  # 7
q
q = elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], []], 5)  # 12
q
q = elements_sum([[3, 2], [4], []])  # 0
q
