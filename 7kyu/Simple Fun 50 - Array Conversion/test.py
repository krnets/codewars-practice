import codewars_test as test
from kata import array_conversion

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(array_conversion([1, 2, 3, 4, 5, 6, 7, 8]),186)
        test.assert_equals(array_conversion([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),64)
        test.assert_equals(array_conversion([3, 3, 5, 5]),60)