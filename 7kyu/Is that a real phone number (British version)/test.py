import codewars_test as test
from kata import validate_number

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(validate_number("07454876120"), "In with a chance")
        test.assert_equals(validate_number("0754876120"), "Plenty more fish in the sea")
        test.assert_equals(validate_number("0745--487-61-20"), "In with a chance")
        test.assert_equals(validate_number("+447535514555"), "In with a chance")
        test.assert_equals(validate_number("-07599-51-4555"), "In with a chance")
        test.assert_equals(validate_number("075335440555"), "Plenty more fish in the sea")
        test.assert_equals(validate_number("+337535512555"), "Plenty more fish in the sea")
        test.assert_equals(validate_number("00535514555"), "Plenty more fish in the sea")
        test.assert_equals(validate_number("+447+4435512555"), "Plenty more fish in the sea", "Not a Briish prefix")
        test.assert_equals(validate_number("+44"), "Plenty more fish in the sea", "Not a Briish prefix")