import codewars_test as test
from kata import sum_triangular_numbers

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sum_triangular_numbers(-291), 0)
        test.assert_equals(sum_triangular_numbers(-971), 0)
        test.assert_equals(sum_triangular_numbers(4), 20)
        test.assert_equals(sum_triangular_numbers(6), 56)
        test.assert_equals(sum_triangular_numbers(34), 7140)
        test.assert_equals(sum_triangular_numbers(943), 140205240)
