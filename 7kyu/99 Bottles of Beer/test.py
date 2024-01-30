import codewars_test as test
from kata import sing


@test.describe("Example Tests")
def example_tests():
    @test.it("It should work for sing test")
    def _():
        test.assert_equals(
            sing()[0], "99 bottles of beer on the wall, 99 bottles of beer."
        )
        test.assert_equals(
            sing()[199],
            "Go to the store and buy some more, 99 bottles of beer on the wall.",
        )
