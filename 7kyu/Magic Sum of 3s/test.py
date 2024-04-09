import codewars_test as test
from kata import magic_sum

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(magic_sum([3]), 3)
        test.assert_equals(magic_sum([3, 13]), 16)
        test.assert_equals(magic_sum([30, 34, 330]), 0)
        test.assert_equals(magic_sum([3, 12, 5, 8, 30, 13]), 16)
        test.assert_equals(magic_sum([]), 0, 'Calling the function with an empty array should return 0 as a sum.')