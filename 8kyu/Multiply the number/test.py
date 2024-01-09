from kata import multiply
import codewars_test as test

test.describe("Basic Tests")
test.assert_equals(multiply(10), 250)
test.assert_equals(multiply(5), 25)
test.assert_equals(multiply(200), 25000)
test.assert_equals(multiply(0), 0)
test.assert_equals(multiply(-2), -10)
