import codewars_test as test
from kata import group

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(group([3, 2, 6, 2, 1, 3]), [[3, 3], [2, 2], [6], [1]])
        test.assert_equals(group([3, 2, 6, 2]), [[3], [2, 2], [6]])
        test.assert_equals(group([]), [])
        test.assert_equals(group([1, 100, 4, 2, 4]), [[1], [100], [4, 4], [2]])
        test.assert_equals(group([-1, 1, -1]), [[-1, -1], [1]])