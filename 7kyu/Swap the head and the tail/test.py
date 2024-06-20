import codewars_test as test
from kata import swap_head_tail


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(swap_head_tail([1, 2, 3, 4, 5]), [4, 5, 3, 1, 2])
        test.assert_equals(swap_head_tail([-1, 2]), [2, -1])
        test.assert_equals(
            swap_head_tail([1, 2, -3, 4, 5, 6, -7, 8]), [5, 6, -7, 8, 1, 2, -3, 4]
        )