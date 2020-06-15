""" 7kyu - Simple Fun #88: Sort By Height

Some people are standing in a row in a park. There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a non-descending order without moving the trees.

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
        [-1, 150, 160, 170, -1, -1, 180, 190].

    [input] integer array a
    If a[i] = -1, then the ith position is occupied by a tree. 
    Otherwise a[i] is the height of a person standing in the ith position.

    Constraints:
    5 ≤ a.length ≤ 30,
    -1 ≤ a[i] ≤ 200.

    [output] an integer array
    Sorted array a with all the trees untouched. """


# def sort_by_height():
#     arr = filter(lambda x: x is not -1, sorted(a))
#     res = []
#     for i in range(len(a)):
#         if a[i] == -1:
#             res.append(-1)
#         else:
#             res.append(next(arr))
#     return res

def sort_by_height(a):
    ascending = filter(lambda x: x is not -1, sorted(a))
    return [next(ascending) if a[i] != -1 else -1 for i in range(len(a))]


q = sort_by_height([-1, 150, 190, 170, -1, -1, 160, 180])
q
#      [-1, 150, 160, 170, -1, -1, 180, 190]
q = sort_by_height([-1, -1, -1, -1, -1]), [-1, -1, -1, -1, -1]
q
q = sort_by_height([4, 2, 9, 11, 2, 16])
q
#      [2, 2, 4, 9, 11, 16]
