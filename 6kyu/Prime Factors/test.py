import codewars_test as test
from kata import prime_factors

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(prime_factors(1), [])
        test.assert_equals(prime_factors(4), [2, 2])
        test.assert_equals(prime_factors(3), [3])
        test.assert_equals(prime_factors(6), [2, 3])
        test.assert_equals(prime_factors(9), [3, 3])
        test.assert_equals(prime_factors(12), [2, 2, 3])
        test.assert_equals(prime_factors(11020332), [2, 2, 3, 918361])