import codewars_test as test
from kata import string_transformer

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(string_transformer("Example string"), "STRING eXAMPLE")
        test.assert_equals(string_transformer("Example Input"), "iNPUT eXAMPLE")
        test.assert_equals(string_transformer("To be OR not to be That is the Question"), "qUESTION THE IS tHAT BE TO NOT or BE tO")
        test.assert_equals(string_transformer(""), "")
        test.assert_equals(string_transformer("You Know When  THAT  Hotline Bling"), "bLING hOTLINE  that  wHEN kNOW yOU")
        test.assert_equals(string_transformer(" A b C d E f G "), " g F e D c B a ")