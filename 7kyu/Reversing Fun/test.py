import codewars_test as test
from kata import reverse_fun

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_fun('012345'), '504132', "should work for even length")
        test.assert_equals(reverse_fun('jointhedarkside'), 'ejdoiisnktrhaed', "should work for odd length")
        test.assert_equals(reverse_fun('012'), '201')
        test.assert_equals(reverse_fun('012345'), '504132')
        test.assert_equals(reverse_fun('0123456789'), '9081726354')
        test.assert_equals(reverse_fun('Hello'), 'oHlel')