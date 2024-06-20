from kata import find_children
import codewars_test as test


@test.describe("tests")
def tests():
    @test.it("sample tests")
    def sample_tests():
        test.assert_equals(find_children("abBA"), "AaBb")
        test.assert_equals(find_children("AaaaaZazzz"), "AaaaaaZzzz")
        test.assert_equals(find_children("CbcBcbaA"), "AaBbbCcc")
        test.assert_equals(find_children("xXfuUuuF"), "FfUuuuXx")
        test.assert_equals(find_children(""), "")
