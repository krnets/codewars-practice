import codewars_test as test
from kata import find_missing_number

test.assert_equals(find_missing_number([2, 3, 4]), 1)
test.assert_equals(find_missing_number([1, 3, 4]), 2)
test.assert_equals(find_missing_number([1, 2, 4]), 3)
test.assert_equals(find_missing_number([1, 2, 3]), 4)
