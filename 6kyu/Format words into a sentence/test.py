import codewars_test as test
from kata import format_words

@test.describe("Format words into a sentence")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(format_words(['one', 'two', 'three', 'four']), 'one, two, three and four', "formatWords(['one', 'two', 'three', 'four'] should return 'one, two, three and four'")
        test.assert_equals(format_words(['one']), 'one', "formatWords(['one']) should return 'one'")
        test.assert_equals(format_words(['one', '', 'three']), 'one and three', "formatWords(['one', '', 'three']) should return 'one and three'")
        test.assert_equals(format_words(['', '', 'three']), 'three', "formatWords(['', '', 'three']) should return 'three'")
        test.assert_equals(format_words(['one', 'two', '']), 'one and two', "formatWords(['one', 'two', '']) should return 'one and two'")
        test.assert_equals(format_words([]), '', 'formatWords([]) should return ""')
        test.assert_equals(format_words(None), '', 'formatWords(null) should return ""')
        test.assert_equals(format_words(['']), '', 'formatWords([""]) should return ""')
