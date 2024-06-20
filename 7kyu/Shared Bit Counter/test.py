import codewars_test as test
from kata import shared_bits

test.assert_equals(shared_bits(1, 2), False)
test.assert_equals(shared_bits(16, 8), False)
test.assert_equals(shared_bits(1, 1), False)
test.assert_equals(shared_bits(2, 3), False)
test.assert_equals(shared_bits(7, 10), False)
test.assert_equals(shared_bits(43, 77), True)
test.assert_equals(shared_bits(7, 15), True)
test.assert_equals(shared_bits(23, 7), True)