import codewars_test as test
from kata import to_integer

@test.describe("Basic Tests")
def _():
    @test.it("Tests")
    def _():
        test.assert_equals(to_integer("123"), 123)
        test.assert_equals(to_integer("0x123"), 0x123)
        test.assert_equals(to_integer("0o123"), 0o123)
        test.assert_equals(to_integer("0123"), 123)
        test.assert_equals(to_integer("123 "), None)
        test.assert_equals(to_integer(" 123"), None)
        test.assert_equals(to_integer("0b1010"), 0b1010)
        test.assert_equals(to_integer("+123"), 123)
        test.assert_equals(to_integer("-123"), -123)
        test.assert_equals(to_integer("0B1010"), None)
        test.assert_equals(to_integer("0b12"), None)
        test.assert_equals(to_integer("-0x123"), -0x123)
        test.assert_equals(to_integer("-0o123"), -0o123)
        test.assert_equals(to_integer("-0123"), -123)
        test.assert_equals(to_integer("123\n"), None)
        test.assert_equals(to_integer("\n123"), None)
        test.assert_equals(to_integer("-0b1010"), -0b1010)
        test.assert_equals(to_integer("0xDEADbeef"), 0xDEADBEEF)
        test.assert_equals(to_integer("0X123"), None)
        test.assert_equals(to_integer("0O123"), None)
        test.assert_equals(to_integer("0o18"), None)
        test.assert_equals(to_integer("0o10"), 8)