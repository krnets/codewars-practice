import codewars_test as test
from kata import age

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_approx_equals(age(6, 3), 9, margin=1e-4)
        test.assert_approx_equals(age(-15, 0.25), 5, margin=1e-4)