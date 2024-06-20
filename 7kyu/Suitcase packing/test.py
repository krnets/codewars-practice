import codewars_test as test
from kata import fit_in

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(fit_in(1,2,3,2), True)
        test.assert_equals(fit_in(1,2,2,1), False)
        test.assert_equals(fit_in(3,2,3,2), False)
        test.assert_equals(fit_in(1,2,1,2), False)
        test.assert_equals(fit_in(6,5,8,7), False)
        test.assert_equals(fit_in(6,6,12,6), True)
        test.assert_equals(fit_in(7,1,7,8), True)
        test.assert_equals(fit_in(10,10,11,11), False)
        test.assert_equals(fit_in(7,2,9,7), True)
        test.assert_equals(fit_in(7,2,8,7), False)
        test.assert_equals(fit_in(4,1,5,3), False)
        test.assert_equals(fit_in(1, 2, 3, 4), True)
        test.assert_equals(fit_in(1, 2, 4, 3), True) 
        test.assert_equals(fit_in(1, 3, 2, 4), False)
        test.assert_equals(fit_in(1, 3, 4, 2), False)
        test.assert_equals(fit_in(1, 4, 2, 3), False)
        test.assert_equals(fit_in(1, 4, 3, 2), False)
        test.assert_equals(fit_in(2, 1, 3, 4), True) 
        test.assert_equals(fit_in(2, 1, 4, 3), True) 
        test.assert_equals(fit_in(2, 3, 1, 4), False)