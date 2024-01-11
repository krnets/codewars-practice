import codewars_test as test
from kata import two_are_positive


@test.describe("Two numbers are positive")
def tests():
    @test.it("Sample Tests")
    def sample_tests():
        test.assert_equals(two_are_positive(2, 4, -3), True, "(2, 4, -3)")
        test.assert_equals(two_are_positive(-4, 6, 8), True, "(-4, 6, 8)")
        test.assert_equals(two_are_positive(4, -6, 9), True, "(4, -6, 9)")
        test.assert_equals(two_are_positive(4, 6, 0), True, "(4, 6, 0)")
        test.assert_equals(two_are_positive(-4, 6, 0), False, "(-4, 6, 0)")
        test.assert_equals(two_are_positive(4, 6, 10), False, "(4, 6, 10)")
        test.assert_equals(two_are_positive(-14, -3, -4), False, "(-14, -3, -4)")
