import codewars_test as test
from kata import solve

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(solve("abcd"),0)
        test.assert_equals(solve("abcda"),1)
        test.assert_equals(solve("abcdabc"),3)
        test.assert_equals(solve("abcabc"),3)
        test.assert_equals(solve("abcabca"),1)
        test.assert_equals(solve("aaaaa"),2)
        test.assert_equals(solve("aaaa"),2)
        test.assert_equals(solve("aaa"),1)
        test.assert_equals(solve("aa"),1)
        test.assert_equals(solve("a"),0)