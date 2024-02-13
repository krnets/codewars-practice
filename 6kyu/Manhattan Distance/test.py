import codewars_test as test
from kata import manhattan_distance


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(manhattan_distance([1, 1], [1, 1]), 0)
        test.assert_equals(manhattan_distance([5, 4], [3, 2]), 4)
        test.assert_equals(manhattan_distance([1, 1], [0, 3]), 3)
