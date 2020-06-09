""" 7ky - Simple Fun #35: Different Squares

Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

For
matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]

the output should be 6.

Here are all 6 different 2 × 2 squares:

 1 2
 2 2

 2 1
 2 2

 2 2
 2 2

 2 2
 1 2

 2 2
 2 3

 2 3
 2 1

Input/Output

    [input] 2D integer array matrix

    Constraints:
    1 ≤ matrix.length ≤ 100,
    1 ≤ matrix[i].length ≤ 100,
    0 ≤ matrix[i][j] ≤ 9.

    [output] an integer
    The number of different 2 × 2 squares in matrix. """


def different_squares(matrix):
    result = set()
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            square = [[matrix[i][j],
                       matrix[i][j+1],
                       matrix[i+1][j],
                       matrix[i+1][j+1]]]
            result.add(''.join(map(str, square)))
    return len(result)

# from itertools import chain

# pairwise = lambda a: list(zip(a, a[1:]))
# transpose = lambda a: list(zip(*a))

# def different_squares(matrix):
#     if 1 in (len(matrix), len(matrix[0])):
#         return 0
#     all_squares = chain.from_iterable(map(pairwise, map(transpose, pairwise(matrix))))
#     unique_squares = set(all_squares)
#     return len(unique_squares)    


matrix = [
    [1, 2, 1],
    [2, 2, 2],
    [2, 2, 2],
    [1, 2, 3],
    [2, 2, 1]]
q = different_squares(matrix), 6
q

matrix = [
    [9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9]]
q = different_squares(matrix), 1
q

matrix = [[3]]
q = different_squares(matrix), 0
q

matrix = [[3, 4, 5, 6, 7, 8, 9]]
q = different_squares(matrix), 0
q

matrix = [
    [3],
    [4],
    [5],
    [6],
    [7]]
q = different_squares(matrix), 0
q

matrix = [
    [2, 5, 3, 4, 3, 1, 3, 2],
    [4, 5, 4, 1, 2, 4, 1, 3],
    [1, 1, 2, 1, 4, 1, 1, 5],
    [1, 3, 4, 2, 3, 4, 2, 4],
    [1, 5, 5, 2, 1, 3, 1, 1],
    [1, 2, 3, 3, 5, 1, 2, 4],
    [3, 1, 4, 4, 4, 1, 5, 5],
    [5, 1, 3, 3, 1, 5, 3, 5],
    [5, 4, 4, 3, 5, 4, 4, 4]]
q = different_squares(matrix), 54
q
