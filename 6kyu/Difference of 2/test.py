import codewars_test as test
from kata import twos_difference

test.assert_equals(twos_difference([1, 2, 3, 4]), [(1, 3), (2, 4)])
test.assert_equals(twos_difference([1, 3, 4, 6]), [(1, 3), (4, 6)])
test.assert_equals(twos_difference([0, 3, 1, 4]), [(1, 3)])
test.assert_equals(twos_difference([4, 1, 2, 3]), [(1, 3), (2, 4)])
test.assert_equals(twos_difference([6, 3, 4, 1, 5]), [(1, 3), (3, 5), (4, 6)])
test.assert_equals(twos_difference([3, 1, 6, 4]), [(1, 3), (4, 6)])
test.assert_equals(twos_difference([1, 3, 5, 6, 8, 10, 15, 32, 12, 14, 56]), [(1, 3), (3, 5), (6, 8), (8, 10), (10, 12), (12, 14)])
test.assert_equals(twos_difference([1, 4, 7, 10]), [])
test.assert_equals(twos_difference([]), [])
