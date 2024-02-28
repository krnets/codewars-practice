import codewars_test as test
from kata import histogram

test.assert_equals(histogram([1, 1, 0, 1, 3, 2, 6], 1), [1, 3, 1, 1, 0, 0, 1])
test.assert_equals(histogram([1, 1, 0, 1, 3, 2, 6], 2), [4, 2, 0, 1])
test.assert_equals(histogram([], 1), [])
test.assert_equals(histogram([8], 1), [0, 0, 0, 0, 0, 0, 0, 0, 1])