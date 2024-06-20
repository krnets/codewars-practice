import codewars_test as test
from kata import money_value

@test.describe("Unwanted dollars")
def unwanted_dollars():
    
    error_tolerance = 1e-9
    
    @test.it('Example Tests')
    def example_tests():
        test.assert_approx_equals(money_value("12.34"), 12.34, error_tolerance)
        test.assert_approx_equals(money_value(" $5.67"), 5.67, error_tolerance)
        test.assert_approx_equals(money_value("-0.89"), -0.89, error_tolerance)
        test.assert_approx_equals(money_value("-$ 0.1"), -0.10, error_tolerance)
        test.assert_approx_equals(money_value("$-2.3456"), -2.3456, error_tolerance)
        test.assert_approx_equals(money_value("007"), 7.00, error_tolerance)
        test.assert_approx_equals(money_value(" $ 89"), 89.0, error_tolerance)
        test.assert_approx_equals(money_value("   .11"), 0.11, error_tolerance)
        test.assert_approx_equals(money_value("$.2"), 0.20, error_tolerance)
        test.assert_approx_equals(money_value("-.34"), -0.34, error_tolerance)
        test.assert_approx_equals(money_value("$$$"), 0.0, error_tolerance)
    