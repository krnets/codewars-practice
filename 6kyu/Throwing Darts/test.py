import codewars_test as test
from kata import score_throws


@test.describe("Basic Tests")
def _():
    @test.it("Tests")
    def _():
        test.assert_equals(score_throws([1, 5, 11]), 15)
        test.assert_equals(score_throws([15, 20, 30, 31, 32, 44, 100]), 0)
        test.assert_equals(score_throws([1, 2, 3, 4]), 140)
        test.assert_equals(score_throws([]), 0, "Empty list")
        test.assert_equals(score_throws([1, 2, 3, 4, 5, 6, 7, 8, 9]), 65)
        test.assert_equals(score_throws([0, 5, 10, 10.5, 4.5]), 30)
        test.assert_equals(score_throws([1]), 110)
        test.assert_equals(score_throws([21, 10, 10]), 10)
        test.assert_equals(score_throws([5, 5, 5, 5]), 20)
        test.assert_equals(score_throws([4.9, 5.1]), 15)
