import codewars_test as test
from kata import no_repeat


@test.describe("Basic tests")
def _():
    @test.it("Tests")
    def _():
        test.assert_equals(no_repeat("aabbccdde"), "e")
        test.assert_equals(no_repeat("wxyz"), "w")
        test.assert_equals(no_repeat("testing"), "e")
        test.assert_equals(no_repeat("codewars"), "c")
        test.assert_equals(no_repeat("Testing"), "T")
