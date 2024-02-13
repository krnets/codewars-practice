import codewars_test as test
from kata import num_primorial

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(num_primorial(3),30)
        test.assert_equals(num_primorial(4),210)
        test.assert_equals(num_primorial(5),2310)
        test.assert_equals(num_primorial(8),9699690)
        test.assert_equals(num_primorial(9),223092870)