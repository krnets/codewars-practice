import codewars_test as test
from kata import remove_parentheses

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(remove_parentheses("example(unwanted thing)example"), "exampleexample")
        test.assert_equals(remove_parentheses("example (unwanted thing) example"), "example  example")
        test.assert_equals(remove_parentheses("a (bc d)e"), "a e")
        test.assert_equals(remove_parentheses("a(b(c))"), "a")
        test.assert_equals(remove_parentheses("hello example (words(more words) here) something"), "hello example  something")
        test.assert_equals(remove_parentheses("(first group) (second group) (third group)"), "  ")