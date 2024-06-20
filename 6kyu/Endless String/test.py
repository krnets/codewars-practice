import codewars_test as test
from kata import endless_string

test.assert_equals(endless_string("xyz", 0, 4), "xyzx")
test.assert_equals(endless_string("xyz", 19, 2), "yz")
test.assert_equals(endless_string("xyz", -4, -4), "zxyz")
test.assert_equals(endless_string("xyz", -23, 6), "yzxyzx")
