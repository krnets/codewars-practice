import codewars_test as test
from kata import eq_sum_powdig

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(eq_sum_powdig(100, 2), [])
        test.assert_equals(eq_sum_powdig(1000, 2), [])
        test.assert_equals(eq_sum_powdig(200, 3), [153])
        test.assert_equals(eq_sum_powdig(370, 3), [153, 370])