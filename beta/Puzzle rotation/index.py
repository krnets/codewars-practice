# Beta - Puzzle rotation

""" A robot PZL-3000 built to gather a squere puzzles.
But it is still a prototype and it has a bug - horizon determination is broken.
PZL-3000 gathers all the puzzles with vertical horizon which means that a puzzle matrix
is 90 degree counterclock-wise rotated.

A presentation of the robot is going to start in a couple of hours so you can't eliminate the bug
and must implement just a quick fix:

Rotate the puzzle ids matrix 90 degree clockwise. After rotation the matrix must be the same object
otherwise the robot will turn it backward.

Definition of identity:

The objects must be kept in place including inner lists of the matrix.

A matrix like that:

0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8

After the fix appliance must look that way:

0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 """


def rotate(matrix):
    size = range(len(matrix))
    for i in size:
        for j in size:
            if j > i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


m = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 4, 5, 6, 7, 8], ]

q = rotate(m)
q
# [[0 0 0 0 0 0 0 0 0], [1 1 1 1 1 1 1 1 1], [2 2 2 2 2 2 2 2 2], [3 3 3 3 3 3 3 3 3], [4 4 4 4 4 4 4 4 4],  [5 5 5 5 5 ..]]