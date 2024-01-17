from kata import validate_word
import codewars_test as test


@test.describe("Sample Tests")
def sample_tests():
    @test.it("Basic text")
    def basic():
        test.assert_equals(validate_word("abcabc"), True)
        test.assert_equals(validate_word("Abcabc"), True)
        test.assert_equals(validate_word("AbcabcC"), False)
        test.assert_equals(validate_word("AbcCBa"), True)
        test.assert_equals(validate_word("pippi"), False)
        test.assert_equals(validate_word("abcabcd"), False)

    @test.it("Special characters")
    def special():
        test.assert_equals(validate_word("?!?!?!"), True)
        test.assert_equals(validate_word("abc123"), True)
        test.assert_equals(validate_word("abc!abc!"), True)
        test.assert_equals(validate_word("abc:abc"), False)
