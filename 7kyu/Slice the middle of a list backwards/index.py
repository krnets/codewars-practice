""" 7kyu - Slice the middle of a list backwards

Write a function that takes a list of at least four elements as an argument 
and returns a list of the middle two or three elements in reverse order. """


# def reverse_middle(lst):
#     mid = len(lst) // 2
#     return lst[mid-1:mid+(2 if len(lst) % 2 else 1)][::-1]

def reverse_middle(lst):
    mid = len(lst) // 2 - 1
    return lst[mid:-mid][::-1]


# Odd list of integers
q = reverse_middle([1, 2, 3, 4, 5]), [4, 3, 2]
q

# Even list of diverse types
q = reverse_middle(['a', [1, 'a'], 'd', True]), ['d', [1, 'a']]
q
