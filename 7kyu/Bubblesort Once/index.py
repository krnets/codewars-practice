""" 7kyu - Bubblesort Once

The Bubblesort Algorithm is one of many algorithms used to sort a list of similar items 
(e.g. all numbers or all letters) into either ascending order or descending order. Given a list (e.g.):

[9, 7, 5, 3, 1, 2, 4, 6, 8]

To sort this list in ascending order using Bubblesort, 
you first have to compare the first two terms of the list. 
If the first term is larger than the second term, you perform a swap. 
The list then becomes:

[7, 9, 5, 3, 1, 2, 4, 6, 8] 
# The "9" and "7" have been swapped because 9 is larger than 7 and thus 9 should be after 7

You then proceed by comparing the 2nd and 3rd terms, performing a swap when necessary, 
and then the 3rd and 4th term, then the 4th and 5th term, etc. etc. When you reach the end of the list, 
it is said that you have completed 1 complete pass.

Given an array of integers, your function bubblesort_once should return a new array equivalent 
to performing exactly 1 complete pass on the original array. Your function should be pure, 
i.e. it should not mutate the input array. """

# def bubblesort_once(l):
#     res = l[:]
#     for i in range(len(res)):
#         for j in range(i+1, len(res)):
#             if res[j-1] > res[j]:
#                 res[j], res[j-1] = res[j-1], res[j]
#         return res
#     return []


def bubblesort_once(l):
    res = l[:]
    for i in range(len(res)-1):
        if res[i] > res[i+1]:
            res[i], res[i+1] = res[i+1], res[i]
    return res


q = bubblesort_once([9, 7, 5, 3, 1, 2, 4, 6, 8]),
q
#       [7, 5, 3, 1, 2, 4, 6, 8, 9]
