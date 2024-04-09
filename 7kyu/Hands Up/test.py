import codewars_test as test
from kata import get_positions

test.assert_equals(get_positions(54), (0, 0, 0))
test.assert_equals(get_positions(98), (2, 2, 1))
test.assert_equals(get_positions(3), (0, 1, 0))