import codewars_test as test
from kata import sum_differences_between_products_and_LCMs

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sum_differences_between_products_and_LCMs([[15,18], [4,5], [12,60]]),840)
        test.assert_equals(sum_differences_between_products_and_LCMs([[1,1], [0,0], [13,91]]),1092)
        test.assert_equals(sum_differences_between_products_and_LCMs([[15,7], [4,5], [19,60]]),0)
        test.assert_equals(sum_differences_between_products_and_LCMs([[20,50], [10,10], [50,20]]),1890)
        test.assert_equals(sum_differences_between_products_and_LCMs([]),0)