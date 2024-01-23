import codewars_test as test
from kata import solve


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(solve([0, 1, 2, 3]), 0)
        test.assert_equals(solve([0, 1, 2, 3, "a", "b"]), 0)
        test.assert_equals(
            solve([0, 15, "z", 16, "m", 13, 14, "c", 9, 10, 13, "u", 4, 3]), 0
        )
        test.assert_equals(solve([13, 6, 8, 15, 4, 8, 13]), 1)
        test.assert_equals(solve([1, "a", 17, 8, "e", 3, "i", 12, 1]), -2)
