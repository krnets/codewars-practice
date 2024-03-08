import codewars_test as test
from kata import nth_perm

test.assert_equals(nth_perm(1, 1), '0')
test.assert_equals(nth_perm(2, 2), '10')
test.assert_equals(nth_perm(12, 5), '02431')
test.assert_equals(nth_perm(1000, 7), '1325460')
test.assert_equals(nth_perm(1000, 8), '02436571')