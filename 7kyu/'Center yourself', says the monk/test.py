import codewars_test as test
from kata import center


@test.describe("tests suite")
def tests_suite():
    @test.it("sample tests")
    def sample_tests():
        test.assert_equals(center("a", 3), " a ")
        test.assert_equals(center("abc", 10, "_"), "____abc___")
        test.assert_equals(center("abcdefg", 2), "abcdefg")
        test.assert_equals(center("a", 2, "_"), "_a")
        test.assert_equals(
            center("L", 44, "f"), "ffffffffffffffffffffffLfffffffffffffffffffff"
        )
        test.assert_equals(center("ab", 3, "_"), "_ab")
        test.assert_equals(
            center("VFMjlorywswhJLnisDbqwdEpkU", 61, "x"),
            "xxxxxxxxxxxxxxxxxxVFMjlorywswhJLnisDbqwdEpkUxxxxxxxxxxxxxxxxx",
        )
