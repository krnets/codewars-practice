import codewars_test as test
from kata import solve_postfix

test.assert_equals(solve_postfix("2 3 +"), 5)
test.assert_equals(solve_postfix("2 8 -"), -6)
test.assert_equals(solve_postfix("4 2 /"), 2)
test.assert_equals(solve_postfix("10 5 / 7 + 3 ^ 10 -"), 719)
