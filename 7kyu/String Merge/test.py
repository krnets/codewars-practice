import codewars_test as test
from kata import string_merge

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(string_merge("hello", "world", "l"), "held")
        test.assert_equals(string_merge("coding", "anywhere", "n"), "codinywhere")
        test.assert_equals(string_merge("jason", "samson", "s"), "jasamson")
        test.assert_equals(string_merge("wonderful", "people", "e"), "wondeople")
        test.assert_equals(string_merge("person","here", "e"), "pere")
        test.assert_equals(string_merge("apowiejfoiajsf","iwahfeijouh", "j"), "apowiejouh")
        test.assert_equals(string_merge("abcdefxxxyzz","abcxxxyyyxyzz", "x"), "abcdefxxxyyyxyzz")
        test.assert_equals(string_merge("12345654321","123456789", "6"), "123456789")
        test.assert_equals(string_merge("JiOdIdA4","oopopopoodddasdfdfsd", "d"), "JiOdddasdfdfsd")
        test.assert_equals(string_merge("incredible","people", "e"), "increople")