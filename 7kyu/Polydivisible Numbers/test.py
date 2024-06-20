import codewars_test as test
from kata import polydivisible

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(polydivisible(1232), True)
        test.assert_equals(polydivisible(123220), False)
        test.assert_equals(polydivisible(0), True)
        test.assert_equals(polydivisible(1), True)
        test.assert_equals(polydivisible(141), True)
        test.assert_equals(polydivisible(1234), False)
        test.assert_equals(polydivisible(21234), False)
        test.assert_equals(polydivisible(81352), False)
        test.assert_equals(polydivisible(987654), True)
        test.assert_equals(polydivisible(1020005), True)
        test.assert_equals(polydivisible(9876545), True)
        test.assert_equals(polydivisible(381654729), True)
        test.assert_equals(polydivisible(1073741823), False)