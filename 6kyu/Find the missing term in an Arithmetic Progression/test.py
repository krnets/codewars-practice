import codewars_test as test
from kata import find_missing

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_missing([1, 2, 3, 4, 6, 7, 8, 9]), 5)
        test.assert_equals(find_missing([1, 3, 4, 5, 6, 7, 8, 9]), 2)