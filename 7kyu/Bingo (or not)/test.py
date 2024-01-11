import codewars_test as test

from kata import bingo


@test.describe("Example Tests")
def example_tests():
    @test.it("")
    def _():
        test.assert_equals(bingo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "LOSE")
        test.assert_equals(bingo([20, 12, 23, 14, 6, 22, 12, 17, 2, 26]), "LOSE")
        test.assert_equals(bingo([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]), "WIN")
        test.assert_equals(bingo([5, 2, 13, 7, 5, 14, 17, 15, 9, 10]), "WIN")
