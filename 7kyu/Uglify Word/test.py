import codewars_test as test
from kata import uglify_word

@test.describe('Sample tests')
def sample_tests():
    @test.it('')
    def _():
        test.assert_equals(uglify_word("AAA"), "AaA")
        test.assert_equals(uglify_word("AaA"), "AaA")
        test.assert_equals(uglify_word("BbB"), "BbB")
        test.assert_equals(uglify_word("aaa-bbb-ccc"), "AaA-BbB-CcC")
        test.assert_equals(uglify_word("AaA-BbB-CcC"), "AaA-BbB-CcC")
        test.assert_equals(uglify_word("eeee-ffff-gggg"), "EeEe-FfFf-GgGg")
        test.assert_equals(uglify_word("EeEe-FfFf-GgGg"), "EeEe-FfFf-GgGg")
        test.assert_equals(uglify_word("qwe123asdf456zxc"), "QwE123AsDf456ZxC")
        test.assert_equals(uglify_word("Hello World"), "HeLlO WoRlD")