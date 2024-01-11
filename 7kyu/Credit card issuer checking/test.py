import codewars_test as test
from kata import get_issuer

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(get_issuer(4111111111111111), 'VISA')
        test.assert_equals(get_issuer(378282246310005), 'AMEX')
        test.assert_equals(get_issuer(9111111111111111), 'Unknown')