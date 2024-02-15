import codewars_test as test
from kata import amount_of_pages

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(amount_of_pages(5), 5)
        test.assert_equals(amount_of_pages(25), 17)
        test.assert_equals(amount_of_pages(1095), 401)        
        test.assert_equals(amount_of_pages(185), 97)
        test.assert_equals(amount_of_pages(660), 256)