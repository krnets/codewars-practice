import codewars_test as test
from kata import i_or_f

test.assert_equals(i_or_f('1'), True)
test.assert_equals(i_or_f('1.0'), True)
test.assert_equals(i_or_f('1e1'), True)
test.assert_equals(i_or_f('1E-1'), True)
test.assert_equals(i_or_f('1e+1'), True)