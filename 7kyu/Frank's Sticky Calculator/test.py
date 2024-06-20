import codewars_test as test
from kata import sticky_calc

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sticky_calc('+', 4, 7), 54)
        test.assert_equals(sticky_calc('-', 15, 10), 1500)
        test.assert_equals(sticky_calc('*', 5, 5), 275)
        test.assert_equals(sticky_calc('/', 10, 7), 15)
        test.assert_equals(sticky_calc('+', 4.2, 7), 54) #Output : (47) + 7 = 54 
        test.assert_equals(sticky_calc('+', 4.7, 7.2), 64) #Output : (57) + 7 = 54
        test.assert_equals(sticky_calc('/', 10, 7), 15)
        test.assert_equals(sticky_calc('/', 51, 63), 82)