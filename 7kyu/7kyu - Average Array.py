# ASC Week 1 Challenge 5 (Medium #2)

""" Create a function that takes a 2D array as an input, and outputs another array that contains the average values for the numbers in the nested arrays at the corresponding indexes.

Note: the function should also work with negative numbers and floats.
Examples

[ [1, 2, 3, 4], [5, 6, 7, 8] ]  ==>  [3, 4, 5, 6]

1st array: [1, 2, 3, 4]
2nd array: [5, 6, 7, 8]
            |  |  |  |
            v  v  v  v
average:   [3, 4, 5, 6]

And another one:

[ [2, 3, 9, 10, 7], [12, 6, 89, 45, 3], [9, 12, 56, 10, 34], [67, 23, 1, 88, 34] ]  ==>  [22.5, 11, 38.75, 38.25, 19.5]

1st array: [  2,   3,    9,   10,    7]
2nd array: [ 12,   6,   89,   45,    3]
3rd array: [  9,  12,   56,   10,   34]
4th array: [ 67,  23,    1,   88,   34]
              |    |     |     |     |
              v    v     v     v     v
average:   [22.5, 11, 38.75, 38.25, 19.5] """


# def avg_array(arrs):
#     res = []
#     for i in range(len(arrs[0])):
#         index_vals = []
#         for x in arrs:
#             index_vals.append(x[i])
#         res.append(sum(index_vals) / len(index_vals))
#     return [int(x) if round(x) == x else x for x in res]

def avg_array(arrs):
    return [sum(vals) / len(vals) for vals in zip(*arrs)]

# from statistics import mean

# def avg_array(arrs):
#     return [mean(vals) for vals in zip(*arrs)]


q = avg_array([[1, 2, 3, 4], [5, 6, 7, 8]]), [3, 4, 5, 6]
q
q = avg_array([[2, 3, 9, 10, 7], [12, 6, 89, 45, 3], [9, 12, 56, 10, 34], [67, 23, 1, 88, 34]])
q
#      [22.5, 11, 38.75, 38.25, 19.5]
q = avg_array([[2, 5, 4, 3, 19], [2, 5, 6, 7, 10]]), [2, 5, 5, 5, 14.5]
q
q = avg_array([[1.2, 8.521, 0.4, 3.14, 1.9], [2, 4.5, 3.75, 0.987, 1.0]])
q
#      [1.6, 6.5105, 2.075, 2.0635, 1.45]
