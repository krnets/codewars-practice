import codewars_test as test
from kata import calculate

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(calculate('1plus2plus3plus4'), '10')
        test.assert_equals(calculate('1minus2minus3minus4'), '-8')
        test.assert_equals(calculate('1plus2plus3minus4'), '2')
        test.assert_equals(calculate('1plus2minus3plus4minus5'), '-1')