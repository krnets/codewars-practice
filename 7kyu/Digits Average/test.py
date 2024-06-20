import codewars_test as test
from kata import digits_average

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(digits_average(246), 4)
        test.assert_equals(digits_average(89), 9)
        test.assert_equals(digits_average(2), 2)
        test.assert_equals(digits_average(245), 4)
        test.assert_equals(digits_average(345), 5)
        test.assert_equals(digits_average(346), 5)
        test.assert_equals(digits_average(3700), 4)