import codewars_test as test
from kata import minimum_sum, maximum_sum

values = [5, 4, 3, 2, 1]
test.assert_equals(minimum_sum(values, 2), 3)
test.assert_equals(maximum_sum(values, 3), 12)