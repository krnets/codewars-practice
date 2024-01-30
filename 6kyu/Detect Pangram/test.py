from kata import is_pangram
import codewars_test as test


@test.describe("sample tests")
def sample_tests():
    @test.it("Should return true for a pangram")
    def test_pangram():
        test.assert_equals(
            is_pangram("The quick, brown fox jumps over the lazy dog!"), True
        )

    @test.it("Should return false for not a pangram")
    def test_not_pangram():
        test.assert_equals(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)
