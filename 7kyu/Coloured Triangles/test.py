import codewars_test as test
from kata2 import triangle


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(triangle("B"), "B")
        test.assert_equals(triangle("R"), "R")
        test.assert_equals(triangle("G"), "G")
        test.assert_equals(triangle("RB"), "G")
        test.assert_equals(triangle("BGR"), "G")
        test.assert_equals(triangle("BBRR"), "G")
        test.assert_equals(triangle("GB"), "R")
        test.assert_equals(triangle("RRR"), "R")
        test.assert_equals(triangle("RGBG"), "B")
        test.assert_equals(triangle("RBRGBRB"), "G")
        test.assert_equals(triangle("RBRGBRBGGRRRBGBBBGG"), "G")
