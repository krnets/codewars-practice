import codewars_test as test
from kata import substring

test.describe("longest 2-char substring tests")
test.it("should return the correct string")
test.assert_equals(substring(""), "", "substring('') should return ''")
test.assert_equals(substring("a"), "a", "substring('a') should return 'a'")
test.assert_equals(substring("aa"), "aa", "substring('aa') should return 'aa'")
test.assert_equals(substring("aaa"), "aaa", "substring('aaa') should return 'aaa'")
test.assert_equals(substring("ab"), "ab", "substring('ab') should return 'ab'")
test.assert_equals(substring("aba"), "aba", "substring('aba') should return 'aba'")
test.assert_equals(substring("abc"), "ab", "substring('abc') should return 'ab'")
test.assert_equals(substring("abcba"), "bcb", "substring('abcba') should return 'bcb'")
test.assert_equals(substring("bbacc"), "bba", "substring('bbacc') should return 'bba'")
test.assert_equals(substring("ccddeeff"), "ccdd", "substring('ccddeeff') should return 'ccdd'")