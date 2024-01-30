import codewars_test as test
from kata import find_squares


# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(find_squares(9), "25-16")

    @test.it("Random Tests")
    def test_case():
        test.assert_equals(find_squares(5), "9-4")
        test.assert_equals(find_squares(7), "16-9")
