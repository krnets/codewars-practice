import codewars_test as test
from kata import duty_free

test.describe("Basic tests")
test.assert_equals(duty_free(12, 50, 1000), 166)
test.assert_equals(duty_free(17, 10, 500), 294)
