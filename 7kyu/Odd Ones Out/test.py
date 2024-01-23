import codewars_test as test
from kata import odd_ones_out


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(odd_ones_out([1, 2, 3, 1, 3, 3]), [1, 1])
        test.assert_equals(odd_ones_out([75, 68, 75, 47, 68]), [75, 68, 75, 68])
        test.assert_equals(odd_ones_out([42, 72, 32, 4, 94, 82, 67, 67]), [67, 67])
        test.assert_equals(
            odd_ones_out([100, 100, 5, 5, 100, 50, 68, 50, 68, 50, 68, 5, 100]),
            [100, 100, 100, 100],
        )
        test.assert_equals(
            odd_ones_out([82, 86, 71, 58, 44, 79, 50, 44, 79, 67, 82, 82, 55, 50]),
            [44, 79, 50, 44, 79, 50],
        )
