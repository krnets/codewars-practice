import codewars_test as test
from kata import matrix_addition

test.assert_equals(matrix_addition(
  [ [1, 2],
    [1, 2] ],
#     +
  [ [2, 3],
    [2, 3] ] ),
#     =gg
  [ [3, 5],
    [3, 5] ] )

test.assert_equals(matrix_addition(
  [ [1] ],
#    +
  [ [2] ] ),
#    =
  [ [3] ] )

test.assert_equals(matrix_addition(
  [ [1, 2, 3],
    [3, 2, 1],
    [1, 1, 1] ],
#       +
  [ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3] ] ),
#       =
  [ [3, 4, 4],
    [6, 4, 4],
    [2, 2, 4] ] )