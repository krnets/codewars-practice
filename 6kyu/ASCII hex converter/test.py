import codewars_test as test
from kata import *

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        s = "Look mom, no hands"
        h = "4c6f6f6b206d6f6d2c206e6f2068616e6473"
        test.assert_equals(Converter.to_hex(s), h)
        test.assert_equals(Converter.to_ascii(h), s)
        test.assert_equals(Converter.to_hex(Converter.to_ascii(h)), h)
        test.assert_equals(Converter.to_ascii(Converter.to_hex(s)), s)