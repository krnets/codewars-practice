import codewars_test as test
from kata import calc

test.assert_equals(calc(""), 0, "Should work with empty string")
test.assert_equals(calc("3"), 3, "Should parse numbers")
test.assert_equals(calc("3.5"), 3.5, "Should parse float numbers")
test.assert_equals(calc("1 3 +"), 4, "Should support addition")
test.assert_equals(calc("1 3 *"), 3, "Should support multiplication")
test.assert_equals(calc("1 3 -"), -2, "Should support subtraction")
test.assert_equals(calc("4 2 /"), 2, "Should support division")
