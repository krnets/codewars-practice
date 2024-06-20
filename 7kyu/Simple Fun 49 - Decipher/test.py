import codewars_test as test
from kata import decipher

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(decipher("10197115121"),"easy")
        test.assert_equals(decipher("98"),"b")
        test.assert_equals(decipher("122"),"z")