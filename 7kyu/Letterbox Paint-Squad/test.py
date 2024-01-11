import codewars_test as test
from kata import paint_letterboxes


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(paint_letterboxes(125, 132), [1, 9, 6, 3, 0, 1, 1, 1, 1, 1])
