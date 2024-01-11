from kata import is_nice
import codewars_test as test


@test.describe("Testing...")
def _():
    @test.it("Basic tests")
    def _():
        test.assert_equals(is_nice([2, 10, 9, 3]), True)
        test.assert_equals(is_nice([3, 4, 5, 7]), False)
