import codewars_test as test
from kata import shift_left

test.assert_equals(shift_left("test", "west"), 2)
test.assert_equals(shift_left("test", "yes"), 7)
test.assert_equals(shift_left("b", "ab"), 1)
test.assert_equals(shift_left("abacabadabacaba", "abacabadacaba"), 18)
test.assert_equals(shift_left("aaabc", "bc"), 3)
test.assert_equals(shift_left("dark", "d"), 5)
test.assert_equals(shift_left("dadc", "dddc"), 4)
test.assert_equals(shift_left("nogkvcdldfpvlbkpedsecl", "nogkvcdldfpvlbkpedsecl"), 0)
