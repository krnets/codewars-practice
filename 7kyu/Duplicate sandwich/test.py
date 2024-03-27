import codewars_test as test
from kata import duplicate_sandwich

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]), [2, 3, 4, 5, 6])
        test.assert_equals(duplicate_sandwich(['None', 'Hello', 'Example', 'hello', 'None', 'Extra']), ['Hello', 'Example', 'hello'])
        test.assert_equals(duplicate_sandwich([0, 0]), [])
        test.assert_equals(duplicate_sandwich([True, False, True]), [False])
        test.assert_equals(duplicate_sandwich(['e', 'x', 'a', 'm', 'p', 'l', 'e']), ['x', 'a', 'm', 'p', 'l'])