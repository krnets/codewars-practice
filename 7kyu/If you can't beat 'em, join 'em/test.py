import codewars_test as test
from kata import cant_beat_so_join

# Normal tests
test.assert_equals(cant_beat_so_join([[1,2], [3,4], [5,6], [7,8], [9]]), [7, 8, 5, 6, 9, 3, 4, 1, 2])
test.assert_equals(cant_beat_so_join([[5, 1],[9, 14],[17, 23],[4, 1],[0, 1]]), [17, 23, 9, 14, 5, 1, 4, 1, 0, 1])
test.assert_equals(cant_beat_so_join([[13, 37], [43, 17], [2,3], [45,64], [1,9]]), [45, 64, 43, 17, 13, 37, 1, 9, 2, 3])
test.assert_equals(cant_beat_so_join([[52,11,33,222], [582,192,442,512,41], [23912], [2314], [2491,2412,84828]]), [2491, 2412, 84828, 23912, 2314, 582, 192, 442, 512, 41, 52, 11, 33, 222])
test.assert_equals(cant_beat_so_join([[1,0,1,0,1,0], [0,1,0,0,1,0,0,1], [0], []]), [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0])

# Test empty lists
test.assert_equals(cant_beat_so_join([[], [], [], []]), [])
test.assert_equals(cant_beat_so_join([[], [], [0], []]), [0])

# Test ordering of lists with same value
test.assert_equals(cant_beat_so_join([[0,1,1,1], [1,0,1,1], [1,1,0,1], [3]]), [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 3])