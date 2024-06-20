import codewars_test as test
from kata import longest

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(longest('asd'), 'as')
        test.assert_equals(longest('nab'), 'ab')
        test.assert_equals(longest('abcdeapbcdef'), 'abcde')
        test.assert_equals(longest('asdfaaaabbbbcttavvfffffdf'), 'aaaabbbbctt')
        test.assert_equals(longest('asdfbyfgiklag'), 'fgikl')
        test.assert_equals(longest('z'), 'z')
        test.assert_equals(longest('zyba'), 'z')