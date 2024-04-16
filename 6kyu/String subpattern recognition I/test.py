import codewars_test as test
from kata import has_subpattern

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(has_subpattern("a"), False)
        test.assert_equals(has_subpattern("aaaa"), True)
        test.assert_equals(has_subpattern("abcd"), False)
        test.assert_equals(has_subpattern("abababab"), True)
        test.assert_equals(has_subpattern("ababababa"), False)
        test.assert_equals(has_subpattern("123a123a123a"), True)
        test.assert_equals(has_subpattern("123A123a123a"), False)
        test.assert_equals(has_subpattern("abbaabbaabba"), True)
        test.assert_equals(has_subpattern("abbabbabba"), False)
        test.assert_equals(has_subpattern("abcdabcabcd"), False)