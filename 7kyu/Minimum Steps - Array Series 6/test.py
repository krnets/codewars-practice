import codewars_test as test
from kata import minimum_steps


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(minimum_steps([4, 6, 3], 7), 1)
        test.assert_equals(minimum_steps([10, 9, 9, 8], 17), 1)
        test.assert_equals(minimum_steps([8, 9, 10, 4, 2], 23), 3)
        test.assert_equals(minimum_steps([19, 98, 69, 28, 75, 45, 17, 98, 67], 464), 8)
        test.assert_equals(minimum_steps([4, 6, 3], 2), 0)
