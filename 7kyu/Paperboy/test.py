import codewars_test as test
from kata import cheapest_quote

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(cheapest_quote(1), 0.10)
        test.assert_equals(cheapest_quote(5), 0.49)
        test.assert_equals(cheapest_quote(10), 0.97)
        test.assert_equals(cheapest_quote(20), 1.93)
        test.assert_equals(cheapest_quote(40), 3.85)
        test.assert_equals(cheapest_quote(41), 3.95, '41 newspapers should be priced as 40 bundle and a 1 bundle')
        test.assert_equals(cheapest_quote(80), 7.70, '80 newspapers should be priced as two 40 bundles')
        test.assert_equals(cheapest_quote(26), 2.52, '26 newspapers should be priced as a 20 bundle, a 5 bundle and a 1 bundle')
        test.assert_equals(cheapest_quote(0), 0.0)
        test.assert_equals(cheapest_quote(499), 48.06)
        test.assert_equals(cheapest_quote(46), 4.44)
        test.assert_equals(cheapest_quote(36), 3.49)
        test.assert_equals(cheapest_quote(38), 3.69)